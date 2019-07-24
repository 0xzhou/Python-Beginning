import tensorflow as tf
import numpy as np
import gym
from gym.spaces import Discrete, Box

def mlp(x, sizes, activation=tf.tanh, outputf_activation=None):
    # Build a feedforward neural
    # Question: x为输入，n维向量；sizes为列表，每层的神经元数目
    for size in sizes[:-1]:
        x=tf.layers.dense(x, units=size, activation= activation)
    return tf.layers.dense(x, units=sizes[:-1], activation= outputf_activation)

def train(env_name='CarPole-v0', hidden_size=[32], lr=1e-2,
          epochs=50, batch_size=5000, render=False):

    # make environment, check spaces, get obs / act dims
    env=gym.make(env_name)
    assert isinstance(env.observation_space, Box), \
        "This example only works for envs with continuous state spaces."
    assert isinstance(env.action_space,Discrete), \
        "This example only works for envs with discret state spaces."

    obs_dim=env.observation_space[0]
    n_acts=env.action_space.n

    # make core of policy network