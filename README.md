<h1 align="center">
  <img align="center"; src="https://flask.palletsprojects.com/en/2.0.x/_static/flask-icon.png"; width="20px">
    Flask API
</h1>

## Steps to start this proyect:
- create database test;
- export DATABASE_URL="postgresql://postgres:secret@localhost/test"
- export APP_SETTINGS="config.Config"
- python manage.py db init
- python manage.py db migrate
- python manage.py db upgrade

## To do:
* [ ] Add tests
* [ ] Make good schemas
* [ ] Deploy with Docker

## My microservices and software developement best practices references:

- [12-Factor App](https://12factor.net/)
- [12-Principles of Agile Software](https://agilemanifesto.org/principles.html)
- [Web API Design by Apigee](https://pages.apigee.com/rs/apigee/images/api-design-ebook-2012-03.pdf)
- [DevSecOps](https://devsecops-latam.org/)
- Design Patterns: Elements of Reusable Object-Oriented Software by Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides.
- ORM: [SQLAlchemy](https://www.sqlalchemy.org/)
- I don't forget [Swagger](https://swagger.io/), Flask and Django docs 😅.
- [PEEEP8](https://www.youtube.com/watch?v=hgI0p1zf31k&ab_channel=PythonDiscord)🎵
