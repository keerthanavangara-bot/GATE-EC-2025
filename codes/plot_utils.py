from pathlib import Path
import os, shutil
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
FIGS = ROOT / "figs"
FIGS.mkdir(parents=True, exist_ok=True)

def savefig(fig, filename, dpi=180):
    """Save to repository figs/ and also Downloads when available; never opens a GUI."""
    path = FIGS / filename
    fig.savefig(path, dpi=dpi, bbox_inches="tight")
    destinations = []
    home_downloads = Path.home() / "Downloads"
    local_downloads = Path.cwd() / "Downloads"
    for d in (home_downloads, local_downloads):
        if d.exists() and d.is_dir() and d.resolve() != FIGS.resolve():
            destinations.append(d / filename)
    for dest in destinations:
        try:
            shutil.copy2(path, dest)
        except OSError:
            pass
    print(f"Saved figure: {path}")
    for dest in destinations:
        print(f"Copied figure: {dest}")
    return path
