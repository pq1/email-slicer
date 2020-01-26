# Read items from a list. Accounting for all data types if possible
def append_lists(email): 
    if '@' in email:
        email_slicer = email.split('@')
        user_name.append(email_slicer[0])
        domain_name.append(email_slicer[1])
    return user_name, domain_name

if __name__ == '__main__':
    # Delcare variables
    email_list = ['goku@dbz.com', 2, 3.14, 'vegeta@super.com', 'pq1', True]
    user_name = []
    domain_name = [] 
    
    # Loop through the list and apply function
    for email in email_list:
        try:
            append_lists(email)
        except TypeError:
            continue
    print(f'Usernames: {user_name} \nDomains: {domain_name}')