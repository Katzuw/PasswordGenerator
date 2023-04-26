import string
import secrets
import time

characters = string.ascii_letters + string.digits
password = "".join(secrets.choice(characters) for i in range(20))
print("Hello")
time.sleep(1)
print(password)
time.sleep(0.5)
print("Bye!")

