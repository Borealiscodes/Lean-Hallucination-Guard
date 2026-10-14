import logging
import sys
from pathlib import Path

def setup_logger(name: str = "lhguard", log_dir: str = "logs") -> logging.Logger:
    """Configures double-destination logs for raw terminals and disk analytics."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    # Block duplicate handlers if initialized repeatedly across threads
    if logger.handlers:
        return logger

    # Enforce safe log directory footprint layout
    log_path = Path(log_dir)
    log_path.mkdir(exist_ok=True)

    # Standardized system metric formatting
    formatter = logging.Formatter(
        '[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Console Stream Handler: Clean high-level milestones
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File System Handler: Complete compiler trace diagnostics
    file_handler = logging.FileHandler(log_path / "compiler_pipeline.log", encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

