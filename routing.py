from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/user/<name>')
def user_page(name):
    if name == "Godwin":
        return redirect(url_for('admin', name=name))
    else:
        return redirect(url_for('guest', name=name))


@app.route('/user/admin/<name>')
def admin(name):
    return 'I am the admin. My name is %s' % name


@app.route('/user/guest/<name>')
def guest(name):
    return 'I am on the guest page. My name is %s' % name


@app.route('/user/payment/<int:sal>')
def payment(sal):
    if sal > 5000:
        return '<h1 style="display:flex;justify-content:center;">You are rich!</h1>'
    elif sal > 2000:
        return 'You got enough?'
    else:
        return 'You are poor'


if __name__ == "__main__":
    app.debug = True
    app.run()
