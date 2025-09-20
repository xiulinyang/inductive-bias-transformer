import torch

cp = 'checkpoints/gn_grammarexp1/0-lstm'

from fairseq.models.transformer_lm import TransformerLanguageModel
custom_lm = TransformerLanguageModel.from_pretrained(cp, 'checkpoint_best.pt')
# Count the parameters
num_params = sum(p.numel() for p in custom_lm.models[0].parameters())
print(f"Number of parameters: {num_params:,}")
