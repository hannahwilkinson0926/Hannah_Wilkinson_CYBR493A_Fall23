import os

ip = ["127.0.0.1","8.0.0.1","192.168.0.10","192.168.10.10"]

for ips in ip:
    ping_cmd = f"ping -c 1 -w 2 {ip} >> ./pinger 2>&1"
    exit_code = os.system(ping_cmd)
    print(exit_code)