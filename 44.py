import urllib.request
import urllib.parse
def main():
    #p=urllib.request.ProxyHandler({'http':'http://user:password@proxysis:8080',         'https':'https://usuario:password@proxysis:8080'})
    #o=urllib.request.build_opener(p)
    #urllib.request.install_opener(o)    
    url_get='http://httpbin.org/get'
    datos_get={'profesor':'Sebastian','alumnos':'AXIA','metodo':'GET'}
    codigo_get=urllib.parse.urlencode(datos_get)
    resultado_get=urllib.request.urlopen(url_get+'?'+codigo_get)
    print('Resultado de GET: {0}'.format(resultado_get.status))
    print(resultado_get.read().decode('utf-8'))
    url_post='http://httpbin.org/post'
    datos_post={'profesor':'Sebastian','alumnos':'AXIA','metodo':'POST'}
    codigo_post=urllib.parse.urlencode(datos_post)
    resultado_post=urllib.request.urlopen(url_post,data=codigo_post.encode())
    print('Resultado de POST: {0}'.format(resultado_post.status))
    print(resultado_post.read().decode('utf-8'))
if __name__=='__main__':main()
