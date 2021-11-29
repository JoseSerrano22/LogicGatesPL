import basic
import basis

print(
	"HERE ARE SOME BASIC OPERATIONS: \n" +
	"AND, *: And operation \n" +
	"OR, +: Or operation \n" +
	"NOT, !: Not operation \n" +
	"XOR, -: XOR operation \n" +
	"VAR: Initialize variables\n" +
	"STOP: end program"
)

while True:

		text = input('basic > ')
		if text == 'stop':
			break
		result, error = basis.run('<stdin>', text)

		if error: print(error.as_string())
		else: print(result)