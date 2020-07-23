# Это игра по угадыванию чисел
import random

guessesTaken = 0


print('Привет! Как тебя зовут?')
myName = input()

number = random.randint(1, 20)
print('Что ж, ' + myName + ', я загадываю число от 1 до 20.')

for guessesTaken in range(6):
	print('Попробуй угадать.')
	guess = input()
	guess = int(guess)

	if guess < number:
		print('Мое число больше!')

	if guess > number:
		print('Мое число меньше!')
	if guess == number:
		break
if guess == number:
	guessesTaken = str(guessesTaken + 1)
	print('Не плохо, ' +  myName + '! Ты справился за ' + guessesTaken + ' попытки!')

if guess != number:
	number = str(number)
	print('Увы( Я загадала число ' + number + '.')