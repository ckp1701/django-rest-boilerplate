# Backend

Added:
- user rest auth
- django rest swagger
- project setup
- basic tests


## Quick project overview


## Development environment (Docker)

If you want you can use docker-compose to setup app.

1. Depends on your platform install docker and docker-compose;
2. Run: `docker-compose build` in the repo root;
3. Run: `docker-composer up -d` in the repo root;
4. Exec to backend docker `docker exec -it <container name> ash` and run migrations `python manage.py migrate`
5. Go to: `http:/0.0.0.0:8000/v1/` or whatever endpoint you want to use;

**This ->** Sometimes for some reason backend can't connect on initial start with PostgreSQL. If this is happening just
try restart `docker-compose` or restart backend docker container `docker restart <container name>`


## Development environment (virtualenv)

`local.py` and `local_settings.py` are setup only for virtualenv environment. `local.py` replace `manage.py` in this setup.
Added for better config per env control and integration with VSC.

1. You need virtualenv installed with python 3.6 or 3.7
2. `git clone` the repository to selected root path
3. Open folder with repository
4. Create and activate virtualenv `virtualenv venv`, `source venv/bin/activate`
5. install `requirements.txt` by `pip install -r requirements.txt`
6. Migrate by `python local.py migrate`
7. Run server `python local.py runserver`


## Comments


## Documentation


## Deployments

