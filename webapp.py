from flask import Flask,render_template,url_for
from forms import RegistrationForm,LoginForm

web_app=Flask(__name__)

#web_app.config['SECRET_KEY']=='f730f4c9478cad96d48595d0c4d7c71309240ca33bad'
web_app.config['SECRET_KEY'] = 'temporary_key'


@web_app.route("/")
@web_app.route("/register",methods="[POST,GET]" )
def register():
    reg_form=RegistrationForm()
    return render_template('register.html',title='Register',form=reg_form)
@web_app.route("/log in")
def log_in():
    login_form=LoginForm()
    return render_template('layout.html',title='Register',form=login_form)

if __name__=='__main__':
    web_app.run(debug=True)   