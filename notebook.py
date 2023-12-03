# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: hydrogen
#       format_version: '1.3'
#       jupytext_version: 1.15.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Using device:", device)

# %%
block_size = 8 # length of input sequence - Tune based on VRAM and Model Performance Requirements
batch_size = 10 # number of batches to run in parallel - Tune based on VRAM

# %%
print("block_size:", block_size)
print("batch_size:", batch_size)
