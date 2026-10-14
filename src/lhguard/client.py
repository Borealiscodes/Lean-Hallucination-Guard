import re
from typing import Callable, Optional, Dict, Any
from .validator import validate_lean_code
from .utils.logger import setup_logger

logger = setup_logger("lhguard.client")

class LeanLLMClient:
    def __init__(self, llm_completion_func: Callable[[str], str], max_retries: int = 4):
        """
        Args:
            llm_completion_func: Connection hook to execute your target LLM prompt.
            max_retries: Maximum correction cycles allowed before execution abort.
        """
        self.llm = llm_completion_func
        self.max_retries = max_retries

    def _extract_lean_block(self, text: str) -> Optional[str]:
        """Extracts the first Lean code block discovered in text."""
        match = re.search(r'```lean\n(.*?)\n```', text, re.DOTALL)
        return match.group(1).strip() if match else None

    def _parse_tactic_state(self, compiler_output: str) -> Dict[str, Any]:
        """
        Parses Lean 4 compiler diagnostics to isolate line numbers 
        and extract the remaining unproven mathematical goals.
        """
        loc_match = re.search(r':(\d+):(\d+):', compiler_output)
        line = int(loc_match.group(1)) if loc_match else "Unknown"
        col = int(loc_match.group(2)) if loc_match else "Unknown"
        
        goals = []
        lines = compiler_output.splitlines()
        capture = False
        for l in lines:
            if "unsolved goals" in l.lower() or "⊢" in l:
                capture = True
            if capture:
                goals.append(l)
        
        tactic_state = "\n".join(goals) if goals else compiler_output
        return {"line": line, "column": col, "tactic_state": tactic_state}

    def generate_theorem(self, prompt: str) -> str:
        """Generates, validates, and recursively fixes a Lean 4 theorem using targeted tactic feedback."""
        current_prompt = (
            f"{prompt}\n\nReturn your answer with the Lean 4 code "
            "wrapped in a standard ```lean ... ``` block. Ensure all necessary Mathlib modules are imported."
        )
        
        for attempt in range(1, self.max_retries + 1):
            logger.info(f"Triggering LLM generation loop pass (Iteration {attempt}/{self.max_retries})...")
            response = self.llm(current_prompt)
            lean_code = self._extract_lean_block(response)
            
            if not lean_code:
                logger.warning("Generation artifact missing expected ```lean code block delimiters.")
                current_prompt = f"Format error. You must explicitly output the theorem inside a ```lean block.\n\n{prompt}"
                continue
                
            result = validate_lean_code(lean_code)
            
            if result.is_valid:
                logger.info(f"Success! Code block compiled perfectly on attempt {attempt}.")
                return response
                
            diagnostics = self._parse_tactic_state(result.error_message)
            logger.warning(f"Lean syntax error captured at line {diagnostics['line']}. Re-routing context loop...")
            
            current_prompt = (
                f"The Lean 4 code you provided failed compilation diagnostics.\n\n"
                f"--- Target Code Fragment ---\n```lean\n{lean_code}\n```\n\n"
                f"--- Error Analysis ---\n"
                f"📍 Fault Location: Line {diagnostics['line']}, Column {diagnostics['column']}\n"
                f"🔮 Active Tactic State / Unsolved Goals:\n{diagnostics['tactic_state']}\n\n"
                f"--- Action Required ---\n"
                f"Analyze the active goals (⊢) and variable states listed above. "
                f"Rewrite the theorem declaration or proof tactics to close this specific goal state. "
                f"Do not introduce new unverified tactics."
            )
            
        err_msg = f"Agent failed to converge on a sound mathematical proof within {self.max_retries} cycles."
        logger.error(err_msg)
        raise RuntimeError(err_msg)
