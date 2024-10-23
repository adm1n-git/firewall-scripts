
import sys;
from netmiko import ConnectHandler;
from netmiko.exceptions import NetmikoTimeoutException;

def main():

    with open("hosts") as file:
        for ip in file:
            device_details = {"device_type": "linux", "ip": ip.strip(), "username": "admin", "use_keys": True, "key_file": "/home/adm1n/.ssh/id_rsa.pub"};
            print(f"\n{ip.strip()}:\n");
            try:
                with ConnectHandler(**device_details) as conn:
                    print(conn.send_command(sys.argv[1].strip(), read_timeout=20.0));
            except NetmikoTimeoutException:
                print(f"[-] Device \"{ip.strip()}\" is down.");

if "__main__" in __name__:
    if len(sys.argv[1:]) != 1:
        print(f"[*] Usage: python3 exec-command.py command");
        sys.exit(1);
    else:
        main();
        