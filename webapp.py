from flask import Flask,render_template,url_for,redirect,flash,request

from forms import RegistrationForm,LoginForm





users={
    'Thomas@email.com':'password',
    'Barbara@email.com':'passward',
    'Samuel@email.com':'Passuard'
}

web_app=Flask(__name__)

#web_app.config['SECRET_KEY']=='f730f4c9478cad96d48595d0c4d7c71309240ca33bad'
web_app.config['SECRET_KEY'] = 'temporary_key'


@web_app.route("/")
@web_app.route("/register", methods=["POST","GET"])
def register():
    form=RegistrationForm()
    return render_template('register.html',title='Register',form=form)


@web_app.route("/login", methods=["POST","GET"])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        email=form.email.data
        password=form.password.data
        if email in users and users[email]==password:
        
            flash(f"{email} has successfully logged in")
            return render_template('register.html')

             
        
    return render_template('login.html',title='Login',form=form)

# if __name__=='__main__':
#     web_app.run(debug=True)   