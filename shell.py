import basic
import basis

while True:
		text = input('basic > ')
		if text == 'stop':
			break
		result, error = basis.run('<stdin>', text)

		if error: print(error.as_string())
		else: print(result)