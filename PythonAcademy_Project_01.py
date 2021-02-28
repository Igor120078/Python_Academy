TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

# Vytvoreni slovniku pristupovyvh udaju do systemu
login_database = {'bob': '123',
                  'ann': 'pass123',
                  'mike': 'password123',
                  'liz': 'pass123'}
# vytvoreni oddelovacu pro tisteny vystup
separator1 = '=' * 46
separator2 = '-' * 46

# Vyzadani prihlasovacich udaju od uzivatele
login_name = input('username: ').strip()
login_psw = input('password: ').strip()
print(separator1)

# Overujeme prihlasovaci udaje
if login_name in login_database.keys():
    if login_database[login_name] == login_psw:
        print(f'Welcome to the app, {login_name}\n'
        'We have 3 texts to be analysed.')
        print(separator1)
        user_choice = input('Enter a number btw. 1 and 3 to select: ').strip()

# overime spravnost volby textu k provedeni analizy
        if not user_choice.isdigit() or int(user_choice) not in list(range(1, len(TEXTS) + 1)):
            print(separator1)
            print(f'Sorry, {login_name}, but you had to enter a number btw. 1 and 3 to select the text.')
            exit()
        else:
            # vytvorime list ocistenych slov ze zvoleneho textu
            clean_words = [word.strip('.,!?)(') for word in TEXTS[int(user_choice) - 1].split()]

            # vytvorime a naplnime slovnik podle zadani
            statistics = {'words_count': sum(1 for word in clean_words),
                          'word_starts_title_count': sum(1 for word in clean_words if word.istitle()),
                          'word_alltitle_count': sum(1 for word in clean_words if word.isupper() and word.isalpha()),
                          'word_allsmall_count': sum(1 for word in clean_words if word.islower() and word.isalpha()),
                          'word_is_number_count': sum(1 for word in clean_words if word.isdigit()),
                          'word_is_number_sum': sum(int(word) for word in clean_words if word.isdigit())
                          }
            # vytiskneme pozadovany vystup
            print(separator1)
            print(f"There are {statistics['words_count']} words in the selected text.")
            print(f"There are {statistics['word_starts_title_count']} titlecase words.")
            print(f"There are {statistics['word_alltitle_count']} uppercase words.")
            print(f"There are {statistics['word_allsmall_count']} lowercase words.")
            print(f"There are {statistics['word_is_number_count']} numeric strings.")
            print(f"The sum of all the numbers {statistics['word_is_number_sum']}")

            # Pro graficky vystup vytvorime a naplnime slovnik s vyskytem slov kazde delky
            words_length = {}
            for word in clean_words:
                words_length[len(word)] = words_length.get(len(word), 0) + 1

            # Pripravime hodnoty pro nasledujici tisk
            list_of_length = sorted(words_length)
            word_max_length = max(words_length.values())

            print(separator2)
            print('LEN|', 'OCCURENCES'.center(word_max_length + 2), '|NR.', sep='')
            print(separator2)
            for i in list_of_length:
                print((str(i) + '|').rjust(4), ('*' * words_length[i]).ljust(word_max_length + 2), '|' + str(words_length[i]), sep='')

# Nasleduje tisk sdeleni pri nesplneni podminek pro provedeni analyzy
    else:
        print('Sorry, but your password is incorrect.')
        exit()
else:
    print('Sorry, but you are not registered in the system :(')
    exit()
