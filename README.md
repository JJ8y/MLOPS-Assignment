# MLOPS Assignment

Our project is to predict Heart disease, Resale price and anomaly in corporate cases

## Tools used in this project
* [Poetry](https://towardsdatascience.com/how-to-effortlessly-publish-your-python-package-to-pypi-using-poetry-44b305362f9f): Dependency management - [article](https://mathdatasimplified.com/2023/06/12/poetry-a-better-way-to-manage-python-dependencies/)
* [hydra](https://hydra.cc/): Manage configuration files - [article](https://mathdatasimplified.com/2023/05/25/stop-hard-coding-in-a-data-science-project-use-configuration-files-instead/)
* [pre-commit plugins](https://pre-commit.com/): Automate code reviewing formatting
* [DVC](https://dvc.org/): Data version control - [article](https://mathdatasimplified.com/2023/02/20/introduction-to-dvc-data-version-control-tool-for-machine-learning-projects-2/)
* [pdoc](https://github.com/pdoc3/pdoc): Automatically create an API documentation for your project

## Set up the environment
1. Install [Poetry](https://python-poetry.org/docs/#installation)
2. Set up the environment:
```bash
make env 
```

## Install dependencies
To install all dependencies for this project, run:
```bash
poetry install
cookiecutter install
```

To install a new package, run:
```bash
poetry add <package-name>
```

## Version your data
To track changes to the "data" directory, type:
```bash
python = "3.9.7"
dvc = "^2.10.0"
hydra-core = "^1.1.1"
pdoc3 = "^0.10.0"
```
## Folder structure
MLOPS Assignment/
├── .dvc/
│   ├── .gitignore
│   └── config
├── .git/
├── .idea/
├── config/
│   ├── preprocessing.yaml
│   ├── main.yaml
│   ├── process.yaml
│   └── model.yaml
├── data/
│   ├── final/
│   ├── processed/
│   ├── raw/
│   ├── raw.dvc
├── docs/
├── models/
│   ├── ensemble_model.pkl
│   └── resale_pipeline.pkl
├── notebooks/
│   ├── .ipynb_checkpoints/
│   ├── .gitkeep
│   ├── 213014M_IT3385_Assignment.ipynb
│   ├── 21409C_Machine Learning Ops Assignment.ipynb
│   ├── keith_MLOPS_assignment.ipynb
├── outputs/
├── src/
│   ├── templates/
│   ├── statics/
│   ├── jj_app.py
│   ├── keith_app.py
│   ├── siddarth_app.py
│   ├── hydra/
│   └── output/
├── tests/
├── .gitattributes
├── .gitignore
├── pre-commit-config.yaml
├── Makefile
├── pyproject.toml
└── README.md