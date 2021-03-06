from flask import Flask, render_template
import click
from .api import api
import os
from .auth import login_required

@click.command()
@click.option('--fps', '-f', default=15, help='Refresh frame rate.')
@click.option('--camera', '-c', default='fake', help='Camera driver to use. Valid options are "fake", "pi". (default is "fake")')
@click.option('--tripod', '-t', default='fake', help='Triod driver to use. Valid options are "fake", "pi". (default is "fake")')
@click.option('--debug/--no-debug', '-d/', default=False, help='Enable or disable debug mode (default is disabled).')
def run_app(fps, camera, tripod, debug):
    """Campy is a webcam server accessible through a REST API."""
    app = Flask(__name__, instance_relative_config=True)
    app.config['CAMERA'] = camera
    app.config['TRIPOD'] = tripod
    app.config['FPS'] = fps
    app.register_blueprint(api)

    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY='dev',
        # store the database in the instance folder
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    app.config.from_pyfile('config.py', silent=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # register the database commands
    from flaskr import db
    app.teardown_appcontext(db.close_db)

    # apply the blueprints to the flaskr
    from flaskr import auth
    app.register_blueprint(auth.bp)

    from .tripods import set_tripod
    set_tripod(app.config['TRIPOD'])

    @app.route('/')
    @login_required
    def index():
        return render_template('camera/index.html', camera=app.config['CAMERA'])

    app.run(host='0.0.0.0', threaded=True, debug=debug)
    return 0
