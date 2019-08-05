"""AWS DeepRacer Challenge
Created By: Ayran Olckers AKA. The Geekiest One
Last Modified: 05/08/2019
Motivation: To Learn Reinforment Learning through Udacity and AWS
"""

def reward_function(params):
    '''
    Rewarding the agent to stay inside the two borders of the track
    Making sure that It does not run out of lane

    gives high rewards if the agent stays inside the borders and lets the agent
    figure out what is the best path to finish a lap. It is easy to program and
    understand, but will be likely to take longer time to converge.
    '''

    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']

    # Give a very low reward by default
    reward = 1e-3

    # Give a high reward if no wheels go off the track and
    # the agent is somewhere in between the track borders
    if all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05:
        reward = 2.0

    # Always return a float value
    return float(reward)
