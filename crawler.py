from utils import *

crawl_userpages_with_keys()
extract_username_from_scrapeData()
eliminate_duplicates()
crawl_user_emailAddress()

fh = open('user_email.txt')
print('Emails of users with private keys kept public:')
for line in fh:
    line = line.rstrip()
    print(line)
    