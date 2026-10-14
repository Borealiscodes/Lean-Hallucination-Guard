# 📁 CONTRIBUTING.md

`markdown

Contributing to Lean‑Hallucination‑Guard

Thank you for your interest in contributing to Lean‑Hallucination‑Guard (lhguard).  
This project implements a bounded non‑harm enclave for Lean 4, enforcing
humanitarian‑aligned constraints on LLM‑generated proofs and preventing
syntactic or semantic mimicry drift.

Because this project includes safety‑critical enforcement modules, all
contributions must follow the rules below.

---

🛡️ 1. Humanitarian‑Invariant Development Rules

All contributions must comply with LICENSE v1.2 (Bounded Non‑Harm Enclave):

- No dual‑use math (trajectory prediction, guidance loops, targeting vectors).
- No coercive surveillance logic.
- No axis‑rotation transformations that strip humanitarian metadata.
- No modules that bypass or weaken the enforcement triad:
  - geometry.py
  - provenance.py
  - interceptor.py

Any PR introducing prohibited exploitation vectors will be rejected.

---

🧩 2. Repository Architecture

Before contributing, familiarize yourself with the core modules:

- geometry.py — spectral collapse modeling & Three‑Sphere invariants  
- provenance.py — humanitarian invariant & prohibited sphere detection  
- interceptor.py — self‑termination & memory purge  
- validator.py — Lean sandbox executor with safety enforcement  
- client.py — agentic correction loop  
- watcher.py — workspace monitor  
- utils/logger.py — dual‑destination telemetry  

All new modules must integrate cleanly with this architecture.

---

🔍 3. Code Style & Standards

- Use Python 3.10+.
- Follow PEP 8 and PEP 621 conventions.
- Avoid unnecessary dependencies; the project intentionally maintains a minimal footprint.
- All safety‑critical logic must be deterministic and auditable.
- No network calls inside runtime modules.
- No LLM calls inside core modules (validator, client, watcher).

---

🧪 4. Testing Requirements

All new features must include:

- unit tests for deterministic behavior  
- safety tests validating:
  - humanitarian invariant enforcement  
  - prohibited sphere detection  
  - interceptor activation  
  - geometric collapse detection  

Tests must not rely on external services or LLMs.

---

📜 5. Commit Message Conventions

Use conventional commits:

- feat: new features  
- fix: bug fixes  
- docs: documentation updates  
- refactor: structural improvements  
- build: packaging or dependency changes  
- test: test suite updates  

Examples:

`
feat(validator): add geometric collapse enforcement to Lean sandbox
docs(architecture): update enforcement triad diagram
refactor(client): remove legacy prompt concatenation loop
`

---

🔒 6. Security & Provenance

All contributors must:

- preserve provenance boundaries  
- avoid introducing ambiguous or unsafe math  
- ensure logs remain non‑sensitive  
- avoid embedding personal contact information in code or docs  
- maintain deterministic behavior in all enforcement modules  

Security reviews may be requested for complex PRs.

---

🤝 7. How to Submit a Contribution

1. Fork the repository.  
2. Create a feature branch.  
3. Ensure your changes pass all tests.  
4. Submit a pull request with:
   - a clear description  
   - justification for the change  
   - confirmation of humanitarian‑invariant compliance  

PRs that modify enforcement logic will undergo additional review.

---

🌱 8. Respect the Project’s Purpose

Lean‑Hallucination‑Guard is a research tool designed to:

- improve interpretability  
- prevent harmful drift  
- enforce humanitarian constraints  
- support safe geometric‑AI development  

Contributions should strengthen these goals, not dilute them.

---

Thank you for helping maintain a safe, rigorous, and principled project.
`

---

