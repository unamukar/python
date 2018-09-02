#!/usr/bin/env python3
class Service:
    def __init__(self,**kwargs):
        self._type=kwargs['type'];self._app=kwargs['app'];self._version=kwargs['version']
    def type(self):return self._type
    def app(self):return self._app
    def version(self):return self._version
def print_service(o):
    print('The {} is {} (version {})'.format(o.type(),o.app(),o.version()))
def main():
    x=Service(type='DNS',app='bind',version='9.11')
    y=Service(type='Web',app='nginx',version='1.13')
    z=Service(type='DB',app='mysql',version='5.5')
    for i in x,y,z:print_service(i)
    print_service(Service(type='CMS',app='drupal',version='7.32'))
if __name__ == '__main__': main()
