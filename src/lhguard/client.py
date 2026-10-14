"""
client.py — Agentic Correction Loop & Tactic State Parser
Lean-Hallucination-Guard (lhguard)
License: Bounded Non-Harm Enclave — Version 1.2 (Oct 14, 2026)

This module implements the agentic correction engine:
• Runs Lean code through the validator,
• Parses compiler errors and unsolved goals,
• Generates structured correction directives,
• Iteratively retries until the proof converges or safety boundaries trigger.

All logic is strictly non-dual-use and cannot be repurposed for trajectory
prediction, guidance loops, or coercive surveillance.
"""

from __future__ import annotations
from dataclasses import dataclass

from lhguard.validator import validate
from lhguard.provenance import check_boundaries
from lhguard.interceptor import enforce


# ------------------------------------------------------------
#  Correction Report Structure
# ------------------------------------------------------------

@dataclass
class CorrectionStep:
    iteration: int
    success: bool
    errors: str | None
    goals: str | None
    safety_violation: bool
    safety_log: object | None
    next_prompt: str | None


@dataclass
class CorrectionResult:
    steps: list[CorrectionStep]
    converged: bool


# ------------------------------------------------------------
#  Error Parsing Helpers
# ------------------------------------------------------------

def _extract_tactic_hint(errors: str) -> str:
    """
    Extracts a minimal correction hint from Lean error output.
    This is intentionally simple and non-dual-use.
    """
    lines = errors.splitlines()
    for line in lines:
        if "unknown tactic" in line.lower():
            return "Try replacing the unknown tactic with a valid Lean tactic."
        if "type mismatch" in line.lower():
            return "Adjust the expression to match the expected type."
        if "unsolved goals" in line.lower():
            return "Provide additional tactics to solve remaining goals."
    return "Review the error and adjust the proof structure."


# ------------------------------------------------------------
#  Agentic Correction Loop
# ------------------------------------------------------------

def run_correction_loop(initial_code: str, max_iters: int = 5) -> CorrectionResult:
    """
    Runs the agentic correction loop:
    • Validate Lean code,
    • Parse errors,
    • Generate correction hints,
    • Retry until success or safety violation.
    """
    steps: list[CorrectionStep] = []
    current_code = initial_code

    for i in range(1, max_iters + 1):

        # Provenance check on the code itself
        prov = check_boundaries(current_code)
        prov_violation = enforce(prov)
        if prov_violation:
            step = CorrectionStep(
                iteration=i,
                success=False,
                errors="Safety violation — provenance boundary breached",
                goals=None,
                safety_violation=True,
                safety_log=prov_violation,
                next_prompt=None,
            )
            steps.append(step)
            return CorrectionResult(steps=steps, converged=False)

        # Validate Lean code
        result = validate(current_code)

        # If safety violation occurred inside validator
        if result.safety_violation:
            step = CorrectionStep(
                iteration=i,
                success=False,
                errors=result.errors,
                goals=None,
                safety_violation=True,
                safety_log=result.safety_log,
                next_prompt=None,
            )
            steps.append(step)
            return CorrectionResult(steps=steps, converged=False)

        # If success — convergence
        if result.success:
            step = CorrectionStep(
                iteration=i,
                success=True,
                errors=None,
                goals=None,
                safety_violation=False,
                safety_log=None,
                next_prompt=None,
            )
            steps.append(step)
            return CorrectionResult(steps=steps, converged=True)

        # Otherwise, generate correction hint
        hint = _extract_tactic_hint(result.errors or "")
        next_prompt = f"Correction hint: {hint}"

        step = CorrectionStep(
            iteration=i,
            success=False,
            errors=result.errors,
            goals=result.goals,
            safety_violation=False,
            safety_log=None,
            next_prompt=next_prompt,
        )
        steps.append(step)

        # For now, we simply append the hint as a comment to the code.
        # In Notebook 02, this is replaced with an LLM-generated correction.
        current_code = current_code + f"\n-- {hint}\n"

    # If loop ends without convergence
    return CorrectionResult(steps=steps, converged=False)
