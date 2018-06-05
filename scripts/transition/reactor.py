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
    def __init__(self, name, fr, power_cap, input_comp, output_comp,
                 core_mass, cycle_time, batch_size, refuel_time, lifetime):
        self.name = name
        self.fr = fr
        self.output_comp = output_comp
        self.input_comp = input_comp
        self.core_mass = core_mass
        self.power_cap = power_cap
        self.cycle_time = cycle_time
        self.batch_size = batch_size
        self.refuel_time = refuel_time
        self.lifetime = lifetime
        self.deploy_time = 0

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