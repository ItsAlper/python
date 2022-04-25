import ipaddress
 
network = ipaddress.IPv4Network("192.168.2.0/24")
print("Síť", network.network_address)
print("Broadcast:", network.broadcast_address) 
print("Maska:", network.netmask)
print("Počet hostů:", network.num_addresses)
