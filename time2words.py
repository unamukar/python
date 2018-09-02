#!/usr/bin/env python3
def m2w(nnnnnn):
    n=tuple(nnnnnn)
    r=n[::-1]
    if len(n)<4:return n2w(nnnnnn)
    else:
        centenas=n2w('{}{}{}'.format(r[2],r[1],r[0]))
        if len(n)==4:millares=n2w('{}'.format(r[3]))
        elif len(n)==5:millares=n2w('{}{}'.format(r[4],r[3]))
        else:millares=n2w('{}{}{}'.format(r[5],r[4],r[3]))
        if r[2]=='0':add=' and '
        else:add=' '
        return '{} thousand{}{}'.format(millares,add,centenas)
def n2w(nnn):
    n=tuple(nnn)
    if len(n)==1:c='0';d='0';u=n[0]
    elif len(n)==2:c='0';d=n[0];u=n[1]
    else:c=n[0];d=n[1];u=n[2]
    ones=(None,'one','two','three','four','five','six','seven','eight','nine')
    tens=(None,'ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety')
    teen=(None,'eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen')
    if d=='0':decenas=ones[int(u)]
    elif u=='0':decenas=tens[int(d)]
    elif d=='1':decenas=teen[int(u)]
    else:decenas='{}-{}'.format(tens[int(d)],ones[int(u)])
    if c=='0':return decenas
    else:return '{} hundred and {}'.format(ones[int(c)],decenas)
class t2w:
    def __init__(self,time):
        _t=time.split(':');self._hour=_t[0];self._minute=_t[1]
    def hour(self):return self._hour
    def minute(self):return self._minute
    def h2w(self):
        _H=self.hour();_h=int(_H)
        if int(self.minute())<=30:
            if _h==0:return 'midnight'
            elif _h==12:return 'noon'
            else:return n2w(_H)
        else:
            if _h==23:return 'midnight'
            elif _h==11:return 'noon'
            else:return n2w(str(1+_h))
    def m2w(self):
        _M=self.minute();_m=int(_M)
        if _m==0:return "o'clock"
        elif _m==30:return 'half past'
        elif _m==15:return 'quarter past'
        elif _m==45:return 'quarter to'
        elif _m<30:return '{} past'.format(n2w(_M))
        else:return '{} to'.format(n2w(str(60-_m)))
    def __str__(self):
        if self.minute()=='00':return '{} {}'.format(self.h2w(),self.m2w())
        else:return '{} {}'.format(self.m2w(),self.h2w())
