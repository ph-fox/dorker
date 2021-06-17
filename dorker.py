import time, readline
import os, sys
from googlesearch import search


def menu():
	dork = input('dork: ')
	amount = int(input('amount: '))
	lang = input('Enter language (e.g: en, fr, jp): ')
	print('='*25)
	count = 0
	for res in search(dork, lang=lang, num_results=amount):
		time.sleep(.1)
		count+=1
		print(f'[{count}] {res}')

		if count >= amount:
			break
	print('\nComplete!')


menu()

