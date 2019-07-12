from flask import Flask
from flask import request
from flask import render_template
import subprocess
import logging
import traceback

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/demo')
def project():
    project_name = request.args.get('project_name')
    project_type = request.args.get('project_type')

    try:
        logging.info('Starting a {} docker container for : {}'.format(project_type, project_name))
        cmd = 'docker run --rm -p 7681:7681 ttyd:latest {} {}'.format(project_name, project_type)
        logging.info('Running : {}'.format(cmd))
        subprocess.call(cmd,
                        shell=True)
    except:
        logging.warning('Encountered an error while running docker')
        logging.warning(traceback.print_exc())

    return render_template('docker_bash.html')


def main():
    logging.getLogger().setLevel(logging.INFO)
    app.run()
    logging.info('Starting the flask server')


if __name__ == '__main__':
    main()
