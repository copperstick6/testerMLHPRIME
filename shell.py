#basic shell with data for our project
#data is manually added until further notice
from flask import Flask, render_template, request
app = Flask(__name__)


# oppList is the defined as the current Opportunity List
totOpps=[]
totUsers = []
# object posted: ["userName", "PhoneNumber", "address"]
@app.route('/addUser', methods=['POST'])
def addingUser():
    username = request.form['username'],
    phonenumber = request.form['phonenumber'],
    address = request.form['address']
    totUsers.append([username, phonenumber, address])
    return str(totUsers)

@app.route('/curUser', methods=['GET'])
def getUsers():
    return str(totUsers)

@app.route('/curOpp', methods = ['GET'])
def getOpps():
    return str(totOpps)



@app.route('/appOpp', methods = ['POST'])
def returnOpps():
    curOpp = str(request.form["opportunity"])
    curDate = str(request.form["date"])
    curLocation = str(request.form["location"])
    curNeeded = str(request.form["needed"])
    totOpps.append([curOpp,curDate,curLocation,curNeeded])
    return str(totOpps)



if __name__ == "__main__":
    app.run()
