# python-crawler

*find_paper* is a script for paper searching. It will return the authors and title of paper containing certain keywords from any conferences (CS, EE related) and any years.

The arguments are keywords (e.g. *adc* and *"neural network"*), conference name (abbreviation, e.g. *nips* and *isscc*), and year (e.g. 2017).

The running environment is python 2.7.

Searching paper containing *binary* from NIPS 2017:
```
# python find_paper.py binary nips 2017
1
Xiaofan Lin, Cong Zhao, Wei Pan,
Towards Accurate Binary Convolutional Neural Network.

2
Bikash Joshi, Massih-Reza Amini, Ioannis Partalas, Franck Iutzeler, Yury Maximov,
Aggressive Sampling for Multi-class to Binary Reduction with Applications to Text Classification.
```

Searching paper containing *neural network* from ISSCC 2017:
```
# python find_paper.py "neural network" isscc 2017
1
Giuseppe Desoli, Nitin Chawla, Thomas Boesch, Surinder-pal Singh, Elio Guidetti, Fabio De Ambroggi, Tommaso Majo, Paolo Zambotti, Manuj Ayodhyawasi, Harvinder Singh, Nalin Aggarwal,
14.1 A 2.9TOPS/W deep convolutional neural network SoC in FD-SOI 28nm for intelligent embedded systems.

2
Dongjoo Shin, Jinmook Lee, Jinsu Lee, Hoi-Jun Yoo,
14.2 DNPU: An 8.1TOPS/W reconfigurable CNN-RNN processor for general-purpose deep neural networks.

3
Bert Moons, Roel Uytterhoeven, Wim Dehaene, Marian Verhelst,
14.5 Envision: A 0.26-to-10TOPS/W subword-parallel dynamic-voltage-accuracy-frequency-scalable Convolutional Neural Network processor in 28nm FDSOI.
```
