from datetime import datetime as dt 
import time
today = dt.now()
hosts_path_linux= "/etc/hosts"
hosts = 'hosts'
redirect = '127.0.0.1'
website_list = ['www.facebook.com']
#if (today > dt(dt.now().year,dt.now().month,dt.now().day)):
#print('hello')
while True:
    if (dt(dt.now().year,dt.now().month,dt.now().day,15))<today<(dt(dt.now().year,dt.now().month,dt.now().day,17,48)):

        print('working hous',dt.now())
        with open (hosts_path_linux,'r+') as file:
            content = file.read()
            for website in website_list:
                if(website in content):
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
#print(dt(dt.now().year,dt.now().month,dt.now().day,dt.now().hour))
    else:
        
       
        with open (hosts_path_linux,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print('not working hours',dt.now())
        
    time.sleep(1)