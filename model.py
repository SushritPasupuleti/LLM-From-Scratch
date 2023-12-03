import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Using device:", device)

block_size = 8 # length of input sequence - Tune based on VRAM and Model Performance Requirements
batch_size = 10 # number of batches to run in parallel - Tune based on VRAM

