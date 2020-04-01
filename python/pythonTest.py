import netmiko

connection = netmiko.ConnectHandler(ip="192.168.1.25", device_type="cisco_ios",
username="Elias", password="class")

print(connection.send_command("sh ip int brief"))
connection.disconnect()
