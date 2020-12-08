batch_file=[]
with open('input.txt', 'r') as fd:
    for line in fd:
        batch_file.append(line.strip('\n'))

field_list = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

passport = {}
valid = 0
for line in batch_file:
    if line == "":
        # check passport
        print(passport)

        invalid = False
        for field in field_list:
            if field not in passport:
                print("Missing field: {}".format(field))
                invalid = True
                
        if not invalid:

            if int(passport["byr"]) < 1920 or int(passport["byr"]) > 2002:
               print("byr out of range")
               invalid = True           
            if int(passport["iyr"]) < 2010 or int(passport["iyr"]) > 2020:
               print("iyr out of range")
               invalid = True
            if int(passport["eyr"]) < 2020 or int(passport["eyr"]) > 2030:
               print("eyr out of range")
               invalid = True

            hgt_unit = passport["hgt"][-2:]
            if hgt_unit == "cm":
                hgt_value = int(passport["hgt"][:-2])
                if hgt_value < 150 or hgt_value > 193:
                    invalid = True
                    print("hgt out of range: {}".format(hgt_value))
            elif hgt_unit == "in":
                hgt_value = int(passport["hgt"][:-2])
                if hgt_value < 59 or hgt_value > 76:
                    invalid = True
                    print("hgt out of range: {}".format(hgt_value))
            else:
                print("Invalid hgt unit: {}".format(hgt_unit))
                invalid = True
            
            if passport["hcl"][0] == "#":
                hcl_code = passport["hcl"][1:]
                if len(hcl_code) == 6:
                    for ch in hcl_code:
                        if ch not in ('0123456789abcdef'):
                            invalid = True
                            print("Invalid char {} in hcl: {}".format(ch, hcl_code ))
                else:
                    invalid = True
                    print("hcl code > 6 chars: {}".format(hcl_code))
            else:
                invalid = True
                print("Missing leading # in hcl: {}".format(passport["hcl"][0]))

            if passport["ecl"] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                invalid = True
                print("Invalid ecl code: {}".format(passport["ecl"]))

            if len(passport["pid"]) == 9:
                for ch in passport["pid"]:
                    if ch not in ('0123456789'):
                        invalid = True
                        print("Invalid char in pid: {}".format(ch))
            else:
                invalid = True
                print("pid not 9 chars: {}".format(len(passport["pid"])))

        if not invalid:
            print("VALID!")
            valid = valid + 1

        print("\n")
       
        passport = {}

    else:
        fields = line.split(" ")
        for field in fields:
            data = field.split(":")
            passport[data[0]]=data[1]

print("Valid passports: {}".format(valid))
