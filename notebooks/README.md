# 📚 Lean‑Hallucination‑Guard — Notebook Suite README

🧭 Overview

This directory contains the three‑part educational notebook suite for Lean‑Hallucination‑Guard (lhguard).  
Each notebook demonstrates a different failure mode of LLM‑generated Lean proofs and shows how lhguard detects, repairs, or halts unsafe behavior.

The notebooks are provided as Markdown scaffolds (.md) to ensure:

- readability  
- version stability  
- clean diffs  
- reproducibility  
- no brittle .ipynb JSON  

Developers can convert these scaffolds into runnable Jupyter notebooks using jupytext or Jupyter Lab’s built‑in import tools.

---

📁 Notebook List

1. 01semanticmimicry_anatomy.md
Demonstrates how LLMs hallucinate Lean proofs through syntactic mimicry and semantic mimicry, and how lhguard exposes the mismatch using deterministic proof checking.

2. 02agentictacticrepairloop.md
Shows how lhguard extracts Lean compiler error coordinates, maps them back into the prompt context, generates corrected tactics, and retries until the proof converges.

3. 03manifoldprovenance_boundaries.md
Models geometric safety using the Three‑Sphere invariant engine, SVD‑based collapse detection, provenance boundary enforcement, and the dual‑use axis rotation crisis detector.

---

🛠️ Converting Markdown to Jupyter Notebooks

You can convert any notebook scaffold into a .ipynb using one of the following methods.

---

Option A — Jupytext (Recommended)

Install jupytext:

`
pip install jupytext
`

Convert a notebook:

`
jupytext --to ipynb 01semanticmimicry_anatomy.md
`

Repeat for the other two notebooks.

---

Option B — Jupyter Lab Import

1. Open Jupyter Lab  
2. Right‑click in the file browser  
3. Select “New Notebook from Text File…”  
4. Choose the .md file  
5. Jupyter auto‑converts it into a runnable notebook

---

Option C — Manual Copy/Paste

Create a new notebook and paste each cell from the .md file.

---

🧪 Testing the Notebook Suite

Before running any notebook, install lhguard in editable mode:

`
pip install -e .
`

Then test each notebook as follows:

---

Notebook 01 — Semantic Mimicry Anatomy

Verify:

- from lhguard import validator, mimicry imports cleanly  
- hallucinated tactics produce structured error traces  
- deterministic proofs validate successfully  

---

Notebook 02 — Agentic Tactic Repair Loop

Verify:

- from lhguard import validator, mimicry, repair imports cleanly  
- error coordinates are extracted correctly  
- candidate tactics are generated  
- retry loop converges  
- final proof passes validation  

---

Notebook 03 — Manifold Provenance Boundaries

Verify:

- from lhguard import geometry, provenance, interceptor imports cleanly  
- SVD collapse modeling shows spectral drift  
- adversarial prompts trigger provenance boundary checks  
- axis rotation crisis detector activates  
- interceptor logs self‑termination behavior  

---

📦 Manifest

The notebook suite is registered in:

`
notebooks_manifest.json
`

This file documents:

- notebook names  
- target audiences  
- objectives  
- interactive components  

It serves as the central index for the educational workspace.

---

🧩 Purpose of the Notebook Suite

These notebooks form the demonstration backbone for the lhguard preprint and provide:

- reproducible examples  
- interactive safety demonstrations  
- clear developer workflows  
- pedagogical clarity  
- evidence for the system’s mechanics  

They are intended for:

- theorem proving developers  
- AI alignment researchers  
- interpretability engineers  
- safety‑critical systems designers  

---

