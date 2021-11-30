# LogicGatesPL

This program is a tool that allows the user to create a truth table from boolean algebra, the tool is aimed primarily aimed at
people beggining to learn the basics of Logic Gates and want a quick and easy way to visualize various combinations in the from
of a truth table 






## Features

- Creating Truth Tables from boolean algebra equations
- Calculating the result of boolean algebra equations after inputing values into the variables



## Usage/Examples


```python
basic > "ab"
+-----+-----+
|  a  |  b  |
|-----+-----+
|  1  |  1  |
|  1  |  0  |
|  0  |  1  |
|  0  |  0  |
+-----+-----+
```

Input : "a + b"

Output:
```python
basic > "a + b"
+-----+-----+----------+
|  a  |  b  |  a or b  |
|-----+-----+----------|
|  1  |  1  |    1     |
|  1  |  0  |    1     |
|  0  |  1  |    1     |
|  0  |  0  |    0     |
+-----+-----+----------+
```

Input: (a * b) or (c - d)

Output:
```python
basic > "(a * b) or (c - d)"
+-----+-----+-----+-----+--------------------------+
|  a  |  b  |  c  |  d  |  (a and b) or (c xor d)  |
|-----+-----+-----+-----+--------------------------|
|  1  |  1  |  1  |  1  |            1             |
|  1  |  1  |  1  |  0  |            1             |
|  1  |  1  |  0  |  1  |            1             |
|  1  |  1  |  0  |  0  |            1             |
|  1  |  0  |  1  |  1  |            0             |
|  1  |  0  |  1  |  0  |            1             |
|  1  |  0  |  0  |  1  |            1             |
|  1  |  0  |  0  |  0  |            0             |
|  0  |  1  |  1  |  1  |            0             |
|  0  |  1  |  1  |  0  |            1             |
|  0  |  1  |  0  |  1  |            1             |
|  0  |  1  |  0  |  0  |            0             |
|  0  |  0  |  1  |  1  |            0             |
|  0  |  0  |  1  |  0  |            1             |
|  0  |  0  |  0  |  1  |            1             |
|  0  |  0  |  0  |  0  |            0             |
+-----+-----+-----+-----+--------------------------+
```

Utilizing initialized variables:
```python
basic > VAR a = 0
0
basic > VAR b = 1
1
basic > a * b
0
basic > a + b
1
basic > a * !b
0
```

## Run Locally

Clone the project

```bash
  git clone https://github.com/JoseSerrano22/LogicGatesPL.git
```

Go to the project directory

```bash
  cd LogicGatesPL
```

Install dependencies

```bash
  pip install truth-table-generator
```

Start Program

```bash
  python3 shell.py
```

To input boolean algebra equations and get a truth table that represents
 the outcomes it must be enclosed by quitation marks and leave spaces between variables and operators.

Ex. ```"a + b"``` or ```"a and b"```

To initialize variable values you must first write ```VAR``` leave a space and indicate the variable then
 equal the value you want to store.

Ex. ```VAR a = 1```


Basic operations available:

	AND, *: And operation
	OR, +: Or operation
	NOT, !: Not operation
	XOR, -: XOR operation
	VAR: Initialize variables
	STOP: end program
## Authors

- [@joseserrano](https://github.com/JoseSerrano22)
- [@moisesrobles](https://github.com/moisesrobles-04)
- [@andreclavell](https://github.com/AndreClavell)
