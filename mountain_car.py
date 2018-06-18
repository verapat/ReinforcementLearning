import gym
import numpy as np

def run_episode(env, parameters):
    observation = env.reset()
    totalreward = 0
    for _ in range(2000):
        action = 0 if np.matmul(parameters, observation) < 0 else 1
        observation, reward, done, info = env.step(action)
        totalreward += reward
        if done:
            break
    return totalreward

def show_episode(env, parameters):
    observation = env.reset()
    firstframe = env.render(mode = 'rgb_array')
    frames = [firstframe]
    for _ in range(2000) :
        action = 0 if np.matmul(parameters, observation) < 0 else 1
        observation, reward, done, info = env.step(action)
        frame = env.render(mode = 'rgb_array')
        frames.append(frame)
        if done:
            break
    return frames

env = gym.make('CartPole-v0')
observation = env.reset()
#firstframe = env.render(mode='rgb_array')

bestparams = None
bestreward = 0
for _ in range(10000):
    parameters = np.random.rand(4) * 2 - 1
    reward = run_episode(env, parameters)
    if reward > bestreward:
        bestreward = reward
        bestparams = parameters
        if reward >= 2000:
            break
print(bestreward)
frames = show_episode(env,bestparams)
env.close()
#display_frames_as_gif(frames, filename_gif = "bestresultrandom.gif")
    
#env = gym.make("CartPole-v0")
#print(env.action_space)
#print(env.observation_space)
#for i_episode in range(20):
#    observation = env.reset()
#    for t in range(100):
#        env.render()
#        print(observation)
#        action = env.action_space.sample()
#        observation, reward, done, info = env.step(action)
#        if done:
#            print("Episode finished after {} timesteps".format(t+1))
#            break
#env.close()