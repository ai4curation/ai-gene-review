"""Re-run unchanged production capacity logic, writing only additive results."""
import importlib.util
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ORIGINAL = HERE.parents[1] / "check_capacity.py"
spec = importlib.util.spec_from_file_location("methionine_original_capacity", ORIGINAL)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
# Original ROOT/MODULE are established by import. HERE is used only for output.
module.HERE = HERE
module.main()
