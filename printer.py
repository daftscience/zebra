import socket
import yaml

config_file = "config.yaml"
config = {"ip": "10.20.12.99","port": 9100,"buffer_size": 1024}
try:
    with open(config_file) as file:
        config = yaml.load(file)
except:
    with open(config_file, 'w') as file:
        file.write(yaml.dump(config))

print(config)

class Printer:
    TCP_IP = config['ip']
    TCP_PORT = config['port']
    BUFFER_SIZE = config['buffer_size']

    def __init__(self, zpl):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.TCP_IP, self.TCP_PORT))
        s.send(bytes(zpl, "utf-8"))
        # s.send(zpl)
        s.close()
