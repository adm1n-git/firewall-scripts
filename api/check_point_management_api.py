
from getpass import getpass;
import requests;
import urllib3;
import json;
import sys;

urllib3.disable_warnings();

class check_point_management_api:
    def __init__(self, management_server_ip, smart_console_user, domain="System Data"):
        self.management_server_ip = management_server_ip;
        self.smart_console_user = smart_console_user;
        self.__smart_console_password = getpass("Password: ");
        self.domain = domain;
        
    def __enter__(self):
        request_data = {"user": self.smart_console_user, "password": self.__smart_console_password, "domain": self.domain};
        self.__api_session_token = self.api("login", request_data).get("sid");
        print(f"[+] The session token has been retrieved from the Check Point management server IP {self.management_server_ip}.");
        return self;
        
    def api(self, path, request_data):
        url = f"https://{self.management_server_ip}/web_api/{path}";
        if "login" in path:
            request_header = {"Content-Type": "application/json"};
        else:
            request_header = {"Content-Type": "application/json", 'X-chkp-sid': self.__api_session_token};
        try:
            response = requests.post(url, verify=False, data=json.dumps(request_data), headers=request_header);
            if response.status_code != 200:
                print(f"[-] {response.json().get('message')}");
                sys.exit(1);
        except requests.exceptions.ConnectionError:
            print(f"[-] Unable to connect to the Check Point management server IP {self.management_server_ip}.");
            sys.exit(1);
        return response.json();
        
    def __exit__(self, exception_type, exception_value, exception_traceback):
        request_data = {};
        self.api("logout", request_data);
        print(f"[+] The session has been successfully logged out.");
        