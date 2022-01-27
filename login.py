#!/usr/bin/env python3
#The code from the TAs lab lecture
import cgi
import cgitb
from http.cookies import SimpleCookie
from tkinter import N
cgitb.enable()

from templates import login_page, secret_page, after_login_incorrect
import secret
import os

#Q4: How does the POSTed data come to the CGI script?

s = cgi.FieldStorage()
username = s.getvalue("username")
password = s.getvalue("password")

form_ok =  username== secret.username and password == secret.password

#setup cookie
cookie = SimpleCookie(os.environ["HTTP_COOKIE"])
cookie_username =   Nonecookie_password = None
if cookie.get("username"):
    cookie_username = cookie.get("username").value
if cookie.get("password"):
    cookie_password = cookie.get("password").value
#check if the cookie username/password == secret username/password
cookie_ok =  cookie_username== secret.username and cookie_password == secret.password

#3 then set cookie username/ password == sercet username/password
if cookie_ok:
    username = cookie_username
    password = cookie_password
    
print("Content-type: text/html")
if form_ok:
    #set cookie iff login info correct
    print(f"Set-Cookie: username={username}")
    print(f"Set-Cookie: password={password}")

print()

if not username and not password:
    print(login_page())

elif username == secret.username and password == secret.password:
    print(secret_page(username, password))
else:
    print(after_login_incorrect())
    #print("<p>username = {}</p> <p> password = {}</p>".format(username, password))