import numpy as np
from math import sqrt
from pyrvea.Selection import niche_count
import copy

def tour_select(fitness, tournament_size):
    """Tournament selection. Choose number of individuals to participate
    and select the one with the best fitness.

    Parameters
    ----------
    fitness : array_like
        An array of each individual's fitness.
    tournament_size : int
        Number of participants in the tournament.

    Returns
    -------
    int
        The index of the best individual.
    """
    aspirants = np.random.choice(len(fitness) - 1, tournament_size, replace=False)
    chosen = []
    for ind in aspirants:
        chosen.append([ind, fitness[ind]])
    chosen.sort(key=lambda x: x[1])

    return chosen[0][0]


def constraint_tour_select(constraints: list, population: list, objectives: list):
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
    
    Returns
    -------
    array_like
        new population
    """
    alt_population = list(population)
    new_population = []
    # count = 0
    while len(alt_population) > 2:
        print(len(alt_population))
        # count = count + 1
        individuals = []
        for i in range(2):
            index = np.random.randint(0, len(alt_population) - 1)
            individuals.append(alt_population[index])
            alt_population.pop(index)
            # alt_population = alt_population.delete(alt_population, index, 0)

        feasibility = [True, True]

        # check feasibility

        for constraint in constraints:
            if constraint(individuals[0]) == False:
                feasibility[0] = False
            if constraint(individuals[1]) == False:
                feasibility[1] = False

        # if feasibilty is not same

        if feasibility[0] != feasibility[1]:
            print("feasibility")
            if feasibility[0]:
                new_population.append(individuals[0])
            else:
                new_population.append(individuals[1])

        # if the feasibilty of both of them is same

        elif feasibility[0] == feasibility[1]:
            comparison_set = []
            comparison_set_type = feasibility[0]

            # create a comparison set

            while len(comparison_set) < 10:
                rand_num = np.random.randint(len(population))
                individual = population[rand_num]
                indi_feasibility = True

                for constraint in constraints:
                    if constraint(individual) != comparison_set_type:
                        indi_feasibility = False

                if indi_feasibility:
                    comparison_set.append(individual)

            dominance = [True, True]

            comparison_set_objective_vals = []

            # find dominance

            for comparitive in comparison_set:
                objective_vals = []
                for obj in objectives:
                    objective_vals.append(obj(comparitive))
                comparison_set_objective_vals.append(objective_vals)
            # print(comparison_set_objective_vals)
            selected_individuals_obj_vals = []

            for i, individual in enumerate(individuals):
                objective_vals = []
                for obj in objectives:
                    objective_vals.append(obj(comparitive))
                flag = False

                selected_individuals_obj_vals.append(objective_vals)

                for cs_indi_vals in comparison_set_objective_vals:
                    print('------')
                    for obj_val, cs_val in zip(objective_vals, cs_indi_vals):
                        print('obj-vals=', obj_val,' cs-val=', cs_val)
                        if obj_val >= cs_val:
                            flag = True
                            break
                    if flag:
                        break
                print(flag)
                if flag == False:
                    dominance[i] = flag

            # check if dominance is same

            if dominance[0] != dominance[1]:
                # print("dominance")
                if dominance[0]:
                    new_population.append(individuals[0])
                else:
                    new_population.append(individuals[1])

            # niche count comparison if both the values are same

            else:
                # print(dominance)
                # print("niche count")
                new_population.append(
                    individuals[
                        niche_count.best_niche_index(
                            population, selected_individuals_obj_vals, objectives
                        )
                    ]
                )

    return new_population

