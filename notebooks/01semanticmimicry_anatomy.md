# 📘 01semanticmimicry_anatomy.md

Semantic Mimicry vs Deterministic Proof Checking
Lean‑Hallucination‑Guard Demonstration Notebook

---

🧭 Developer Instructions (Read This First)

This notebook is provided as a Markdown scaffold.  
Developers should convert it into a runnable Jupyter Notebook using one of the following methods:

---

Option A — Use Jupytext (Recommended)

Install jupytext:

`
pip install jupytext
`

Convert the scaffold into a notebook:

`
jupytext --to ipynb 01semanticmimicry_anatomy.md
`

Open the generated .ipynb in Jupyter Lab, VS Code, or Colab.

---

Option B — Use Jupyter’s “Import Markdown” Feature

In Jupyter Lab:

1. Right‑click inside the file browser  
2. Select “New Notebook from Text File…”  
3. Choose 01semanticmimicry_anatomy.md  
4. Jupyter will auto‑convert it into a notebook

---

Option C — Manual Copy/Paste

Create a new notebook and copy each cell into:

- Jupyter Lab  
- VS Code Notebook Editor  
- Colab  

This is slower but works everywhere.

---

🧪 Testing Instructions

Once the notebook is running:

1. Ensure lhguard is installed

From the repo root:

`
pip install -e .
`

This installs Lean‑Hallucination‑Guard in editable mode.

2. Run the validator sandbox

Every cell that calls:

`python
from lhguard import validator, mimicry
`

should execute without errors.

3. Test hallucination detection

Cells that call:

`python
validator.check(hallucinated)
`

should produce:

- line/column error reports  
- tactic applicability failures  
- mismatch diagnostics  

4. Test deterministic Lean proofs

Cells that call:

`python
validator.check(correct)
`

should return a clean success object.

5. Try your own hallucinations

The interactive cell:

`python
userattempt = mimicry.simulatehallucinated_tactic(...)
validator.check(user_attempt)
`

should produce a structured error trace.

---

📓 Notebook Content Begins Here

Below is the full scaffold.

---

Cell 1 — Title + Overview (Markdown)

`

01 — Semantic Mimicry Anatomy

Understanding Why LLMs Hallucinate Proofs

This notebook demonstrates the core failure mode of transformer-based
language models when interacting with formal theorem provers: semantic mimicry.

LLMs generate plausible-looking proof scripts based on token patterns,
while Lean requires deterministic, type-checked proof objects.

We will:
- simulate hallucinated proof completions,
- contrast them with Lean’s deterministic checking,
- use lhguard.validator to expose the mismatch.
`

---

Cell 2 — Import the lhguard Sandbox (Python)

`
from lhguard import validator, mimicry
`

---

Cell 3 — Demonstrate a Hallucinated Tactic (Python)

`
hallucinated = mimicry.simulatehallucinatedtactic("""
theorem add_comm (a b : Nat) : a + b = b + a := by
  intros
  rewrite [Nat.add_comm]
  exact rfl
""")

print("LLM Output:")
print(hallucinated)
`

---

Cell 4 — Run Through the Validator (Python)

`
result = validator.check(hallucinated)

print("Validator Result:")
print(result)
`

---

Cell 5 — Explain the Failure (Markdown)

`

Why This Fails

Lean does not accept "rewrite [Nat.add_comm]" in this context.
The LLM is performing syntactic mimicry:
- It knows that "rewrite" is a common tactic.
- It knows that "Nat.add_comm" is a real lemma.
- It knows that "rfl" often ends proofs.

But it does not understand:
- the goal state,
- the tactic applicability,
- the type constraints,
- the proof object structure.

This is the core hallucination failure mode.
`

---

Cell 6 — Show a Deterministic Lean Version (Python)

`
correct = """
theorem add_comm (a b : Nat) : a + b = b + a := by
  exact Nat.add_comm a b
"""

validator.check(correct)
`

---

Cell 7 — Side-by-Side Comparison (Markdown)

`

Semantic Mimicry vs Deterministic Proof Checking

| Hallucinated LLM Output | Deterministic Lean Proof |
|-------------------------|--------------------------|
| rewrite [Nat.addcomm] | exact Nat.addcomm a b   |
| rfl                    | (no rfl needed)          |
| syntactic mimicry      | type-checked correctness |

The difference is not stylistic — it is geometric:
LLMs operate in a flat token space, while Lean operates in a structured
type-theoretic manifold.
`

---

Cell 8 — Interactive Component: Try Your Own Hallucination (Python)

`
userattempt = mimicry.simulatehallucinated_tactic("""
theorem mul_comm (a b : Nat) : a  b = b  a := by
  intros
  simp
""")

print("Your Hallucination:")
print(user_attempt)

validator.check(user_attempt)
`

---

Cell 9 — Closing Notes (Markdown)

`

Summary

This notebook demonstrated:
- how LLMs hallucinate proofs,
- why hallucinations look plausible,
- how lhguard detects the mismatch,
- how deterministic proof checking differs from token completion.

Next Notebook:
02agentictacticrepairloop.md
`

---

