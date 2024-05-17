---
title: "Rethinking pooling in graph neural networks"
date: 2020-10-20
externalUrl: "https://proceedings.neurips.cc/paper/2020/hash/1764183ef03fc7324eb58c3842bd9a57-Abstract.html"
authors: ["Diego Mesquita", "Amauri Souza", "Samuel Kaski"]
---

Graph pooling is a central component of a myriad of graph neural network (GNN) architectures. As an inheritance from traditional CNNs, most approaches formulate graph pooling as a cluster assignment problem, extending the idea of local patches in regular grids to graphs. Despite the wide adherence to this design choice, no work has rigorously evaluated its influence on the success of GNNs. In this paper, we build upon representative GNNs and introduce variants that challenge the need for locality-preserving representations, either using randomization or clustering on the complement graph. Strikingly, our experiments demonstrate that using these variants does not result in any decrease in performance. To understand this phenomenon, we study the interplay between convolutional layers and the subsequent pooling ones. We show that the convolutions play a leading role in the learned representations. In contrast to the common belief, local pooling is not responsible for the success of GNNs on relevant and widely-used benchmarks.
