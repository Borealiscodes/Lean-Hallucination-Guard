import time
import re
from pathlib import Path
from typing import Callable, Dict, List
from .utils.logger import setup_logger
from .validator import validate_lean_code

logger = setup_logger("lhguard.watcher")

class WorkspaceWatcher:
    def __init__(self, target_dir: str, callback_action: Optional[Callable[[Path, List[str]], None]] = None, interval: float = 1.0):
        """
        Args:
            target_dir: System path directory path to monitor.
            callback_action: Action function executed when file changes register.
            interval: Loop cooling time interval in seconds.
        """
        self.target_dir = Path(target_dir)
        self.callback = callback_action
        self.interval = interval
        self.snapshot: Dict[Path, float] = {}

    def _scan_workspace(self) -> Dict[Path, float]:
        """Returns a snapshot dictionary mapping paths to modification timestamps."""
        if not self.target_dir.exists():
            return {}
        return {p: p.stat().st_mtime for p in self.target_dir.rglob("*.md") if p.is_file()}

    def _parse_markdown_blocks(self, content: str, lang: str = "lean") -> List[str]:
        """Extracts code blocks matching a specific language identifier."""
        pattern = rf'```{lang}\n(.*?)\n```'
        return re.findall(pattern, content, re.DOTALL)

    def process_file(self, path: Path):
        """Extracts and verifies all embedded Lean blocks inside a single markdown file."""
        try:
            content = path.read_text(encoding="utf-8")
            blocks = self._parse_markdown_blocks(content)
            
            if not blocks:
                logger.debug(f"Scan complete: No Lean blocks discovered in {path.name}.")
                return

            logger.info(f"Evaluating {len(blocks)} code block(s) within structural document: {path.name}")
            
            all_valid = True
            for idx, block in enumerate(blocks, 1):
                result = validate_lean_code(block, workspace_dir=str(path.parent))
                if not result.is_valid:
                    all_valid = False
                    logger.error(f"❌ Structural Fault in {path.name} [Block {idx}]:\n{result.error_message}")
                else:
                    logger.info(f"✅ Verified {path.name} [Block {idx}]: Static type check passed.")

            if self.callback:
                self.callback(path, blocks)
                
        except Exception as e:
            logger.error(f"Failed to process markdown file content: {e}")

    def start_monitoring(self):
        """Launches the persistent file system evaluation thread loop."""
        logger.info(f"Target system watcher active. Monitoring directory: {self.target_dir.resolve()}")
        self.snapshot = self._scan_workspace()
        
        try:
            while True:
                time.sleep(self.interval)
                current_state = self._scan_workspace()
                
                for path, mtime in current_state.items():
                    if path not in self.snapshot or mtime > self.snapshot[path]:
                        logger.info(f"Modification delta captured on file: {path.name}")
                        self.process_file(path)
                            
                self.snapshot = current_state
        except KeyboardInterrupt:
            logger.info("Workspace watcher system gracefully deactivated via human sign-off request.")
