import numpy as np
import pandas as pd
import time

np.random.seed(2)

N_STATE=6 # the length of the 1 dimenstional world
ACTIONS={'left','right'}
EPSILON=0.9
ALPHA=0.1
LAMBDA=0.9
MAX_EPISODES=13
FRESH_TIME=0.3 # fresh time for one move

def build_q_table(n_states,actions):
    table=pd.Dataframes(
        np.zeros((n_states,len(actions))), # q_table initial values
        columns=actions, # action's name
    )
    # print(table)
    return table

def chose_action(state,q_table):
    state_actions=q_table.iloc[state,:]
    if(np.random.uniform()>EPSILON) or (state_actions.all()==0):
        action_name=np.random.choice(ACTIONS)
    else: # act greedy
        action_name=state_actions.argmax()
    return action_name

def get_env_feedback(S,A):
    # This is how the agent interacts with the environment

def rl():



