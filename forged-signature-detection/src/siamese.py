import torch
import torch.nn as nn
import torch.nn.functional as F
import math


class siamese_conv(nn.Module):
    def __init__(self, height, width) -> None:
        super(siamese_conv, self).__init__()
        self.conv1 = nn.Sequential(
            nn.Conv2d(1, 16, 3, stride=1, padding=1),
            nn.ReLU())
        self.conv2 = nn.Sequential(
            nn.Conv2d(16, 16, 3, padding=1),
            nn.ReLU(),
            nn.Conv2d(16, 32, 3, padding=1, stride=2),
            nn.BatchNorm2d(32),
            nn.ReLU())
        self.conv3 = nn.Sequential(
            nn.Conv2d(32, 32, 3, padding=1),
            nn.ReLU(),
            nn.Conv2d(32, 64, 3, padding=1, stride=2),
            nn.BatchNorm2d(64),
            nn.ReLU())
        self.flatten = nn.Flatten()
        self.fc1 = nn.Sequential(
            nn.Linear(4*height*width, height),
            nn.ReLU())
        self.fc2 = nn.Linear(height, int(math.sqrt(height)))

    def forward(self, inp):
        x = self.conv1(inp)
        x = self.conv2(x)
        x = self.conv3(x)
        x = self.flatten(x)
        x = self.fc1(x)
        x = self.fc2(x)
        return x


def Contrastive_loss(target: int, alpha, beta, s1, s2):
    Dw = torch.pairwise_distance(s1, s2, p=2)
    term1 = alpha*(1-target)*Dw**2
    term2 = beta*target*F.relu(10-Dw)**2
    return torch.mean(term1+term2, dtype=torch.float)
