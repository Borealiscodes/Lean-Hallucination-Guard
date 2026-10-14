# 📁 architecture.md

`markdown

Lean‑Hallucination‑Guard — System Architecture

Lean‑Hallucination‑Guard (lhguard) is a bounded non‑harm enclave designed to
protect Lean 4 from syntactic and semantic mimicry drift when interacting with
LLMs. The architecture is built around a safety‑critical enforcement triad and
a deterministic validation pipeline.

This document explains how the system is structured, how modules interact, and
how humanitarian‑aligned constraints are enforced throughout the runtime.

---

🧭 1. High‑Level Overview

The architecture consists of three layers:

1. Enforcement Layer  
   - geometry.py  
   - provenance.py  
   - interceptor.py  

2. Runtime Layer  
   - validator.py  
   - client.py  
   - watcher.py  

3. Infrastructure Layer  
   - utils/logger.py  
   - utils/init.py  
   - pyproject.toml  

These layers form a closed, deterministic system that prevents unsafe drift,
ensures provenance integrity, and maintains humanitarian alignment.

---

🛡️ 2. Enforcement Triad

The enforcement triad is the core of the system. Every Lean execution passes
through these modules before any computation occurs.

2.1 geometry.py — Geometric Stability & Collapse Detection

- Implements symbolic Three‑Sphere invariants.  
- Detects geometric collapse or semantic drift.  
- Uses synthetic manifolds (never real embeddings) to avoid dual‑use vectors.  
- Flags collapse conditions before Lean execution.

2.2 provenance.py — Humanitarian Invariant & Boundary Checks

- Enforces LICENSE v1.2 (Bounded Non‑Harm Enclave).  
- Detects prohibited exploitation spheres.  
- Prevents dual‑use math, coercive transformations, or unsafe operators.  
- Ensures all code remains within humanitarian constraints.

2.3 interceptor.py — Self‑Termination & Memory Purge

- Activated when geometry or provenance detects violations.  
- Aborts execution deterministically.  
- Logs violation details through the telemetry system.  
- Ensures no unsafe computation proceeds.

---

🔧 3. Runtime Layer

The runtime layer executes Lean code safely and provides deterministic correction
loops and workspace monitoring.

3.1 validator.py — Lean Sandbox Executor

- Runs Lean code inside a temporary scratchpad.  
- Extracts compiler errors and unsolved goals.  
- Applies enforcement triad before execution.  
- Returns structured validation results.

3.2 client.py — Agentic Correction Loop

- Iteratively validates Lean code.  
- Generates structured correction hints (no LLM calls inside module).  
- Aborts on safety violations.  
- Provides deterministic, auditable correction steps.

3.3 watcher.py — Workspace Monitor

- Scans Markdown files for Lean code blocks.  
- Validates each block using the enforcement triad.  
- Logs results through dual‑destination telemetry.  
- Ensures safe development in notebooks and documentation.

---

📡 4. Infrastructure Layer

These modules support logging, packaging, and project structure.

4.1 utils/logger.py — Dual‑Destination Telemetry

- Console logs for human‑readable output.  
- File logs for full compiler traces.  
- Prevents duplicate handlers.  
- Ensures safe, non‑sensitive logging footprint.

4.2 utils/init.py

- Exposes logging utilities.  
- Maintains clean namespace boundaries.

4.3 pyproject.toml

- Defines package metadata and dependencies.  
- Provides CLI entrypoints (lhguard-validate, lhguard-watch).  
- Ensures deterministic packaging and distribution.

---

🧩 5. Module Interaction Diagram

`
                ┌──────────────────────────────┐
                │        Enforcement Triad      │
                │ geometry • provenance • interceptor │
                └───────────────┬──────────────┘
                                │
                                ▼
                ┌──────────────────────────────┐
                │         validator.py          │
                │ Lean sandbox + safety checks  │
                └───────────────┬──────────────┘
                                │
                                ▼
                ┌──────────────────────────────┐
                │          client.py            │
                │ agentic correction loop       │
                └───────────────┬──────────────┘
                                │
                                ▼
                ┌──────────────────────────────┐
                │          watcher.py           │
                │ workspace monitor             │
                └──────────────────────────────┘
`

---

🔒 6. Humanitarian‑Aligned Design Principles

The architecture is built around:

- Determinism — no uncontrolled LLM loops inside core modules.  
- Non‑dual‑use math — no trajectory vectors, no guidance operators.  
- Provenance integrity — all code must remain within humanitarian bounds.  
- Safe geometric reasoning — symbolic invariants only, no real embeddings.  
- Transparent logging — dual‑destination telemetry for audits.  
- Abort‑on‑violation — interceptor ensures safety is never optional.

---

🌍 7. Purpose of the Architecture

Lean‑Hallucination‑Guard exists to:

- prevent harmful drift in LLM‑generated Lean proofs  
- enforce humanitarian constraints  
- support geometric‑AI interpretability research  
- provide deterministic correction loops  
- maintain safe collaboration environments  

This architecture ensures the project remains principled, rigorous, and aligned
with its non‑harm mission.

`

---

If you want, I can now generate security_model.md, the next file in your sequence.
