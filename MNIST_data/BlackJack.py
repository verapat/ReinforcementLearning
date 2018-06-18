# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 14:58:14 2018

@author: vw1586
"""
from random import randint
state_space = list()
action_space = list()
counter_state = dict()
state_value = dict()
total_return = dict()
policy = dict()
def init_state_space():
    for player_hand in range(12,22):
        for dealer_hand in range(1,13):
            dealer_hand = min(dealer_hand, 10)
            for usable_ace in range(0,2):
                state_space.append((player_hand, dealer_hand, usable_ace))
def init_action_space():
    action_space.append('draw')
    action_space.append('stop')
def draw_card():
    return min(randint(1,13),10)
def random_init_state():
    player_hand = randint(12,21)
    dealer_hand = draw_card()
    usable_ace = randint(0,1)
    return (player_hand, dealer_hand, usable_ace)
def init_policy():
    for this_state in state_space:
        if this_state[0] < 20:
            policy[this_state] = 'draw'
        else:
            policy[this_state] = 'stop'
def init_counter():
    for state in state_space:
        counter_state[state] = 0
def init_total_return():
    for state in state_space:
        total_return[state] = 0
def init_state_value():
    for state in state_space:
        state_value[state] = 0
def is_valid_state(this_state):
    if this_state in state_space:
        return True
    else:
        return False
def random_episode(init_state):
    in_episode_list = list()
    in_episode_list.append(init_state)
    this_state = init_state
    action = policy[init_state]
    reward = 0
    player_hand = init_state[0]
    while action != 'stop':
        new_card = draw_card()
        player_hand += new_card
        this_state = (player_hand, init_state[1], init_state[2])
        if is_valid_state(this_state):
            in_episode_list.append(this_state)
            action = policy[this_state]
        else:
            action = 'stop'
    if this_state[0] > 21:
        reward = -1
    else:
        dealer_hand = this_state[1]
        while dealer_hand < 17:
            new_card = draw_card()
            dealer_hand += new_card
        if dealer_hand > 21:
            reward = 1
        elif dealer_hand > this_state[0]:
            reward = -1
        elif dealer_hand < this_state[0]:
            reward = 1
    return in_episode_list, reward
def set_up_game():
    init_state_space()
    init_action_space()
    init_policy()
    init_counter()
    init_total_return()
def evaluate_policy():
    for epoch in range(10):
        init_state = random_init_state()
        in_episode_list, reward = random_episode(init_state)
        for this_state in in_episode_list:
            counter_state[this_state] += 1
            total_return[this_state] += reward
            state_value[this_state] = total_return[this_state] / counter_state[this_state]
def black_jack():
    set_up_game()
    evaluate_policy()
    
black_jack()
    
    