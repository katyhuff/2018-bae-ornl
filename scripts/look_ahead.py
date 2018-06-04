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
    def __init__(self, name, fr, power_cap, input_comp, output_comp, core_mass, cycle_time,
                 batch_size, refuel_time, deploy_time, lifetime):
        self.name = name
        self.fr = fr
        self.output_comp = output_comp
        self.input_comp = input_comp
        self.core_mass = core_mass
        self.power_cap = power_cap
        self.cycle_time = cycle_time
        self.batch_size = batch_size
        self.refuel_time = refuel_time
        self.deploy_time = deploy_time
        self.lifetime = lifetime

        # here are calculated values
        self.get_fuel_schedule()

    def get_fuel_schedule(self):
        fuel_time_list = np.array([self.deploy_time])
        time = self.deploy_time
        decom_time = self.deploy_time + self.lifetime
        while True:
            time += self.cycle_time + self.refuel_time
            if time > decom_time:
                break
            fuel_time_list = np.append(fuel_time_list, time)
        if fuel_time_list[-1] != decom_time:
            fuel_time_list = np.append(fuel_time_list, decom_time)

        fuel_in_list = np.array([self.batch_size] * len(fuel_time_list))
        fuel_in_list[0] = self.core_mass
        fuel_in_list[-1] = 0

        fuel_out_list = np.array([self.batch_size] * len(fuel_time_list))
        fuel_out_list[0] = 0
        fuel_out_list[-1] = self.core_mass

        self.fuel_in_list = fuel_in_list
        self.fuel_out_list = fuel_out_list
        self.fuel_time_list = fuel_time_list


lwr1 = reactor('lwr1', False, 1000, {'U235': 0.05, 'U238': 0.95}, {'U235': 0.3, 'Pu239': 0.4, 'Pu241': 0.3}, 99, 18, 33, 1, 0, 120)
lwr2 = reactor('lwr2', False, 1000, {'U235': 0.05, 'U238': 0.95}, {'U235': 0.3, 'Pu239': 0.4, 'Pu241': 0.3}, 99, 18, 33, 1, 0, 120)
lwr3 = reactor('lwr3', False, 1000, {'U235': 0.05, 'U238': 0.95}, {'U235': 0.3, 'Pu239': 0.4, 'Pu241': 0.3}, 99, 18, 33, 1, 0, 120)
lwr4 = reactor('lwr4', False, 1000, {'U235': 0.05, 'U238': 0.95}, {'U235': 0.3, 'Pu239': 0.4, 'Pu241': 0.3}, 99, 18, 33, 1, 0, 120)

sfr1 = reactor('sfr1', True, 600, {'U238': 0.9, 'Pu239': 0.1}, {'U238': 0.85, 'Pu239': 0.15}, 60, 12, 15, 1, 50, 160)
sfr2 = reactor('sfr2', True, 600, {'U238': 0.9, 'Pu239': 0.1}, {'U238': 0.85, 'Pu239': 0.15}, 60, 12, 15, 1, 60, 160)
sfr3 = reactor('sfr3', True, 600, {'U238': 0.9, 'Pu239': 0.1}, {'U238': 0.85, 'Pu239': 0.15}, 60, 12, 15, 1, 70, 160)
sfr4 = reactor('sfr4', True, 600, {'U238': 0.9, 'Pu239': 0.1}, {'U238': 0.85, 'Pu239': 0.15}, 60, 12, 15, 1, 80, 160)

reactor_list = np.array([lwr1, lwr2, lwr3, lwr4, sfr1, sfr2, sfr3, sfr4])

def unf_inv(reactor_list):
    unf_inv = np.zeros(timestep)
    for reactor in reactor_list:
        for indx, fuel_discharge in enumerate(reactor.fuel_out_list):
            discharge_time = reactor.fuel_time_list[indx]
            if discharge_time < timestep:
                unf_inv[discharge_time] += fuel_discharge
    return np.cumsum(unf_inv)

def pu_inv(reactor_list):
    pu_inv = np.zeros(timestep)
    for reactor in reactor_list:
        # find pu content of reactor discharge comp
        pu_content = sum([value for key, value in reactor.output_comp.items() if 'Pu' in key])
        for indx, fuel_discharge in enumerate(reactor.fuel_out_list):
            discharge_time = reactor.fuel_time_list[indx]
            if discharge_time < timestep:
                pu_inv[discharge_time] += fuel_discharge * pu_content
    return np.cumsum(pu_inv)

def fuel_demand(reactor_list):
    fuel_demand = np.zeros(timestep)
    for reactor in reactor_list:
        for indx, fuel_request in enumerate(reactor.fuel_in_list):
            request_time = reactor.fuel_time_list[indx]
            if request_time < timestep:
                fuel_demand[request_time] += fuel_request
    return fuel_demand



print(lwr1.fuel_time_list)
print(lwr1.fuel_in_list)
print(lwr1.fuel_out_list)
print(unf_inv(reactor_list))
print(pu_inv(reactor_list))
print(fuel_demand(reactor_list))
