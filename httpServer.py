from http.server import HTTPServer, BaseHTTPRequestHandler
from DBManager.DBManager import DBManager
import pandas as pd
import os


class FlatsHTTPServer(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        flats = flatsDB.get_flats()
        df = pd.DataFrame.from_dict(flats)
        df[1] = df[1].apply(lambda x: "<img src='" + str(x)) + "'>"
        html = df.to_html(index=False, classes='stocktable', table_id='flats', escape=False)
        self.wfile.write(bytes(html, 'utf-8'))


flatsDB = DBManager()
httpd = HTTPServer((os.environ.get('HTTP_HOST'), 8080), FlatsHTTPServer)
httpd.serve_forever()
