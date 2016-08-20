

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# creating the application object
app = Flask(__name__)
# App the module that gets assigned the flask instance
# App the package from where we import the views module
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/pre-registration'
# Setting the path to the db(configuring)
db = SQLAlchemy(app)

# Set "homepage" to index.html
@app.route('/')
def index():
    return render_template('index.html')

# Save e-mail to database and send to success page
@app.route('/prereg', methods=['POST'])
def prereg():
    email = None
    if request.method == 'POST':
        email = request.form['email']
        # Check that email does not already exist (not a great query, but works)
        if not db.session.query(User).filter(User.email == email).count():
            reg = User(email)
            db.session.add(reg)
            db.session.commit()
            return render_template('index2.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
