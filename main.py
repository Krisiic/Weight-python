weight = int(input('How much do you weight: '))
type = input('Kg or Lb: ')
formula = float(2.205)

if type == 'K':
    result = weight * formula
    print('Your weight in Lb is: ', result)

if type == 'L':
    result = weight / formula
    print('Your weight in Kg is: ', result)