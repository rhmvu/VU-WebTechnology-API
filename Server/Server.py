'''
Created on 23 jan. 2017

@author: Ruben and Kostas
'''
###############################################################################
# Web Technology at VU University Amsterdam
# Assignment 3
#
# The assignment description is available on Blackboard.
# This is a template for you to quickly get started with Assignment 3. Read
# through the code and try to understand it.
#
# Have you looked at the documentation of bottle.py?
# http://bottle.readthedocs.org/en/stable/index.html
#
# Once you are familiar with bottle.py and the assignment, start implementing
# an API according to your design by adding routes.
###############################################################################

# Include more methods/decorators as you use them
# See http://bottle.readthedocs.org/en/stable/api.html#bottle.Bottle.route
from bottle import response, error, get, route, BaseRequest, request,abort
import json
from argparse import Namespace







###############################################################################
# Routes
#
# TODO: Add your routes here and remove the example routes once you know how
#       everything works.
###############################################################################
@route('/easteregg' , method='GET')
def hello_world():
    response_body = "You reached the easteregg page"
    return response_body
#Used for Id, seems not neccesary:
#db.execute('SELECT id FROM table ORDER BY column DESC LIMIT 1')
#id =db.fetchone()


#{"category": "FruitR", "date": "2014-10-06", "amount": 5, "name": "BananaSSS", "location": "DAMSCO"}

@route('/create', method='POST') 
def db_create(db):
    try:
        Update = json.load(request.body)
        data= json.dumps(Update)
        n = json.loads(data, object_hook=lambda d: Namespace(**d))
    except:
        abort(415)
        return
    
    db.execute('INSERT INTO inventory(name, category, location, date, amount) VALUES (?,?,?,?,?)',(n.name,n.category,n.location,n.date,n.amount))
    response.set_header('content-type', 'text/txt')
    response.add_header('accept','application/json')
    response.add_header('Access-Control-Allow-Origin', '*')
    response.add_header('Allow', 'POST, HEAD')
    response.status = 201
    return "OK"

@route('/update/<rownumber>', method='PUT')
def db_update(db,rownumber):
    try:
        Update = json.load(request.body)
        data= json.dumps(Update)
        x = json.loads(data, object_hook=lambda d: Namespace(**d))
    except:
        abort(415)
        return
    
    db.execute("UPDATE inventory SET name = ?,category= ?, location= ?, date= ?, amount= ?  WHERE id = ?", (x.name,x.category,x.location,x.date,x.amount, rownumber))
    response.set_header('content-type', 'text/txt')
    response.add_header('accept','application/json')
    response.add_header('Access-Control-Allow-Origin', '*')
    response.add_header('Allow', 'PUT, HEAD')
    return "OK"

@route('/delete/<rownumber>', method="DELETE")

def db_delete(db,rownumber):
    db.execute('DELETE FROM inventory WHERE id=?',rownumber)
    response.add_header('Access-Control-Allow-Origin', '*')
    response.add_header('Allow', 'DELETE, HEAD')
    return "OK"


@route('/reset', method='DELETE')
def db_reset(db):
    db.execute('DELETE  FROM inventory')
    db.execute("INSERT INTO inventory(name, category, location, date, amount) VALUES ('Banana', 'Fruit', 'Amsterdam', '2014-10-05', '15')")
    response.add_header('Access-Control-Allow-Origin', '*')
    response.add_header('Allow', 'DELETE, HEAD')
    return "OK"

@route('/reset-all', method='DELETE')
def db_resetall(db):
    db.execute("DELETE FROM inventory")
    response.add_header('Access-Control-Allow-Origin', '*')
    response.add_header('Allow', 'DELETE, HEAD')
    return "OK"

@route('/retrieve-all', method='GET')
def retrieve_db(db):
    db.execute("SELECT name, category, location, date, amount FROM inventory")
    names = db.fetchall()
    database = json.dumps(names)
    response.set_header('content-type', 'application/json')
    response.add_header('Access-Control-Allow-Origin', '*')
    response.add_header('Allow', 'GET, HEAD')
    return database


@route('/retrieve/<rownumber>', method='GET')
def retrieveone_db(db,rownumber):
    db.execute("SELECT name, category, location, date, amount FROM inventory WHERE id=?", rownumber)
    rowRAW=db.fetchone()
    rowJSON=json.dumps(rowRAW)
    response.set_header('content-type', 'application/json')
    response.add_header('Access-Control-Allow-Origin', '*')
    response.add_header('Allow', 'GET, HEAD')
    return rowJSON
    


###############################################################################
# Error handling
#
# TODO: Add sensible error handlers for all errors that may occur when a user
#       accesses your API.
###############################################################################

@error(404)
def error_404_handler(e):

    # Content type must be set manually in error handlers
    response.content_type = 'application/json'

    return json.dumps({'Error': {'Message': e.status_line, 'Status': e.status_code}})
@error(415)
def error_415_handler(e):
    response.content_type = 'text/txt'
    response.set_header('Access-Control-Allow-Origin','*')
    return "Valid JSON format expected in body"

###############################################################################
# This starts the server
#
# Access it at http://localhost:8080
#
# If you have problems with the reloader (i.e. your server does not
# automatically reload new code after you save this file), set `reloader=False`
# and reload manually.
#
# You might want to set `debug=True` while developing and/or debugging and to
# `False` before you submit.
#
# The installed plugin 'WtPlugin' takes care of enabling CORS (Cross-Origin
# Resource Sharing; you need this if you use your API from a website) and
# provides you with a database cursor.
###############################################################################

if __name__ == "__main__":
    from bottle import install, run
    from wtplugin import WtDbPlugin, WtCorsPlugin

    install(WtDbPlugin())
    install(WtCorsPlugin())
    run(host='localhost', port=8080, reloader=True, debug=True, autojson=False)