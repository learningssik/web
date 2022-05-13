#!C:\Users\wonsik\anaconda3\python.exe

import cgi, os

form = cgi.FieldStorage()
pageId = form["pageId"].value
title = form["title"].value
description = form["description"].value

opened_tile = open('data/'+pageId,'w')
opened_tile.write(description)
opened_tile.close()

os.rename('data/'+pageId, 'data/'+title)

#Redirection
print("Location: index.py?id="+title)
print()
