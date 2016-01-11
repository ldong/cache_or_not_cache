#!/usr/bin/env python
import SimpleHTTPServer

class MyHTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_my_headers()
        SimpleHTTPServer.SimpleHTTPRequestHandler.end_headers(self)

    def send_my_headers(self):
        # Cache for 2 DAYS
        self.send_header("cache-control", "public, max-age=290304000")
        self.send_header("expires", "Fri, 18 Jan 2016 19:39:13 GMT")
        # self.send_header("Last-Modified", "Fri, 18 Jan 2016 19:39:13 GMT")

        # No Cahce
        # self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        # self.send_header("Pragma", "no-cache")
        # self.send_header("Expires", "0")


if __name__ == '__main__':
    SimpleHTTPServer.test(HandlerClass=MyHTTPRequestHandler)
