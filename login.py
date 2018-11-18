from flask import *
from flask_login import LoginManager, UserMixin, login_user, current_user, login_required, logout_user
from DBClasses.loginform import LoginForm

app = Flask(__init__)
app.config['SECRET_KEY'] = 'a551d32359baf371b9095f28d45347c8b8621830'
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return User.fetch_userid(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash(f'Login Successful')
		return redirect(url_for('profile'))
	return render_template('login.html')

@app.route('/profile/<username>', methods=['GET', 'POST'])
@login_required
def profile(username):
	return render_template('profile.html')