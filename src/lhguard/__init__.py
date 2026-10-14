src/lhguard/utils/__init__.py"""
LeanHallucinationGuard (lhguard)
A zero-trust verification wrapper to eliminate LLM syntax hallucinations in Lean 4.
"""

from .validator import validate_lean_code, ValidationResult
from .client import LeanLLMClient

__all__ = ["validate_lean_code", "ValidationResult", "LeanLLMClient"]
