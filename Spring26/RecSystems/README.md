# AI Club Workshop - 4/17 Recommendation Systems

## Setup Instructions:

### 1. Install uv, VS Code, and VS Code Python + Jupyter Extensions

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```


### 2. Clone the workshops repo & navigate to directory

```bash
git clone https://github.com/SDSUAIClub25-26/workshops.git
cd /workshops/Spring26/RecSystems
```

### 4. Install correct python version + deps
```bash
uv python install
uv sync
```

### 5. Open folder in VS Code

```bash
code .
```

### 6. Open the notebook file.

### 7.  In the upper-right corner, click **Select Kernel** and choose the interpreter from `.venv`.

### 8. Run the cells.


## Resources:
- [microsoft/recommenders](https://github.com/microsoft/recommenders) — rich set of examples
- [Surprise documentation](https://surpriselib.com/) — great for prototyping CF models
- [RecSys conference papers](https://recsys.acm.org/) — state of the art
- [Medium Article](https://medium.com/data-science/recommender-systems-a-complete-guide-to-machine-learning-models-96d3f94ea748) — a great article breaking down the theory in a digestable way
