from flask import render_template, flash, redirect, url_for, request, jsonify, json
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User, Citation


@app.route('/')
@app.route('/index')
@login_required
def index():

    citations=Citation.query.all()

    return render_template('index.html', title='Home', citations=citations)


@app.route('/RequestCitations', methods=['POST'])
def send_citations():
    
    variable = int(request.get_data().decode('utf8'))

    #citations=Citation.query.all()
    citations=Citation.query.order_by(Citation.SRR).order_by(Citation.TRT.desc()).all()
    #citations=Citation.query.order_by(Citation.TRT.desc()).order_by(Citation.SRR).all()
    print(citations)
    #dicts = {0:'zero'}
    dicts = {}
    keys = range(1,int(variable)+1)
    #keys=range(int(variable))

    for i in keys:
             #dicts[citations[i].number] = citations[i].text
             dicts[i]=[citations[i-1].number,citations[i-1].text,citations[i-1].SRR,citations[i-1].TRT]

    print(dicts)
    #return jsonify({'text':citations[variable].text,
    #                'number':citations[variable].number})
    return jsonify(dicts)
    #return json.dumps([dict(citation) for citation in citations])



@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
