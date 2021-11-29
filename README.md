# My Weather App Heroku

This project will be built through a series of videos. I hope to help people learn how to build an application locally and shift it to the cloud.

Before starting it will be ideal (not mandatory) to have a basic understanding of Python.

You can use this project as a jump start to build something more advanced or as a learn by doing exercise.

1. Create flask server with outbound api calls to obtain weather information
2. Add frontend static content to display weather
3. Create Docker container
4. Deploy app to Heroku
5. Continuous deployments with GitHub actions

## Skills you will practice

- Python, Flask, Jinja templating
- Heroku
- GitHub actions
- Docker
- Coding and research skills
- Bootstrap styling

## Requirements

- Python
- Code editor of your choice
- Virtual environment (optional)
- Docker
- Heroku CLI

### Helpful Commands

Create virtual environment:
`python -m venv env`

Enter virtual environment:
`source ./env/Scripts/activate`

Install dependencies
`pip install flask requests python-dotenv`

Run flask server
`flask run`

Create requirements.txt
`pip freeze > requirements.txt`

### Heroku Container Deployment

`docker login`

`docker build . -t app`

`docker image ls`

`docker run -p 5000:5000 --env-file .env app`

`heroku login` (to logout, `heroku logout`)

`heroku create my-great-weather` (if name is taken, choose another)

`heroku stack:set container --app my-great-weather`

`heroku config:set FLASK_APP=server --app my-great-weather`

`heroku config:set FLASK_ENV=production --app my-great-weather` (set environment variables)

Manual push to heroku - not required as we use GitHub actions
`git push heroku master` (after committing your changes to git)
