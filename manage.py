# Set the path
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask.ext.script import Manager, Server
from tumblood import app

manager = Manager(app)

# Turn on debugger by default and reloader
#to enable python shell withen the context of the app enable this line of code
# and change th app.run() to manage.run()
#manager.add_command("runserver", Server(
use_debugger = True,
use_reloader = True,
host = '0.0.0.0'
#)

if __name__ == "__main__":
    app.run()
