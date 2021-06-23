from flask import Blueprint, render_template, request, redirect, url_for, flash
from forms import UserLoginForm
from models import User, db


auth = Blueprint('auth',__name__,template_folder='auth_templates')


@auth.route('/signup',methods = ['GET','POST'])
def signup():
    form = UserLoginForm()
    try:
        if request.method == 'POST' and form.validate_on_submit():
            username = form.username.data
            email = form.email.data
            password = form.password.data
            print(username,email,password)

            user = User(email, username = username, password = password)
            db.session.add(user)
            db.session.commit()

            flash(f"{username}: Your account has been created")
            return redirect(url_for('site.home'))
    except:
        raise Exception('Fill in those forms better')

    return render_template('signup.html', form=form)




@auth.route('/signin',methods = ['GET','POST'])
def signin():
    return render_template('signin.html')
