from flask_api import FlaskAPI
from flask_login import LoginManager
from app.utils import get_user


from app.models import User


app = FlaskAPI(__name__)
app.secret_key = 'some secret key'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return get_user(user_id)


from app.routes import *