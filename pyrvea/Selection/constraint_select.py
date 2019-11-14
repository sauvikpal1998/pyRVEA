import numpy as np
from math import sqrt
from pyrvea.Selection import niche_count
import copy


class constraint_tour_select:
    def __init__(self, constraints: list, objectives: list, flags: list):
        """
        A binary Tournament constraint selection method.

        Parameters
        ----------
        contraints : array_like
            An array of contraint functions.
        population : array_like
            The total population
        objectives : array_like
            Objective functions
        flags : array_like
            An array of flags whether the objective function should be max. in min.
        
        Returns
        -------
        array_like
            new population
        """
        self.constraints = constraints
        self.objectives = objectives
        self.flags = flags

    def select_individuals(self, population):
        individuals = []
        for i in range(2):
            index = np.random.randint(0, len(population)-1)
            individuals.append(population[index])
            # population.pop(index)
        return individuals

    def get_feasibility(self, individuals):
        feasibility = [True for i in range(len(individuals))]
        # check feasibility
        # print("Individuals-", end=" ")
        # print(individuals)
        for constraint in self.constraints:
            for i in range(len(individuals)):
                if constraint(individuals[i])==False:
                    feasibility[i] = False

        return feasibility

    def get_dominance(self, individuals, feasibility, population):
        comparison_set = []
        comparison_set_type = feasibility[0]

        # create a comparison set

        while len(comparison_set) < 10:
            rand_num = np.random.randint(len(population))
            individual = population[rand_num]
            indi_feasibility = True

            for constraint in self.constraints:
                if constraint(individual) != comparison_set_type:
                    indi_feasibility = False

            if indi_feasibility:
                comparison_set.append(individual)

        dominance = [True, True]
        # True => non dominant to all
        # False => dominated by atleast one

        comparison_set_objective_vals = []
        for comparitive in comparison_set:
            objective_vals = []
            for obj in self.objectives:
                objective_vals.append(obj(comparitive))
            comparison_set_objective_vals.append(objective_vals)
        

        # print("comparison_set_objective_vals", np.array(comparison_set_objective_vals))
        
        selected_individuals_obj_vals = []
        for i, individual in enumerate(individuals):
            # print(f"individual-{i} = {individual}")
            objective_vals = []
            for obj in self.objectives:
                objective_vals.append(obj(individual))
            selected_individuals_obj_vals.append(objective_vals)
            
            # print(f"obj_vals", np.array(objective_vals))
            
            for cs_indi_vals in comparison_set_objective_vals:
                
                # Check whether an objective is dominated by an individual
                indi_flag = False
                for j, (obj_val, cs_val) in enumerate(zip(objective_vals, cs_indi_vals)):
                    # print('obj-vals=', obj_val,' cs-val=', cs_val)
                    # print(obj_val, cs_val)
                    if self.flags[j]=="max":
                        if obj_val < cs_val:
                            indi_flag = True
                        else:
                            indi_flag = False
                            break

                    elif self.flags[j]=="min":
                        if obj_val > cs_val:
                            indi_flag = True
                        else:
                            indi_flag = False
                            break
                
                if indi_flag:
                    dominance[i] = False
                    break

        if dominance[0]==dominance[1]:
            self.selected_individuals_obj_vals = selected_individuals_obj_vals
            
        return dominance

    def get_new_pop(self, population):
        self.population = population
        self.new_population = []
        alt_population = list(self.population)

        while(len(self.new_population)<=len(population)):

            # Selecting individuals for comparison
            # if len(alt_population)==2:
            #     individuals = [alt_population[0], alt_population[1]]
            #     alt_population.pop(0)
            # else:
            #     individuals = self.select_individuals(alt_population)
            
            individuals = self.select_individuals(population)

            # Getting feasibilities
            feasibility = self.get_feasibility(individuals)

            # if feasibilty is not same
            if feasibility[0] != feasibility[1]:
                # print("feasibility")
                if feasibility[0]:
                    self.new_population.append(individuals[0])
                else:
                    self.new_population.append(individuals[1])

                # Done here, go to next loop
                continue

            # If feasibilty is the same
            dominance = self.get_dominance(individuals, feasibility, alt_population)

            if dominance[0]!=dominance[1]:
                # print("dominance", dominance)
                if dominance[0]:
                    self.new_population.append(individuals[0])
                else:
                    self.new_population.append(individuals[1])

                # Done here, go to next loop
                continue
            
            # Niche count
            # print("Niche count")
            # print(len(alt_population), self.selected_individuals_obj_vals)
            self.new_population.append(
                    individuals[
                        niche_count.best_niche_index(
                            alt_population, self.selected_individuals_obj_vals, self.objectives
                        )
                    ]
                )

        return self.new_population
            
