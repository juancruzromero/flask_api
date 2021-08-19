<h1 align="center">
  <img align="center"; src="https://flask.palletsprojects.com/en/2.0.x/_static/flask-icon.png"; width="20px">
    Flask API
</h1>

## Introduction:
I create this repository to test Flask and Postgres connection with SQLAlchemy ORM.

## Steps to start this proyect:
- **Create Postgres:** create database test;
- **Add environment variable like:**
  - export DATABASE_URL="postgresql://postgres:secret@localhost/crehana"
  - export APP_SETTINGS="config.Config"
- **Run migrations:**
  - python manage.py db init
  - python manage.py db migrate
  - python manage.py db upgrade

## To do:
* [x] Model + Detect request's browser.
* [x] API CRUD.
* [ ] Add tests
* [ ] Deploy with Docker
* [ ] API docs
* [ ] Full 12FactorApp

## My microservices and software developement best practices references:

- [12-Factor App](https://12factor.net/)
- [12-Principles of Agile Software](https://agilemanifesto.org/principles.html)
- [Web API Design by Apigee](https://pages.apigee.com/rs/apigee/images/api-design-ebook-2012-03.pdf)
- [DevSecOps](https://devsecops-latam.org/)
- Design Patterns: Elements of Reusable Object-Oriented Software by Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides.
- TDD developement.
- I don't forget [Swagger](https://swagger.io/), Flask and Django docs 😅.
- [PEEEP8](https://www.youtube.com/watch?v=hgI0p1zf31k&ab_channel=PythonDiscord)🎵
