from utils import *

crawl_userpages_with_keys()
extract_username_from_scrapeData()

fh = open('user_email_data.txt')
print('Emails of users with private keys kept public:')
for line in fh:
    line = line.rstrip()
    print(line)
    print("done")
    print("Reporatqe")
