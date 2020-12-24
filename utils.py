import requests
import re
import json
def crawl_userpages_with_keys():

    print("Crawling github to find users facing the issue.....")
    i = '1'
    #url = 'https://github.com/search?p=2&q=.key+in%3Apath&type=Code&utf8=%E2%9C%93'
    #header = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Encoding":"gzip, deflate, br","Accept-Language":"en-US,en;q=0.5","Cache-Control":"max-age=0","Connection":"keep-alive","Cookie":"logged_in=yes; _gh_sess=T251b2JtcHFjcnhDYnMzbE1FS2dwK0JUclFRaEJPcjlFbmNkWk4vSXFNOXFWYkkzRFNZZmIrOFVzNDJ2alhSRVRBd0Y3TXFYejdXOS9mYXdnNWdyMWlrVmFwdGN2aHpjTUlUQnB5ZmNPTCtrZ0tXcHZwTWw2N3RNTUdQUFRQa3YrOTFJdGlaUFVWWGlhK1dueTRlWEFQRCtoYkhVVVpodmxUOHczRjA0RXJVTVA0M2E2MDM5Z0hVRzVNeDNYM1k5LS1tZ2grN2plRURtQUxlZEJGRkM0Szd3PT0%3D--0e8b5e14530ecbc7dca5faa08c768518e4b4c226; _ga=GA1.2.314509565.1524473613; _gat=1; _octo=GH1.1.29416258.1524473613; tz=Asia%2FKolkata; user_session=GSHgc_Tpf7riNXy2LDrjvcFIU1jLbHlYYfrHxWinTv7JiGYL; __Host-user_session_same_site=GSHgc_Tpf7riNXy2LDrjvcFIU1jLbHlYYfrHxWinTv7JiGYL;dotcom_user=hello12321","Host":"github.com","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0"}
    header = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Encoding":"gzip, deflate, br",
"Accept-Language":"en-US,en;q=0.5",
"Cache-Control":"max-age=0",
"Connection":"keep-alive",
"Cookie":"logged_in=yes; _ga=GA1.2.314509565.1524473613; _octo=GH1.1.29416258.1524473613; user_session=iMeJg5oriIkvi0lLAoYjAIJpMlap59nTfsNo0V5ZHZuTR8Jg; __Host-user_session_same_site=iMeJg5oriIkvi0lLAoYjAIJpMlap59nTfsNo0V5ZHZuTR8Jg; dotcom_user=s-o-s-c; _gh_sess=cVFsM2NlZmplMGlkWGdmd0ZTdGNBNDRKTGxVaWVvRmFnVktGaXVaTkJwRFNSc0hOMFJLU2NEdEMyUkJZTVNHdDRubkhGd1MxZkh6c2dSNjNHL2JEc0ZRR0pOR3F0WjI1VVRscXZYRGlTTVFYYWJ4ODJJZnkybDNRL3dCK05DMW1kanJvaGNDTzY5RzFZNzJwM1dDUFVucTI4QzEzamEyTytyWTAzZmhYSHNFSmtvRXJQS3J2TnF4MEI2VHBuMktVNnpRK25na3FiV01ySkNuSTFtZ3kxRVN3UW9UOVlnWFM0VUJCeStUV1NHTmNMcFVKazJMWU41bm9GRzRDMjZaaEhOdkdoNC90RVJwTnZSZkZIS3JtVHc9PS0ta1BXMFcvVUp0RGd1VHgrbG1iV3dhQT09--a9c7afbe84af5c075fe88144167e786076e6700d; _gat=1; tz=Asia%2FKolkata",
"Host":"github.com",
"Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0" }
    fh = open("r.txt","a+")
    inp = int(input("Enter the limit : (number of search pages to crawl):"))
    ch='1'
    for i in range(inp):
        if i == 0:
            continue
        # x = chr(ord(ch)+i)
        # url = 'https://github.com/search?p=%d&q=.key+in%3Apath&type=Code&utf8=%E2%9C%93'
        else:
            url = 'https://github.com/search?p=%d'%(i)+'&q=.key+in%3Apath&type=Code&utf8=%E2%9C%93'
            print('Crawling : ' + url)
            r = requests.get(url, headers=header)
        
            fh.write('*****************************************')
            fh.write(str(r.headers))
            fh.write('*****************************************')
            fh.write(str(r.content))
            fh.write('*****************************************')
            print('Crawled page : %d' %(i))
        
    fh.close()
    print('First part of crawling successfully completed')

