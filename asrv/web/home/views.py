headers = (
    "HTTP/1.1 200 OK\r\nServer: nginx/1.2.1\r\n"
    "Date: Sat, 08 Mar 2014 22:53:46 GMT\r\n"
    "Content-Type: text/html\r\n"
    "Content-Length: {}\r\n"
    "Connection: keep-alive\r\n\r\n"
)

body = (
    "<html>"
    "<head><title>Document</title></head >"
    "<body bgcolor='white'>"
    "<center><h1>Hello</h1></center>"
    "<hr><center>nginx</center>"
    "</body>"
    "</html>"
)


def home_page(request):
    return (headers.format(len(body)) + body).encode('utf-8')
