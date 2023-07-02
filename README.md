# Backend

For the server-side we use FastAPI.

## Initial setup

Download Python (or something like Anaconda), make sure to use a version of 3.7+.

Once Python is installed, open a terminal window in the root folder.

## Getting Started

### Creating the environment

```bash
# ! using pyenv
# use the name "virtualenv" to play well with the gitignore
python -m venv virtualenv
# change the slashes if not using windows
virtualenv\Scripts\activate.bat

# ! using conda - name and version can be different, version must be 3.7+ though
conda create --name waffle python=3.10
conda activate waffle

# to check the previously created envs with conda use the following
conda activate base
conda info --envs
```

### Starting the server

```bash
# get the dependencies before first start
pip install -r requirements.txt
uvicorn main:app --reload
```

After starting up the project locally, you can visit the Swagger API descriptions [here](http://127.0.0.1:8000/docs).

### Generate dependency list

```bash
pip freeze > requirements.txt
```
