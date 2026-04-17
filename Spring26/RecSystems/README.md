# AI Club Workshop - 4/17 Recommendation Systems

## Setup Instructions:

### Prerequisites
Install the following first:

- [uv](https://docs.astral.sh/uv/)
- VS Code
- VS Code Python extension
- VS Code Jupyter extension

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Clone the repository
```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

### Install the pinned Python version and project dependencies
```bash
uv python install 3.11.15
uv sync
```

This project is pinned to Python 3.11.15 and uses a locked dependency set.

### Open in VS Code
```bash
code .
```

### Open the notebook
Open the workshop notebook in VS Code.

### Select the kernel
In the upper-right corner of the notebook, click **Select Kernel** and choose the interpreter from:

```text
.venv
```

### Run the notebook
You should now be able to run all cells.

## Troubleshooting

### Wrong Python version
If VS Code selects the wrong interpreter, manually choose the one inside `.venv`.

### Fresh reinstall
If your environment gets into a bad state, delete the local environment and resync:

```bash
rm -rf .venv
uv sync
```


## Resources:
- [microsoft/recommenders](https://github.com/microsoft/recommenders) — rich set of examples
- [Surprise documentation](https://surpriselib.com/) — great for prototyping CF models
- [RecSys conference papers](https://recsys.acm.org/) — state of the art
- [Medium Article](https://medium.com/data-science/recommender-systems-a-complete-guide-to-machine-learning-models-96d3f94ea748) — a great article breaking down the theory in a digestable way
