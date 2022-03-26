import json
import os

from flask import Flask, send_from_directory
from functools import wraps
from flask import Response
from flask import request
import mongo_client
# from pymongo import mongo_client


ROOT_FOLDER = "../my-app/build"

app = Flask(__name__, static_folder=os.path.join(ROOT_FOLDER))



class NetflixResponse(object):
    def __init__(self, data, status="success", http_status_code=200, http_extra_headers=None):
        self.data = data
        self.status = status
        self.http_status_code = http_status_code
        self.http_extra_headers = http_extra_headers

    def dictify(self):
        return {"status": self.status, "data": self.data}


def response_wrapper(func):
    @wraps(func)
    def wrapper(**params):

        try:
            func_result = func(**params)
            if type(func_result) is Response:
                return func_result

            response = NetflixResponse(func_result)


        except Exception as err:
            response = NetflixResponse(str(err), "error", 500, {})

        return _make_http_response(response.dictify(), response.http_status_code, response.http_extra_headers)

    return wrapper


def _make_http_response(content=None, status_code=200, extra_headers=None, mimetype="application/json"):
    extra_headers = extra_headers or {}

    if content is None:
        content_string = ""
        mimetype = "text/plain"
    else:
        if mimetype == "application/json":
            content_string = json.dumps(content)
        else:
            content_string = content

    return Response(content_string, status_code, extra_headers, mimetype)

is_task_currently_running = False

favorite_list = []

# this is a function that serves all your UI files - just make sure to edit ROOT_FOLDER to match your project structure
@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path:path>', methods=["GET"])
def files(path):
    return send_from_directory(ROOT_FOLDER, path)

# go ahead and open chrome at http://localhost/demoJson
@app.route('/demoJson', methods=["GET", "POST"])
@response_wrapper
def demoAsJson():
    return "wanna watch a movie?"

# go ahead and open chrome at http://localhost/demoRaw
@app.route('/demoRaw', methods=["GET", "POST"])
def demoRaw():
    return "wanna watch a movie?"

# go ahead and open chrome at http://localhost/demoRaw


@app.route('/addFav', methods=["GET", "POST"])
@response_wrapper
def favorite():
    favorite_movie = request.data
    data_movie = json.loads(favorite_movie)
    #print(favorite_movie)
    #print(data_movie)
    #favorite_list.append(data["fav"])
    mongo_client.insert("amit_fav", data_movie) 
    data = mongo_client.find("amit_fav", {"Title" : "amit"})
    
    print((data[0]["Title"]))
    return json.dumps(data)
   

@app.route('/removeFav', methods=["GET", "POST"])
@response_wrapper
def Favorite():
    favorite_movie = request.data
    data = json.loads(favorite_movie)
    if data["fav"] in favorite_list:
        favorite_list.remove(data["fav"])
    else:
        return "there is not such movie"


if __name__ == '__main__':
    app.run("0.0.0.0", 80, debug=True)
