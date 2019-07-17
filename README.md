# Magic Live Demo Runtime app

This repository contains the code to run mentee submitted projects, specifically
Python CLI projects and self-contained HTML/CSS/JS projects and allow them to be
demoed in a web browser.

## Setup

- You would first need to install Docker CE for your platform from
	https://download.docker.com
- You will need to have a Python dev environment setup with either Python 2.7 or
  Python 3 with the `pip` tool.
- From the root directory of this repository, run `pip install -r requirements.txt`
  If you have a Python 3 environment, you might need to change `pip` to `pip3`

This completes the basic setup of the environment for running the Flask web app.

Next we need to build the Docker images within which the projects will actually
run.

For HTML project support

```
cd docker/apache
docker build . -t magic_html
```

For Python CLI project support

```
cd docker/python
docker build . -t magic_python
```

Once the above two are done, the Docker images for the respective runtimes are
built.

## Running

To run, you will need to first start the Flask app, which can be done by running

```
cd web_app
python web_server.py
```

In your browser, you can try hitting the following two demo URLs to see the
Python and HTML demos in action:

- [python](http://localhost:5000/demo?project_name=demoPython&project_type=python)

- [html](http://localhost:5000/demo?project_name=demoHTML&project_type=html)
