import torch.nn as nn


class Truncated_VGG(nn.Module):
    def __init__(self, pretrained_vgg_model):
        super(Truncated_VGG, self).__init__()

        ''' {conv_1: 0, conv_2: 5, conv_3: 10, conv_4: 19, conv_5: 28}'''
        self.content_reconstruction_layers = [0, 5, 10, 19, 28]
        self.model = pretrained_vgg_model

    def forward(self, image):
        reconstructed_images = []

        for idx, layer in enumerate(self.model):
            image = layer(image)
            
            # storing output of the above defined layers
            if idx in self.content_reconstruction_layers:
                N, H, W = image.shape
                reconstructed_images.append(image.view(N, H*W))

        return reconstructed_images
