# encoding: utf-8

from flask import Blueprint, request, jsonify
import requests


blueprint = Blueprint('user', __name__, url_prefix='/user')


@blueprint.route("/login", methods=["GET"])
def login():
    github_code = request.args.get('code') 
                           
    auth_data={
            "code": github_code,
            "client_id":"YOUR_AUTH_APP_CLIENT_ID", 
            "client_secret":"YOUR_AUTH_APP_CLIENT_SECRET",
            "redirect_uri": "http://localhost:3000/login"                
        }
    resp = requests.post("https://github.com/login/oauth/access_token", data=auth_data)       
    print(resp.text)
    if resp.status_code == 200 and "access_token=" in resp.text:        
        token = resp.text.split("access_token=")[1]
        token = token.split("&")[0]
        user = requests.get("https://api.github.com/user", headers={"Authorization": "token " + token})            
        if user.status_code == 200:
            user_data = user.json()                
            response_data = {}                           
            response_data["github_token"] = token
            response_data["username"] = user_data.get('login')            
            response = jsonify({'_result': response_data})        
            return response
     