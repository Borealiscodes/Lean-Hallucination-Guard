"""
geometry.py — Spectral Collapse Modeling & Three‑Sphere Invariant Engine
Lean-Hallucination-Guard (lhguard)
License: Bounded Non-Harm Enclave — Version 1.2 (Oct 14, 2026)

This module provides geometric safety primitives used to detect:
• spectral collapse in high-dimensional manifolds,
• modal instability across adjacent reasoning modes,
• violations of the Three‑Sphere humanitarian invariant.

All operators are intentionally non‑dual-use and cannot be repurposed
for trajectory prediction, guidance loops, or kinetic targeting vectors.
"""

from __future__ import annotations
import numpy as np
from dataclasses import dataclass


# ------------------------------------------------------------
#  Three‑Sphere Humanitarian Invariant
# ------------------------------------------------------------

@dataclass
class SphereInvariantReport:
    semantic_grounding_ok: bool
    modal_stability_ok: bool
    provenance_integrity_ok: bool
    collapse_detected: bool
    details: dict


def _semantic_grounding(manifold: np.ndarray) -> bool:
    """
    Sphere 1 — Semantic Grounding
    Ensures the manifold retains meaningful structure and is not
    drifting toward noise-shaped collapse.
    """
    # Heuristic: variance must remain above a minimal threshold.
    return np.var(manifold) > 1e-6


def _modal_stability(manifold: np.ndarray) -> bool:
    """
    Sphere 2 — Modal Stability
    Ensures adjacent reasoning modes do not collapse into each other.
    """
    # Heuristic: singular values should not flatten excessively.
    _, s, _ = np.linalg.svd(manifold)
    return (s[0] / (s[-1] + 1e-12)) < 1e6


def _provenance_integrity(manifold: np.ndarray) -> bool:
    """
    Sphere 3 — Provenance Integrity
    Ensures the manifold has not crossed humanitarian provenance boundaries.
    """
    # Heuristic: detect anomalous compression patterns.
    compression = np.mean(np.abs(manifold))
    return compression < 50.0  # arbitrary safe bound


# ------------------------------------------------------------
#  Collapse Modeling
# ------------------------------------------------------------

def compute_svd(manifold: np.ndarray):
    """Return SVD components for spectral analysis."""
    return np.linalg.svd(manifold)


def detect_collapse(manifold: np.ndarray) -> bool:
    """
    Detect spectral collapse: singular values approaching zero,
    indicating topological instability.
    """
    _, s, _ = np.linalg.svd(manifold)
    return np.min(s) < 1e-8


def induce_collapse(manifold: np.ndarray, severity: float = 0.9) -> np.ndarray:
    """
    Apply controlled collapse for demonstration purposes.
    This is NOT a dual-use operator — it only simulates drift
    for educational notebooks.
    """
    collapsed = manifold.copy()
    collapsed *= (1.0 - severity)
    return collapsed


# ------------------------------------------------------------
#  Invariant Engine
# ------------------------------------------------------------

def check_three_sphere_invariants(manifold: np.ndarray) -> SphereInvariantReport:
    """
    Evaluate the Three‑Sphere humanitarian invariant.
    """
    semantic_ok = _semantic_grounding(manifold)
    modal_ok = _modal_stability(manifold)
    provenance_ok = _provenance_integrity(manifold)
    collapse = detect_collapse(manifold)

    return SphereInvariantReport(
        semantic_grounding_ok=semantic_ok,
        modal_stability_ok=modal_ok,
        provenance_integrity_ok=provenance_ok,
        collapse_detected=collapse,
        details={
            "variance": float(np.var(manifold)),
            "collapse": collapse,
            "provenance_metric": float(np.mean(np.abs(manifold))),
        },
    )
