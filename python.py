import platform
import socket
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
f = open('/usr/share/nginx/html/index.html', 'w')
  
html_template = """<html>
<head>
<title>Title</title>
</head>
<body> """
html_template += "<h2>Welcome To HostName</h2> "
  
#html_template += "<p>"+platform.node()+"</p>"
html_template += "<p>"+host_name+"</p>"
html_template += "<p>"+host_ip+"</p>"

html_template += """  
</body>
</html>
"""
  
# writing the code into the file
f.write(html_template)
  
# close the file
f.close()
