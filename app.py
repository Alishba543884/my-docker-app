from flask import Flask, render_template

app = Flask(__name__)

shoes = [
    {"name": "Nike Air", "price": "$120"},
    {"name": "Adidas Runner", "price": "$100"},
    {"name": "Puma Sport", "price": "$90"},
    {"name": "Reebok Classic", "price": "$110"}
]

@app.route("/")
def home():
    return render_template("index.html", shoes=shoes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)