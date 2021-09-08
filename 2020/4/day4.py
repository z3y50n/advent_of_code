def read_data(filename):
    with open(filename, "r") as f:
        data = []
        passport = []
        for line in f.readlines():
            if line != "\n":
                passport.append(line.replace("\n", ""))
            else:
                data.append(" ".join(passport))
                passport = []
    return data

def valid_passport(data):
    counts = 0
    for passport in data:
        fields = {code[:3]:code[4:] for code in passport.split(" ")}
        if len(fields) == 8 or (len(fields) == 7 and ('cid' not in fields)):
            flag = True
            for field in fields:
                if field == "byr":
                    if int(fields[field]) < 1920 or int(fields[field]) > 2002:
                        flag = False
                        break
                elif field == "iyr":
                    if int(fields[field])<2010 or int(fields[field]) > 2020:
                        flag = False
                        break
                elif field == "eyr":
                    if int(fields[field])<2020 or int(fields[field]) > 2030:
                        flag = False
                        break
                elif field == "hgt":
                    if fields[field][-2:] not in ("in", "cm"):
                        flag = False
                        break
                    elif fields[field][-2:] == "in" and (int(fields[field][:-2]) < 59 or int(fields[field][:-2])>76):
                        flag = False
                        break
                    elif fields[field][-2:] == "cm" and (int(fields[field][:-2]) < 150 or int(fields[field][:-2]) > 193):
                        flag = False
                        break
                elif field == "hcl":
                    if fields[field][0] != "#" or len(fields[field][1:]) != 6:
                        flag = False
                        break
                elif field == "ecl":
                    if fields[field] not in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
                        flag = False
                        break
                elif field == "pid":
                    if len(fields[field]) != 9 or not fields[field].isdecimal():
                        flag = False
                        break
            if flag:
                counts += 1
    return counts


data = read_data("day4.txt")

print(valid_passport(data))

