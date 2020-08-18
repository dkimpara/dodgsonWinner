import os
from random import shuffle, choice
import numpy as np
from multiprocessing import Pool
import pandas as pd
import pickle as pk

from alg import *


#want to test the algorithm for a range of n,m
#and graph it. how many trials per run? depends on
#size of probability

def collect_data(candidates, exps):
    trials = 100
    
    input_list = [(e, c, trials) for e in exps for c in candidates]
    with Pool(processes=os.cpu_count() - 1) as pool:
        process = pool.map_async(run_trial, input_list)
        data = process.get()
        
    write_dataframe(data, str([candidates, exps]))
    
def run_trial(input_data):
    exp, candidates, trials = input_data
    data_dict = {'v_exp': exp, 
                'candidates': candidates,
                'success': test_sample(candidates ** exp, candidates, trials),
                'trials': trials}
    
    return data_dict

def test_sample(n, m, trials = 100):
    success = 0
    for i in range(trials):
        C, V = uniform_random(n, m)
        res = greedy_winner(C, 0, V)
        if res[1]:
            success += 1
    return success/trials

def uniform_random(n, m):
    """n, int, number of voters
    m, the number of candidates
    returns a uniform random election"""
    #make sure inputs are ints
    n, m = int(n), int(m)
    V = [list(range(m)) for i in range(n)]
    for v in V:
        shuffle(v)

    C = list(range(m))
    return C, V


def write_dataframe(data, experiment_name):
    df = pd.DataFrame(data)  # empty dicts will be stored as NaNs
    df.name = experiment_name
    df.to_pickle('./df_' + df.name)

    '''to unpickle:
    df =pd.read_pickle("./dummy.pkl")
    '''

def combine():
    abs_folder_path = get_exp_path()
    frames = []
    for filename in os.listdir(abs_folder_path):
        frames.append(pd.read_pickle("data/" + filename))
    return pd.concat(frames)

def get_exp_path():
    script_dir = os.path.dirname(__file__)
    rel_path = "../data"
    return os.path.join(script_dir, rel_path)

def lower(m):
    #returns number of voters that makes probability less than 1
    return -8 * m **2 * np.log(1 / (2 * (m-1) * m))

