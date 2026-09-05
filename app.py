def main():
	"""Simple addition program: reads two numbers and prints their sum."""
	try:
		a = input("Enter first number: ")
		b = input("Enter second number: ")

		# Try to parse as integer first, then float
		try:
			a_val = int(a)
		except ValueError:
			a_val = float(a)

		try:
			b_val = int(b)
		except ValueError:
			b_val = float(b)

		result = a_val + b_val
		print(f"{a_val} + {b_val} = {result}")
	except Exception as e:
		print("Error:", e)


if __name__ == '__main__':
	main()

