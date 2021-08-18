SHELL=/bin/bash
PYTHON=python
MAIN=app.py
ARGS=$(filter-out $@,$(MAKECMDGOALS))

# Runserver -> Example: make run
run: $(MAIN)
	python $(MAIN)

# Create enviroment variables -> Example make envars
envars:
	@export DATABASE_URL="postgresql://postgres:secret@localhost/test" && export APP_SETTINGS="config.Config"

# Migrations -> Example: make migrations
migrations: $(MAIN)
	python manage.py db init && python manage.py db migrate && python manage.py db upgrade
