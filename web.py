from http.server import HTTPServer, BaseHTTPRequestHandler
content = """

<!DOCTYPE html>
<html>
<head>
<title>My webserver</title>
</head>
<body  bgcolor="lightblue">
<h1>TOP 5 LARGEST SOFTWARE COMPANIES IN THE WORLD</h1>
<br>
<br>
<h2>
    <ol>
        <li>GOOGLE</li>
        <li>APPLE</li>
        <li>AMAZON</li>
        <li>TESLA</li>
        <li>MICROSOFT</li>
    </ol>
</h2>
</body>
</html>

"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
