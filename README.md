# DAIC-WOZ classifiers on Akida — reviewer materials

Four Jupyter notebooks reproduce the numerical analyses from the saved aggregate metrics. The notebooks run on an ordinary computer with Python 3.11.

| Notebook | Results covered |
| --- | --- |
| [01 Main study](notebooks/01_main_study.ipynb) | 30,600 fits, deployment and recovery counts, validation ranking, M9 partition results, matched comparisons, and inference stages. |
| [02 Exploratory extension](notebooks/02_extension.ipynb) | 900 fits, metrics by design, and software-to-board agreement. |
| [03 Sustained measurements](notebooks/03_sustained.ipynb) | CPU and Akida latency, counted inference intervals, model mapping, and monitored power and energy. |
| [04 Intermittent measurements](notebooks/04_intermittent.ipynb) | Paired LowPower results, request latency, and CPU-package controls. |

## Run

```sh
python3.11 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python run_notebooks.py
```

The command saves computed tables, plots, and executed notebooks in `generated/`. The notebooks can also be run individually in a Jupyter interface using this Python environment.

The CSVs in `data/` contain aggregate fit or measurement metrics. Partition, seed, and measurement identifiers describe the experiment. Participant-level materials are governed by the DAIC-WOZ data-use terms. Eligible researchers can apply to the USC Institute for Creative Technologies (USC ICT) for access to the original DAIC-WOZ corpus. Training and hardware acquisition are described in the manuscript and use the original data and device. [DAIC-WOZ access](https://dcapswoz.ict.usc.edu/)
