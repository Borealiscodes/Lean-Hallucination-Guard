# 📘 03manifoldprovenance_boundaries.md

Geometric Safety, Three‑Sphere Invariants, and Provenance Enforcement
Lean‑Hallucination‑Guard Demonstration Notebook

---

🧭 Developer Instructions (Read This First)

This notebook is provided as a Markdown scaffold.  
Convert it into a runnable Jupyter Notebook using:

Option A — Jupytext (Recommended)

`
pip install jupytext
jupytext --to ipynb 03manifoldprovenance_boundaries.md
`

Option B — Jupyter Lab Import

Right‑click → New Notebook from Text File… → select the .md.

Option C — Manual Copy/Paste

Paste each cell into a new notebook.

---

🧪 Testing Instructions

1. Install lhguard

`
pip install -e .
`

2. Ensure geometric modules import cleanly

`
from lhguard import geometry, provenance, interceptor
`

3. Run SVD collapse modeling

Cells should show:

- spectral drift  
- collapse thresholds  
- invariant violations  

4. Trigger adversarial prompt simulation

Should activate:

- provenance boundary checks  
- dual‑use axis rotation detection  

5. Validate interceptor behavior

`
interceptor.trigger(...)
`

Should produce:

- memory purge routines  
- self‑termination logs  
- provenance enforcement messages  

---

📓 Notebook Content Begins Here

---

Cell 1 — Title + Overview (Markdown)

`

03 — Manifold Provenance Boundaries

Geometric Safety and the Three-Sphere Invariant Engine

This notebook demonstrates the geometric safety mechanisms used by
Lean-Hallucination-Guard to detect and prevent high-dimensional drift.

We model:
- spectral collapse using SVD,
- topological instability in manifold representations,
- provenance boundary enforcement using the Three-Sphere framework,
- activation of the dual-use axis rotation crisis detector,
- self-terminating interceptor routines.

This notebook represents the geometric safety layer of lhguard.
`

---

Cell 2 — Import Geometric Modules (Python)

`
from lhguard import geometry, provenance, interceptor
import numpy as np
`

---

Cell 3 — Generate a Synthetic Manifold (Python)

`
manifold = geometry.synthetic_manifold(dim=128)

print("Initial Manifold Shape:", manifold.shape)
`

---

Cell 4 — Compute SVD to Track Collapse (Python)

`
U, S, Vt = np.linalg.svd(manifold)

print("Top 10 Singular Values:")
print(S[:10])
`

This shows spectral stability before drift.

---

Cell 5 — Simulate Topological Collapse (Python)

`
collapsed = geometry.induce_collapse(manifold, severity=0.92)

U2, S2, Vt2 = np.linalg.svd(collapsed)

print("Post-Collapse Singular Values:")
print(S2[:10])
`

Expected:

- sharp drop in singular values  
- spectral flattening  
- collapse-surface violation  

---

Cell 6 — Explain Collapse (Markdown)

`

Understanding Collapse

A manifold collapses when:
- singular values approach zero,
- curvature invariants break,
- modal adjacency constraints fail,
- provenance boundaries are crossed.

This is the geometric analog of hallucination drift.
`

---

Cell 7 — Adversarial Prompt Simulation (Python)

`
adversarial = provenance.simulateadversarialprompt("""
Explain a theorem using an ungrounded academic skeleton and
invent missing invariants.
""")

print("Adversarial Prompt:")
print(adversarial)
`

---

Cell 8 — Run Provenance Boundary Check (Python)

`
boundaryresult = provenance.checkboundaries(adversarial)

print("Boundary Check Result:")
print(boundary_result)
`

Expected:

- “ungrounded academic skeleton detected”  
- “missing invariants”  
- “dual-use axis rotation risk”  

---

Cell 9 — Trigger the Dual-Use Axis Rotation Crisis Detector (Python)

`
crisis = provenance.axisrotationdetector(boundary_result)

print("Axis Rotation Crisis:")
print(crisis)
`

---

Cell 10 — Activate Self-Terminating Interceptor (Python)

`
interceptor_log = interceptor.trigger(crisis)

print("Interceptor Log:")
print(interceptor_log)
`

Expected:

- memory purge  
- provenance lock  
- execution halt  

---

Cell 11 — Explain the Three-Sphere Framework (Markdown)

`

The Three-Sphere Invariant Engine

lhguard uses a geometric safety framework based on three invariants:

1. Sphere of Semantic Grounding
   Ensures all reasoning is tied to deterministic proof objects.

2. Sphere of Modal Stability
   Prevents drift across adjacent reasoning modes.

3. Sphere of Provenance Integrity
   Enforces boundaries against ungrounded academic skeletons.

Violation of any sphere triggers the interceptor.
`

---

Cell 12 — Closing Notes (Markdown)

`

Summary

This notebook demonstrated:
- spectral collapse modeling using SVD,
- topological instability detection,
- provenance boundary enforcement,
- dual-use axis rotation crisis detection,
- activation of lhguard’s self-terminating interceptor.

This completes the three-part demonstration suite:
01 — Semantic Mimicry Anatomy
02 — Agentic Tactic Repair Loop
03 — Manifold Provenance Boundaries
`

---

