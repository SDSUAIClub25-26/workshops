# OpenCV Hand Detection Workshop - Getting Started Guide

Welcome to the Hand Detection Workshop! Follow these steps to set up your development environment before the workshop begins.

## Prerequisites

- A computer with a webcam
- Internet connection for initial setup
- Administrative privileges to install software

You can also access these steps here: https://code.visualstudio.com/docs/python/python-tutorial

## Step 1: Install Python 3.11.9

### Windows
1. Go to [python.org/downloads](https://www.python.org/downloads/)
2. Download Python 3.11.9 for Windows
3. **Important**: During installation, check "Add Python to PATH"
4. Verify installation by opening Command Prompt and typing:
   ```
   python --version
   ```
   You should see: `Python 3.11.9`

**Note: If you have multiple python versions (like 3.12 or 3.13), the above command may return another version like 3.13.3. If so, follow steps below:**
1. Run `py -0` to show all installed Python versions and you should see one for 3.11
2. To check that you have 3.11.9 installed specifically run: `py -3.11 --version` -> should return 'Python 3.11.9'

<img width="1795" height="807" alt="cmd-screenshot-workshop" src="https://github.com/user-attachments/assets/c0d744ce-8f7a-412d-821f-5ba276c574d2" />


### macOS
1. Open a terminal and check if brew is installed. Run ```brew --version```. If installed, jump to step 3.
2. Install brew by running this command:
   ```
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   sudo xcodebuild -license accept
   ```
3. brew install pyenv pyenv-virtualenv
4. pyenv install 3.11.9
5. eval "$(pyenv init -)"
6. eval "$(pyenv virtualenv-init -)"
7. pyenv virtualenv 3.11.9 venv311
8. pyenv activate venv311

**Note: to deactivate the virtual environment, run** ```pyenv deactivate```.

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3.11 python3.11-venv python3.11-pip
python3.11 --version
```

## Step 2: Install VS Code

1. Download VS Code from [code.visualstudio.com](https://code.visualstudio.com/)
2. Install the Python extension:
   - Open VS Code
   - Go to Extensions (Ctrl+Shift+X)
   - Search for "Python" by Microsoft
   - Click Install

## Step 3: Clone the Workshop Repository

1. Open VS Code
2. Open Terminal in VS Code: `Terminal → New Terminal`
3. Navigate to where you want the workshop folder:
   ```bash
   cd Desktop  # or wherever you prefer
   ```
**Note: you can also perform these steps using the VS Code Interface, clicking "Clone Github Repository" and pasting the url**

4. Clone the repository:
   ```bash
   git clone https://github.com/SDSUAIClub25-26/WorkshopMaterials.git
   ```
5. Open workshop folder in VS Code:
   ```bash
   cd WorkshopMaterials
   code .
   ```
**Don't have git?** 
- For Windows: you can install it [here](https://git-scm.com/downloads), then run installer and follow default settings (keep clicking 'Next'), then restart VS Code
- For Mac: You can run `brew install git` (if you have homebrew installed)

## Step 4: Create a Virtual Environment in Workshop Folder

Once you have opened 'WorkshopMaterials' folder in VS Code:

### Windows
1. To open command palette, hit `Ctrl+Shift+P`, start typing 'Python: Create Environment'
2. It should now present a list of environment types, either venv or conda. Click venv
3. Now you should see a list of python interpreters that can be used. Select the one for Python 3.11.9
4. A notification will now pop up showing that your environment is being created:

<img width="644" height="113" alt="image" src="https://github.com/user-attachments/assets/1729f0e4-a0fb-4f0c-ac41-2ac2ed8447d4" />

5. Ensure the environment is selected by going back to 'Python: Select Interpeter' from the command palette and selecting the .venv

### MacOS
Since we used pyenv, no local virtual envornment is needed in the project directory.
1. Hit `Cmd+Shift+P`
2. Search `Python: Select Interpreter`.
3. Select the version that says `venv311`.
4. In the HandTracking_OpenCV_Completed.ipynb file, change the interpreter in the top right to venv311

## Step 5: Install Dependencies

With your virtual environment activated, open up a terminal and run:

```bash
pip install -r requirements.txt
```

This will install:
- OpenCV (computer vision library)
- MediaPipe (hand detection)
- Matplotlib (visualization)
- NumPy (numerical computing)
- ipykernel (notebooks)

**Note (for Mac users): sometimes ipykernel will not download. When running the first block of code, you may get prompted to install the necessary package. Accept it and after it is downloaded, rerun the block of code.** 

## Step 6: Select correct Python Interpreter in VS Code (if it prompts you again)

1. Press `Ctrl+Shift+P` (Cmd+Shift+P on Mac)
2. Type "Python: Select Interpreter"
3. Choose the interpreter from your virtual environment:
   - Look for the path containing `myenv` or your venv name

## Step 7: Run the imports in the completed notebook or create your own notebook and import libraries

If 'Everything Imported Successfully' is printed out you are good to go!


## Troubleshooting

### Python Version Issues
- Make sure you're using Python 3.11.9 specifically
- If you have multiple Python versions, you might need to use `python3.11` instead of `python` or another version you have installed like 3.13

### Permission Errors
- On Windows, try running VS Code as Administrator
- On macOS/Linux, you might need `sudo` for some commands

### Camera Not Working
- Check if other applications are using your camera
- Try restarting VS Code
- Test camera in app
- If not, you can just follow along

### Import Errors
- Make sure your virtual environment is activated (you should see `(venv)` in terminal)
- Try reinstalling requirements: `pip install -r requirements.txt --force-reinstall`

## Workshop Day Checklist

Before the workshop starts, make sure:
- [ ] Python 3.11.9 is installed
- [ ] VS Code is open with the workshop folder
- [ ] Virtual environment is activated
- [ ] All dependencies are installed
- [ ] Camera is working (or you're okay with following along)

## What's Next?

Once setup is complete, we'll dive into:
1. Understanding MediaPipe hand landmarks
2. Creating gesture-based interactions
3. Building a finger counting application


Get ready for an awesome hands-on experience! 🙌
