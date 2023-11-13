# working with dictionary 

kronyx = {}

Reddoor = {}
Reddoor['Abayomi'] = 'Team lead'
Reddoor['Vivian'] = 'Networking instructor'
Reddoor['Bolu'] = 'Python instructor'
Reddoor['Modupe'] = 'Cybersecurity instructor'
Reddoor['Abigeal'] = 'Project manager'
Reddoor['Jacob'] = 'Networkiing engineer'

kronyx = {key : value for key, value in Reddoor.items() if key != value}
if Reddoor == kronyx:
    New_entry = kronyx
    
    print(New_entry, 'coming soon...')
else:
    message = "Checkback later "
    print(message)
list_of_courses = []
new_course = 0
while True:
    try:
        
            
        Topics = input("List of course: ")
        list_of_courses.append(Topics.title())
        new_course += 1
        print(list_of_courses)
        
        if len(list_of_courses) < 5:
            continue
            break
        if len(list_of_courses) >  5:
            print('Limit Exceeded')
        
                        
            break
    except:
        print('Error occured')
        
        
ssid  = 'oxide'
passphrase = '5mith'
login = []
authentication = False
user = 'YOUR SSID: '
users = input(user)
if users == ssid:
    log= 'password: '
    logs = input(log)
    if logs == passphrase:
        print('Access allowed')
        login.append(users)
        login.append(logs)
        print('ssid => ',users, 'password => ',logs)
        authentication = True
    else:
        authentication=False
        if users==ssid and passphrase != logs:
            print(logs, 'is an invalid passcode')
            print('Access denied, unable to connect')

payment = 'https://wa.me/c/2349090397455'
def lunchaExchange(Trading, signal):
    if Trading == '100%':
        reply = 'Vibe with lunchaeXchange when it comes to trading'
        print(reply)
        signal = input('Have you paid for the signal?: ')
        if signal == 'About to':
            request = 'pay 20k to get free signal that last a month with 99% signal strength assured'
            print('Use the link =>', payment, 'to make payment for the signal')
            print(request)
        else:
            if signal != 'About to':
                money = 'Daily dollar wallet is 0%'
                print(money)
                print(payment, 'to make payment for the signal')
           
        
lunchaExchange(Trading= '100%', signal= 'About to ')

def exchange():
    return lunchaExchange('100%', 'About to')
if __name__ == '__main__':
    print('Trading with lunchaeXchange signal, 99% profit GUARANTEE... ')
else :
    print('Write another program')
exchange()

