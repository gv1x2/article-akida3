"""Execute the four offline notebooks in order and preserve the source notebooks."""
from pathlib import Path
import argparse
import os

from nbclient import NotebookClient
import nbformat


ROOT = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT/"generated")
    args = parser.parse_args()
    out = args.output.resolve()
    out.mkdir(parents=True, exist_ok=True)
    nb_env = {**os.environ, "ARTICLE_RESULTS_DIR": str(out), "MPLBACKEND": "Agg"}
    notebooks = sorted((ROOT/"notebooks").glob("*.ipynb"))
    for path in notebooks:
        notebook = nbformat.read(path, as_version=4)
        nbformat.validate(notebook)
        client = NotebookClient(notebook, timeout=180, kernel_name="python3")
        client.execute(cwd=str(ROOT), env=nb_env)
        nbformat.write(notebook, out/(path.stem + ".executed.ipynb"))
        print(f"Passed {path.name}", flush=True)
    if len(notebooks) != 4:
        raise SystemExit(f"Expected four offline notebooks, found {len(notebooks)}")


if __name__ == "__main__":
    main()
