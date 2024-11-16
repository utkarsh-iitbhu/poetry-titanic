# Titanic prediction with Poetry

Overview: 
Poetry is a Python dependency management and packaging tool that helps manage libraries and applications with ease. It simplifies the process of handling dependencies, version management, and packaging Python projects.

1. Installation
Install Poetry Globally: To install Poetry globally, use the following command:
pip install poetry
Verify the Installation: This command will display the currently installed version of Poetry, ensuring it's set up correctly.
poetry --version 
 

2. Creating a New Poetry Project
Create a New Poetry Project: This creates a project named proj and navigates into the project directory.
poetry new proj
cd proj
Add Required Dependencies: This command installs these libraries and updates the pyproject.toml file with the required dependencies.
poetry add numpy pandas scikit-learn 
Activate Poetry’s Virtual Environment: This will activate the virtual environment, where you can install packages, run scripts, and test your project.
poetry shell 


3. Managing Dependencies
Verify Installed Dependencies: This will display a list of all installed packages in the environment.
pip list 
Populate Your Project: After setting up the dependencies, you can start writing your code. Here’s an example of what the main.py file could look like:
import numpy as np
import pandas as pd
print("Hello PS folks, Poetry ML tutorial!")


4. Building and Installing Your Project
Build the Project: Create a distributed package from your project will generate .whl (wheel) and .tar.gz files inside the dist/ directory.
poetry build 
Install the Package Locally: This will install your package locally from the built wheel file.
pip install dist/<proj-name>-0.1.0-py3-none-any.whl
Run the Installed Project: This will execute your project as a module to test if everything works correctly.
python -m proj 


5. Updating Dependencies
Update Dependencies: Update all project dependencies from the pyproject.toml to their latest compatible version.
poetry update 
Show Dependency Tree: Displays a tree structure of all the installed dependencies and their versions.
poetry show --tree 
Add a Specific Version of a Package: Installs the latest version of numpy and updates the pyproject.toml file accordingly.
poetry add numpy@latest 


6. Exporting Dependencies
Export to requirements.txt: To export the dependencies to a requirements.txt file, you can use the following commands:

With hashes:

poetry export -f requirements.txt --output requirements.txt
 

Without hashes:

poetry export --without-hashes --output requirements.txt
 

7. Miscellaneous Commands
Show Installed Dependencies: To view the installed dependencies in your Poetry project.
poetry show
Show Outdated Dependencies: To check if any dependencies are outdated.
poetry show --outdated 
Check Project Integrity: To check the integrity of your pyproject.toml file and dependencies.
poetry check
Run a Script or Command: To run a Python script or any other command within the Poetry-managed virtual environment.
poetry run python main.py


8. Working with PyPI
Configure PyPI Token: To configure a PyPI token for publishing.
poetry config pypi-token.pypi <your-token-here> 
Publish to PyPI: To publish your project to PyPI, assuming your credentials are configured.
poetry publish --build


9. Using Poetry with Existing Project
Remove Existing .venv Directory: If you want to use Poetry with a project that already has a .venv directory or uses another environment manager.
rm -rf .venv

Initialize Poetry for the Project: This will guide you through creating a pyproject.toml file.
poetry init
Install Dependencies from requirements.txt: If you have an existing requirements.txt file, you can add all its dependencies to Poetry with.
poetry add $(cat requirements.txt)


Install the Project Dependencies: To install the dependencies listed in your pyproject.toml

poetry install 
Activate Poetry’s Virtual Environment: To activate the Poetry-managed virtual environment for your project.

poetry shell


10. Configure Poetry to Use .venv in the Project Directory
Keep the .venv directory:  Within your project, you can configure Poetry to do so.

poetry config virtualenvs.in-project true
Install the dependencies: This will create a .venv directory inside your project.

poetry install


Conclusion
Poetry is a powerful tool for managing Python dependencies and packaging projects. By following the above steps, you can streamline your development process, manage dependencies more efficiently, and ensure project is ready for distribution and deployment.
