import basic
import basis

while True:
		text = input('basic > ')
		result, error = basis.run('<stdin>', text)

		if error: print(error.as_string())
		else: print(result)