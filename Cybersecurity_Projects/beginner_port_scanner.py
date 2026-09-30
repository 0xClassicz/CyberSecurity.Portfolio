import nmap

nm = nmap.PortScanner()

# This asks the user to input the target's ip address to scan (Example: 45.33.32.156)
target = input("Enter the target's IP address: ")
options = input(int(
    "What type of scan do you want?\n1. -sS (TCP SYN scan)\n2. -sT (TCP connect scan)\n3. -sU (UDP scan)\n\nEnter option # here: "))
while True:
    if options == 1:
        options = "-sS"
    elif options == 2:
        options = "-sT"
    elif options == 3:
        options = "-sU"
    else:
        print("please enter a valid option #")
        break


nm.scan(target, arguments=options)

for host in nm.all_hosts():
    print("Host: %s (%s)" % (host, nm[host].hostname()))
    print("State: %s" % nm[host].state())
    for protocol in nm[host].all_protocols():
        print("Protocol: %s" % protocol)
        port_info = nm[host][protocol]
        for port, state in port_info.items():
            print("Port: %s\tState: %s" % (port, state))


# https://www.youtube.com/watch?v=fhn9-PQBN7g
