# OpenCV Hand Detection Workshop - Getting Started Guide

Welcome to the Hand Detection Workshop! Follow these steps to set up your development environment before the workshop begins.

## Prerequisites

- A computer with a webcam
- Internet connection for initial setup
- Administrative privileges to install software

## Step 1: Install Python 3.11.9

### Windows (navigate to Powershell)
**Option One:**
1. Set up pyenv on your environment (check this [README](https://github.com/pyenv-win/pyenv-win) for how to do so)
2. Then install python 3.11.9 through this

**Option Two:**
1. Go to [python.org/downloads](https://www.python.org/downloads/)
2. Download Python 3.11.9 for Windows
3. **Important**: During installation, check "Add Python to PATH"
4. Verify installation by opening Command Prompt and typing:
   ```
   python --version
   ```
   You should see: `Python 3.11.9`


### macOS
1. brew install pyenv pyenv-virtualenv
2. pyenv install 3.11.9
3. eval "$(pyenv init -)"
4. eval "$(pyenv virtualenv-init -)"

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
   cd HandTrackingCV
   ```

   **Don't have git?** 
   - Download the workshop files as a ZIP from the repository
   - Extract to your Desktop
   - Open the folder in VS Code

## Step 4: Create a Virtual Environment

In VS Code's terminal, inside the workshop folder:

**As a note myenv is just an arbitrary name, you can name it what you want. I usually go with .venv**

### Windows
```bash
python -m venv myenv
myenv\Scripts\activate
```

### macOS/Linux
```bash
pyenv virtualenv 3.11.9 venv311
continue with virtual env
   ```
   python3 --version
   ```
   You should see: `Python 3.11.9`

You should see `(env)` at the beginning of your terminal prompt.

## Step 5: Install Dependencies

With your virtual environment activated:

```bash
pip install -r requirements.txt
```

This will install:
- OpenCV (computer vision library)
- MediaPipe (hand detection)
- Matplotlib (visualization)
- NumPy (numerical computing)
- Jupyter (notebooks)

## Step 6: Select Python Interpreter in VS Code

1. Press `Ctrl+Shift+P` (Cmd+Shift+P on Mac)
2. Type "Python: Select Interpreter"
3. Choose the interpreter from your virtual environment:
   - Look for the path containing `myenv` or your venv name

## Step 7: Run the imports in the completed notebook or create your own and import libraries

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
