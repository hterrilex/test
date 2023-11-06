import locale
locale.setlocale(locale.LC_ALL, '')

import datetime as dt
hoy = dt.date.today()
hora = dt.datetime.now()
t1= dt.time(11,11,11)
t2= dt.time(12,11,11)

print (t2,t1, hoy, hora)

print (t2>t1)