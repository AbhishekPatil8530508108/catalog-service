from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    return "welcome to catalog server"

@app.route('/products', methods=['GET'])
def products():
    return [
        {"id": 1, "title": "product1", "price": 100},
        {"id": 2, "title": "product2", "price": 200},
        {"id": 3, "title": "product3", "price": 300},
        {"id": 4, "title": "product4", "price": 400},
        {"id": 5, "title": "product5", "price": 500}
    ]

app.run(port=4000, host="0.0.0.0", debug=True)