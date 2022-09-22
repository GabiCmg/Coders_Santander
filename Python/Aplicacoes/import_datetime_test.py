import datetime as dt
import csv

print(dt.time(12, 6, 21, 2), 'Hora:minuto:segundo.microsegundo')
print('---------------------------------')
print(dt.date(2020, 4, 25), 'Ano-mês-dia')
print('---------------------------------')
print(dt.datetime(2020, 4, 25, 12, 6, 21, 2), 'Ano-mês-dia Hora:minuto:segundo.microsegundo')

print('\n\n==============================\n\n')

natal = dt.date(2020, 12, 25)
reveillon = dt.date(2021, 1, 1)

print(reveillon - natal)
print((reveillon - natal).days)
print((reveillon - natal).seconds)
print((reveillon - natal).microseconds)