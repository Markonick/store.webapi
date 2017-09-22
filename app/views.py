from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Markonick'}
    products = [
        {
            'item': {'name': 'Shoes'},
            'description': 'Designer high heels from Prada'
        },
        {
            'item': {'name': 'Bag'},
            'description': 'Topshop bag with studs'
        },
        {
            'item': {'name': 'Jeans'},
            'description': 'JBrand black jeans size 25'
        },
        {
            'item': {'name': 'Trainers'},
            'description': 'Nike trainers size 4'
        }
    ]
    return render_template('index.html', title='Home', user=user, products=products)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested fot OpenID="%s", remember_me=%s' %(form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form, providers=app.config['OPENID_PROVIDERS'])