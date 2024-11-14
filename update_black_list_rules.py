
from api.check_point_management_api import check_point_management_api;
import json;
import sys;

def main():
    try:
        with open("data/malicious.json", "r") as file:
            malicious = json.load(file);
    except json.decoder.JSONDecodeError as exception:
        print(f"[-] Exception JSONDecodeError - {exception}");
        sys.exit(1);
        
    with check_point_management_api("100.64.10.254", "admin", "Global") as conn:
        for request_data in malicious.get("host"):
            conn.api("")

if "__main__" in __name__:
    main();