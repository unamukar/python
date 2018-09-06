from http import HTTPStatus
import urllib.request
from urllib.error import HTTPError,URLError
def main():
    url_html='http://httpbin.org/html'
    url_404='http://httpbin.org/status/404'
    url_wrong='http://nosuchserver.org'
    for x in url_html,url_404,url_wrong:
        try:
            y=urllib.request.urlopen(x)
            print('Resultado: {0}'.format(y.status))
            if y.getcode()==HTTPStatus.OK:print(y.read().decode('utf-8'))
        except HTTPError as z:print('Error HTTP: {0}'.format(z.code))
        except URLError as z:print('Error URL: {0}'.format(z.reason))
if __name__=='__main__':main()
