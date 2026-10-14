"""
watcher.py — Continuous Workspace Monitor with Safety Enforcement
Lean-Hallucination-Guard (lhguard)
License: Bounded Non-Harm Enclave — Version 1.2 (Oct 14, 2026)

This module:
• Monitors Markdown files for Lean code blocks,
• Validates each block using the enforcement-aware validator,
• Enforces provenance boundaries and humanitarian invariants,
• Triggers interceptor self-termination on violations,
• Logs results using the dual-destination telemetry logger.

This watcher is strictly non-dual-use and cannot be repurposed for
trajectory prediction, guidance loops, or coercive surveillance.
"""

from __future__ import annotations
import re
import pathlib
import time

from lhguard.validator import validate
from lhguard.provenance import check_boundaries
from lhguard.interceptor import enforce
from lhguard.utils.logger import setup_logger

logger = setup_logger("lhguard.watcher")


# ------------------------------------------------------------
#  Lean Block Extraction
# ------------------------------------------------------------

LEAN_BLOCK_PATTERN = re.compile(r"```lean\n(.*?)```", re.DOTALL)

def extract_lean_blocks(text: str) -> list[str]:
    """Extract all Lean code blocks from a Markdown document."""
    return [m.group(1).strip() for m in LEAN_BLOCK_PATTERN.finditer(text)]


# ------------------------------------------------------------
#  File Watcher
# ------------------------------------------------------------

def watch_markdown(path: str, interval: float = 1.0):
    """
    Continuously monitors a Markdown file for Lean code blocks.
    Validates each block using the enforcement-aware validator.
    """
    file_path = pathlib.Path(path)
    last_content = None

    logger.info(f"Watcher activated for {file_path}")

    while True:
        if not file_path.exists():
            logger.warning(f"File missing: {file_path}")
            time.sleep(interval)
            continue

        content = file_path.read_text()

        if content != last_content:
            logger.info(f"Change detected in {file_path}")
            last_content = content

            blocks = extract_lean_blocks(content)
            logger.info(f"Found {len(blocks)} Lean code blocks")

            for idx, block in enumerate(blocks, start=1):
                logger.info(f"Validating block #{idx}")

                # Provenance check
                prov = check_boundaries(block)
                prov_violation = enforce(prov)
                if prov_violation:
                    logger.error(f"Safety violation in block #{idx}: {prov_violation.reason}")
                    continue

                # Lean validation
                result = validate(block)

                if result.safety_violation:
                    logger.error(f"Interceptor triggered in block #{idx}: {result.errors}")
                    continue

                if result.success:
                    logger.info(f"Block #{idx} compiled successfully")
                else:
                    logger.warning(f"Block #{idx} failed:\n{result.errors}")

        time.sleep(interval)
