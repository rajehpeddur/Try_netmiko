from netmiko import ConnectHandler

ios_xe_R1 = {
    'device_type': 'cisco_xe',
    'ip': '10.106.71.109',
    'username': 'admin',
    'password': 'cisco!123',
}

ios_xe_R2 = {
    'device_type': 'cisco_xe',
    'ip': '10.106.69.108',
    'username': 'admin',
    'password': 'cisco!123',
}

ios_s1 = {
    'device_type': 'cisco_ios',
    'ip': '10.106.68.109',
    'username': 'admin',
    'password': 'cisco!123',
}

#wlc_w1 = {
 #   'device_type': 'cisco_wlc',
  #  'ip': '10.104.210.140',
   # 'port': '2034',
   # 'username': 'admin',
   # 'password': 'cisco!123',
#}

with open('Iosxe_file') as f:
    lines = f.read().splitlines()
print(lines)

all_devices = [ios_xe_R1, ios_xe_R2]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print(output)

with open('Ios_file') as f:
    lines = f.read().splitlines()
print(lines)

all_devices = [ios_s1]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print(output)

#with open('wlc_file') as f:
#    lines = f.read().splitlines()
#print(lines)

#all_devices = [wlc_w1]

#for devices in all_devices:
 #   net_connect = ConnectHandler(**devices)
  #  output = net_connect.send_config_set(lines)
   # print(output)