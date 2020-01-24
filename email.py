email = input('Enter Email: ')

if '@' in email:
  email_slicer = email.split('@')
  print(email_slicer)
else:
  print('Enter in a correct email')
