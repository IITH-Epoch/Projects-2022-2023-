import torch
from torchvision.utils import save_image

HYPERPARAMETERS = {"Learning Rate": 5*1e-3,
                   "Epochs": 400,
                   "alpha": 1e-4,
                   "beta": 1,
                   "print_interval": 25,
                   "save_interval": 200}


def loss_fn(gen_features, ori_features, style_features, alpha=1e-3, beta=1):
    content_loss = 0.0
    style_loss = 0.0
    num_layers = len(gen_features)

    # iterating for outputs of each layer stored in ***_features variable
    for generated_image, original_image, style_image in zip(gen_features, ori_features, style_features):

        content_loss += torch.mean((generated_image - original_image)**2)

        # Gram Matrix
        Gl = torch.matmul(generated_image, generated_image.T)
        Al = torch.matmul(style_image, style_image.T)

        # averaging over the layers
        style_loss += (1/num_layers) * torch.mean((Gl - Al)**2)

    total_loss = alpha*content_loss + beta*style_loss

    return total_loss


def generating_image(original_image, style_image, model, hyperparameters=HYPERPARAMETERS, verbose=True):
    lr, epochs, alpha, beta, print_interval, save_interval = hyperparameters.values()

    generated_image = original_image.clone()
    generated_image.requires_grad = True

    optimizer = torch.optim.AdamW(params=[generated_image], lr=lr)

    for epoch in range(epochs+1):
        gen_features = model(generated_image)
        ori_features = model(original_image)
        style_features = model(style_image)

        loss = loss_fn(gen_features, ori_features, style_features, alpha, beta)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if verbose:
            if epoch % print_interval == 0:
                print(f"Epoch: {epoch} | Loss {loss.item()}")
        if epoch % save_interval == 0:
            print(f"Saving generated_image: {epoch}")
            save_image(generated_image,
                       "./output/generated-image" + str(epoch) + ".png")

    return generated_image
