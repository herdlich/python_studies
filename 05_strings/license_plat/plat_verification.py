# Task description: The number must follow this format:
# 1) <LETTER><NUMBER><NUMBER><NUMBER><LETTER><LETTER>_<NUMBER><NUMBER>
# 2) <LETTER><NUMBER><NUMBER><NUMBER><LETTER><LETTER>_<NUMBER><NUMBER><NUMBER>
# 3) The letters contain Cyrillic characters: “АВЕКМНОРСТУХ”

license_plate = input('Enter licence plate number: ')
count = 0
letters = 'АВЕКМНОРСТУХ'
let = license_plate[0] + license_plate[4:6]

# Here we check that the license plate number is in the correct format:
if license_plate[0].isalpha() and license_plate[1:4].isdigit() and license_plate[4:6].isalpha() and license_plate[
    6] == '_' and license_plate[7:10].isdigit() and license_plate.isupper() and 9 <= len(license_plate) <= 10:
    for el in let:  # Here we determine the correspondence with the Cyrillic alphabet
        if el in letters:
            count += 1
if count == 3:  # Only 3 letters in all license plate formats
    print('YES')
else:
    print('NO')
