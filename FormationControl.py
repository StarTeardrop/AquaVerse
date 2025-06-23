from AquaUDPReceiver import AquaReceiverStart
from AquaUDPTransporter import *
import time
import threading
import csv
import os
from PacketParse import parse_position_packet


def handle_position(msg):
    pass


if __name__ == '__main__':
    on_topic_callbacks = {
        '/BlueRov2/0/Position': handle_position,
    }

    receiver_thread = threading.Thread(target=AquaReceiverStart, args=(on_topic_callbacks,))
    receiver_thread.start()

    while True:
        robots = [
            SendMessage(10, 10, 10, 10, 0, 0, 0, 0, enum_robots['BlueRov2'], 0),
            SendMessage(10, 10, 10, 10, 0, 0, 0, 0, enum_robots['BlueRov2'], 1),
            SendMessage(10, 10, 10, 10, 0, 0, 0, 0, enum_robots['BlueRov2'], 2),
            SendMessage(10, 10, 10, 10, 0, 0, 0, 0, enum_robots['BlueRov2'], 3),
            SendMessage(10, 10, 10, 10, 0, 0, 0, 0, enum_robots['BlueRov2'], 4),
            SendMessage(10, 10, 10, 10, 0, 0, 0, 0, enum_robots['BlueRov2'], 5),
            SendMessage(10, 10, 10, 10, 0, 0, 0, 0, enum_robots['BlueRov2'], 6),

        ]
        control_multi_agents(robots)
        time.sleep(0.001)
