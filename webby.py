from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>

<head>
<title>Top 5 companies</title>
</head>
<body>
<table border="4" cellspacing="8" cellpadding="5" width="50" height="50">
<h3>Top 5 Software Companies</h3>
<tr>
<th>Rank</th>
<th>Name of the company</th>
<th>Revenue(in billion)</th>
</tr>
<tr>
<td>1.</td>
<td>Microsoft</td>
<td>1,780</td>
</tr>
<tr>
<td>2.</td>
<td>Google</td>
<td>1,195</td>
</tr>
<tr>
<td>3.</td>
<td>Oracle</td>
<td>240</td>
</tr>
<tr>
<td>4.</td>
<td>SAP</td>
<td>132</td>
</tr>
<tr>
<td>5.</td>
<td>IBM</td>
<td>131.1</td>
</tr>
</table>
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