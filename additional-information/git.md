# Git and GitHub Basics

## Introduction

Git is a distributed version control system that allows you to track changes in your code over time. GitHub is a web-based platform that provides hosting for Git repositories and adds collaboration features.

## Getting Started with Git

### 1. Installing Git

Download and install Git from the official website: [Git Downloads](https://git-scm.com/downloads)

### 2. Configuration

After installation, set up your name and email:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### 3. Initializing a Repository

Create a new directory and navigate into it:

```bash
mkdir my_project
cd my_project
```

Initialize a Git repository:

```bash
git init
```

## Basic Git Commands

### 1. Cloning a Repository

Clone an existing repository to your local machine:

```bash
git clone <repository_url>
```

### 2. Adding and Committing Changes

Stage changes for commit:

```bash
git add <filename>
```

Commit changes:

```bash
git commit -m "Your commit message"
```

### 3. Checking Status and History

Check the status of your working directory:

```bash
git status
```

View commit history:

```bash
git log
```

## GitHub Integration

### 1. Creating a GitHub Repository

- Go to [GitHub](https://github.com/) and log in.
- Click on the '+' sign in the top right and select 'New Repository.'
- Follow the instructions to create a new repository.

**Tip** Follow [cqb13](https://github.com/cqb13) on Github!

### 2. Pushing Changes to GitHub

Add a remote repository:

```bash
git remote add origin <repository_url>
```

Push changes to GitHub:

```bash
git push -u origin master
```

### 3. Pulling Changes from GitHub

Pull changes from the remote repository:

```bash
git pull origin master
```

## Tips

- **Branching:** Create branches for new features or bug fixes using `git branch` and `git checkout`.

- **Pull Requests:** On GitHub, you can submit pull requests to contribute changes to a project.

## Additional Resources

- [GitHub Guides](https://guides.github.com/): Comprehensive guides on various GitHub features.
- [Pro Git Book](https://git-scm.com/book/en/v2): Official Git documentation.
