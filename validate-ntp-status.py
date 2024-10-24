
import os, time;

def main():
    ntp_status = os.popen("clish -c 'show ntp current'").read();
    
    if "not synchronized" in ntp_status:
        os.popen("service ntpd stop");
        time.sleep(1);
        os.popen("service ntpd start");
        print(f"[-] NTP servers are not in sync. NTP service has been restarted.");
        time.sleep(2);
        
    else:
        print(f"[+] NTP servers are in sync.");
        
    ntp_status = os.popen("ntpq -np").read();
    print(f"\nNTP Status:\n\n{ntp_status}");

if "__main__" in __name__:
    main();
    