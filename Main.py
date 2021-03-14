from flask import Flask, render_template, url_for
app = Flask(__name__)

# 157.230.63.172 
@app.route("/")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)