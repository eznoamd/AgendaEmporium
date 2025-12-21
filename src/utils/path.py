from pathlib import Path
import sys

def get_style_path() -> str:
    if getattr(sys, "frozen", False):
        base = Path(sys.executable).parent
    else:
        base = Path(__file__).resolve().parent.parent

    return str(base / "ui" / "style.qss")

def get_data_path(path=""):
    _DATA = "../data/"
    return _DATA + path
