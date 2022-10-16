#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


#старое решение


text = 'не выходи из комнаты абв не совершай ошибку абв зачем тебе солнце абв если ты куришь шипку абв'
print(f"Исходный текст: {text}")
del_txt = "абв"
lst = [i for i in text.split() if del_txt not in i]
print(f'Результат: {" ".join(lst)}')

# Новое решение

def delite_abv(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)

text = delite_abv(text)
print(text)






