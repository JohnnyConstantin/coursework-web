from flask import request, Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/get_laptops', methods=['POST'])
def get_laptops():
    #here will be parsing
    checked = request.form.get('laptop')
    item = request.form.get('item_to_search')
    print(checked)
    print(item)
    return render_template('index.html')
