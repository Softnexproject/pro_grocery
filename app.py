from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home_page.html")


# ---------------- SELLER REGISTER ----------------
@app.route("/seller_register", methods=["GET", "POST"])
def seller_register():
    if request.method == "POST":
        shop_name = request.form["shop_name"]
        shopkeeper_name = request.form["shopkeeper_name"]
        age = request.form["age"]
        address = request.form["address"]
        phone = request.form["phone"]

        # TEMPORARY: just print to terminal
        print("Seller Registered:")
        print(shop_name, shopkeeper_name, age, address, phone)

        # Redirect after submit (PRG pattern)
        return redirect(url_for("home_page"))

    return render_template("seller_register.html")


if __name__ == "__main__":
    app.run(debug=True)
