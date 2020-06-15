from bs4 import BeautifulSoup
import urllib.request
import csv
import sys

def parse(CVE):
    page = "https://www.cvedetails.com/cve-details.php?t=1&cve_id={}".format(CVE)
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers={'User-Agent':user_agent,}
    request=urllib.request.Request(page,None,headers)
    response = urllib.request.urlopen(request)
    data = response.read()
    soup = BeautifulSoup(data,"html.parser")
    need_to_find = ['CVSS Score','Confidentiality Impact','Integrity Impact','Availability Impact','Access Complexity',
                'Authentication','Gained Access','Vulnerability Type(s)','CWE ID',]
    # Parsing CVSS Scores & Vulnerability Types 
    CVE_info_list = []
    for i in need_to_find:
        match = soup.find(string = "{}".format(i)).find_next().text.split("(")[0].replace("\n","")
        element = [i, match]
        CVE_info_list.append(element)
    with open('CVE.csv', 'a', newline="") as f:
        writer = csv.writer(f)
        writer.writerows(CVE_info_list)
    with open('CVE.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([CVE,""])
    # Parsing Products Affected sheet
    table = soup.find("table", id = 'vulnprodstable')
    rows = table.find_all('tr')
    data_values = [['#','Product Type','Vendor','Product','Version','Update','Edition','Language','']]
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data_values.append([ele for ele in cols])
    data_values.pop(1)
    with open('CVE.csv', 'a', newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data_values)

# Running
CVE = sys.argv[1]
with open('CVE.csv','r') as f:
    content = f.readlines()
    if str(CVE)+",\n" in content:
        print("Already in file")                  
    else:
        parse(CVE)
    
        


