#!/usr/bin/env python3
class Service:
    def __init__(self,**kwargs):
        if 'type' in kwargs:self._type=kwargs['type']
        if 'app' in kwargs:self._app=kwargs['app']
        if 'version' in kwargs:self._version=kwargs['version']
    def type(self,t=None):
        if t:self._type=t
        try:return self._type
        except AttributeError:return '"unknown service type"'
    def app(self,a=None):
        if a:self._app=a
        try:return self._app
        except AttributeError:return '"unknown app"'
    def version(self,v=None):
        if v:self._version=v
        try:return self._version
        except AttributeError:return '"unknown version"'
    def __str__(self):
        return 'The {} is {} ({})'.format(self.type(),self.app(),self.version())
class DNS(Service):
    def __init__(self,**kwargs):
        self._type='DNS'
        if 'type' in kwargs:del kwargs['type']
        super().__init__(**kwargs)
class Web(Service):
    def __init__(self,**kwargs):
        self._type='Web'
        if 'type'in kwargs:del kwargs['type']
        super().__init__(**kwargs)
class DB(Service):
    def __init__(self,**kwargs):
        self._type='DB'
        if'type'in kwargs:del kwargs['type']
        super().__init__(**kwargs)
    def password(self,p=None):
        if p:self._password=p
        try:return self._password
        except AttributeError:return 'unknown.'
    def __str__(self):
        return 'The {} is {} ({}) and the root password is: {}'.format(self.type(),self.app(),self.version(),self.password())
def main():
    x=DNS(app='bind',version='9.11')
    y=Web(app='nginx',version='1.13')
    z=DB(app='mysql',version='5.5')
    for i in x,y,z:print(i)
    print(Service())
    z.version('5.6');print(z);print(x)
    print(z);z.password('pa$$w0rd');print(z)
if __name__ == '__main__': main()
