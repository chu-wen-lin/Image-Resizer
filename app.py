from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from utilities import tools


app = Flask(__name__)


@app.route("/")
def index():
    return redirect(url_for('resize_image'))


@app.route('/resizer', methods=['POST', 'GET'])
def resize_image():
    if request.method == 'POST':
        length, width = request.form.get("length"), request.form.get("width")
        img_url = tools.resize_image(int(length), int(width))
        return render_template("image.html",
                               image=img_url,
                               length=length,
                               width=width)
    return render_template("resize.html")


if __name__ == '__main__':
    app.run()
