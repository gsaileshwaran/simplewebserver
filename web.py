from django.shortcuts import render,HttpResponse
from http.server import HTTPServer,BaseHTTPRequestHandler
content="""
<!DOCTYPE html>
<html>
<head>
  <title>Countries and Capitals</title>
</head>
<body>
  <h1>List of Countries and Their Capitals</h1>

  <p><strong>Name:</strong> Saileshwaran Ganesan</p>
  <p><strong>Register Number:</strong> 212224230237</p>

  <p>Below is a simple table showing some countries and their respective capitals.</p>

  <table border="1">
    <tr>
      <th>Country</th>
      <th>Capital</th>
      <th>Continent</th>
    </tr>
    <tr>
      <td>India</td>
      <td>New Delhi</td>
      <td>Asia</td>
    </tr>
    <tr>
      <td>France</td>
      <td>Paris</td>
      <td>Europe</td>
    </tr>
    <tr>
      <td>Brazil</td>
      <td>Brasília</td>
      <td>South America</td>
    </tr>
    <tr>
      <td>Canada</td>
      <td>Ottawa</td>
      <td>North America</td>
    </tr>
    <tr>
      <td>Australia</td>
      <td>Canberra</td>
      <td>Australia</td>
    </tr>
    <tr>
      <td>Japan</td>
      <td>Tokyo</td>
      <td>Asia</td>
    </tr>
  </table>

</body>
</html>

"""
class Myserver(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200)
        self.send_header("content-type","text/html")
        self.end_headers()
        self.wfile.write(content.encode())
print("This is my webserver")
serveraddress=('',8000)
httpd = HTTPServer(serveraddress,Myserver)
httpd.serve_forever()