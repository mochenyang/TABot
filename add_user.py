# this script adds users to the database. It is not meant to be a part of the app - use it separately
import pymongo

dbclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = dbclient["TABot"]
user_col = mydb["user"]

def add_single_user(record):
    if user_col.find_one({"x500": record['x500']}):
        print("User already exists")
    else:
        _ = user_col.insert_one(record)
        print("User " + record['x500'] + " added")

# process student info files from Canvas, should be tab delimited
# first column should be name (Last, First), second column should be email
def process_file(filename):
    records = []
    f = open(filename, "r")
    for line in f:
        record = {}
        name, email = line.rstrip('\n').split('\t')
        name = name.strip('"')
        record['last_name'], record['first_name'] = name.split(', ')
        record['email'] = email
        record['x500'] = email.split('@')[0]
        records.append(record)
    f.close()
    return records

if __name__ == "__main__":
    selection = input("Add a single user or process a file? (1-single; 2-file): ")
    match selection:
        case "1":
            record = {}
            record['x500'] = input("Enter x500: ")
            record['first_name'] = input("Enter first name: ")
            record['last_name'] = input("Enter last name: ")
            record['email'] = input("Enter email: ")
            add_single_user(record)
        case "2":
            filename = input("Enter filename: ")
            records = process_file(filename)
            for record in records:
                add_single_user(record)
        case _:
            print("Invalid selection")
            exit(1)