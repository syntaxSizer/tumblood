from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "my_tumble_log"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

db = MongoEngine(app)

if __name__ == '__main__':
    app.run()

#register the blueprint to avoid circular dependancy
def register_blueprints(app):
    #pervent circuar import
    from tumblood.views import posts 
    app.register_bluprints(posts)

register_blueprints(app)
    
