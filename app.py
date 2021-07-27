from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://viko:4p3r7a6c82e@localhost/flask_test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'secret string'
db = SQLAlchemy(app)

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(length=50), nullable=False)
    registration_date = db.Column(db.DateTime, default=datetime.utcnow())
    product_id = db.Column(db.Integer, nullable=False)

    def __init__(self, name, product_id):
        self.name = name
        self.product_id = product_id

    def __repr__(self):
        return '<Company %>' % self.id


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return 'User page:' + name + '-' + str(id)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/create-company', methods=['POST', 'GET'])
def create_company():
    if request.method == 'POST':
        name = request.form['name']
        product_id = request.form['product_id']

        company = Company(name=name, product_id=product_id)

        try:
            db.session.add(company)
            db.session.commit()
            return redirect('/all-companies')
        except:
            return "Error when add"

    else:
        return render_template("create-company.html")


@app.route('/all-companies')
def all_companies():
    #companies = Company.query.order_by(Company.registration_date).all()
    #return render_template("all-companies.html", companies=companies)
    return render_template("all-companies.html")


if __name__ == '__main__':
    #db.create_all()
    app.run(debug=True)
