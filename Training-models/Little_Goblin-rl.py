"""AWS DeepRacer Challenge
Created By: Ayran Olckers AKA. The Geekiest One
Last Modified: 05/08/2019
Motivation: To Learn Reinforment Learning through Udacity and AWS
"""

import math
def reward_function(params):

'''
Use square root for center line

{
"all_wheels_on_track": Boolean,    # flag to indicate if the vehicle is on the track
"x": float,                        # vehicle's x-coordinate in meters
"y": float,                        # vehicle's y-coordinate in meters
"distance_from_center": float,     # distance in meters from the track center
"is_left_of_center": Boolean,      # Flag to indicate if the vehicle is on the left side to the track center or not.
"heading": float,                  # vehicle's yaw in degrees
"progress": float,                 # percentage of track completed
"steps": int,                      # number steps completed
"speed": float,                    # vehicle's speed in meters per second (m/s)
"steering_angle": float,           # vehicle's steering angle in degrees
"track_width": float,              # width of the track
"waypoints": [[float, float], … ], # list of [x,y] as milestones along the track center
"closest_waypoints": [int, int]    # indices of the two nearest waypoints.
}



'''
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    steering = abs(params['steering_angle'])
    direction_stearing=params['steering_angle']
    speed = params['speed']
    steps = params['steps']
    progress = params['progress']
    all_wheels_on_track = params['all_wheels_on_track']
    ABS_STEERING_THRESHOLD = 15
    SPEED_TRESHOLD = 5
    TOTAL_NUM_STEPS = 85

    # Read input variables
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']
    reward = 1.0

    if progress == 100:
        reward += 100
    # Calculate the direction of the center line based on the closest waypoints
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]

    # Calculate the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])

    # Convert to degree
    track_direction = math.degrees(track_direction)

    # Calculate the difference between the track direction and the heading direction of the car
    direction_diff = abs(track_direction - heading)

    # Penalize the reward if the difference is too large
    DIRECTION_THRESHOLD = 10.0
    goblin = 1

    if direction_diff > DIRECTION_THRESHOLD:
        goblin = 1 - (direction_diff / 50)

    if goblin < 0 or goblin > 1:
        goblin = 0
        reward *= goblin
    return reward
