import sys
import os
import subprocess

def main():
    if  len (sys.argv) < 2:
        print("Usage: new_data_project <project_name>")
        return
    project = sys.argv[1]

    #TO CREATE FOLDERS
    folders = [
        project,
        f"{project}/src",
        f"{project}/tests",
        f"{project}/data",
        f"{project}/notebooks"
    ]

    for folder in folders:
        os.makedirs(folder,exist_ok=True)


    #TO CREATE FILES ==========>>

    #CREATE README.md
    readme = F"{project}/README.md"
    with open(readme, "w") as f:
        f.write(f"# {project}")

    #CREATE README.md
    gitignore = F"{project}/.gitignore"
    with open(gitignore, "w") as f:
        f.write(f"# {project}")

    #CREATE REQUIREMENTS.TXT
    requirements = F"{project}/requirements.txt"
    with open(requirements, "w") as f:
        f.write(f"# {project}")

    #CREATE MAIN.PY
    main = F"{project}/main.py"
    with open(main, "w") as f:
        f.write(f"# {project}")

    #CREATE CONFIG.PY
    config = F"{project}/config.py"
    with open(config, "w") as f:
        f.write(f"# {project}")

    # INSTALL ENVIRONMENTS

    subprocess.run([sys.executable,
                    "-m",
                    "venv",
                    f"{project}/.venv"], check=True
    )

    # INSTALL PACKAGES
    python_path = f"{project}/.venv/Scripts/python.exe"

    subprocess.run([
        python_path,
        "-m",
        "pip",
        "install",
        "numpy",
        "pandas",
        "matplotlib",
        "numpy",
        "requests"
    ])

    # GIT INITIALIZATION
    subprocess.run([
        "git",
        "init"], 
        cwd=project
    )

    # OPEN VS CODE
    try:
        subprocess.run([
            "code.cmd","."], 
            cwd=project,
            check=True
        )
    except Exception as e:
        print(f"could not open vscode: {e}")

    print("New Project Creaated!")
    print("New environment Created!")
    print("Essential Packages Installed!")
    print("Git Created!")
    print("You can Start working now!") 