from collections import deque
from typing import Mapping
from openpi_client import image_tools
from openpi_client import websocket_client_policy as _websocket_client_policy
import numpy as np
import torch

class PI0RemotePolicy:
    def __init__(self, host: str, port: int, n_action_steps: int | None = None):
        self.client = _websocket_client_policy.WebsocketClientPolicy(host, port)
        self.action_queue = deque()
        self.n_action_steps = n_action_steps

    def select_action(self, observation: Mapping[str, np.ndarray]) -> np.ndarray:
        if len(self.action_queue) == 0:
            # Query model to get action
            action_chunk = self.client.infer(observation)["actions"]
            if self.n_action_steps is not None:
                action_chunk = action_chunk[:self.n_action_steps]
            self.action_queue.extend(action_chunk)

        action = self.action_queue.popleft()

        return torch.tensor(action)

    def chunk_start(self) -> bool:
        return len(self.action_queue) > 0

    def to(self, device: str):
        return self