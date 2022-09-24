# tcp full scan (connect scan) module 

import optparse 
from socket import *
import sys

def gen_portlist(option, opt, value, parser):
    setattr(parser.values, option.dest, value.split(','))

def scan_port(target, port):
# core function to scan port 
    data = 'g-banner - version 0.1.0\r\n\r\n'.encode('utf-8')
    try:
        setdefaulttimeout(3)
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((target, port))
        print("[INFO] {ip}'s TCP port {port} is open !".format(ip=target, port=port))
    
    except Exception:
        print("[INfO] {target}'s TCP port {port} is closed|filtered !".format(target=target, port=port))
        return
        
    try:
        sock.send(data)
        banner = sock.recv(1024)
        sock.close()
        print("[INFO] Banner on port {port}({ip}):\n\n{banner}".format(ip=target, port=port, banner=banner.decode('utf-8')))
    
    except Exception:
        print("[INFO] {target}'s TCP port {port} seems to be open|filtered !".format(target=target, port=port))

def scanner(host, port_list):
    # handle to scan_host and converting host name 
    try:
        target_ip = gethostbyname(host)
        print("[INFO] Resolved {domain} into {ip}".format(domain=host, ip=target_ip))
    except Exception:
        print("[ALRT] Problem occured for resolving {domain} !".format(domain=host))
        print("[ALRT] Aborting....")
        return 
    try:
        target_name = gethostbyaddr(host)
        print("[INFO] Reversed {ip} into {domain}".format(ip=target_ip, domain=target_name[0]))
        print("[INFO] Starting TCP scan for {domain}......\n".format(domain=target_name[0]))
    except Exception:
        print("[INFO] Starting TCP scan for {ip}......\n".format(ip=target_ip))
        
    for port in port_list:
        scan_port(target_ip, int(port))

def main():
    print("######################################################")
    print("##  G-Banner : Banner grabbing tool  Version 0.1.0  ##")
    print("##                                   By: Falsedeer  ##")
    print("######################################################\n")
    parser = optparse.OptionParser("%prog -t <target host> -p <target port>")
    parser.add_option("-t", "--target", type="string", dest="host", help="The specified host to perform the scan")
    parser.add_option("-p", "--port", type="string", dest="ports", action="callback", callback=gen_portlist, help="Specify the target ports seperated in comma(without space)")
    (options, args) = parser.parse_args()
    
    if options.host is None:
        print(parser.get_usage())
        sys.exit(0)
        
    elif options.ports is None:
        print(parser.get_usage())
        sys.exit(0)
        
    else:
        pass
        
    scanner(options.host, options.ports)

if __name__ == "__main__":
    main()
