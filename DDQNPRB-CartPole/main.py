# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from DDQN import DDQN_agent
from buffer import PrioritizedReplayBuffer
import gym

def main():
    env = gym.make("CartPole-v1", render_mode="rgb_array")
    rew_threshold = 400
    agent = DDQN_agent(env, rew_threshold)
    agent.train()

    eval_env = gym.make("CartPole-v1", render_mode="human")
    agent.evaluate(eval_env)

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
