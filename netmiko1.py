from netmiko import ConnectHandler

iosv_l2_s1 = {
    'device_type': 'cisco_ios_telnet',
    'ip': '10.76.76.139',
    'port': '2018',
   # 'username': 'admin',
   # 'password': 'cisco',
}
def cisco_prompt_reset(connection):
   # if connection.check_enable_mode():
   #     connection.exit_enable_mode()
    if connection.check_config_mode():
        connection.exit_config_mode()

net_connect = ConnectHandler(**iosv_l2_s1)
prompt=net_connect.find_prompt()
print(prompt)
cisco_prompt_reset(net_connect)

output = net_connect.send_command('show ip int brief | in up')
print(output)