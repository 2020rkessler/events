
from app import app
from flask import render_template, request, redirect

from flask_pymongo import PyMongo


app.config['MONGO_DBNAME'] = 'events'

app.config['MONGO_URI'] = 'mongodb+srv://admin:6bJqPlWkdC3QSvUC@cluster0-qrzjp.mongodb.net/admin?retryWrites=true&w=majority'

#password
#6bJqPlWkdC3QSvUC
mongo = PyMongo(app)


#index home page
@app.route('/')
@app.route('/index')

def index():
    #connects mongo collection events
    collection = mongo.db.events
    #searches DB 'events' for everything in the collection
    events = list(collection.find({}))
    #shows the frontend
    return render_template('index.html', events = events)



@app.route('/input')
def input():
    return render_template('input.html')

@app.route('/results', methods = ["Get", "Post"])
def results():
    #gets information from form, conerts it into a dict and then sets that info equal to variable 'userdata'
    userdata = dict(request.form)
    print(userdata)
    #storing the variables for the event data
    event_name = userdata['event_name']
    event_date = userdata['event_date']
    event_type = userdata['event_type']
    #connects mongo
    events = mongo.db.events
    events.insert({'name': event_name, 'date': event_date, 'type': event_type})
    #query database for all events and convert to a list
    events = list(events.find({}))
    print(events)
    return render_template('index.html', events = events)
