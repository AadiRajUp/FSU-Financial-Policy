from flask import Flask ,render_template

app = Flask(__name__)
app.secret_key = "HELLO123"


@app.route('/automation/financial-policy')
def financial_policy():
    return render_template("index.html")

