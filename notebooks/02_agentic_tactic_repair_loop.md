# 02agentictacticrepairloop.md

Mapping Lean Goal Coordinates Back Into Prompt Context
Lean‑Hallucination‑Guard Demonstration Notebook

---

🧭 Developer Instructions (Read This First)

This notebook is provided as a Markdown scaffold.  
Convert it into a runnable Jupyter Notebook using one of the following methods:

---

Option A — Jupytext (Recommended)

Install jupytext:

`
pip install jupytext
`

Convert the scaffold:

`
jupytext --to ipynb 02agentictacticrepairloop.md
`

Open the generated notebook in Jupyter Lab, VS Code, or Colab.

---

Option B — Jupyter Lab Import

1. Right‑click in the file browser  
2. Select “New Notebook from Text File…”  
3. Choose 02agentictacticrepairloop.md  
4. Jupyter auto‑converts it

---

Option C — Manual Copy/Paste

Create a new notebook and paste each cell.

---

🧪 Testing Instructions

1. Install lhguard

From the repo root:

`
pip install -e .
`

2. Ensure the validator and repair loop modules import cleanly

`
from lhguard import validator, repair
`

3. Run the repair loop on a hallucinated tactic

Cells should show:

- extracted Lean goal coordinates  
- line/column mapping  
- retry milestones  
- convergence timeline  

4. Validate the final repaired proof

`
validator.check(repaired)
`

Should return a clean success object.

---

📓 Notebook Content Begins Here

---

Cell 1 — Title + Overview (Markdown)

`

02 — Agentic Tactic Repair Loop

Mapping Lean Goal Coordinates Back Into Prompt Context

This notebook demonstrates the agentic repair loop used by
Lean-Hallucination-Guard to correct hallucinated Lean proofs.

The repair loop works by:
- parsing Lean compiler error coordinates (line/column),
- mapping those coordinates back into the user's prompt context,
- generating a corrected tactic candidate,
- retrying until the proof converges.

This is the core mechanism that transforms hallucinated proof scripts
into valid Mathlib proofs.
`

---

Cell 2 — Import lhguard Modules (Python)

`
from lhguard import validator, mimicry, repair
`

---

Cell 3 — Generate a Hallucinated Proof (Python)

`
hallucinated = mimicry.simulatehallucinatedtactic("""
theorem mul_comm (a b : Nat) : a  b = b  a := by
  intros
  rewrite [Nat.mul_comm]
  exact rfl
""")

print("Hallucinated Proof:")
print(hallucinated)
`

---

Cell 4 — Run Initial Validation (Python)

`
initial = validator.check(hallucinated)

print("Initial Validator Output:")
print(initial)
`

Expected:

- invalid rewrite  
- incorrect tactic  
- mismatch between goal and lemma  

---

Cell 5 — Extract Lean Goal Coordinates (Python)

`
coords = repair.extract_coordinates(initial)

print("Extracted Coordinates:")
print(coords)
`

This shows:

- line number  
- column number  
- failing tactic region  
- failing lemma reference  

---

Cell 6 — Map Coordinates Back Into Prompt Context (Python)

`
context = repair.maptoprompt_context(hallucinated, coords)

print("Mapped Prompt Context:")
print(context)
`

This is the “agentic” part — the system reconstructs the intent behind the hallucinated tactic.

---

Cell 7 — Generate a Corrected Tactic Candidate (Python)

`
candidate = repair.generate_candidate(context)

print("Candidate Repair:")
print(candidate)
`

This should produce something like:

`
exact Nat.mul_comm a b
`

---

Cell 8 — Retry Until Convergence (Python)

`
repaired, timeline = repair.retryuntilconverged(hallucinated)

print("Repaired Proof:")
print(repaired)

print("\nConvergence Timeline:")
for step in timeline:
    print(step)
`

Timeline entries include:

- “parsed error coordinates”  
- “generated candidate tactic”  
- “validator success”  

---

Cell 9 — Validate the Final Proof (Python)

`
validator.check(repaired)
`

Should return a clean success object.

---

Cell 10 — Explain the Repair Loop (Markdown)

`

How the Agentic Repair Loop Works

1. The LLM produces a hallucinated tactic.
2. Lean rejects the tactic and provides error coordinates.
3. lhguard extracts the coordinates and maps them back into the prompt.
4. The system generates a corrected tactic candidate.
5. The validator checks the candidate.
6. The loop repeats until the proof converges.

This mechanism transforms syntactic/semantic mimicry into
deterministic proof correctness.
`

---

Cell 11 — Interactive Component (Python)

`
userhallucination = mimicry.simulatehallucinated_tactic("""
theorem add_assoc (a b c : Nat) : a + b + c = a + (b + c) := by
  intros
  simp
""")

repaired, timeline = repair.retryuntilconverged(user_hallucination)

print("Your Repaired Proof:")
print(repaired)
`

---

Cell 12 — Closing Notes (Markdown)

`

Summary

This notebook demonstrated:
- how lhguard extracts Lean error coordinates,
- how it maps them back into the prompt context,
- how it generates corrected tactics,
- how the retry loop converges to a valid Mathlib proof.

Next Notebook:
03manifoldprovenance_boundaries.md
`

---

