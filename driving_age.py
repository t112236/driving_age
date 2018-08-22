age = input('請輸入年齡: ')
country = input('請輸入國籍: ')
age = int(age)
if country == '台灣':
	if age > 18:
		print('你可以考駕照了')
	else:
		print('你還不能考駕照')
else:
	print('請諮詢您的國家 謝謝!')