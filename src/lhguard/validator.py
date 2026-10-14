import subprocess
from pathlib import Path
from typing import NamedTuple
from .utils.logger import setup_logger

logger = setup_logger("lhguard.validator")

class ValidationResult(NamedTuple):
    is_valid: bool
    error_message: str

def validate_lean_code(code: str, workspace_dir: str = ".") -> ValidationResult:
    """Validates raw Lean 4 code strings inside an isolated compilation sandbox."""
    workspace = Path(workspace_dir)
    temp_file = workspace / "Verification_Enclave_Sandbox.lean"
    
    logger.debug(f"Writing temporary verification workspace to: {temp_file}")
    temp_file.write_text(code, encoding="utf-8")
    
    try:
        logger.info("Invoking Lake compiler environment validation pass...")
        process = subprocess.run(
            ["lake", "env", "lean", str(temp_file)],
            capture_output=True,
            text=True,
            timeout=25
        )
        
        if process.returncode == 0:
            logger.info("Verification Complete: Zero compiler syntax structural faults.")
            return ValidationResult(True, "")
        
        errors = (process.stderr + process.stdout).strip()
        logger.warning(f"Compiler validation fault detected (Exit Code {process.returncode}). Details logged.")
        logger.debug(f"Raw compiler traceback:\n{errors}")
        return ValidationResult(False, errors)
        
    except FileNotFoundError:
        err_msg = "Lake utility or Lean 4 toolchain binary is absent from system PATH execution parameters."
        logger.error(err_msg)
        return ValidationResult(False, err_msg)
    except subprocess.TimeoutExpired:
        err_msg = "Compilation cycle exceeded the designated 25-second gatekeeper timeout limit."
        logger.error(err_msg)
        return ValidationResult(False, err_msg)
    finally:
        if temp_file.exists():
            temp_file.unlink()
            logger.debug("Cleaned up sandbox temporary verification files.")
