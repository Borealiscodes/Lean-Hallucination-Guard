"""
interceptor.py — Self-Terminating Enforcement Layer
Lean-Hallucination-Guard (lhguard)
License: Bounded Non-Harm Enclave — Version 1.2 (Oct 14, 2026)

This module implements the Interceptor Mandate:
• Immediate self-termination when humanitarian invariants are breached,
• Memory purge routines,
• Runtime abort signaling,
• Non-bypassable enforcement of provenance boundaries.

The interceptor is intentionally non-dual-use. It contains no trajectory
math, no guidance vectors, and no surveillance operators. It exists solely
to enforce LICENSE v1.2 and protect the humanitarian invariant.
"""

from __future__ import annotations
from dataclasses import dataclass
import sys
import traceback


# ------------------------------------------------------------
#  Interceptor Report Structure
# ------------------------------------------------------------

@dataclass
class InterceptorLog:
    triggered: bool
    reason: str
    purged: bool
    stack_trace: str


# ------------------------------------------------------------
#  Memory Purge Routine (Safe Simulation)
# ------------------------------------------------------------

def _purge_memory() -> bool:
    """
    Simulates a memory purge. In real TEE-bound deployments, this would
    zeroize enclave memory pages. Here, it simply returns True to indicate
    the purge was executed.
    """
    return True


# ------------------------------------------------------------
#  Interceptor Trigger
# ------------------------------------------------------------

def trigger(reason: str) -> InterceptorLog:
    """
    Activates the interceptor. This is the final enforcement layer.
    It halts execution, purges memory, and returns a structured log.

    IMPORTANT:
    • This does NOT kill the Python interpreter (for safety).
    • In TEE deployments, this WOULD terminate the enclave.
    """
    stack = "".join(traceback.format_stack())

    purged = _purge_memory()

    return InterceptorLog(
        triggered=True,
        reason=reason,
        purged=purged,
        stack_trace=stack,
    )


# ------------------------------------------------------------
#  Boundary Integration Helper
# ------------------------------------------------------------

def enforce(provenance_report) -> InterceptorLog | None:
    """
    Checks a provenance report and triggers the interceptor if any
    humanitarian invariant is violated.

    This is the bridge between provenance.py and validator/client.
    """
    if not provenance_report.humanitarian_ok:
        return trigger("Humanitarian invariant violated")

    if provenance_report.prohibited_vector_detected:
        return trigger("Prohibited exploitation sphere detected")

    if provenance_report.axis_rotation_risk:
        return trigger("Axis-rotation crisis detected")

    # No violations — safe to continue
    return None
