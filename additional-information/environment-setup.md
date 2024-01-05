# Environment Setup

## Windows Computer

### 1. Install Python

Download the latest version of Python from the official website: [Python Downloads](https://www.python.org/downloads/)

During installation, make sure to check the box that says "Add Python to PATH." This will allow you to run Python from the command line.

### 2. Install a Code Editor

Choose a code editor for a better coding experience. [Visual Studio Code](https://code.visualstudio.com/) is a popular choice. Download and install it.

### 3. Verify Installation

Open a command prompt and run the following commands to verify the installations:

```bash
python --version
```

This should display the installed Python version.

```bash
pip --version
```

This should display the version of the package manager for Python.

## macOS

### 1. Install Homebrew (if not already installed)

Open Terminal and run the following command:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 2. Install Python

Use Homebrew to install Python:

```bash
brew install python
```

### 3. Install a Code Editor

You can use Visual Studio Code on macOS as well. Install it using Homebrew:

```bash
brew install --cask visual-studio-code
```

## Online IDE

If you are using a chromebook, you will have to use an online IDE.

### [Replit](https://replit.com/)

1. Visit [Replit](https://replit.com/) and sign up for an account.
2. Create a new Repl (project) for your Python code.
3. Start coding in the online environment without the need for any installations.

## Additional Tips

- **Understanding Virtual Environments:**
  Create a virtual environment for the project using the following command:

  ```bash
  python -m venv venv
  ```

  Activate the virtual environment:

  - On Windows: `.\venv\Scripts\activate`
  - On macOS: `source venv/bin/activate`

  This isolates project dependencies, preventing conflicts with other projects.

- **Troubleshooting:**
  If any issues arise during the installation or setup process, let me know. I'll be happy to help.
