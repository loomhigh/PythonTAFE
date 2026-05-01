# import random number generator module
import random

# set min and max values
min_value = 1
max_value = 50

# Generate a random whole number between 1-50
secret_number = random.randint(min_value, max_value)

# set the default value for guess to Zero
user_guess = 0

# set attempts value
attempts = 0

print(secret_number)