from flask import render_template, flash, redirect, url_for, request, jsonify, json
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User, Citation
from random import sample


@app.route('/seneque')
def seneque():

    citations=Citation.query.order_by(Citation.number).all()

    return render_template('seneque.html', title='Seneque', citations=citations)


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', title='Home')


@app.route('/RequestCitations', methods=['POST'])
def RequestCitations():
    
    ReceivedData = request.get_data().decode('utf8')
    ReceivedData=json.loads(ReceivedData)

    if ReceivedData[2]=="SRR/TRT":
        citations=Citation.query.order_by(Citation.SRR).order_by(Citation.TRT.desc()).filter(Citation.number>=int(ReceivedData[0])).all()
        #print(citations)
    elif ReceivedData[2]=="TRT":
        citations=Citation.query.order_by(Citation.TRT.desc()).filter(Citation.number>=int(ReceivedData[0])).all()
        #print(citations)
    elif ReceivedData[2]=="SRR":
        citations=Citation.query.order_by(Citation.SRR).filter(Citation.number>=int(ReceivedData[0])).all()
        #print(citations)
    elif ReceivedData[2]=="order" or ReceivedData[2]=="rand" :
        citations=Citation.query.order_by(Citation.number).filter(Citation.number>=int(ReceivedData[0])).all()
        #print(citations)

    dicts = {}

    # keys and keys2 allow me to deal with index of javascript dict (beginning at 1) and python indexes that
    # begin at zero
    keys = range(1,int(ReceivedData[1])+1)
    keys2= range(0,int(ReceivedData[1]))

    if ReceivedData[2]=="rand":
        keys2= sample(keys2, len(keys2)) # the sample function randomly shuffle the list keys2


    for i in keys:
        dicts[i]=[citations[keys2[i-1]].number,citations[keys2[i-1]].text,citations[keys2[i-1]].SRR,citations[keys2[i-1]].TRT]
        
    #print(dicts)

    return jsonify(dicts, keys2)


@app.route('/SaveTrainingResults', methods=['POST'])
def SaveTrainingResults():

    citations=Citation.query.order_by(Citation.number).all()
    ReceivedDict = request.get_data().decode('utf8')
    ReceivedDict=json.loads(ReceivedDict)

    citation=Citation.query.get(int(ReceivedDict['CurrentCitationNumber']))

    # the -1 in the two following line come from indexation from zero of python
    citations[int(ReceivedDict['CurrentCitationNumber'])-1].SRR=ReceivedDict['NewSRR']
    citations[int(ReceivedDict['CurrentCitationNumber'])-1].TRT=ReceivedDict['NewTRT']
    db.session.commit()

    # in the following line, there is no -1 because indexation of the query (bdd) begin from 1
    citation=Citation.query.get(int(ReceivedDict['CurrentCitationNumber']))

    return jsonify(citation.SRR,citation.TRT)

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


#@app.route('/register', methods=['GET', 'POST'])
#def register():
#    if current_user.is_authenticated:
#        return redirect(url_for('index'))
#    form = RegistrationForm()
#    if form.validate_on_submit():
#        user = User(username=form.username.data, email=form.email.data)
#        user.set_password(form.password.data)
#        db.session.add(user)
#        db.session.commit()
#        flash('Congratulations, you are now a registered user!')
#        return redirect(url_for('login'))
#    return render_template('register.html', title='Register', form=form)
