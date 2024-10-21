
import sys, os, re;
from glob import glob;
from netmiko import ConnectHandler, file_transfer;
from netmiko.exceptions import NetmikoTimeoutException;

def main():
    
    if not os.path.exists(sys.argv[1]):
        print(f"[-] Path {sys.argv[1]} doesn't exist.");
        sys.exit(1);

    with open("hosts") as file:
        for ip in file:
            device_details = {"device_type": "linux", "ip": ip.strip(), "username": "admin", "use_keys": True, "key_file": "/home/adm1n/.ssh/id_rsa.pub"};
            print(f"\n{ip.strip()}:\n");
            try:
                with ConnectHandler(**device_details) as conn:
                    for local_file_path in glob(f"{sys.argv[1]}/*.py"):
                        file_transfer(conn, source_file=local_file_path, file_system=sys.argv[2], dest_file= re.sub(".*/", "", local_file_path), direction="put", overwrite_file=True);
                        print(f"[+] File transferred - ({local_file_path} > {sys.argv[2]}{re.sub(".*/", "", local_file_path)})");
            except NetmikoTimeoutException:
                print(f"[-] Device \"{ip.strip()}\" is down.");
                
if "__main__" in __name__:
    if len(sys.argv[1:]) != 2:
        print(f"[*] Usage: python3 dispatch-files.py local-path remote-path");
        sys.exit(1);
    else:
        main();
        