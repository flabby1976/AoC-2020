batch_file=[]
with open('input.txt', 'r') as fd:
    for line in fd:
        batch_file.append(line.strip('\n'))

field_list = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

passport = {}
valid = 0
invalid = False
for line in batch_file:
    if line == "":
        # check passport
        print(passport)
        for field in field_list:
            if field not in passport:
                invalid = True
                break
        if not invalid:
            valid = valid + 1
        passport = {}
        invalid = False
    else:
        fields = line.split(" ")
        for field in fields:
            data = field.split(":")
            passport[data[0]]=data[1]

print("Valid passports: {}".format(valid))
