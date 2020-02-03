import paho.mqtt.client as mqtt


class MQTT(mqtt.Client):

    def __init__(self, host='localhost', port=1883, username=None, passwd=None, *args, **kw):
        super().__init__(*args, **kw)

        self.host = host
        self.port = port
        self.username = username
        self.passwd = passwd
        self.username_pw_set(self.username, password=self.passwd)
        self.on_message = self.on_message_new
    
    def connect_broker(self):
        if self.is_connected() == False:
            self.connect(self.host, port=self.port)

    def on_message_new(self, client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))
        return True
