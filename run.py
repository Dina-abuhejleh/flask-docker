
from project import app

if __name__=='__main__':

    app.run(host='0.0.0.0',port=5000)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import config



app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()
db=SQLAlchemy(app)
db.init_app(app)
db.create_all()



from project import routes
