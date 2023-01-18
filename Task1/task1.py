# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

stroka_teksta = 'орравро ьбтолв тмп абвгурпа тропа приабв длоабвкидп'
print(stroka_teksta)
delst = list(filter(lambda x: 'абв' not in x.lower(), stroka_teksta.split()))
print(delst)