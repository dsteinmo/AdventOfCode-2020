#!/usr/bin/python3

class Passport: 
    # Props:
    # byr (Birth Year)
    # iyr (Issue Year)
    # eyr (Expiration Year)
    # hgt (Height)
    # hcl (Hair Color)
    # ecl (Eye Color)
    # pid (Passport ID)
    # cid (Country ID, optional)
    def __init__(self, byr, iyr, eyr, hgt, hcl, ecl, pid, cid):
        self.byr = byr
        self.iyr = iyr
        self.eyr = eyr
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid
        self.cid = cid

    def print(self):
        print(f"byr: {self.byr}, iyr: {self.iyr}, eyr: {self.eyr}, \
            hgt: {self.hgt}, hcl: {self.hcl}, ecl: {self.ecl}, pid: {self.pid}, cid: {self.cid}")

    def is_valid(self, version=1) -> bool:
        if version < 2:
            # version 1 rules:
            return (self.byr is not None and 
                self.iyr is not None and
                self.eyr is not None and
                self.hgt is not None and
                self.hcl is not None and
                self.ecl is not None and
                self.pid is not None)

        return (self.byr_is_valid() and
            self.iyr_is_valid() and
            self.eyr_is_valid() and
            self.hgt_is_valid() and
            self.hcl_is_valid() and
            self.ecl_is_valid() and
            self.pid_is_valid()) # cid ignored.

    # version 2 rules:
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    # cid (Country ID) - ignored, missing or not.

    def byr_is_valid(self):
        if self.byr is None:
            return False
        byr_num = int(self.byr)
        if (byr_num >= 1920 and byr_num <= 2002):
            return True
        print("bad byr")
        return False

    def iyr_is_valid(self):
        if self.iyr is None:
            return False
        iyr_num = int(self.iyr)
        if (iyr_num >= 2010 and iyr_num <= 2020):
            return True
        print("bad iyr")
        return False

    def eyr_is_valid(self):
        if self.eyr is None:
            return False
        eyr_num = int(self.eyr)
        if (eyr_num >= 2020 and eyr_num <= 2030):
            return True
        print("bad eyr")
        return False

    def hgt_is_valid(self):
        if self.hgt is None:
            return False
        if len(self.hgt) < 3:
            return False
        meas = self.hgt[-2:]
        if meas != "in" and meas != "cm":
            print("height bad units")
            return False
        
        hgt_num = int(self.hgt[:-2])
        if meas == "in":
            if hgt_num >= 59 and hgt_num <= 76:
                return True
            else:
                print("bad inches height")
                return False
        # must be "cm":
        if hgt_num >= 150 and hgt_num <= 193:
            return True
        print("bad cm height")
        return False

    def hcl_is_valid(self):
        if self.hcl is None:
            return False
        if self.hcl[0] != "#":
            return False

        color = self.hcl[1:]
        if (len(color) != 6):
            return False
        valid_chars = set(['a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3',
            '4', '5', '6', '7', '8', '9'])

        for char in color:
            if char not in valid_chars:
                print("bad color string")
                return False

        return True

    def ecl_is_valid(self):
        if self.ecl is None:
            return False
        valid_ecls = set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
        if self.ecl not in valid_ecls:
            print("invalid ecl")
            return False
        return True

    def pid_is_valid(self):
        if self.pid is None:
            return False
        if len(self.pid) != 9:
            return False
        valid_chars = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
        for char in self.pid:
            if char not in valid_chars:
                return False
        return True


passports = []

with open("day4_input.txt", mode="r") as f:
    eof_reached = False
    eor_reached = False

    passport_fields = {
        "byr": None, "iyr": None, "eyr": None, "hgt": None,
        "hcl": None, "ecl": None, "pid": None, "cid": None
    }

    while(eof_reached == False):
        line = f.readline().strip()
        if len(line) == 0 and eor_reached == True:
            eof_reached = True
        elif len(line) == 0:
            # Blank line -- end of record, so add to list of passports.
            passports.append(Passport(passport_fields["byr"], passport_fields["iyr"], passport_fields["eyr"],
                 passport_fields["hgt"], passport_fields["hcl"], passport_fields["ecl"],
                 passport_fields["pid"], passport_fields["cid"]))

            # Reset fields for next record.
            passport_fields = {
                "byr": None, "iyr": None, "eyr": None, "hgt": None,
                "hcl": None, "ecl": None, "pid": None, "cid": None
            }
            eor_reached = True
        else:
            # Data line -- parse what we can, and wait until end-of-record (empty line).
            eor_reached = False
            fields = line.split(" ")
            for field in fields:
                kv_pair = field.split(":")
                key = kv_pair[0]
                val = kv_pair[1]
                passport_fields[key] = val

if __name__ == "__main__":
    print("Day 4")
    print("=====")

    num_valid = 0
    for passport in passports:
        if passport.is_valid():
            num_valid += 1
    
    print(f"Part 1: Number of valid passports: {num_valid}")

    num_valid = 0
    for passport in passports:
        passport.print()
        if passport.is_valid(version=2):
            num_valid += 1
            print("passport is valid")
        else:
            print("not valid")

    print(f"Part 2: Number of valid passports: {num_valid}")
