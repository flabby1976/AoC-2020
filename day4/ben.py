def get_passport(data):
    return {
        f.split(':')[0]: f.split(':')[1]
        for f in [field for field in data.split()]
    }

with open('input.txt') as f:
    passports = [get_passport(d) for d in f.read().split('\n\n')]

validate_byr = lambda byr: int(byr) in range(1920, 2003)
validate_iyr = lambda iyr: int(iyr) in range(2010, 2021)
validate_eyr = lambda eyr: int(eyr) in range(2020, 2031)
validate_ecl = lambda ecl: ecl in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

def validate_hgt(hgt):
    if hgt.endswith('cm'):
        assert int(hgt[:-2]) in range(150, 194)
        return True
    elif hgt.endswith('in'):
        assert int(hgt[:-2]) in range(59, 77)
        return True
    else:
        return False

def validate_hcl(hcl):
    try:
        assert hcl.startswith('#')
        assert len(hcl) == 7
        try:
            int(hcl[1:], 16)
        except ValueError:
            return False
        return True
    except AssertionError:
        return False
    
def validate_pid(pid):
    try:
        assert len(pid) == 9
        try:
            int(pid, 10)
        except ValueError:
            return False
        return True
    except AssertionError:
        return False

def validate_fields(passport):
    fields = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
    return all(field in passport for field in fields)

def validate_passport(passport):    
    try:
        assert validate_fields(passport)
        assert validate_byr(passport['byr'])
        assert validate_iyr(passport['iyr'])
        assert validate_eyr(passport['eyr'])
        assert validate_hgt(passport['hgt'])
        assert validate_hcl(passport['hcl'])
        assert validate_ecl(passport['ecl'])
        assert validate_pid(passport['pid'])
        return True
    except AssertionError as e:
        if str(e): print(e)
        return False

print(sum(validate_passport(passport) for passport in passports))