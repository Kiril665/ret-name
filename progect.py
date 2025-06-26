
print("привіт, відповіси на питання")

num = input('1 питання: як мене звати?\n')
if num.lower() == 'kiril':
    print('молодець')
else:
    print('ні, ти шо')

num2 = input('2 питання: скільки мені років?\n')
if num2 == '14':
    print('правильно')
else:
    print('неправильно')

num3 = input('3 питання: моя улюблена мова програмування?\n')
if num3.lower() == 'c#' or num3.lower() == 'csharp':
    print('красава')
else:
    print('не вгадав')

print('дякую за відповіді!')


