import random 
import simpy

class Sensor():
    def __init__(self, env, name, interval):
        self.env = env
        self.name = name
        self.interval = interval
        self.action = env.process(self.run())
        self.data = []

    def run(self):
        while True:
            # wait for next transmission
            yield self.env.timeout(self.interval)
            # generate random data
            data = random.randint(0, 100)
            self.data.append(data)
            print(f'{self.name} sent data: {data}')


class Controller():
    def __init__(self, env, sensors):
        self.env = env
        self.sensors = sensors
        self.action = env.process(self.run())

    def run(self):
        while True:
            # wait for all sensors to send data
            yield self.env.all_of([sensor.action for sensor in self.sensors])
            # process data
            data = [sensor.data for sensor in self.sensors]
            print(f'Controller received data: {data}')


## Sample code to run the simulation
# env = simpy.Environment()
# sensor1 = Sensor(env, 'Sensor1', 5)
# sensor2 = Sensor(env, 'Sensor2', 10)
# controller = Controller(env, [sensor1, sensor2])
# env.run(until=20)

