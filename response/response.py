from validator_collection import checkers

def main():
     print(validate(input("What's your email address? ")))

def validate(value):
     email_address = checkers.is_email(value)
     if email_address:
          return 'Valid'
     else:
          return 'Invalid'

if __name__ == '__main__':
     main()