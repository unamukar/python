#!/usr/bin/env python3
def n2w(nn):
    n=tuple(nn)
    if len(n)==1:d='0';u=n[0]
    else:d=n[0];u=n[1]
    ones=(None,'uno','dos','tres','cuatro','cinco','seis','siete','ocho','nueve')
    tens=(None,'diez','veinte','treinta','cuarenta','cincuenta','sesenta','setenta','ochenta','noventa')
    teen=(None,'once','doce','trece','catorce','quince','dieciseis','diecisiete','dieciocho','diecinueve')
    if d=='0':return ones[int(u)]
    elif u=='0':return tens[int(d)]
    elif d=='1':return teen[int(u)]
    elif d=='2':return 'veinti{}'.format(ones[int(u)])
    else:return '{} y {}'.format(tens[int(d)],ones[int(u)])
class t2w:
    def __init__(self,time):
        t=time.split(':');self._hour=t[0];self._minute=t[1]
    def hour(self):return self._hour
    def minute(self):return self._minute
    def h2w(self):
        H=self.hour();h=int(H)
        if int(self.minute())<=30:
            if h==0:return 'las doce'
            elif h==1:return 'la una'
            elif h==13:return 'la una'
            elif h<13:return 'las {}'.format(n2w(H))
            else:return 'las {}'.format(n2w(str(h-12)))
        else:
            if h==23:return 'las doce'
            elif h==0:return 'la una'
            elif h==12:return 'la una'
            elif h<13:return 'las {}'.format(n2w(str(1+h)))
            else:return 'las {}'.format(n2w(str(1+h-12)))
    def m2w(self):
        M=self.minute();m=int(M)
        if m==0:return "en punto"
        elif m==30:return 'y media'
        elif m==15:return 'y cuarto'
        elif m==45:return 'menos cuarto'
        elif m<30:return 'y {}'.format(n2w(M))
        else:return 'menos {}'.format(n2w(str(60-m)))
    def __str__(self):
        H=self.hour();h=int(H)
        hora=self.h2w();minuto=self.m2w()
        if h<6:return '{} {} de la madrugada'.format(hora,minuto)
        elif h<13:return '{} {} de la manana'.format(hora,minuto)
        elif h<21:return '{} {} de la tarde'.format(hora,minuto)
        else:return '{} {} de la noche'.format(hora,minuto)
