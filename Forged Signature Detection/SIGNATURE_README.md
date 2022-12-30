# Signature Verification
Signature verification is an important task in computer vision. The approach to solve the problem can change based on the kind of problem we are trying to solve. A model is first trained on a dataset of signatures (original and forged) to learn to distinguish between original and forged signatures, the model learns the distance between two signatures, the distance should be large for dissimilar or forged signatures and original signature, and should be small between original signatures. 

The same model could be used in few shot learning to get embeddings, say we have a set of signatures (could be in a different language), we can fine tune the model or add another fully-connected layer over the embedding layer to learn the distance between the images of given small dataset or fine tune the model.


Refer the [signet paper](https://arxiv.org/abs/1707.02131) for more

```citation
@misc{https://doi.org/10.48550/arxiv.1707.02131,
  doi = {10.48550/ARXIV.1707.02131},
  
  url = {https://arxiv.org/abs/1707.02131},
  
  author = {Dey, Sounak and Dutta, Anjan and Toledo, J. Ignacio and Ghosh, Suman K. and Llados, Josep and Pal, Umapada},
  
  keywords = {Computer Vision and Pattern Recognition (cs.CV), FOS: Computer and information sciences, FOS: Computer and information sciences},
  
  title = {SigNet: Convolutional Siamese Network for Writer Independent Offline Signature Verification},
  
  publisher = {arXiv},
  
  year = {2017},
  
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

