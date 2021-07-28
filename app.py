from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://viko:4p3r7a6c82e@localhost/flask_test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True
app.secret_key = 'secret string'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(length=50), nullable=False)
    description = db.Column(db.Text, default="No description")
    registration_date = db.Column(db.DateTime, default=datetime.utcnow())
    product_id = db.Column(db.Integer, nullable=False)

    def __init__(self, name, product_id, description):
        self.name = name
        self.product_id = product_id
        self.description = description

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
        description = request.form['description']

        company = Company(name=name, product_id=product_id, description=description)

        try:
            db.session.add(company)
            db.session.commit()
            return redirect('/all-companies')
        except:
            return "Error when add"

    else:
        return render_template("create-company.html")


@app.route('/update-company/<int:id>', methods=['POST', 'GET'])
def update_company(id):
    company = Company.query.get(id)
    print(company.id)
    if request.method == 'POST':
        print(company.id)
        company.name = request.form['name']
        company.product_id = request.form['product_id']
        company.description = request.form['description']

        try:
            db.session.commit()
            return redirect('/all-companies')
        except:
            return "Error when add"

    else:
        return render_template("update-company.html", company=company)


@app.route('/delete-company/<int:id>')
def delete_company(id):
    company = Company.query.get_or_404(id)

    try:
        db.session.delete(company)
        db.session.commit()
        return redirect('/all-companies')
    except:
        return 'Delete error'


@app.route('/all-companies')
def all_companies():
    companies = Company.query.order_by(Company.registration_date).all()
    return render_template("all-companies.html", companies=companies)
    #return render_template("all-companies.html")


if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', port='5000', debug=True)
