from flask import Flask
from blueprints.user import user_blueprint

from extensions import db
app=Flask(__name__,instance_relative_config=True,static_folder="image")
app.config.from_object('config.settings')
app.config.from_pyfile('settings.py',silent=True)

#register blueprints
app.register_blueprint(user_blueprint)

#initialize extensions
db.init_app(app)

if __name__=='__main__':
    app.run()