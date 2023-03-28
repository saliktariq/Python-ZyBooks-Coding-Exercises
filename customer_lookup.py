# A customer database file named CustomerDb.txt contains a list of customers (one per line), each customer consisting of a unique customer id followed by a first and last name. Given an id, output the customer's first and last name. If the id is not found, output "Not found". If the input id is 27, the output might be "Sarah Lee" (if found).
#
# FYI, the customer database's contents happen to be: 42 Mike Jones 16 Al Garcia 27 Sarah Lee 12 Stan Lee 99 Amy Hernandez

idToFind = input()  # Using input() instead of cin

dbId = ""
dbFirstName = ""
dbLastName = ""
try:
    with open("CustomerDb.txt") as customerDb:
        # When reaching end of file, customerDb.readline() will return an empty string
        while True:
            line = customerDb.readline().strip()
            if not line:
                break
            dbId, dbFirstName, dbLastName = line.split()
            if dbId == idToFind:
                print(dbFirstName, dbLastName)
                break
        else:
            print("Not found")
except FileNotFoundError:
    print("Could not open CustomerDb.txt")
