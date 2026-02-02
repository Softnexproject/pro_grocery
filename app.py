from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home_page.html")


@app.route("/seller_register")
def seller_register():
    return render_template("seller_register.html")


@app.route("/seller")
def seller_dashboard():
    return render_template("seller.html")


@app.route("/seller-portal")
def seller_portal():
    return render_template("seller_portal.html")


@app.route("/sellers")
def sellers_list():
    return render_template("sellers.html")


@app.route("/seller-items")
def seller_items():
    return render_template("seller_items.html")


@app.route("/selected-items")
def selected_items():
    return render_template("selected_items.html")


if __name__ == "__main__":
    app.run(debug=True)
