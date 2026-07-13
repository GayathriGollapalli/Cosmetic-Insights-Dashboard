from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)

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
    df = pd.read_csv("data/cosmetics.csv", encoding="latin1")

    data = df.to_dict(orient="records")
    columns = df.columns.tolist()

    return render_template(
        "brands.html",
        data=data,
        columns=columns
    )

    

if __name__ == "__main__":
    app.run(debug=True)