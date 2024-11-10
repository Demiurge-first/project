import os
import random

clear = lambda: os.system('cls')

print('Привет! Я загадал слово, твоя задача - угадать его по буквам.')
input('*Нажмите Enter, чтобы продолжить*')
clear()
print('Поехали!')

words = ['исподвыподверта','пирожок', 'чебурек', 'огурец', 'сосиска', 'котик', 'квокка', 'корабль', 'самолет', 'автомобиль', 'дирижабль']
word = random.choice(words)
print(word)

letters = []
isWin = True
hp = 10

while hp > 0:
    isWin = True
    for sumb in word:
        if sumb in letters:
            print(sumb, end=' ')
        else:
            print('*', end=' ')
            isWin = False
    print()

    if isWin:
        print('Ты угодал! Молодец!')
        break

    letter = input('Введите букву: ').lower()
    letters.append(letter)
    clear

    if letter not in word:
        hp -= 1
        print(f'Осталось попыток: {hp}')

if hp <= 0:
    print('Вы повесились!')