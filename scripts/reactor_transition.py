import numpy as np
from reactor import reactor
import parser
import copy
import matplotlib.pyplot as plt

class institution:
    def __init__(self, timestep, power_eq, lwr, fr, trans_start):
        self.timestep = timestep
        self.power_timeseries = self.get_power_timeseries(power_eq)
        self.trans_start = trans_start
        self.lwr = lwr
        self.fr = fr

        # recording variables
        self.lwr_deployment = np.zeros(timestep)
        self.fr_deployment = np.zeros(timestep)
        self.deployed_lwrs = np.zeros(timestep)
        self.deployed_frs = np.zeros(timestep)

        # initial conditions
        self.reactor_list = np.empty(0)
        self.time = 0
        self.pu_inv = 0

        # pu_composition
        self.fr_in_pu_comp = sum([value for key, value in self.fr.input_comp.items() if 'Pu' in key])
        self.fr_out_pu_comp = sum([value for key, value in self.fr.output_comp.items() if 'Pu' in key])
        self.lwr_out_pu_comp = sum([value for key, value in self.lwr.output_comp.items() if 'Pu' in key])
        self.fr_startup_pu = self.fr.core_mass * self.fr_in_pu_comp

        # actually do the things to get deployment timeseries
        self.meet_init_power()
        while self.time < timestep:
            print('Time: %i' %self.time)
            print('Power Demand:' + str(self.power_timeseries[self.time]))
            print('Reactors Deployed: ' + str(len(self.reactor_list)))
            print('\n')
            self.update_pu_inv()
            if self.pu_inv < 0:
                raise ValueError('PU INV IS NEGATIVE. FAIL!')
            print('PU INVENTORY')
            print(self.pu_inv)
            ### RECORDING
            self.deployed_lwrs[self.time] = sum([1 for reactor in self.reactor_list if not reactor.fr])
            self.deployed_frs[self.time] = sum([1 for reactor in self.reactor_list if reactor.fr])
            self.build_lacking()
            self.decom()
            self.time += 1


    def get_power_timeseries(self, power_eq):
        eq = parser.expr(power_eq).compile()
        power_timeseries = np.zeros(self.timestep)
        for indx, value in enumerate(power_timeseries):
            t = indx
            power_timeseries[indx] = eval(eq)
        return power_timeseries

    def meet_init_power(self):
        # deploy initial reactors. Always over estimate
        num_deploy = np.ceil(self.power_timeseries[0] / self.lwr.power_cap)
        init_lwrs = self.deploytime_change(0, False)
        init_lwrs.get_fuel_schedule()
        self.reactor_list = np.append(self.reactor_list, [init_lwrs] * int(num_deploy))
        print('%i LWRs are built initially' %(num_deploy))
        self.lwr_deployment[0] = num_deploy


    def decom(self):
        hitlist = []
        for indx, reactor in enumerate(self.reactor_list):
            if reactor.deploy_time + reactor.lifetime == self.time:
                hitlist.append(indx)
        self.reactor_list = np.delete(self.reactor_list, hitlist)
        if len(hitlist) > 0:
            print('%i reactors are decomed at timestep %i' %(len(hitlist), self.time))

    def build_lacking(self):
        diff = self.power_timeseries[self.time] - self.calc_deployed_power()
        if self.time < self.trans_start:
            if diff > self.lwr.power_cap:
                num_build = np.ceil(diff / self.lwr.power_cap)
                built_lwrs = self.deploytime_change(self.time, False)
                built_lwrs.get_fuel_schedule()
                self.reactor_list = np.append(self.reactor_list, [built_lwrs] * int(num_build))
                if num_build > 0:
                    print('%i LWRs are built at timestep %i' %(num_build, self.time))
                    self.lwr_deployment[self.time] = num_build

        else:
            if diff > self.fr.power_cap:
                num_build = np.ceil(diff / self.fr.power_cap)
                built_frs = self.deploytime_change(self.time, True)
                built_frs.get_fuel_schedule()

                # check pu inventory
                if self.pu_inv < (num_build * self.fr_startup_pu):
                    num_build = np.floor(self.pu_inv / self.fr_startup_pu)

                self.reactor_list = np.append(self.reactor_list, [built_frs] * int(num_build))
                if num_build > 0:
                    print('%i FRs are built at timestep %i' %(num_build, self.time))
                    self.fr_deployment[self.time] = num_build

                diff = self.power_timeseries[self.time] - self.calc_deployed_power()
                if diff > self.lwr.power_cap:
                    num_build = np.ceil(diff / self.lwr.power_cap)
                    built_lwrs = self.deploytime_change(self.time, False)
                    built_lwrs.get_fuel_schedule()
                    self.reactor_list = np.append(self.reactor_list, [built_lwrs] * int(num_build))
                    if num_build > 0:
                        print('%i LWRs are built at timestep %i' %(num_build, self.time))
                        self.lwr_deployment[self.time] = num_build


    def update_pu_inv(self):
        for reactor in self.reactor_list:
            if not reactor.fr:
                for indx, fuel_discharge_time in enumerate(reactor.fuel_time_list):
                    if fuel_discharge_time == self.time:
                        self.pu_inv += reactor.fuel_out_list[indx] * self.lwr_out_pu_comp
            else:
                for indx, fuel_load_time in enumerate(reactor.fuel_time_list):
                    if fuel_load_time == self.time:
                        self.pu_inv -= reactor.fuel_in_list[indx] * self.fr_in_pu_comp
                        self.pu_inv += reactor.fuel_out_list[indx] * self.fr_out_pu_comp

    def calc_deployed_power(self):
        power = 0
        for reactor in self.reactor_list:
            power += reactor.power_cap
        return power

    def deploytime_change(self, deploy_time, fr):
        if not fr:
            clone = copy.copy(self.lwr)
        else:
            clone = copy.copy(self.fr)
        clone.deploy_time = deploy_time
        return clone

    def plot_power_cap(self):
        timeseries = np.arange(self.timestep)
        plt.plot(timeseries, self.deployed_lwrs * self.lwr.power_cap, label='LWR')
        plt.plot(timeseries, self.deployed_frs * self.fr.power_cap, label='FR')
        plt.plot(timeseries, self.power_timeseries, label='POWER TIMESERIES')
        plt.grid()
        plt.legend()
        plt.show()

    def plot_deployment(self):
        timeseries = np.arange(self.timestep)
        plt.plot(timeseries, self.lwr_deployment, label='LWR')
        plt.plot(timeseries, self.fr_deployment, label='FR')
        plt.grid()
        plt.legend()
        plt.show()



lwr = reactor('lwr1', False, 1000, {'U235': 0.05, 'U238': 0.95}, {'U235': 0.99, 'Pu239': 0.01},
              99, 2, 33, 1, 10)
fr = reactor('sfr1', True, 600, {'U238': 0.9, 'Pu239': 0.1}, {'U238': 0.85, 'Pu239': 0.15},
             60, 2, 15, 1, 10)

z = institution(100, '10000 + (300 * t)', lwr, fr, trans_start=50)
z.plot_power_cap()
plt.close()
z.plot_deployment()


