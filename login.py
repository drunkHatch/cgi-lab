#!/usr/bin/env python3

import cgi
import cgitb
import os
import json
from templates import login_page, secret_page, after_login_incorrect
from secret import username, password

cgitb.enable()

# print("Content-Type: text/html\n") # showing set cookies here
# print()
# print("<!doctype html><title>Hello</title><h2>Hello World</h2>")
# print(login_page())
"""
form = cgi.FieldStorage()
print("NAME: ")
print(form.getvalue("username"))
print(form.getvalue("password"))
"""

# set cookies
form = cgi.FieldStorage()
p_user = form.getvalue("username")
p_password = form.getvalue("password")

c_username = ""
c_password = ""

try:
    cookie_string = os.environ.get("HTTP_COOKIE")
    cookie_pairs = cookie_string.split(":") #
    for pair in cookie_pairs:
        key, value = pair.split("=")
        if "username" in key:
            c_username = val
        elif "password" in key:
            c_password = val
    print(cookie_string)
except Exception as e:
    pass


if c_username and c_password:
    print("\n\n")
    print(secret_page(c_username, c_password))
elif os.environ.get("REQUEST_METHOD", "GET") == "POST":
    if p_user == username and p_password == password:
        print("Set-Cookies: username={}:".format(p_user))
        # set password cookies
        print("Set-Cookies: password={}:".format(p_password))
        print(secret_page(p_user, p_password))
    else:
        print(after_login_incorrect())
else:
    print(login_page())




"""
# 1 - 3
print(os.environ)

# json for environment variable
env_json = {}
for key,value in os.environ.items():
    env_json[key] = value
#print(json.dumps(env_json))
print("BROWSER: ")
print(os.environ.get("HTTP_USER_AGENT"))
"""
