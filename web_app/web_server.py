from flask import Flask
from flask import request
from flask import render_template
import subprocess
import logging
import traceback
import json

from constants import *

app = Flask(__name__)
project_type_metadata = None


@app.route('/')
def index():
    return render_template(INDEX_TEMPLATE)


@app.route('/demo')
def project():
    project_name = request.args.get('project_name')
    project_type = request.args.get('project_type')

    logging.info('Starting a {} docker container for : {}'.format(project_type, project_name))

    try:
        assert project_type in project_type_metadata

        cmd = 'docker run -d --rm -p {}:{} {}:latest {} {}'.format(
            project_type_metadata.get(project_type).get('out_port'),
            project_type_metadata.get(project_type).get('in_port'),
            project_type_metadata.get(project_type).get('docker_image'),
            project_name,
            project_type)
        logging.info('Running : {}'.format(cmd))
        subprocess.call(cmd,
                        shell=True)
    except:
        # TODO: Better error handling and redirection if project does not exist
        logging.warning('Encountered an error while running docker')
        logging.warning(traceback.print_exc())

    if project_type in project_type_metadata:
        return render_template(DOCKER_BASH_HTML,
                               port=project_type_metadata.get(project_type).get('out_port'))
    else:
        return render_template(INDEX_TEMPLATE)


def main():
    # Setup logger
    logging.getLogger().setLevel(logging.INFO)

    # Load metadata
    logging.info(PROJECT_TYPE_METADATA_FILE)
    global project_type_metadata
    project_type_metadata = json.load(open(PROJECT_TYPE_METADATA_FILE, 'r'))
    logging.info(project_type_metadata)

    # Run the flask server
    app.run()

    logging.info('Starting the flask server')


if __name__ == '__main__':
    main()
