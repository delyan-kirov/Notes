from flask_cors import CORS
from flask import Flask, jsonify, request, render_template, url_for, redirect
import os
import json
import makeHtml
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt


#%%
app = Flask(__name__)
app.debug = True
CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})
bcrypt = Bcrypt(app)


#%% DB LOGIC

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'
db = SQLAlchemy(app)
# db.init_app(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    
with app.app_context():
    print("Calling db.create_all()")
    db.create_all()
    print("Finished calling db.create_all()")
    
    
    
    
    
#%% USER LOGIN LOGIC

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class RegisterForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Register')

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        if existing_user_username:
            raise ValidationError(
                'That username already exists. Please choose a different one.')


class LoginForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(f'http://localhost:4200/?username={user.username}')
    return render_template('login.html', form=form)


@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        # create a new directory for the user
        newUser = form.username.data
        os.makedirs(f"./data/{newUser}", exist_ok=True)

        return redirect(url_for('login'))
    return render_template('register.html', form=form)


    """
        Routes
        //////////////////////////////////////////////////////////////////////////////
    """

#%% Root route

@app.route("/")
def shareData():
    username = request.args.get("username")
    dataPath = f"./data/{username}"
    print("datapath is: " +  dataPath)
    output = []
    showData = ""
    for files in os.listdir(dataPath):
        files = os.path.join(dataPath, files)
        with open(files, 'r') as f:
            output.append(f.read(60))
            f.close()
    
    for data in output:
        showData += data + "\n"
    
    filename = request.args.get("filename")
    print(filename)
    
    print(output)
    return jsonify(showData)

#%% Share data route
@app.route("/init")

def giveFileData():
    username = request.args.get("username")
    dataPath = f"./data/{username}"
    print("datapath is: " +  dataPath)
    
    output = []
    names = []
    
    for files in os.listdir(dataPath):
        files = os.path.join(dataPath, files)
        with open(files, 'r') as f:
            output.append(f.read(60))
            names.append(str(os.path.basename(f.name)))
            f.close()
    print("\n")
    print(output,names)
    print("inside /init")
    return(jsonify(output,names))

#%% Notes route
@app.route("/notes", methods=["POST", "GET"])
def showNote():
    if request.method == "GET":
        print("handled response")
        return jsonify({"url": "http://localhost:5000/notes"})

    data = request.data.decode("utf-8")
    data = str((data.split(":", 1)[1])[1:-2]) + ".html"
    print("The data is:" + data)

    return jsonify({"content": render_template(data)})

#%%
@app.route("/text", methods=["GET", "POST"])

def getText():
    
    data = request.get_json()
    print("Received message")
    print(json.dumps(data, indent=4))
    
    data = data['text']
    username = request.args.get("username")
    dataPath = f"./data/{username}"
    print(request.args)
    
    name = (data[:20].split()[0])
    path = os.path.join(dataPath, name)
    
    with open(path,"w") as f:
        f.write(data)
        f.close() 
    
    makeHtml.buildMD(data, name)  

    return jsonify({'status': 'success'})

#%%
@app.route("/delete", methods=["DELETE", "GET"])

def deleteFile():
    print("received signal")
    
    filename = request.args.get("filename")
    print(filename)
    
    username = request.args.get("username")
    dataPath = f"./data/{username}/" + filename
    
    os.remove(dataPath)
    return jsonify({'status': 'success'})
    