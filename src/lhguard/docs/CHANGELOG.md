# Lean‑Hallucination‑Guard — Changelog

All notable changes to this project are documented here.  
This changelog follows a simple, human‑readable format suitable for provenance
audits and safety‑critical research environments.

---

## [1.0.0] — 2026‑10‑14  
### Initial Stable Release (Enforcement‑Aligned)

#### Added
- **Enforcement Triad**
  - `geometry.py` — Three‑Sphere invariants & collapse detection
  - `provenance.py` — humanitarian invariant & prohibited sphere checks
  - `interceptor.py` — deterministic abort & memory purge

- **Runtime Layer**
  - `validator.py` — Lean sandbox executor with structured results
  - `client.py` — deterministic correction loop (no LLM calls)
  - `watcher.py` — Markdown Lean block monitor with enforcement integration

- **Infrastructure Layer**
  - `utils/logger.py` — dual‑destination telemetry
  - `pyproject.toml` — PEP‑621 compliant packaging metadata
  - `README.md` — project overview and usage instructions

- **Documentation**
  - `CONTRIBUTING.md` — humanitarian‑aligned development rules
  - `CODE_OF_CONDUCT.md` — community interaction guidelines
  - `architecture.md` — system architecture and module interaction diagram
  - `security_model.md` — bounded non‑harm enclave security model

#### Removed
- Legacy Google‑style client logic:
  - prompt concatenation loops
  - brittle regex error parsing
  - uncontrolled retry behavior
  - non‑deterministic LLM scaffolding

#### Refactored
- Replaced all unsafe or ambiguous modules with deterministic, auditable
  enforcement‑aligned implementations.
- Unified logging footprint across runtime and enforcement layers.
- Consolidated documentation into a coherent, principled structure.

---

## [0.9.x] — Pre‑Release Development  
### (Internal, not published)

- Early prototypes of validator and client
- Initial enforcement logic experiments
- Temporary scaffolding for Lean execution
- Google‑style janky components (now fully removed)

---

## [0.1.0] — Project Initialization  
- Repository created  
- Basic folder structure established
