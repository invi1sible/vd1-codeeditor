import phonenumbers
import validators, sys, time, os, webbrowser
from phonenumbers import geocoder, carrier, timezone, number_type, PhoneNumberType
import nmap, requests, json
import socket

nm = nmap.PortScanner()

map = {
    PhoneNumberType.FIXED_LINE: "FIXED_LINE",
    PhoneNumberType.MOBILE: "MOBILE",
    PhoneNumberType.FIXED_LINE_OR_MOBILE: "FIXED_LINE_OR_MOBILE",
    PhoneNumberType.TOLL_FREE: "TOLL_FREE",
    PhoneNumberType.PREMIUM_RATE: "PREMIUM_RATE",
    PhoneNumberType.SHARED_COST: "SHARED_COST",
    PhoneNumberType.VOIP: "VOIP",
    PhoneNumberType.PERSONAL_NUMBER: "PERSONAL_NUMBER",
    PhoneNumberType.PAGER: "PAGER",
    PhoneNumberType.UAN: "UAN",
    PhoneNumberType.VOICEMAIL: "VOICEMAIL",
    PhoneNumberType.UNKNOWN: "UNKNOWN"
}


class gg:
    def __init__(self):
        os.system('clear')
        while True:
            try:
                print('*Put the IP to check Put it correct like  (  ***.***.1.101   )  or   0  To Exit*')
                self.ipp = input('\033[0moSNeT/ip   :  \033[32m   ')
                if self.ipp == '0':
                    print(' \033[0mexiting..... ')
                    break
                if not (validators.ipv4(self.ipp) or validators.ipv6(self.ipp)):
                    print('\033[0mpput correct ip adress')
                    continue

                print(f'scanning service  \033[91m{self.ipp}\033[0m')
                print('-' * 40)
                iip = f'https://ipinfo.io/{self.ipp}'
                try:
                    self.req = requests.get(iip, timeout=10)
                    dat = self.req.json()
                except Exception:
                    dat = {}

                city = dat.get("city", "N/A")
                country = dat.get("country", "N/A")
                timee = dat.get("timezone", "N/A")
                org = dat.get("org", "N/A")
                loc = dat.get("loc", "N/A")
                region = dat.get("region", "N/A")
                ip = dat.get("ip", self.ipp)

                try:
                    cs = nm.scan(self.ipp, arguments='-F')
                    cs_detail = cs.get('scan', {}).get(self.ipp, {})
                    k = json.dumps(cs_detail, indent=2, ensure_ascii=False)
                    gh = nm[self.ipp].all_protocols() if self.ipp in nm.all_hosts() else []
                    g = json.dumps(gh, indent=2, ensure_ascii=False)
                except Exception:
                    k = '{}'
                    g = '[]'

                h = '-' * 40

                txe = f'''\033[0m
         Location / NeT osint

  target  :   (  \033[91m{ip}\033[0m  )  
 country  :   (  \033[91m{country}\033[0m  ) 
 city  :  (  \033[91m{city}\033[0m  )
 region   :  (  \033[91m{region}\033[0m  )
 location   :   (  \033[91m{loc}\033[0m  )
 google_map  :   ( \033[91mhttps://www.google.com/maps?q={loc}\033[0m  )
 timezone  :  (  \033[91m{timee}\033[0m  )
 company  :  (  \033[91m{org}\033[0m  )

{h} ()
 
'''
                print(txe)
                ext = f'''
                            
    Open ports / service 
    
Protocols  :   

\033[91m{g}\033[0m


ports   :  

\033[91m{k}\033[0m

'''
                print(ext)

            except KeyboardInterrupt:
                break
            except Exception:
                continue


tx = """
 OS\033[32mNeT\033[0m  Nothing does not exist  \033[32m!\033[0m
"""
for char in tx:
    try:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    except KeyboardInterrupt:
        sys.exit()

os.system('clear')


while True:
    try:
        os.system('clear')
        print('''                    ______________
                    |    \033[32m◣   ◢\033[0m   |
                    |____________|

𝟷  :  PHONENUMBER OSINT ?

𝟸  :  IP OSINT  ?

𝟹  : Exit  ? 

''')
        OSNET = input('\033[0moSNeT/home  :\033[32m   ')

        if not OSNET.isdigit():
            print('Enter a valid number!')
            time.sleep(3)
            continue
    except KeyboardInterrupt:
        break

    if OSNET == '1':
        try:
            os.system('clear')
            print(''' *Type phone number like this  (  +1************  ) 
            0  To Exit''')
            while True:
                pho = input('\033[0moSNeT/phone  :\033[32m   ')
                if pho == '0':
                    os.system('clear')
                    break
                try:
                    parsed = phonenumbers.parse(pho, None)
                    if phonenumbers.is_valid_number(parsed):
                        print(''''\n\033[0mChecking...... 
ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ''')
                        time.sleep(1)
                        print(f"country :  \033[91m{geocoder.description_for_number(parsed,'en')}\033[0m ")
                        print(f"Timezone :  \033[91m{timezone.time_zones_for_number(parsed)}\033[0m")
                        print(f"Service :  {carrier.name_for_number(parsed,'en')}\033[0m") 
                        num = number_type(parsed)
                        print(f'\nNumber type  :   \033[91m{map.get(num)}\033[0m')
                    else:
                        print("Invalid phone number")
                except Exception:
                    print("\nError parsing number")
        except KeyboardInterrupt:
            break

    elif OSNET == '2':
        gg()

    elif OSNET == '3':
        sys.exit()
        print('bye')

if __name__ == "__main__":
    pass
