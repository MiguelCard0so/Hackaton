import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from collections import deque
import random

# Define the DQN (Deep Q-Network)
class DQN(nn.Module):
    def __init__(self, state_size, action_size):
        super(DQN, self).__init__()
        self.fc1 = nn.Linear(state_size, 64)
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, action_size)
        
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        return self.fc3(x)

# Replay Buffer for experience storage
class ReplayBuffer:
    def __init__(self, capacity):
        self.buffer = deque(maxlen=capacity)
    
    def push(self, state, action, reward, next_state, done):
        self.buffer.append((state, action, reward, next_state, done))
    
    def sample(self, batch_size):
        return random.sample(self.buffer, batch_size)
    
    def __len__(self):
        return len(self.buffer)

# DRL Agent
class DRLAgent:
    def __init__(self, state_size, action_size):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.state_size = state_size
        self.action_size = action_size
        self.model = DQN(state_size, action_size).to(self.device)
        self.target_model = DQN(state_size, action_size).to(self.device)
        self.optimizer = optim.Adam(self.model.parameters(), lr=0.001)
        self.memory = ReplayBuffer(10000)
        self.batch_size = 64
        self.gamma = 0.95
        self.epsilon = 1.0
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        
    def act(self, state, training=True):
        if training and np.random.rand() <= self.epsilon:
            return np.random.choice(self.action_size)
        
        state = torch.FloatTensor(state).to(self.device)
        with torch.no_grad():
            q_values = self.model(state)
        return torch.argmax(q_values).item()
    
    def train(self):
        if len(self.memory) < self.batch_size:
            return
        
        batch = self.memory.sample(self.batch_size)
        states, actions, rewards, next_states, dones = zip(*batch)
        
        states = torch.FloatTensor(np.array(states)).to(self.device)
        next_states = torch.FloatTensor(np.array(next_states)).to(self.device)
        actions = torch.LongTensor(actions).to(self.device)
        rewards = torch.FloatTensor(rewards).to(self.device)
        dones = torch.FloatTensor(dones).to(self.device)
        
        current_q = self.model(states).gather(1, actions.unsqueeze(1))
        next_q = self.target_model(next_states).max(1)[0].detach()
        target_q = rewards + (1 - dones) * self.gamma * next_q
        
        loss = nn.MSELoss()(current_q.squeeze(), target_q)
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
        
        # Update epsilon
        self.epsilon = max(self.epsilon_min, self.epsilon * self.epsilon_decay)
        
    def update_target_network(self):
        self.target_model.load_state_dict(self.model.state_dict())

# Example usage in your game loop
class GameEnvironment:
    def __init__(self):
        # Define your game state parameters (player position, NPC state, etc.)
        self.state_size = 8  # Adjust based on your needs
        self.action_size = 4  # [up, down, left, right] for example
        
        # Initialize agent
        self.agent = DRLAgent(self.state_size, self.action_size)
        self.update_target_freq = 1000
        self.steps = 0
        
    def get_state(self):
        # Implement your actual game state observation
        # Should return player position, NPC position, game context, etc.
        return np.random.randn(self.state_size)  # Replace with real data
        
    def step(self, action):
        # Implement game physics and return:
        # next_state, reward, done
        reward = 0  # Calculate based on game objectives
        done = False  # Game termination condition
        return self.get_state(), reward, done
        
    def train_agent(self, episodes=1000):
        for episode in range(episodes):
            state = self.get_state()
            total_reward = 0
            done = False
            
            while not done:
                action = self.agent.act(state)
                next_state, reward, done = self.step(action)
                self.agent.memory.push(state, action, reward, next_state, done)
                self.agent.train()
                
                state = next_state
                total_reward += reward
                self.steps += 1
                
                if self.steps % self.update_target_freq == 0:
                    self.agent.update_target_network()
            
            print(f"Episode: {episode}, Total Reward: {total_reward:.2f}, Epsilon: {self.agent.epsilon:.2f}")

# Initialize and train
env = GameEnvironment()
env.train_agent(episodes=1000)