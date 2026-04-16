## AI Club Workshop - 4/17 Recommendation Systems

Getting Setup (VS Code):
### 1. Clone the workshops repo
git clone https://github.com/SDSUAIClub25-26/workshops.git

### 2. Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

### 3. Create and activate a new virtual environment (this can also be located at the root of the workshops git repo)
uv venv ~/.venvs/recommenders --python 3.11
source ~/.venvs/recommenders/bin/activate

### 4. Install the core recommenders package and other dependencies
uv pip install recommenders scikit-surprise pandas matplotlib seaborn ipykernel

### 5. Create a Jupyter kernel
python -m ipykernel install --user --name recommenders --display-name "Python (recommenders)"

### 7. Within VSCode:
   a. Open the notebook: workshops/Spring26/RecSystems/recsys_workshop.ipynb;
   b. Select Jupyter kernel "Python (recommenders)";
   c. Run the notebook.
