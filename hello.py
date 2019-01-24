#!/usr/bin/env python3

import cgi
import cgitb
import os
import json
from templates import login_page

cgitb.enable()

print("Content-Type: text/html\n")
print()
print("<!doctype html><title>Hello</title><h2>Hello World</h2>")
print(login_page())

form = cgi.FieldStorage()
print("NAME: ")
print(form.getvalue("username"))
print(form.getvalue("password"))



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
