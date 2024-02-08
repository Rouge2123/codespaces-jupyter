# Username and password generator
def username_generator(first_name, last_name):
  if len(first_name) < 3 or len(last_name) < 4:
    username = first_name + last_name
  else:
    username = first_name[:3] + last_name[:4]
  return username
print(username_generator('Abe', 'Simpson'))

def password_generator(username):
  password = ''
  for char in range(0, len(username)):
    password += username[char-1]
  return password

print(password_generator(username_generator('Abe', 'Simpson')))

