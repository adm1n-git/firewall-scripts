
import os, re;

def main():

    interfaces = os.popen(f"clish -c 'show interfaces'").read().split()[:-1];

    for interface in interfaces:
        return_string = os.popen(f"clish -c 'show interface {interface}'").read();
        print(f"\n{interface}:\n");
        for line in return_string.split("\n"):

            if re.search(r"state (on|off)", line):
                interface_administrative_state = re.search(r"state (on|off)", line).group(1);
                if "on" in interface_administrative_state:
                    continue;
                else:
                    print(f"[-] The interface {interface} is administratively down.");

            if re.search(r"link-state link (up|down)", line):
                interface_state = re.search(r"link-state link (up|down)", line).group(1);
                if "on" in interface_administrative_state:
                    continue;
                else:
                    print(f"[-] The interface {interface} is down.");

            if re.search(r"mtu (\d+)", line):
                interface_mtu = int(re.search(r"mtu (\d+)", line).group(1));
                if interface_mtu != 1300:
                    print(f"[-] The interface {interface} is configured with a higher MTU (>1300).");
                else:
                    continue;

            if re.search(r"auto-negotiation (on|off)", line):
                interface_state = re.search(r"auto-negotiation (on|off)", line).group(1);
                if "on" in interface_administrative_state:
                    continue;
                else:
                    print(f"[-] The interface {interface} is configured with auto-negotiation turned-off.");

if "__main__" in __name__:
    main();
    