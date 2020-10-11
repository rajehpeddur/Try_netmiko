from netmiko import ConnectHandler

cisco_3750 = {
    'device_type': 'cisco_ios_telnet',
    'ip': '10.76.76.139', #01A6096#
    'port': '2018',
   # 'username': 'admin',
    #'password': 'cisco!123',

}


def cisco_prompt_reset(connection):
#    if connection.check_enable_mode():
#        connection.config_mode()
   if connection.check_config_mode():
       connection.exit_config_mode()


net_connect=ConnectHandler(**cisco_3750)
#prompt=net_connect.find_prompt()
#print(prompt)
cisco_prompt_reset(net_connect)
#prompt=net_connect.find_prompt()
#print(prompt)

op = net_connect.send_command("show ip int bri | in up")
print(op)


#net_connect.enable()
#net_connect.config_mode()
#net_connect.send_config_set([' int GigabitEthernet1/0/1', 'shut'])
#net_connect.exit_config_mode()
#net_connect.exit_enable_mode()

