# look ahead

#input:
# start_pu_inventory
# input_comp_fr
# input_comp_lwr
# input_mass_fr
# input_mass_lwr
# cycle_time_lwr
# cycle_time_fr
# batch_size_lwr
# batch_size_lwr

import numpy as np
timestep = 100

class reactor:
    """
        reactor class describes reactor parameters
    """
    def __init__(self, name, output_comp, core_mass, cycle_time,
                 batch_size, refuel_time, deploy_time, decom_time):
        self.name = name
        self.output_comp = output_comp
        self.core_mass = core_mass
        self.cycle_time = cycle_time
        self.batch_size = batch_size
        self.refuel_time = refuel_time
        self.deploy_time = deploy_time
        self.decom_time = decom_time

        # here are calculated values
        self.get_fuel_schedule()

    def get_fuel_schedule(self):
        fuel_time_list = np.array([self.deploy_time])
        time = self.deploy_time
        while True:
            time += self.cycle_time + self.refuel_time
            if time > self.decom_time:
                break
            fuel_time_list = np.append(fuel_time_list, time)
        if fuel_time_list[-1] != self.decom_time:
            fuel_time_list = np.append(fuel_time_list, self.decom_time)

        fuel_in_list = np.array([self.batch_size] * len(fuel_time_list))
        fuel_in_list[0] = self.core_mass
        fuel_in_list[-1] = 0

        fuel_out_list = np.array([self.batch_size] * len(fuel_time_list))
        fuel_out_list[0] = 0
        fuel_out_list[-1] = self.core_mass

        self.fuel_in_list = fuel_in_list
        self.fuel_out_list = fuel_out_list
        self.fuel_time_list = fuel_time_list



lwr1 = reactor('lwr1', {'U235': 0.3, 'Pu239': 0.4, 'Pu241': 0.3}, 99, 18, 33, 1, 0, 100)
lwr2 = reactor('lwr2', {'U235': 0.3, 'Pu239': 0.4, 'Pu241': 0.3}, 99, 18, 33, 1, 0, 100)
lwr3 = reactor('lwr3', {'U235': 0.3, 'Pu239': 0.4, 'Pu241': 0.3}, 99, 18, 33, 1, 0, 100)
lwr4 = reactor('lwr4', {'U235': 0.3, 'Pu239': 0.4, 'Pu241': 0.3}, 99, 18, 33, 1, 0, 100)

reactor_list = np.array([lwr1, lwr2, lwr3, lwr4])

def pu_inv(reactor_list):
    unf_inv = np.zeros(timestep)
    for reactor in reactor_list:
        for indx, fuel_discharge in enumerate(reactor.fuel_out_list):
            unf_inv[indx] += fuel_discharge

    pu_inv = np.zeros(timestep)
    for reactor in reactor_list:
        # find pu content of reactor discharge comp
        pu_content = sum([value for key, value in reactor.output_comp.items() if 'Pu' in key])
        for indx, fuel_discharge in enumerate(reactor.fuel_out_list):
            discharge_time = reactor.fuel_time_list[indx]
            print(discharge_time)
            pu_inv[discharge_time-1] += fuel_discharge * pu_content

    return pu_inv

