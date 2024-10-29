import random


class NumberGuessingGame:
    def __init__(self):
        self._random_number = random.randint(1, 100)
        self._attempts_count = 0
        print(self._random_number)

    def _check_user_guess(self, guess_number: int) -> bool:
        if guess_number == self._random_number:
            print(f"Congratulations! You've guessed the number in {self._attempts_count} attempts")
            return True
        elif guess_number > self._random_number:
            print("Too high!")
        elif guess_number < self._random_number:
            print("Too low!")
        return False

    def get_user_guess(self):
        while True:
            guess = input("Enter your guess: ")
            self._attempts_count += 1
            if guess.isnumeric():
                guess = int(guess)
                is_right = self._check_user_guess(guess)
                if is_right:
                    break
            else:
                print("Please enter nothing other than number!")

    def start(self):
        print("Try to guess the number between 1 to 100")
        self.get_user_guess()


NumberGuessingGame().start()
