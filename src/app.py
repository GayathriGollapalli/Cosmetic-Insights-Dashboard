from flask import Flask, render_template
import pandas as pd

app = Flask(
    __name__,
    template_folder=".",
    static_folder=".",
    static_url_path=""
)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/story")
def story():
    return render_template("story.html")


@app.route("/brands")
def brands():
    df = pd.read_csv("../data/cosmetics.csv", encoding="latin1")

    brands = sorted(df["Brand"].dropna().unique())

    return render_template("brands.html", brands=brands)


if __name__ == "__main__":
    app.run(debug=True)