#from urllib import request,parse
import urllib.request
import urllib.parse

def main():
    url_get='http://httpbin.org/get'
    datos_get={'profesor':'Sebastian','alumnos':'UTE','metodo':'GET'}
    codigo_get=urllib.parse.urlencode(datos_get)
    resultado_get=urllib.request.urlopen(url_get+'?'+codigo_get)
    print('Resultado de GET: {}'.format(resultado_get.status))
    print(resultado_get().decode('utf-8'))
#    url_post='http://httpbin.org/put'
#    datos_post={'profesor':'Sebastian','alumnos':'UTE','metodo':'POST'}
#    codigo_post=urllib.parse.urlencode(datos_post)
#    resultado_post=urllib.request.urlopen(url_post,data=codigo_post.encode())
#    print('Resultado de POST: {}'.format(resultado_post.status))
#    print(resultado_post().decode('utf-8'))
if __name__=='__main__':main()

