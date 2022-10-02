from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.utils import secure_filename
import os

auth = Blueprint('auth', __name__)

uploads = {"UPLOADS": ""}


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif','pdf'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@auth.route('/blood', methods =['GET'])
def home_blood():
    return render_template('blood.html')

@auth.route('/eye', methods =['GET'])
def home_eye():
    return render_template('eye.html')

@auth.route('/kidney', methods =['GET'])
def home_kidney():
    return render_template('kidney.html')

@auth.route('/thyroid', methods =['GET'])
def home_thyroid():
    return render_template('thyroid.html')

@auth.route('/liver', methods =['GET'])
def home_liver():
    return render_template('liver.html')

@auth.route('/heart', methods =['GET'])
def home_heart():
    return render_template('heart.html')

@auth.route('/blood', methods=['POST'])
def upload_image():
    if request.method == 'POST':
        print(request.files)
        if 'file' not in request.files:
            flash('No file part')
            return 'OK'
        file = request.files['file']
        if file.filename == '':
            flash('No image selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(uploads["UPLOADS"], filename))
            #print('upload_image filename: ' + filename)
            flash('Image successfully uploaded and displayed below')
            
            print(uploads["UPLOADS"])
            return render_template("blood.html", user=current_user)
        else:
            flash('Allowed image types are - png, jpg, jpeg, gif')
            return redirect(request.url)

    

@auth.route('/liver', methods=['POST'])
def liver():
        if request.method == 'POST':
            print(request.files)
        if 'file' not in request.files:
            flash('No file part')
            return 'OK'
        file = request.files['file']
        if file.filename == '':
            flash('No image selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(uploads["UPLOADS"], filename))
            #print('upload_image filename: ' + filename)
            flash('Image successfully uploaded and displayed below')
            print(uploads["UPLOADS"])
            return render_template("liver.html", user=current_user)
        else:
            flash('Allowed image types are - png, jpg, jpeg, gif')
            return redirect(request.url)
    
@auth.route('/eye', methods=['POST'])
def eye():
        if request.method == 'POST':
            print(request.files)
        if 'file' not in request.files:
            flash('No file part')
            return 'OK'
        file = request.files['file']
        if file.filename == '':
            flash('No image selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(uploads["UPLOADS"], filename))
            #print('upload_image filename: ' + filename)
            flash('Image successfully uploaded and displayed below')
            print(uploads["UPLOADS"])
            return render_template("eye.html", user=current_user)
        else:
            flash('Allowed image types are - png, jpg, jpeg, gif')
            return redirect(request.url)

@auth.route('/kidney', methods=['POST'])
def kidney():
        if request.method == 'POST':
            print(request.files)
        if 'file' not in request.files:
            flash('No file part')
            return 'OK'
        file = request.files['file']
        if file.filename == '':
            flash('No image selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(uploads["UPLOADS"], filename))
            #print('upload_image filename: ' + filename)
            flash('Image successfully uploaded and displayed below')
            print(uploads["UPLOADS"])
            return render_template("kidney.html", user=current_user)
        else:
            flash('Allowed image types are - png, jpg, jpeg, gif')
            return redirect(request.url)

@auth.route('/thyroid', methods=['POST'])
def thyroid():
        if request.method == 'POST':
            print(request.files)
        if 'file' not in request.files:
            flash('No file part')
            return 'OK'
        file = request.files['file']
        if file.filename == '':
            flash('No image selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(uploads["UPLOADS"], filename))
            #print('upload_image filename: ' + filename)
            flash('Image successfully uploaded and displayed below')
            print(uploads["UPLOADS"])
            return render_template("thyroid.html", user=current_user)
        else:
            flash('Allowed image types are - png, jpg, jpeg, gif')
            return redirect(request.url)

@auth.route('/heart', methods=['POST'])
def heart():
        if request.method == 'POST':
            print(request.files)
        if 'file' not in request.files:
            flash('No file part')
            return 'OK'
        file = request.files['file']
        if file.filename == '':
            flash('No image selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(uploads["UPLOADS"], filename))
            #print('upload_image filename: ' + filename)
            flash('Image successfully uploaded and displayed below')
            print(uploads["UPLOADS"])
            return render_template("heart.html", user=current_user)
        else:
            flash('Allowed image types are - png, jpg, jpeg, gif')
            return redirect(request.url)