def extract_username_from_scrapeData():
    print('Extracting usernames from the crawled data')
    fhand = open('r.txt')
    lst = []
    pattern = '<a class="text-bold" href="/[^/]+'
    for line in fhand:
        line = line.rstrip()
        lst = re.findall(pattern, line)
    
    fhand.close()
    fhand = open('temp.txt', 'w')
    
    for i in range(len(list(lst))):
        fhand.write(lst[i] + '\n')
    
    fhand.close()

    fhand = open('temp.txt')
    fhand1 = open('username_list.txt', 'w')

    for line in fhand:
        line = line.rstrip()
        fhand1.write(line[28:])
        fhand1.write('\n')

    fhand.close()
    fhand1.close()
    print('Usernames extracted.')

def eliminate_duplicates():
    lines_seen = set() # holds lines already seen
    outfile = open("username_distinct.txt", "w")
    for line in open("username_list.txt", "r"):
        if line not in lines_seen: # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()
    print('Duplicates eliminated')


def crawl_user_emailAddress():
    print("Crawling api.github.com to get the email id's of users facing the issue")
    fsave = open('user_email.txt', 'w')
    fhandle = open('username_distinct.txt')
    fhand = open('temp.txt')
    fhand1 = open('username_list.txt', 'w')
    
    lst = []

    for line in fhandle:
        line = line.rstrip()
        #fhand1.write(line[28:])
        lst.append(line)

    fhandle.close()
    fhand.close()
    fhand1.close()

    flag = int(1)
    p=0
    for i in lst:
        url = 'https://api.github.com/users/'+i+'/events/public'
        header = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Encoding":"gzip, deflate, br","Accept-Language":"en-US,en;q=0.5","Cache-Control":"max-age=0","Connection":"keep-alive","Cookie":"logged_in=yes; _gh_sess=T251b2JtcHFjcnhDYnMzbE1FS2dwK0JUclFRaEJPcjlFbmNkWk4vSXFNOXFWYkkzRFNZZmIrOFVzNDJ2alhSRVRBd0Y3TXFYejdXOS9mYXdnNWdyMWlrVmFwdGN2aHpjTUlUQnB5ZmNPTCtrZ0tXcHZwTWw2N3RNTUdQUFRQa3YrOTFJdGlaUFVWWGlhK1dueTRlWEFQRCtoYkhVVVpodmxUOHczRjA0RXJVTVA0M2E2MDM5Z0hVRzVNeDNYM1k5LS1tZ2grN2plRURtQUxlZEJGRkM0Szd3PT0%3D--0e8b5e14530ecbc7dca5faa08c768518e4b4c226; _ga=GA1.2.314509565.1524473613; _gat=1; _octo=GH1.1.29416258.1524473613; tz=Asia%2FKolkata; user_session=GSHgc_Tpf7riNXy2LDrjvcFIU1jLbHlYYfrHxWinTv7JiGYL; __Host-user_session_same_site=GSHgc_Tpf7riNXy2LDrjvcFIU1jLbHlYYfrHxWinTv7JiGYL;dotcom_user=hello12321","Host":"github.com","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0"}
        #print('crawling ' + i + '\n')
        print(str(p) + " Crawling " + url)
        p+=1
        data = requests.get(url)
        #print("Crawled " + url)
        r = data.json()
        with open('r.json', 'w') as f:
            json.dump(r, f)

        
       
        x = []
        fh = open("r.json")
        for line in fh:
            line = line.rstrip()
            x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z0-9]', line)
            #print(x)
            if(len(x) > 0):
                fsave.write(x[0] + '\n')

    print("Successfully extracted email ids ")
    fsave.close()


