## 1. Download and Install the Latest Python Version
- [Python Downloads](https://www.python.org/downloads/)

## 2. Download and Install PyCharm Professional Edition
- [PyCharm Professional Download](https://www.jetbrains.com/pycharm/download/?section=windows)

## 3. Clone GitHub Repository
- Open the command prompt and navigate to the folder where you want to clone the project.
- Use this command to clone the repository:  
  `git clone https://github.com/GezimC/DataScience_2026.git`

### 3.1 Alternative - Download as a ZIP File
- Note: You can download the project as a ZIP file, but this will only give you a snapshot of the current code. You will not be able to pull the latest changes later.

## 4. Create a Virtual Environment (`.venv` folder)
- Open the command prompt in your project folder.
- Run the following command to create the virtual environment:  
  `py -m venv .venv`

## 5. Install Required Libraries
- In the project terminal, run this command to install all the required libraries from the `requirements.txt` file:  
  `pip install -r requirements.txt`

### After completing these steps, you should be able to run Python scripts or Jupyter files.

---

### Recommendation:
- **Always pull the latest changes before working on this project:**  
  `git pull origin main`
- **Commit your changes frequently:**  
  `git add .`  
  `git commit -m "My latest changes"`
- If you want to experiment with code, it's recommended to create a new Jupyter file to avoid conflicts when pulling changes.
- To reset your local changes and get a fresh copy, run:  
  `git reset --hard origin/main`  
  (This will discard all local changes).