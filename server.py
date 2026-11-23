#!/usr/bin/env python3
"""Serve the hello zuzu page on the local network at port 8080."""

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import socket

HOST = "0.0.0.0"
PORT = 8080

HTML = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>hello zuzu</title>
  <style>
    html, body { width: 100%; min-height: 100%; margin: 0; }
    body {
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: system-ui, sans-serif;
      font-size: min(12vw, 70vh);
      white-space: nowrap;
    }
  </style>
</head>
<body>hello zuzu</body>
</html>
"""


class PageHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path not in ("/", "/index.html"):
            self.send_error(404)
            return
        body = HTML.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format_string, *args):
        pass


def get_lan_ip():
    """Find the preferred local IPv4 address without sending network traffic."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.connect(("192.0.2.1", 80))  # TEST-NET address; UDP connect sends no packet.
        return sock.getsockname()[0]
    except OSError:
        return "127.0.0.1"
    finally:
        sock.close()


def main():
    server = ThreadingHTTPServer((HOST, PORT), PageHandler)
    server.daemon_threads = True
    lan_ip = get_lan_ip()
    print(f"Local: http://localhost:{PORT}", flush=True)
    print(f"LAN:   http://{lan_ip}:{PORT} (ouvrez cette adresse depuis un appareil du même réseau)", flush=True)
    print("Si nécessaire, autorisez les connexions entrantes sur le port 8080 dans le pare-feu.", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nArrêt du serveur.", flush=True)
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
