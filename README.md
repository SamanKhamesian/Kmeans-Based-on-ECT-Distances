# Kmeans-Based-on-ECT-Distances

### Abstract
[This work](https://perso.uclouvain.be/michel.verleysen/papers/esann05ly.pdf) proposes a simple way to improve a clustering algorithm. The idea is to exploit a new distance metric called the "Euclidian Commute Time" (ECT) distance, based on a random walk model on a graph derived from the data. Using this distance measure instead of the usual Euclidean distance in a k-means algorithm allows to retrieve well separated clusters of arbitrary shape, without working hypothesis about their data distribution. Experimental results show that the use of this new distance measure significantly improves the quality of the clustering on the tested data sets. This project is an implementation of this technique.

#### To use this work on your researches or projects you need:
* Python 3.7.0
* Python packages:
	* pykov
	* pandas
	* networkx
	* matplotlib
	* numpy
	* scikit_learn
	* seaborn
	* cmake

#

#### To install Python:
_First, check if you already have it installed or not_.
~~~~
python3 --version
~~~~
_If you don't have python 3 in your computer you can use the code below_:
~~~~
sudo apt-get update
sudo apt-get install python3
~~~~
#

#### To install packages via pip install:
~~~~
sudo pip3 install pandas networkx matplotlib numpy scikit_learn seaborn cmake
sudo pip3 install git+git://github.com/riccardoscalco/Pykov@master
~~~~
_If you haven't installed pip, you can use the codes below in your terminal_:
~~~~
sudo apt-get update
sudo apt install python3-pip
~~~~
_You should check and update your pip_:
~~~~
pip3 install --upgrade pip
~~~~
#
