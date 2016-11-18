# basic shell with data for our project
# data is manually added until further notice
from flask import Flask, request
import logging
import sys
app = Flask(__name__)

# Configure logging.
app.logger.setLevel(logging.DEBUG)
del app.logger.handlers[:]

handler = logging.StreamHandler(stream=sys.stdout)
handler.setLevel(logging.DEBUG)
handler.formatter = logging.Formatter(
    fmt=u"%(asctime)s level=%(levelname)s %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%SZ",
)
app.logger.addHandler(handler)

# oppList is the defined as the current Opportunity List
totOpps = []
totUsers = {
    'james': [
        'Gabriel Richardson',
        '2162454523',
        '3829 Norman Lane, Flower Mound, Texas',
        18,
        '1. I like volunteering'
    ],
    'goosh': [
        'Jamin Goo',
        '5203893829',
        '2537 E Dean Keeton, Austin, Texas',
        19,
        '1. I love volunteering.\n2. I also love peace'
    ]
}

@app.route('/clearUsers', methods=['GET'])
def removeUsers():
    totUsers = {}
    return str(totUsers)

@app.route('/clearOpp', methods=['GET'])
def removeOpps():
    del totOpps [:]
    return str(totOpps)

# object posted: ["userName", "PhoneNumber", "address"]
@app.route('/addUser', methods=['POST'])
def addUser():
    username = request.form['username']
    name = request.form['name']
    phonenumber = request.form['phonenumber']
    address = request.form['address']
    age = request.form['age']
    bio = request.form['bio']
    totUsers[username] = [name, phonenumber, address, age, bio]
    return str(totUsers)


@app.route('/curUser', methods=['GET'])
def getUsers():
    return str(totUsers)


@app.route('/curOpp', methods=['GET'])
def getOpps():
    return str(totOpps)


@app.route('/appOpp', methods=['POST'])
def returnOpps():
    curOpp = str(request.form["opportunity"])
    curDate = str(request.form["date"])
    curLocation = str(request.form["location"])
    curNeeded = str(request.form["needed"])
    totOpps.append([curOpp, curDate, curLocation, curNeeded])
    return str(totOpps)

if __name__ == '__main__':
    app.run(debug=True)
