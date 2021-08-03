from flask import render_template, redirect, request

from sweater import app, db
from sweater.models import Company


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

