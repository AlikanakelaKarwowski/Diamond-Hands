from flask import Flask, render_template, url_for, request, redirect, Response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import io
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_ERI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# 157.230.63.172 
@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        stock_info = request.form['content']
    return render_template('index.html')

@app.route('/plot.png')
def plot_png():
    getvar = "postwas"
    fig = create_figure("Stock", 5)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure(Stock, Time):
    #lr = LinearRegression()
    #lr.predict(Stock, Time)
    fig = Figure()
    axis = fig.add_subplot(1,1,1)
    xs = range(6)
    ys = [random.randint(1,50) for x in xs]
    axis.plot(xs, ys)
    return fig

if __name__ == "__main__":
    app.run(debug=True)