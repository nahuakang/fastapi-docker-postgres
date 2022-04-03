# Docker-Composed FastAPI with Database Migrations, SQLAlchemy, and Alembic

This is template project is a fork from [ianrufus](https://github.com/ianrufus/BlogPosts/tree/master/AlembicMigrations) and illustrates how to run `docker-compose` with FastAPI and how to create and run Alembic migrations for SQLAlchemy to create tables and set up a one-to-many relationship between the tables using `ForeignKeyConstraint`.

Ian Rufus's blog post this code accompanies can be found here: [https://ianrufus.com/blog/2020/12/sqlalchemy-alembic-migrations](https://ianrufus.com/blog/2020/12/sqlalchemy-alembic-migrations).

This forked project included some `schemas`, `crud`, and `API endpoints` to test the database inside the `docker-compose` network.

## Getting Started

Included in the example is a Docker Compose file to run the API and a Postgres database.

Create a virtual environment for the Python API:  
`python3 -m venv virtualenv`

Activate the environment:  
`source virtualenv/bin/activate`

Then install the required dependencies:  
`pip install -r requirements.txt`

The first step is to build the required container for the API:  
`docker-compose build`

Once built, you can run the API and Database:  
`docker-compose up`

In another terminal you can run the migrations with:  
`alembic upgrade head`

If you want to revert the migration, you can run:  
`alembic downgrade -1`

## Notes on Alembic

We use [alembic](https://alembic.sqlalchemy.org/) to manage database migrations. First, initialize alembic to generate `alembic.ini` file in the project root:

```shell
$ alembic init alembic
  Creating directory /Users/nahua/projects/fastapi/sqlapp/alembic ...  done
  Creating directory /Users/nahua/projects/fastapi/sqlapp/alembic/versions ...  done
  Generating /Users/nahua/projects/fastapi/sqlapp/alembic/script.py.mako ...  done
  Generating /Users/nahua/projects/fastapi/sqlapp/alembic/env.py ...  done
  Generating /Users/nahua/projects/fastapi/sqlapp/alembic/README ...  done
  Generating /Users/nahua/projects/fastapi/sqlapp/alembic.ini ...  done
  Please edit configuration/connection/logging settings in '/Users/nahua/projects/fastapi/sqlapp/alembic.ini' before proceeding.
```

Open `alembic.ini` file to modify the database URL connection to the one that is identical to the one inside `database.py`:

```
sqlalchemy.url = postgresql://postgres:password@localhost/sqlapp
```

Now, run the following to create the first database migration file inside `/alembic/versions/` directory:

```shell
$ alembic revision -m "init"
 Generating /Users/nahua/projects/fastapi/sqlapp/alembic/versions/da2c7e5d242e_init.py ...  done
```

Fill in the migration operations and then perform upgrade or downgrade:

```shell
$ alembic upgrade head
# or
$ alembic downgrade -1
# or
$ alembic history
```

## Notes on Postgres Errors

If running `alembic upgrade head` results in:

```shell
sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) FATAL:  database "sqlapp" does not exist
```

Make sure to terminate the running Postgres in your OS.
