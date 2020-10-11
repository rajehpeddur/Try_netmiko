from netmiko import ConnectHandler

iosv_l2_s1 = {
     'device_type': 'cisco_iso_telnet',
    'ip': '10.76.76.139',
    'port': '2018',
}

iosv_l2_s2= {
     'device_type': 'cisco_ios_telnet',
    'ip': '10.76.76.139',
    'port': '2045',
}

#def cisco_prompt_reset(connection):
   # if connection.check_enable_mode():
   #     connection.exit_enable_mode()
 #   if connection.check_config_mode():
 #       connection.exit_config_mode()

#iosv_l2_s3 = {
 #   'device_type': 'cisco_ios_telnet',
  #  'ip': '10.76.76.139',
   # 'port': '2018',
#}

with open('vlan_multiple') as f:
    lines = f.read().splitlines()
print (lines)

all_devices = [iosv_l2_s1, iosv_l2_s2]  #iosv_l2_s3]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    prompt = net_connect.find_prompt()
    print(prompt)
   # cisco_prompt_reset(net_connect)
    output = net_connect.send_config_set(lines)
    print (output)