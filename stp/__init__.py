from flask import Flask
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin

app = Flask(__name__)

app.config['SECRET_KEY'] = 'b6256de812325752f664b0br58bba652'
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

# Login Manager
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

# from stp.models import
admin = Admin(app, name='Starup Punjab >>', template_mode='bootstrap3') #, index_view=MyAdminIndexView())
# admin.add_view(AdminView(User_Byld, db.session))
# admin.add_view(AdminView(Device, db.session))
# admin.add_view(AdminView(Key, db.session))

from stp import routes
