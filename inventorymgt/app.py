from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import pygal
from configs import Development, Production
import psycopg2

app = Flask(__name__)

app.config.from_object(Development)

db = SQLAlchemy(app)

from models.inventories import InventoryModel
from models.sales import SalesModel


@app.before_first_request
def create_tables():
    # db.drop_all()
    db.create_all()


@app.route('/')
def hello_world():
    pie_chart = pygal.Pie()
    pie_chart.title = 'services vs products in percentage'
    pie_chart.add('products', InventoryModel.getCountType("Product"))
    pie_chart.add('sales', InventoryModel.getCountType("Service"))

    graph_data = pie_chart.render_data_uri()

    conn = psycopg2.connect("dbname='ims' user='postgres' host='localhost' password='apple'")

    cur = conn.cursor()
    cur.execute("""SELECT (sum(i.bp  * s.quantity)) as subtotal, EXTRACT(MONTH FROM s.created_date)as sales_month
FROM sales as s
join inventories as i on s.inv_id = i.id
GROUP BY sales_month
ORDER BY sales_month""")
    rows = cur.fetchall()
    # print(rows)

    x = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
    y = []

    for r in rows:
        # x.append(r[1])
        y.append(r[0])

    line_chart = pygal.Line()
    line_chart.title = 'Subtotal of a period in %'
    line_chart.x_labels = map(str, x)
    line_chart.add('Subtotal', y)
    line_data = line_chart.render_data_uri()

    line_some = pygal.HorizontalStackedBar()
    line_some.title = 'Subtotal of a period in %'
    line_some.x_labels = map(str, x)
    line_some.add('Subtotal', y)
    line_some = line_some.render_data_uri()

    return render_template("index.html", graph_data=graph_data, line_data=line_data, line_some=line_some)





@app.route('/contact_us')
def reach_us():
    return render_template("contact_us.html")


@app.route('/inventory', methods=['GET', 'POST'])
def inventory():
    x = InventoryModel.query.all()
    # for i in x:
    #     print(i.Inv_name)

    if request.method == 'POST':
        Inv_name = request.form['inventory']
        Inv_type = request.form['type']
        BP = request.form['bp']
        SP = request.form['sp']
        Stock = request.form['stock']
        RP = request.form['rp']

        obj = InventoryModel(inv_name=Inv_name, inv_type=Inv_type, bp=BP, sp=SP, stock=Stock, rp=RP)
        db.session.add(obj)
        db.session.commit()

        print("submitted")
        return redirect(url_for("inventory"))
        # print(Inv_type)
        # print(BP)
        # print(SP)
        # print(Stock)
        # print(RP)
    # we a passing a variable to display the end product on you webpage.
    return render_template('inventory.html', inventories=x)


@app.route('/sales', methods=['GET', 'POST'])
def sales():
    if request.method == 'POST':
        quantity = request.form['quantity']
        forkey = request.form['forkey']

        if InventoryModel.update(id=forkey, qt=int(quantity)):
            print('success')
            sale = SalesModel(Inv_id=forkey, Quantity=quantity)
            db.session.add(sale)
            db.session.commit()
        else:
            print("You dont have enough stock")
        # print(quantity, forkey)
        #
        # print('success')
        #

    return redirect(url_for('inventory'))


@app.route('/delete', methods=["POST"])
def delete(id):
    try:
        delete = InventoryModel.delete(id)
        if delete:
            print("record has been successfully deleted")
            return redirect(url_for('inventory'))
    except Exception:
        return redirect(url_for('inventory'))


# @app.route('/edit', methods="POST")
# def edit(id):
#     if request.method == 'POST':
#         ID = request.form('id')
#         Inv_name = request.form['inventory']
#         Inv_type = request.form['type']
#         BP = request.form['bp']
#         SP = request.form['sp']
#         Stock = request.form['stock']
#         RP = request.form['rp']
#
#         edit = InventoryModel.edit(id=ID, name=Inv_name, type=Inv_type, bp=BP, sp=SP, stock=Stock, rp=RP)
#         return True
#     else:
#         return False
#
#     return redirect(url_for('inventory'))


if __name__ == '__main__':
    app.run(debug=True)
