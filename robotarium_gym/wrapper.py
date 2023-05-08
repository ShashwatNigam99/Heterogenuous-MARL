from gym import spaces, Env
from .scenarios.PredatorCapturePrey.PredatorCapturePrey import PredatorCapturePrey
from .scenarios.Warehouse.warehouse import Warehouse
from .scenarios.Simple.simple import simple
from .scenarios.ArcticTransport.ArcticTransport import ArcticTransport
#Add other scenario imports here
from robotarium_gym.utilities.misc import objectview
import os
import yaml

env_dict = {'PredatorCapturePrey': PredatorCapturePrey,
            'Warehouse': Warehouse,
            'Simple': simple,
            'ArcticTransport': ArcticTransport}


class Wrapper(Env):
    def __init__(self, env_name, config_path):
        """Creates tje Gym Wrappers

        Args:
            env (PredatorCapturePrey): A PredatorCapturePrey object to wrap in a gym env
        """
        super().__init__()
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
        
        args = objectview(config)
        self.env = env_dict[env_name](args)
        self.observation_space = self.get_observation_space()
        self.action_space = self.get_action_space()
        self.n_agents = self.env.num_robots

    def reset(self):
        # Reset the wrapped environment and return the initial observation
        observation = self.env.reset()
        return observation

    def step(self, action_n):
        # Execute the given action in the wrapped environment
        obs_n, reward_n, done_n, info_n = self.env.step(action_n)
        return tuple(obs_n), reward_n, done_n, info_n
    
    def get_action_space(self):
        return self.env.get_action_space()
    
    def get_observation_space(self):
        return self.env.get_observation_space()
        
    def get_adj_matrix(self):
        """Returns the adjacency matrix of the environment """
        return self.env.get_adj_matrix()
