# Cheat Sheet
clone → Get the repo <br>
branch → Create a feature branch<br>
checkout → Switch to it<br>
add → Stage your changes<br>
commit → Save your changes<br>
push → Upload your branch<br>
pull request → Ask to merge your work<br>
merge → Combine branches<br>

### **clone** – Get a copy of a remote repository
**Purpose**: Download an existing repo (e.g., from GitHub/GitLab) to your local machine.
```
git clone <repository-url>
```
### **branch** – Create or list branches
**Purpose**: Work on features/changes without affecting main.
* List branches:
```
git branch
```
* Create a new branch:
```
git branch <branch-name>
```
### **checkout** – Switch between branches
**Purpose**: Move to a different branch or create + switch in one step.
* Switch branches:
```
git checkout <branch-name>
```
### **add** – Stage changes
**Purpose**: Tell Git which file changes should be part of the next commit.
* Add specific file:
```
git add <file>
```
### **commit** – Save a snapshot of your changes
**Purpose**: Record your staged changes with a message.
```
git commit -m "Describe what you changed"
```
### **push** – Upload your commits to a remote repository
**Purpose**: Send your local commits to GitHub/GitLab/etc.
```
git push origin <branch-name>
```
### **pull request (PR)** – Ask to merge your branch into another
Technically done on GitHub/GitLab, not the terminal, but very important.
**Purpose**:
* Review your changes
* Discuss with teammates
* Merge into main or another branch

Typical sequence:
* Push your branch
* Open a PR on the website UI
* Get approvals
*  Merge

## **merge** – Combine one branch into another
**Purpose**: Bring changes from a feature branch into a base branch.
* Merge <branch> into the current branch:
```
git merge <branch-name>
```