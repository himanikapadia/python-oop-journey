# Custom Exceptions

class InvalidUsernameError(Exception):
    """Raised when the username is incorrect."""
    pass


class InvalidPasswordError(Exception):
    """Raised when the password is incorrect."""
    pass


# Stored Credentials

USERNAME = "admin"
PASSWORD = "python123"


# Driver Code

try:
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username != USERNAME:
        raise InvalidUsernameError("Invalid Username!")

    if password != PASSWORD:
        raise InvalidPasswordError("Invalid Password!")

except InvalidUsernameError as e:
    print(f" {e}")

except InvalidPasswordError as e:
    print(f" {e}")

else:
    print("\n---- Login Successful! ----")
    print(f"Welcome, {username}!")

finally:
    print("\nLogin session ended.")