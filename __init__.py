"""Press Ctrl + Shift + P → type Python: Select Interpreter.
Choose the Python interpreter inside your venv (it usually shows the path ending with venv\Scripts\python.exe on Windows)."""

"""Configuration basically means the settings that control how something behaves. Its not code that does work—it tells the program how to work.
In Flask (and most apps), configuration usually includes things like:
   1. Secret keys → for security, sessions, cookies (SECRET_KEY)
   2. Database paths or URLs → where your app stores data (DATABASE)
   3. Debug mode → whether the app should show detailed error messages (DEBUG=True)
   4. Environment-specific settings → dev, testing, production (like turning off debug in production)
So when you see app.config.from_mapping() or app.config.from_pyfile(), youre basically telling Flask how to behave in this project or environment.
Think of it like the settings page on your phone—it doesnt make calls itself, but it controls how the phone behaves when you use it. """

# flask --app flaskr run --debug (run this in terminal of main folder of project not in 'flaskr')
import os
from flask import Flask
def create_app(test_config=None):

    # create and configure the app
    app=Flask(__name__, instance_relative_config=True) #__name__ is the name of the current Python module, instance_relative_config=True tells the app that configuration files are relative to the instance folder.
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    os.makedirs(app.instance_path, exist_ok=True)

    # register the database with the app
    from . import db
    db.init_app(app)
    
    # register the blueprint
    from . import auth
    app.register_blueprint(auth.bp)
    
    #Import and register the blueprint from the factory
    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app
    
