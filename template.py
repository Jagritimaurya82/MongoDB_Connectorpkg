import os
from pathlib import Path

# print(Path("a/b/c.txt")) # pathlib handles all "\" and "/" related issue (in windows there is "\"(backword slash) , for linux there is "/"(forword slash) )

package_name = "mongodb_connect"

list_of_files = [
    r".github\workflows\ci.yaml",
    r"src\__init__.py",
    f"src\\{package_name}\\__init__.py", #component is part of pipeline
    f"src\\{package_name}\\mongo_crud.py",
    r"test\__init__.py",
    r"test\unit\__init__.py",
    r"test\unit.py",
    r"test\integration\__init__.py",
    r"test\integration\int.py",
    "init_setup.sh", 
    "requirements.txt",         # for production environment
    "requirements_dev.txt",     # for development environment
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    r"experiment\experiments.ipynb",
]

 
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        # logging.info(f"Creating directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass # create empty file

