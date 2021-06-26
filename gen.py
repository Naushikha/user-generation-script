import csv
import random
import sys
import pickle
import hashlib

# https://stackoverflow.com/questions/2673385/how-to-generate-random-number-with-the-specific-length-in-python

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return random.randint(range_start, range_end)

# Fancy function to generate random people
def genRanList(n):
    rList = []
    for i in range(n):
        first_name = random.choice(list(open('first_names.txt'))).strip()
        last_name = random.choice(list(open('last_names.txt'))).strip()
        full_name = first_name + ' ' + last_name
        # email_domain = random.choice(list(open('email_domains.txt'))).strip()
        # email = (first_name + '.' + last_name + '@' + email_domain).lower()
        # contact_number = "0" + str(random_with_N_digits(9));
        # passwordText = first_name.lower() + last_name.upper() + '@' + '123';
        # salt = str(hashlib.md5(str(random.randint(3, 9000)).encode('utf-8')).hexdigest())
        # password = hashlib.sha256(str(passwordText + salt).encode('utf-8')).hexdigest()
        # https://stackoverflow.com/questions/50711258/how-to-get-a-random-birthday-in-python
        dob = (
            random.choice(["1980", "1981", "1982", "1983", "1984", "1985", "1986", "1987", "1988", "1989", "1990", "1991", "1992", "1993", "1994", "1996", "1997", "1998", "1999", "2000"]) + "-" +
            random.choice(["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]) + "-" + 
            random.choice(["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28"]) 
            )
        
        if (bool(random.getrandbits(1))): gender = "M"
        else: gender = "F"

        address = random.choice(list(open('addresses.txt'))).strip()

        rList.append([str(first_name),
                    str(last_name),
                    str(full_name),
                    str(dob),
                    str(gender),
                    str(address)])
    return rList

def genSQLFromList(iList):
    rList = []
    for item in iList:
        SQL =  (
            "INSERT INTO student(first_name, last_name, full_name, address, dob, gender ) "
            f"VALUES ('{item[0]}','{item[1]}', '{item[2]}','{item[6]}','{item[3]}','{item[4]}')"
            )
        rList.append([SQL])
    return rList

def writeList(pList, filename):
    with open(filename, 'wb') as fp:
        pickle.dump(pList, fp)

def readList(filename):
    with open (filename, 'rb') as fp:
        pList = pickle.load(fp)
    return pList

def writeListAsCSV(pList, filename):
    with open(filename, 'w', newline='') as f:
        wr = csv.writer(f, quoting=csv.QUOTE_ALL)
        for p in pList:
            wr.writerow(p)

def printList(list):
    for x in range(len(list)):
        print(list[x])


testList = genRanList(15)
writeListAsCSV(testList, 'users_details.csv')
testList = genSQLFromList(testList)
writeListAsCSV(testList, 'users_sql.csv')
