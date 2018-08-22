age = input('請輸入年齡(age): ')
country = input('請輸入國籍(country): ')
age = int(age)
if country == '台灣' or country == '美國':
	if country == '台灣':
		if age > 18:
			print('你可以考駕照了')
		else:
			print('你還不能考駕照')
	if country == '美國':
		if age > 16:
			print('你可以考駕照了')
		else:
			print('未到達法定年齡')
else:
	print('請諮詢您的國家 謝謝!')