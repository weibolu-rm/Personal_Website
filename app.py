import csv
from flask import Flask, render_template, url_for, flash, redirect
from forms import SignupForm, LoginForm, ContactForm

app = Flask(__name__)
app.secret_key = '4f3c2b1a6c977eef'

@app.route('/')
@app.route('/home')
def home():
    with open('static/data/skills.csv') as f:
        skill_list = list(csv.reader(f))[1:]
    return render_template('home.html', skill_list=skill_list)


@app.route('/projects')
def projects():
    with open('static/data/projects.csv') as f:
        project_list = list(csv.reader(f))[1:]
    return render_template('projects.html', active_page='projects',
                            project_list=project_list)


@app.route('/art')
def art():
    return render_template('art.html', active_page='art')


@app.route('/contact', methods=['GET','POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        flash(f'Message sent successfully.\nName: {form.name.data}\nEmail: {form.email.data}\nMessage: \"{form.message.data}\"', 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html', active_page='contact', form=form)


@app.route('/register')
def register():
    form = SignupForm()
    return render_template('register.html', active_page='register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
