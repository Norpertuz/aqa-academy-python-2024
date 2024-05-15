# aqa-academy-python-2024
Repo created regarding to AQA Academy requirements

# Coding rules
## Excluded folders
1. .venv folder. 
See link for venv creation https://docs.python.org/3/library/venv.html
2. Reports
In order to avoid conflicts during git push

## Dep updates
1. Major libs version needs to be revisisted once per month

# How to
1. Setup your env
1.1 Create venv into .venv folder
1.2 Install deps from requirements.txt file

2. Before commit
2.1 run black tool LINK_ADDED
2.2 run flak8 tool LINK_ADDED
2.3 run isort tool LINK_ADDED

3. Run the tests
3.1 Execute `pytest . -s -v` command staying in the root of the framework
. To form a report execute `pytest . -s -v --html=reports/report.html --self-contained-html` command

# Structure of the framework
1. tests - folder for tests
2. reports - folder to store local reports
3. src/applications - folder for system under tests abstractions
4. src/config - folder for configuration of framework
5. src/helpers - folder for single-use functions, etc