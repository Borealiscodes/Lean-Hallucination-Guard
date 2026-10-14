# 🛡️ Lean‑Hallucination‑Guard (lhguard)

Lean‑Hallucination‑Guard is a safety‑critical enforcement enclave for Lean 4.  
It prevents syntactic mimicry and semantic mimicry in LLM‑generated Lean
proofs using geometric stability checks, humanitarian‑aligned provenance
constraints, and deterministic abort logic.

This project is not a validator.  
It is a boundary.

It ensures that Lean code — especially code produced by large models — remains:
- safe  
- interpretable  
- non‑dual‑use  
- humanitarian‑aligned  
- geometrically stable  
- provenance‑preserving  

If a transformation violates these principles, execution terminates immediately.

---

🧠 Syntactic Mimicry vs Semantic Mimicry

Large language models generate Lean code using two distinct failure modes.

🧩 Syntactic Mimicry — token‑pattern imitation

LLMs imitate the surface form of Lean:

- tactic shapes  
- lemma names  
- proof pacing  
- keyword sequences  
- indentation patterns  

This is pattern completion, not reasoning.

📐 Mathematical framing

Syntactic mimicry corresponds to generating elements of a free magma  
over the token alphabet \( X \):

`math
M(X) = \text{all binary trees over } X
`

LLMs generate trees that look like valid Lean derivations but do not correspond
to meaningful proof objects.

📚 Academic references

- Chomsky (1995), The Minimalist Program — syntax as algebraic tree structure  
- Merrill (2020), ACL — transformers approximate tree languages  

---

🧭 Semantic Mimicry — reasoning‑shaped text continuation

Semantic mimicry is deeper: the model imitates the shape of mathematical
reasoning without performing actual semantic operations.

This produces:

- “fake” lemma applications  
- “fake” rewrites  
- “fake” goal closures  
- “fake” reasoning chains  

These look correct but lack Lean’s semantic transformations.

📐 Mathematical framing

Semantic mimicry corresponds to generating sequences that approximate semantic
operators without executing them:

`math
\text{LLM output} \approx f_{\text{semantic}}(x)
\quad \text{but is actually} \quad
f_{\text{syntactic}}(x)
`

This mismatch between syntactic and semantic representation spaces is well
documented: syntax and semantics exhibit weak observable correspondence.

📚 Academic references

- Bender & Koller (2020), ACL — LLMs model form, not meaning  
- Piantadosi & Hill (2022), Cognition — meaning cannot be inferred from surface form  
- Chiang & Cholak (2023), ICLR — LLM proofs exhibit semantic drift even when syntactically correct  
- Wu et al. (2024), NeurIPS — LLMs fail symbolic reasoning even with perfect syntax  

---

🌱 Simple Accessibility Example

A gentle illustration of syntactic vs semantic mimicry

Imagine a student who has memorized the shape of a math proof but doesn’t
understand the math.

🧩 Syntactic mimicry example
They write:

> “We apply the lemma, rewrite the goal, and close the proof.”

It looks like a proof, but nothing actually happens.

🧭 Semantic mimicry example
They say:

> “Since the function is continuous, the derivative is zero.”

This sounds like reasoning, but it’s false — continuity does not imply zero
derivative.

🛡️ Why lhguard matters
LLMs do the same thing: they produce Lean code that looks correct but does not
perform the semantic operations Lean requires.

Lean‑Hallucination‑Guard detects this mismatch and stops unsafe or meaningless
proofs before they reach the Lean kernel.

---

🛡️ Enforcement Triad

Every Lean execution passes through three mandatory enforcement modules.

🔷 geometry.py — Spectral Collapse & Drift Detection

Symbolic Three‑Sphere invariants detect:

- semantic drift  
- geometric collapse  
- unsafe operator chains  
- destabilizing transformations  

No real‑world coordinate embeddings.  
No dual‑use math.

🔶 provenance.py — Humanitarian Invariant Enforcement

Implements LICENSE v1.2 (Bounded Non‑Harm Enclave):

- prohibited exploitation sphere detection  
- intent boundary checks  
- metadata preservation  
- humanitarian constraint enforcement  

If a transformation could be repurposed for harm, it is rejected.

🔺 interceptor.py — Deterministic Abort & Memory Purge

If geometry or provenance detects a violation:

- execution halts  
- memory is purged  
- telemetry logs the violation  
- no unsafe computation proceeds  

Safety is not optional.

---

🧭 System Architecture

The system is organized into three layers.

🛡️ 1. Enforcement Layer
- geometry.py  
- provenance.py  
- interceptor.py  

⚙️ 2. Runtime Layer
- validator.py — Lean sandbox executor  
- client.py — deterministic correction loop  
- watcher.py — Markdown Lean block monitor  

🧱 3. Infrastructure Layer
- utils/logger.py — dual‑destination telemetry  
- pyproject.toml — PEP‑621 metadata  

Full architecture: docs/architecture.md.

---

🚀 Installation

Requires Python 3.10+.

`bash
pip install .
`

Development mode:

`bash
pip install -e .
`

---

🔧 CLI Tools

Validate Lean files
`bash
lhguard-validate path/to/file.lean
`

Watch Markdown files for Lean code blocks
`bash
lhguard-watch path/to/notebook.md
`

Both commands route execution through the enforcement triad.

---

📡 Logging

Telemetry is dual‑destination:

- Console logs — human‑readable  
- File logs — full compiler traces  

Logs are non‑sensitive and provenance‑aligned.

---

🔒 Security Model

Lean‑Hallucination‑Guard enforces the Humanitarian Invariant:

> No output, transformation, or operator may be used to harm, target, coerce,
> or exploit any individual or population.

The system rejects:

- dual‑use mathematical operators  
- coercive or surveillance logic  
- unsafe axis‑rotation transformations  
- collapse operators that strip humanitarian metadata  

Full security model: docs/security_model.md.

---

🤝 Contributing

Contributions must follow:

- CONTRIBUTING.md — technical rules  
- CODEOFCONDUCT.md — human interaction rules  
- LICENSE.md — humanitarian constraints  

Unsafe or dual‑use contributions will be rejected.

---

📝 Changelog

See docs/CHANGELOG.md.

---

🌍 Purpose

Lean‑Hallucination‑Guard exists to support:

- geometric‑AI interpretability  
- safe experimentation  
- humanitarian‑aligned research  
- deterministic correction loops  
- principled collaboration  

This project is a boundary — not a loophole.
`

---

