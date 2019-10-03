from flask import Flask
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)

app.config['SECRET_KEY'] = 'b6256de812325752f664b0br58bba652'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

# bcrypt manager
bcrypt = Bcrypt(app)

# Login Manager
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from .models import users, posts, startups, incubators, analysis
admin = Admin(app, name='Starup Punjab >>', template_mode='bootstrap3') #, index_view=MyAdminIndexView())
admin.add_view(ModelView(users, db.session))
admin.add_view(ModelView(posts, db.session))
admin.add_view(ModelView(startups, db.session))
admin.add_view(ModelView(incubators, db.session))
admin.add_view(ModelView(analysis, db.session))


# admin.add_view(AdminView(users, db.session))
# admin.add_view(AdminView(posts, db.session))
# admin.add_view(AdminView(Key, db.session))

from stp import routes
