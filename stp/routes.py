from stp import app

@app.route("/")
def index():
    return "Home.html"
