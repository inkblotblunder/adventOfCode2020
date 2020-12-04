import re

min_viable_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def is_valid_height(str):
    if 'cm' in str:
        height = int(str.strip('cm'))
        return height >= 150 and height <= 193
    if 'in' in str:
        height = int(str.strip('in'))
        return height >= 59 and height <= 76

passport_policies = {
    'byr': lambda year: int(year) >= 1920 and int(year) <= 2002,
    'iyr': lambda year: int(year) >= 2010 and int(year) <= 2020,
    'eyr': lambda year: int(year) >= 2020 and int(year) <= 2030,
    'hgt': lambda height: is_valid_height(height),
    'hcl': lambda hair: True if re.match(r'#[0-9a-z]{6}\b', hair) else False,
    'ecl': lambda eye: True if re.match(r'(\bamb\b|\bblu\b|\bbrn\b|\bgry\b|\bgrn\b|\bhzl\b|\both\b)', eye) else False,
    'pid': lambda id: True if re.match(r'\b[0-9]{9}\b', id) else False,
    'cid': lambda id: True
}

passports = []
with open ('./day4input.txt') as f:
    data = f.read();
    passport_entries = data.split('\n\n')
    for entry in passport_entries:
        single_line = re.sub('\n', ' ', entry)
        passports.append(single_line)

def part1():
    valid_passport_count = 0
    super_valid_passport_count = 0
    for passport in passports:
        print("passport: {}".format(passport))
        is_valid = True
        for field in min_viable_fields:
            if field not in passport:
                is_valid = False
        if is_valid:
            valid_passport_count += 1
            super_valid_passport_count += part2(passport)
    return valid_passport_count, super_valid_passport_count

def part2(passport):
    passport_props = passport.split(' ')
    is_super_valid = True
    for prop in passport_props:
        key, value = prop.split(':')
        is_super_valid = passport_policies[key](value)
        if not is_super_valid:
            return 0
    return 1


print part1()
