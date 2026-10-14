import unittest
from unittest.mock import MagicMock
from lhguard.client import LeanLLMClient
from lhguard.validator import ValidationResult

class TestLeanLLMCorrectionLoop(unittest.TestCase):
    def setUp(self):
        # Target prompts and mock generational inputs
        self.target_prompt = "Prove that adding zero to a real number is identity."
        
        # Simulated broken proof: Attempt 1 uses an invalid tactic name 'magic_solve'
        self.hallucinated_response = """
Here is the theorem. I will use a shortcut tactic.
```lean
import Mathlib.Data.Real.Basic

theorem add_zero_identity (x : ℝ) : x + 0 = x := by
  magic_solve
```
"""
        # Simulated corrected proof: Attempt 2 relies on valid Mathlib rewrite steps
        self.corrected_response = """
Apologies, correcting the tactic to use the standard definition.
```lean
import Mathlib.Data.Real.Basic

theorem add_zero_identity (x : ℝ) : x + 0 = x := by
  rw [add_zero]
```
"""

    def test_successful_self_correction_loop(self):
        """Tests that the client catches a compiler error and converges on a correction."""
        # 1. Mock the LLM function to return the failure block followed by the fix
        mock_llm = MagicMock(side_effect=[self.hallucinated_response, self.corrected_response])
        
        # 2. Mock out the validator to mimic local compiler behavior
        # First call fails with an unknown tactic string, second call returns success
        mock_errors = "Verification_Enclave_Sandbox.lean:5:2: error: unknown tactic 'magic_solve'"
        mock_validate = MagicMock(side_effect=[
            ValidationResult(is_valid=False, error_message=mock_errors),
            ValidationResult(is_valid=True, error_message="")
        ])
        
        # Initialize client with our mock hooks
        client = LeanLLMClient(llm_completion_func=mock_llm, max_retries=3)
        
        # Patch the internal validator import path during execution
        import lhguard.client as client_module
        original_validator = client_module.validate_lean_code
        client_module.validate_lean_code = mock_validate
        
        try:
            # 3. Trigger the verification pipeline
            final_result = client.generate_theorem(self.target_prompt)
            
            # 4. Assert correct execution routes were followed
            self.assertIn("rw [add_zero]", final_result)
            self.assertEqual(mock_llm.call_count, 2)
            self.assertEqual(mock_validate.call_count, 2)
            
            # Verify the parsed error feedback was sent back to the LLM context
            second_call_prompt = mock_llm.call_args_list[1][0][0]
            self.assertIn("unknown tactic 'magic_solve'", second_call_prompt)
            self.assertIn("📍 Fault Location:", second_call_prompt)
            
        finally:
            # Revert the monkeypatch to keep environmental imports pristine
            client_module.validate_lean_code = original_validator

if __name__ == "__main__":
    unittest.main()
