from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
@app.route("/data_yen",methods=["POST", "GET"],)
def show_data():
    # data = request.form.get('Insert a link')
    # request.body.get()
    kronyx = {}
    Reddoor = {}
    Reddoor['Abayomi'] = 'Team lead'
    Reddoor['Vivian'] = 'Networking instructor'
    Reddoor['Bolu'] = 'Python instructor'
    Reddoor['Modupe'] = 'Cybersecurity instructor'
    Reddoor['Abigeal'] = 'Project manager'
    Reddoor['Jacob'] = 'Networkiing engineer'
    krynox = {key:value for key, value in Reddoor.items() if key != value}
    Reddoor == krynox
    castData = krynox
    data_to_be_sent={"Name":"Olasiyan Daniel",'class':"5","year":'2017'}
    return json.dumps(castData)

if __name__== "__main__":
    app.run(debug=True)


    
