# Introduction
This project shows how to sort the content in rasa's yaml files

# Prerequisities

* Python 3.8.12
* [Poetry](https://python-poetry.org/docs/#installation)
* [make](https://www.gnu.org/software/make/)

# Usage
1. Run `make install`
2. Run `make NLU_FILE=/path/to/nlu.yml OUTPUT_FILE=/path/to/save/nlu_sorted.yml sort-intents`

# Note
For help, run `make help`