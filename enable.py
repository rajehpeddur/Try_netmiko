from netmiko import ConnectHandler
import re

cisco_3750 = {
    'device_type': 'cisco_ios_telnet',
    'ip': '10.76.76.139',  # 01A6096#
    'port': '2018',
    # 'username': 'admin',
    # 'password': 'cisco!123',

}


def check_enable_mode(self, check_string="#"):
    """Check if in enable mode. Return boolean.

    :param check_string: Identification of privilege mode from device
    :type check_string: str
    """
    self.write_channel(self.RETURN)
    output = self.read_until_prompt()
    return check_string in output


net_connect = ConnectHandler(**cisco_3750)
# prompt = net_connect.find_prompt()
# print(prompt)
check_enable_mode(net_connect)

op = net_connect.send_command("show ip int bri | in up")
print(op)
