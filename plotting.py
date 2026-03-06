from flask import Flask, render_template, request
import io
import base64
import random

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def home_page():
    return render_template('index.html')

@app.route('/d3example')
def display_d3():
    return render_template('d3_example.html')

@app.route('/choose_numbers')
def choose_numbers_view():
    return render_template('choose_numbers.html')

@app.route("/display_plot", methods=["GET"])
def plotView():
    ##TODO: refactor to move this to a helper function.... ick!
    random_min = int(request.args["min"])
    random_max = int(request.args["max"])

    x_values = random.choices(range(random_min, random_max), k=10)
    y_values = random.choices(range(random_min, random_max), k=10)

    # Generate plot
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.set_title("Random points")
    axis.set_xlabel("This is the x-axis label")
    axis.set_ylabel("This is the y-axis label")
    axis.grid()
    axis.plot(x_values, y_values, "o")
    # Convert plot to PNG image
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)
    # Encode PNG image to base64 string
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    return render_template("image.html", image=pngImageB64String)


if __name__ == "__main__":
    app.run(port=8000)