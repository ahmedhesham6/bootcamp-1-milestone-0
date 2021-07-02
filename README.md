# bootcamp-1-milestone-0
Build a simple RESTful CRUD API for a merchant application to manage 2 resources; items and orders.


## Installation

 requires [Python](https://www.python.org/) v3.6+ to run.
 
#### Clone

```sh
git clone https://github.com/ahmedhesham6/bootcamp-1-milestone-0.git
cd bootcamp-1-milestone-0
```

#### Virtualenv
```sh
python -m venv venv
. venv/bin/activate
```

#### Install Dependencies
```sh
pip install -r requirements.txt
```

#### Configure Environment Variables
- Create .env file
- Add both active and testing database urls
```
DATABASE_URL=sqlite:///development_database.db
TEST_DATABASE_URL=sqlite:///./test.db
```

## Run it

```sh
uvicorn main:app
```

## Test it

```sh
$ pytest
```
