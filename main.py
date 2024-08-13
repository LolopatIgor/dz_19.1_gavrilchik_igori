from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse
import os

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):


    def __get_html_content(self):
        file_path = os.path.join(os.path.dirname(__file__), 'index.html')

        try:
            # Открываем файл и читаем его содержимое
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            # Если файл не найден, возвращаем сообщение об ошибке
            return "<html><body><h1>404 Not Found</h1></body></html>"

    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)
        page_content = self.__get_html_content()
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))


if __name__ == "__main__":
    server = HTTPServer((hostName, serverPort), MyServer)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

    server.server_close()

