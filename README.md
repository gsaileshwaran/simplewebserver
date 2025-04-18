# EX01 Developing a Simple Webserver
## Date: 18-04-2025

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```
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
```
## OUTPUT:

![alt text](<Screenshot 2025-04-18 130405.png>)

![alt text](<Screenshot 2025-04-18 130415.png>)

## RESULT:
The program for implementing simple webserver is executed successfully.
