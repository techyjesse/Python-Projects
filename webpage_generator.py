import webbrowser

f = open('newfile.html', 'w')

message = """<html>
<head>Summer Sale!</head>
<body><p>Stay tuned for our amazing summer sale!</p></body>
</html>"""

f.write(message)
webbrowser.open_new_tab('newfile.html')
