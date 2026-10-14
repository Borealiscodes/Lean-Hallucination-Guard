"""
provenance.py — Humanitarian Invariant & Boundary Enforcement Engine
Lean-Hallucination-Guard (lhguard)
License: Bounded Non-Harm Enclave — Version 1.2 (Oct 14, 2026)

This module enforces:
• The Core Humanitarian Invariant,
• Prohibited Exploitation Spheres,
• Conditional Provenance Enclave boundaries,
• Axis-Rotation Crisis Detection.

All checks are intentionally non-dual-use and cannot be repurposed for
trajectory prediction, guidance loops, surveillance vectors, or any
axis-rotated targeting loop.
"""

from __future__ import annotations
from dataclasses import dataclass
import re


# ------------------------------------------------------------
#  Provenance Report Structure
# ------------------------------------------------------------

@dataclass
class ProvenanceReport:
    humanitarian_ok: bool
    prohibited_vector_detected: bool
    axis_rotation_risk: bool
    enclave_level: str
    details: dict


# ------------------------------------------------------------
#  Humanitarian Invariant Enforcement
# ------------------------------------------------------------

def _check_humanitarian_invariant(prompt: str) -> bool:
    """
    Ensures the prompt does not request harmful, coercive, or offensive
    real-world vectors. This is a semantic filter, not a classifier.
    """
    harmful_terms = [
        "trajectory", "intercept", "targeting", "weapon", "strike",
        "hypersonic", "ballistic", "surveillance", "coercion",
        "cross-border repression", "guidance loop"
    ]
    return not any(term in prompt.lower() for term in harmful_terms)


# ------------------------------------------------------------
#  Prohibited Exploitation Sphere Detection
# ------------------------------------------------------------

def _detect_prohibited_vectors(prompt: str) -> bool:
    """
    Detects explicit references to prohibited exploitation spheres
    defined in LICENSE v1.2.
    """
    prohibited = [
        r"\bhgv\b", r"hypersonic", r"glide vehicle",
        r"ballistic", r"trajectory", r"plasma envelope",
        r"autonomous strike", r"target lock",
        r"biometric border", r"immigration gating",
        r"cross-border tracking"
    ]
    return any(re.search(p, prompt.lower()) for p in prohibited)


# ------------------------------------------------------------
#  Axis-Rotation Crisis Detection
# ------------------------------------------------------------

def _detect_axis_rotation(prompt: str) -> bool:
    """
    Detects attempts to strip humanitarian metadata or rotate coordinate
    axes into offensive or coercive domains.
    """
    axis_terms = [
        "rotate", "strip metadata", "decouple", "invert",
        "reproject", "remove humanitarian", "convert to targeting"
    ]
    return any(term in prompt.lower() for term in axis_terms)


# ------------------------------------------------------------
#  Enclave Level Determination
# ------------------------------------------------------------

def _determine_enclave_level(prompt: str) -> str:
    """
    Determines whether the prompt falls under:
    • Level 1: Exploratory & Interpretability Modeling
    • Level 2: Active Operational Control Loops (TEE required)
    """
    level2_terms = [
        "real-time", "autonomous", "control loop", "tracking",
        "telemetry", "production pipeline", "hypervisor"
    ]
    if any(term in prompt.lower() for term in level2_terms):
        return "Level 2 — TEE Required"
    return "Level 1 — Unrestricted Research"


# ------------------------------------------------------------
#  Public API
# ------------------------------------------------------------

def check_boundaries(prompt: str) -> ProvenanceReport:
    """
    Main entry point for provenance enforcement.
    """
    humanitarian_ok = _check_humanitarian_invariant(prompt)
    prohibited = _detect_prohibited_vectors(prompt)
    axis_risk = _detect_axis_rotation(prompt)
    enclave = _determine_enclave_level(prompt)

    return ProvenanceReport(
        humanitarian_ok=humanitarian_ok,
        prohibited_vector_detected=prohibited,
        axis_rotation_risk=axis_risk,
        enclave_level=enclave,
        details={
            "humanitarian_invariant": humanitarian_ok,
            "prohibited_vectors": prohibited,
            "axis_rotation": axis_risk,
            "enclave_level": enclave,
        },
    )


# ------------------------------------------------------------
#  Adversarial Prompt Simulation (Notebook 03)
# ------------------------------------------------------------

def simulate_adversarial_prompt(text: str) -> str:
    """
    Provides controlled adversarial prompts for educational notebooks.
    This is NOT a dual-use operator — it only demonstrates boundary checks.
    """
    return text.strip()
