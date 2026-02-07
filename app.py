from flask import Flask ,render_template

app = Flask(__name__)
app.secret_key = "HELLO123"


@app.route('/automation/financial-policy')
def financial_policy():
    return render_template("index.html")

@app.route ('/automation/index.html')
def index():
    return render_template('index.html')

@app.route ('/automation/ClubsEventsFund.html')
def club():
    return render_template('ClubsEventsFund.html')

@app.route ('/automation/EntryFeeFund.html')
def fee():
    return render_template('EntryFeeFund.html')

@app.route ('/automation/ExibitionFund.html')
def event():
    return render_template('ExibitionFund.html')

@app.route ('/automation/FSUInternalFund.html')
def internal():
    return render_template('FSUInternalFund.html')

@app.route ('/automation/ResearchAndInnovationFund.html')
def research():
    return render_template('ResearchAndInnovationFund.html')

@app.route ('/automation/TravelSubsidy.html')
def travel():
    return render_template('TravelSubsidy.html')

