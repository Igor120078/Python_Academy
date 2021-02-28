# MINIPROJECT 01
# Přiřaď proměnným příslušná data
cities = ("Prague", "Wien", "Brno", "Svitavy", "Zlin", "Ostrava")
prices = (1000, 1100, 2000, 1500, 2300, 3400)
discount_cities = ('Svitavy', 'Ostrava')
discount = 0.25
this_year = 2021
oddelovac1 = '=' * 90
oddelovac2 = '-' * 90

# Pozdrav klienta

print(oddelovac1)
print('''Welcome to the DESTINATIO,
place where people plan their trips''')
print(oddelovac1)

# Nabídni mu destinace
print('We can offer you the following destinations:')
print(oddelovac2)
print('''
1 - Prague   | 1000
2 - Wien     | 1100
3 - Brno     | 2000
4 - Svitavy  | 1500
5 - Zlin     | 2300
6 - Ostrava  | 3400
''')
print(oddelovac2)

# Získej vstup uživatele o destinaci
index_destination = (int(input("Please enter the destination number to select: ")) - 1)

if (index_destination) in range(len(cities)):
    aim_city = cities[index_destination]
    price_aim_destination = prices[index_destination]
    # Chek if destination has a discount
    if aim_city in discount_cities:
        price_aim_destination *= (1 - discount)
        print('Luky you! You have just earned 25% discount for your destination -', aim_city)
        input('Press enter to continue...')
    # Začni registraci
    print(oddelovac1)
    print("REGISTRATION:")
    print(oddelovac1)
    print('In order to complete your reservations, please share few details about yourself with us.')
    print(oddelovac2)
    # Check Name and Surname
    name = input("Enter your NAME: ")
    print(oddelovac2)
    surname = input("Enter your SURNAME: ")
    print(oddelovac2)
    if (name + surname).isalpha():
        print(f'Hello, {name} {surname}')
        print(oddelovac2)
    else:
        print('Name and Surname must contain only letters')
        exit()
    # Chek year of birth
    year_of_birth = int(input("YEAR of BIRTH: "))
    if this_year - year_of_birth >= 16:
        print("Countinue, please ...")
    else:
        print("Sorry, but our services are available for people over 16.")
        exit()
    # Check email
    email = input("EMAIL: ")
    if '@' in email and '.' in email:
        print('You email is Ok')
        print(oddelovac2)
    else:
        print('You email is not correct. It must contain "@" and "." !')
        exit()
    # Check password
    psw = input("Enter your PASSWORD: ")
    if len(psw) >= 8 and not psw.isalpha() and not psw.isdecimal() and not psw[0].isdecimal() and not psw[-1].isdecimal():
        print('You password is Ok.')
        print(oddelovac1)
        print(f'Thank you {name} {surname}')
        print('We have made your reservation to', aim_city)
        print('The total price is', price_aim_destination)
        print(f'We will send your ticket to your email {email}')
        print(oddelovac1)
    else:
        print('''The email you entered is in wrong format!
1. Must contain both letters and numbers.
2. Must be at least 8 characters long.
3. Can't begin and end with number.''')
        exit()
else:
    print(f'Choose numbers from 1 to {len(cities)}')
    exit()
