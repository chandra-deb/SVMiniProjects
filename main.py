class Calculator:
    def __init__(self):
        self.num1 = None
        self.num2 = None

    def _get_number_input(self, prompt: str):
        num = input(prompt)
        try:
            num = float(num)
            return num
        except ValueError:
            print(num, "is not a number!")
            return self._get_number_input(prompt)

    def _pretty_print(self, operation_sign: str, result: str):
        print(self.num1, operation_sign, self.num2, '=', result)

    def get_input_numbers(self):
        self.num1 = self._get_number_input("Enter first number: ")
        self.num2 = self._get_number_input("Enter second number: ")

    def add(self):
        result = self.num1 + self.num2
        self._pretty_print("+", result)

    def subtract(self):
        result = self.num1 - self.num2
        self._pretty_print("-", result)

    def multiply(self):
        result = self.num1 * self.num2
        self._pretty_print("*", result)

    def _handle_zero_division(self, operation_method):
        print("Cannot divide by zero! Try again with different values.")
        self.get_input_numbers()
        return operation_method()

    def divide(self):
        try:
            result = self.num1 / self.num2
            self._pretty_print("/", result)
        except ZeroDivisionError:
            self._handle_zero_division(self.divide)

    def modulus(self):
        try:
            result = self.num1 % self.num2
            self._pretty_print("%", result)
        except ZeroDivisionError:
            self._handle_zero_division(self.modulus)


print('''Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Modulus
''')
prompt = "Enter choice (1/2/3/4/5):"


def process_selection():
    selected_operation = input(prompt)
    try:
        selected_operation = int(selected_operation)
        if selected_operation < 1 or selected_operation > 5:
            raise ValueError
        return selected_operation
    except ValueError:
        print("Please enter a right choice!")
        return process_selection()


selected_operation = process_selection()
calculator = Calculator()

if selected_operation == 1:
    calculator.get_input_numbers()
    calculator.add()
elif selected_operation == 2:
    calculator.get_input_numbers()
    calculator.subtract()
elif selected_operation == 3:
    calculator.get_input_numbers()
    calculator.multiply()
elif selected_operation == 4:
    calculator.get_input_numbers()
    calculator.divide()
elif selected_operation == 5:
    calculator.get_input_numbers()
    calculator.modulus()
