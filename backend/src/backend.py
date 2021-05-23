from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import pyramid.httpexceptions as exc
import json
import random
import time

USER_DB_FILE_PATH = './user_database.txt'    # Location of User DB relative to backend.py
TELLO_DB_FILE_PATH = './tello_moves_database.txt'    # Location of User DB relative to backend.py
BACKEND_PORT = 5001    # This is the port number for the backend server

#----------------------Helper Functions-------------------------
# Get ALL users from DB
def get_users(req):
    # Try to read DB to file and catch OSErrors -> system-related error, 
    # including I/O failures such as “file not found”
    try:
        with open(USER_DB_FILE_PATH,'r') as db_file:
            users = json.load(db_file)
    except OSError:
        return exc.HTTPInternalServerError()    # Code 500
    return users

# Add a user to the DB
def add_user(req):
    # Simple server-side validation. 
    # req_fields are the expected fields for the DB.
    # "req.POST.mixed()" returns POST data as a dict.
    req_fields = ["firstName", "lastName", "email", "userName", "pwd"]
    new_user = req.POST.mixed()

    # Extract the keys from the POSTed data and ensure they match the required fields.
    if (sorted(req_fields) == sorted(list(new_user.keys()))):
        users = get_users(req)
        users.append(new_user)

        # Try to write DB to file and catch OSErrors -> system-related error, 
        # including I/O failures such as “file not found”
        try:
            with open(USER_DB_FILE_PATH,'w') as db_file: 
                json.dump(users, db_file)
        except OSError:
            return exc.HTTPInternalServerError()    # Code 500
    else:
        return exc.HTTPBadRequest()    # Code 400

    return exc.HTTPCreated()    # Code 201

# Edit a user in the DB
def edit_user(req):
    
    # Add your code here:
    user_edit = req.POST.mixed()
    entire_users= get_users(req)

    for x in range(0, len(entire_users)):
        if(entire_users[x]['userName'] == user_edit['userName']):
            entire_users[x]['firstName'] = user_edit['firstName']
            entire_users[x]['lastName'] = user_edit['lastName']
            entire_users[x]['email'] = user_edit['email']
            entire_users[x]['userName'] = user_edit['userName']
            entire_users[x]['pwd'] = user_edit['pwd']
            
    try:
        with open(USER_DB_FILE_PATH,'w') as db_file: 
            json.dump(entire_users, db_file)
    except OSError:
        
        return exc.HTTPInternalServerError()    # Code 500
    
    return exc.HTTPCreated()
    #return {} # Placeholder!

def get_tello_moves(req):

    # Add your code here:
    try:
        with open(TELLO_DB_FILE_PATH,'r') as db_file:
            shows = json.load(db_file)
    except OSError:
        return exc.HTTPInternalServerError()    # Code 500
    return shows

# Return fake tello state data

def fake_data(req):
    randValues = random.sample(range(1, 400), 16)
    keys = ["pitch", "roll", "yaw", "vgx", "vgy", "vgz", "templ",
            "temph", "tof", "h", "bat", "baro", "time", "agx", "agy", "agz"]

    fakeData = dict(zip(keys, randValues))

    # This Response sets a header so that CORS requests can be handled... should be behind OAUTH
    response = Response(body=json.dumps(fakeData))
    response.headers.update({'Access-Control-Allow-Origin': '*',})
    return response

if __name__ == '__main__':
    config = Configurator()
    
    #--------------------------Routes---------------------------
    config.add_route('get_users', '/get_users')
    config.add_view(get_users, route_name='get_users', renderer='json')

    config.add_route('add_user', '/add_user')
    config.add_view(add_user, route_name='add_user', renderer='json')

    # Add route to edit user (PUT request)
    # NOTE: route must be '/edit_user'

    # Add route to get Tello moves
    # NOTE: route must be '/get_tello_moves'

    # Add route to get fake Tello move data
    config.add_route('fake_data', '/fake_data')
    config.add_view(fake_data, route_name='fake_data', renderer='json')

    config.add_route('edit_user', '/edit_user')
    config.add_view(edit_user, route_name='edit_user', renderer='json')

    config.add_route('get_tello_moves', '/get_tello_moves')
    config.add_view(get_tello_moves, route_name='get_tello_moves', renderer='json')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', BACKEND_PORT, app)
    server.serve_forever()
