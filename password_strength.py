  def check_password_strength(password):
  """
  This function checks the strength of a password based on various criteria.

  Args:
      password (str): The password to be checked.

  Returns:
      str: A message indicating the password strength and suggestions for improvement.
  """
  minLength = 8
  hasUpper = False
  hasLower = False
  hasNumber = False
  hasSymbol = False
  for char in password:
    if char.isupper():
      hasUpper = True
    elif char.islower():
      hasLower = True
    elif char.isdigit():
      hasNumber = True
    else:
      hasSymbol = True

  score = 0
  if len(password) >= minLength:
    score += 1
  if hasUpper:
    score += 1
  if hasLower:
    score += 1
  if hasNumber:
    score += 1
  if hasSymbol:
    score += 1

  feedback = ""
  if score == 0:
    feedback = "This password is extremely weak. Please choose a new password."
  elif score <= 2:
    feedback = "This password is weak. It should be at least {} characters long and include a combination of uppercase, lowercase, numbers, and symbols.".format(minLength)
  elif score == 3:
    feedback = "This password is moderately strong. Consider adding another character type for better security."
  else:
    feedback = "This password is strong!"

  return feedback

# Get password input from user
password = input("Enter your password: ")

# Print the strength feedback
strength_message = check_password_strength(password)
print(strength_message)
