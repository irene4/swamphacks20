from flask import Flask, flash, redirect, render_template, request
from color import Color
from dmc_type import DmcType
import dmc_file

app = Flask(__name__)

dmcs = DmcType()
dmc_file.load('static/dmc_refs.csv', dmcs)

def format(close : list) -> list:
    out_list = []
    for i in close:
        out_list.append((i[0], dmcs.get(i[0])[0], dmcs.get(i[0])[1].asWebHex()))
    return out_list

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        color_in = request.form["color_in"]
    else:
        color_in = "#000000"
    target = Color(color_in)
    closests = format(dmcs.getClosest(target, 15))
    return render_template('home.html', results=closests)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
