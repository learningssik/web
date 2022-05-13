#!C:\Users\wonsik\anaconda3\python.exe
print('content-type: text/html; charset=UTF-8')
print()
import cgi, os, view

form = cgi.FieldStorage()
# pageId = form.getvalue("id")
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId,'r').read()

else:
    pageId = "Hello"
    description = "Hello web"

print('''<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <title>WEB1 - welcome</title>
    <meta charset="utf-8">

  </head>
  <body>
    <h1><a href="index.py">WEB</a></h1>

    <ol>
        {listStrs}
    </ol>

    <form action="process_create.py" method="post">
        <p><input type="text" name="title" placeholder="title"></p>
        <p><textarea rows="4" name="description" placeholder="description"></textarea></p>
        <p><input type="submit"</p>
    </form>
  </body>
</html>

'''.format(title=pageId, desc=description, listStrs=view.getList()))
