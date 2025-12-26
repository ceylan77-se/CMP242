import random
import string


class PasswordGenerator:
    def __init__(self, length=12):
        self.length = length
        self.characters = (
            string.ascii_letters +
            string.digits +
            string.punctuation
        )

    def generate(self):
        return "".join(random.choice(self.characters) for _ in range(self.length))


class PasswordManager:
    def __init__(self, filename="passwords.txt"):
        self.filename = filename

    def save_password(self, password):
        with open(self.filename, "a", encoding="utf-8") as file:
            file.write(password + "\n")

    def show_saved(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                print("\n--- Saved Passwords ---")
                print(file.read())
        except FileNotFoundError:
            print("No saved passwords yet.")

def main():
    print("=== OOP Password Generator ===")

    length = int(input("Enter password length: "))

    generator = PasswordGenerator(length)
    manager = PasswordManager()

    password = generator.generate()
    print("\nGenerated Password:")
    print(password)

    manager.save_password(password)
    print("\nPassword saved to passwords.txt")

    show = input("\nShow saved passwords? (y/n): ")
    if show.lower() == "y":
        manager.show_saved()


if __name__ == "__main__":
    main()