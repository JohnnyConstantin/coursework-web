from flask import Flask, render_template, request
from Model import Model, find_max, find_min

app = Flask(__name__)


@app.route('/')
def start():
    return render_template('index.html')


@app.route('/get_laptops', methods=['POST'])
def get_laptops():
    # Controller for interacting with view

    item = request.form.get('item_to_search')

    if item != "":
        d = []

        Entity = Model.Model(item, d)
        Entity.parse_kns(item, d)
        Entity.parse_mobicom(item, d)

        min = find_min.find_min(d)
        max = find_max.find_max(d)

        if len(d) == 0:
            return render_template('not_found.html')
        else:
            #Returning data into view
            return render_template('result.html', datas=d, min=d[min], max=d[max])
    else:
        return render_template('no_args.html')
