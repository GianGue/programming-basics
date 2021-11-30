#different list of month divided by number of days
group1 = ["Gennaio", "Marzo", "Maggio", "Luglio", "Agosto", "Ottobre", "Dicembre"]

#request insert month with capital letter and in italian
month=input(str("Per favore inserisci il mese utilizzando la prima lettera maiuscola: "))
if month in group1: 
  print("Il tuo mese ha 31 giorni!")
elif month == str("Febbraio"):
  print("Il tuo mese potrebbe avere 28 o 29 giorni!")
else:
    print("Il tuo mese ha 30 giorni!")