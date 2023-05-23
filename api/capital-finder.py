from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):

        s= self.path
        
        url_com = parse.urlsplit(s)
        query_list = parse.parse_qsl(url_com.query)
        # print (query_list)
        dic = dict(query_list)
        country = dic.get("country")
        
        if country:
            url= "https://restcountries.com/v3.1/name/"
            res = requests.get(url+country)
            data = res.json()
            result = data[0]["capital"][0]
            result2 = f"The capital of {country} is {result}."

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(result2.encode('utf-8'))
        return