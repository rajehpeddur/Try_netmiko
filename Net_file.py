from netmiko import ConnectHandler

with open('commands_file') as f:
    commands_to_send = f.read().splitlines()

ios_devices = {
    'device_type': 'cisco_ios_telnet',
    'ip': '10.76.76.139',
    'port': '2018',
    # 'username': 'admin',
    # 'password': 'cisco',
}


#def cisco_prompt_reset(connection):
#    if connection.check_enable_mode():
 #       connection.exit_enable_mode()
#    if connection.check_config_mode():
 #       connection.exit_config_mode()


all_devices = [ios_devices]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    prompt = net_connect.find_prompt()
    print(prompt)
 #   cisco_prompt_reset(net_connect)
    output = net_connect.send_config_set(commands_to_send)
    print(output)
# net_connect = ConnectHandler(**ios_devices)
# prompt=net_connect.find_prompt()
# print(prompt)
# cisco_prompt_reset(net_connect)

# all_devices = [ios_devices]

# for devices in all_devices:
#   net_connect = ConnectHandler(**devices)
#  output = net_connect.send_command(commands_to_send)
# print (output)
