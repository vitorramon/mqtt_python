import paho.mqtt.client as mqtt

class MqttClientConnection:
    def __init__(self, broker_ip: str, broker_port: int, client_name: str, keepalive=60):
        self.__broker_ip = broker_ip
        self.__broker_port = broker_port
        self.__client_name = client_name
        self.__keepalive = keepalive

    def start_connection(self):
        mqtt_client = mqtt.Client(client_id=self.__client_name)
        mqtt_client.connect(host=self.__broker_ip, port=self.__broker_port, keepalive=self.__keepalive)
        mqtt_client.loop_start()
        return mqtt_client

