import matplotlib.pyplot as figure

from Source.algorithms import *
from Source.utility import load_dataset
from Source.config import COLOR, K


def plot_dataset(data, labels):
    for i in range(K):
        figure.scatter(x=data[labels == i, 0], y=data[labels == i, 1], c=COLOR[i], s=20, edgecolors='k', label='Class ' + str(i))
    figure.xlabel('X')
    figure.ylabel('Y')
    figure.title('Dataset Clustering Result')

    figure.legend()
    figure.show()


def compare_clustering_algorithms(dataset_name, data, labels):

    print('Running Algorithms ...')
    nmi_kmeans = run_kmeans(data=data, labels=labels)
    nmi_hierarchical = run_hierarchical(data=data, labels=labels)
    nmi_ectkmeans, predicts = run_ectkmeans(data, labels)

    if len(data[0]) == 2:
        plot_dataset(data, predicts)

    print('\nResults for ' + dataset_name + ' :')
    print('NMI K-Means : ' + str(nmi_kmeans))
    print('NMI Hierarchical : ' + str(nmi_hierarchical))
    print('NMI ECT-KMeans : ' + str(nmi_ectkmeans))
    print('\n--------------------------------------\n')


def test_algorithms():
    resource = load_dataset()
    for dataset_name in resource:
        data = resource[dataset_name]['data']
        labels = resource[dataset_name]['labels']
        compare_clustering_algorithms(dataset_name, data, labels)


if __name__ == '__main__':
    test_algorithms()
