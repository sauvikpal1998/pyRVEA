import numpy as np
from math import sqrt

def get_niche_count(
    f_diff: np.ndarray,             # list of objectives max-min value
    min_dist: int,                  # minimum distance param
    sigma_share: int,               # sigma share value
    f_pop_vals: np.ndarray,         # calculated values of objective funcs. for population - shape=[objectives][pops]
    f_selected_val: np.ndarray,     # calculated values of objective funcs. for selected individual - shape=[objectives]
    # objectives: list,             # list of objective funcs.
):

    niche_count = 0

    for i in range(len(f_pop_vals)):
        dist = 0
        for j in range(len(f_selected_val)):
            dist += ((f_selected_val[j]-f_pop_vals[i][j])/f_diff[j])**2
        dist = sqrt(dist)

        if(dist<min_dist):
            niche_count += 1-(dist/sigma_share)
    # print(niche_count)
    return niche_count


def best_niche_index(
    population: list,
    # individuals: list,
    indi_obj_vals: np.ndarray,
    objectives: list,
):
    fmax = []
    fmin = []
    f_pop_vals = []
    f_temp = []

    for obj in objectives:
        temp_max = -2**9
        temp_min = 2**9
        f_temp = []
        for indi in population:
            obj_val = obj(indi)
            f_temp.append(obj_val)
            temp_max = max(obj_val, temp_max)
            temp_min = min(obj_val, temp_min)
        f_pop_vals.append(f_temp)
        fmax.append(temp_max)
        fmin.append(temp_min)
    fmax = np.array(fmax)
    fmin = np.array(fmin)
    f_pop_vals = np.array(f_pop_vals)

    f_diff = fmax-fmin

    # TODO: How to optimize niche count calculation

    # params set
    sigma_share = 25
    min_dist = 20

    niche_counts = []

    for f_selected_val in indi_obj_vals:
        niche_counts.append(get_niche_count(f_diff, min_dist, sigma_share, f_pop_vals, f_selected_val))

    return niche_counts.index(min(niche_counts))