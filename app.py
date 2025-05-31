from flask import Flask,render_template,request
app = Flask(__name__)

# define a menu as a dictionary using python

menu = {
    'pasta':400,
    'Pizza':3000,
    'Snacks':70,
    'Coffee':600,
    'Milk':300,
    'Burger':150,
    'Fruits':100,
}

@app.route('/')
def index():
    return render_template('index.html',menu=menu)

@app.route('/order',methods=['POST'])
def order():
    order_items = request.form.getlist('item')
    quantities = request.form.getlist('quantity')
    order = {}

    for item,quantity in zip(order_items,quantities):
        if item in menu and int(quantity) > 0:
            order[item] = int(quantity)

    # Calculate the total cost 
    total = sum(menu[item] * quantity for item, quantity in order.items())

    # pass order,total,and menu to the template 
    return render_template('order_summary.html',order=order, total=total,menu=menu)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)