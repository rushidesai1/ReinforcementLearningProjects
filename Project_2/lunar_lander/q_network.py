import pytorch_lightning as pl
import torch.nn as nn


# class DQN(nn.Module):
class DQN(pl.LightningModule):
    """
    Linear Neural Net as a function approximator for state action values
    """

    def __init__(self, network_config):
        """
        Assume network_config:dictionary contains:
            state_dim: int
            hidden_dim: int
            num_actions: int
        """
        super(DQN, self).__init__()
        input_dim = network_config['state_dim']
        hidden_dim = network_config['num_hidden_units']
        output_dim = network_config['action_dim']
        super(DQN, self).__init__()
        self.network = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(inplace=True),
            nn.Linear(hidden_dim, output_dim)
        )

    def forward(self, x):
        return self.network(x)
