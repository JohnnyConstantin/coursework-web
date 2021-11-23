import cgi

form = cgi.FieldStorage()
searchterm = form.getvalue('item_to_search')
print(searchterm)