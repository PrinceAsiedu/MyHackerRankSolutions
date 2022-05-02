#Given  names and phone numbers, assemble a phone book that maps friends' 
#names to their respective phone numbers. You will then be given an unknown 
# number of names to query your phone book for. For each  queried, print the 
# associated entry from your phone book on a new line in the form 
# name = phoneNumber if an entry for is not found, print Not found instead.

if __name__ == "__main__":
    phonebook = {}
    n_entries = int(input().strip())
    for i in range(n_entries):
        name, number = input().rstrip().split()
        phonebook[name] = int(number)
    while True:
        try:
            query_name = input().strip()
            if query_name:
                num = phonebook[query_name]
                print('{}={}'.format(query_name, num))
        except EOFError:
            break
        except KeyError:
            print('Not found')
