from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:troy@localhost/yi'
db = SQLAlchemy(app)

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
            return render_template('success.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
