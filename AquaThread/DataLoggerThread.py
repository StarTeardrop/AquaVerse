from AquaThread.BaseCallbackThread import *
from PacketParse import parse_imu_packet, parse_dvl_packet, parse_position_packet

class DataLoggerThread(BaseCallbackWorker):
    def __init__(self, tag="IMU"):
        super().__init__(name=tag)
        self.tag = tag

    def run(self):
        while self._running:
            with self._lock:
                data = self._data
            if data is not None:
                if self.tag == "IMU":
                    # Parse IMU packet
                    imu_data = parse_imu_packet(data)
                    print(f"[{self.tag}] Accel: {imu_data['Acceleration']}, Gyro: {imu_data['AngularVelocity']}, Orientation: {imu_data['Orientation']}")

                elif self.tag == "DVL":
                    # Parse DVL packet
                    dvl_data = parse_dvl_packet(data)
                    print(f"[{self.tag}] Velocity: {dvl_data['Velocity']}")

                elif self.tag == "POSITION":
                    # Parse Position packet
                    position_data = parse_position_packet(data)
                    print(f"[{self.tag}] Position: {position_data['Position']}, Euler: {position_data['OrientationEuler']}")

            time.sleep(0.01)
