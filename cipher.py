"""
Substitution cipher

Copyright 2013 Yasukawa.T
"""

def rotate_word2(word,n):
	"""return decoded or encoded strings by number 'n'
	word: strings you wanna encode or decode
	n: a number you wanna encode or decode by
	"""
	rotate = ''
	for letter in word:
		if letter in ',. ?\'"-=`\\;:/!@#$%^&*()1234567890':
			rotate += letter
			continue
		rotate += rotate_num(letter,n,letter.islower())
	return rotate

def rotate_num(letter,n,lower):
	"""return rotated letter by a number n
	this function, first, figure out if the letter is uppercase or not.
	then will rotate the letter accordinglly
	letter: a letter of word you wanna encode or decode
	n: a number you wanna encode or decode by
	lower:Assign True if the letter is lowercase, otherwiser False
	"""
	if lower:
		a = 'a'
		z = 'z'
	else:
		a = 'A'
		z = 'Z'
	code = ord(letter)+n
	if code > ord(z):
		code = code - 1  - ord(z)+ ord(a)
	if code < ord(a):
		code = ord(z) -   ( ord(a)-code-1)
	return chr(code) 

if __name__ == '__main__':

		while True:
			message  = raw_input('Write a word or strings you wanna decode or encode (to end Enter q) >>> ')
			if message == 'q':
				break
			n = raw_input('Enter a number you wanna decode or encode by >>> ')
			print 'ta da'
			print 
			print ' '*6,rotate_word2(message,int(n))
			print 
