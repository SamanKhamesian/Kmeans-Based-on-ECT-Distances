from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics.cluster import normalized_mutual_info_score as nmi
from Source import ectkmeans


def run_ectkmeans(data, labels):
    predicts = ectkmeans.fit(data)
    _nmi = nmi(labels, predicts, average_method='geometric')

    print('ECT-KMeans Algorithm Finished!')
    return _nmi, predicts


def run_kmeans(data, labels):
    predicts = KMeans().fit(X=data).labels_
    _nmi = nmi(labels, predicts, average_method='geometric')

    print('KMeans Algorithm Finished!')
    return _nmi


def run_hierarchical(data, labels):
    predicts = AgglomerativeClustering().fit(X=data).labels_
    _nmi = nmi(labels, predicts, average_method='geometric')

    print('Hierarchical Algorithm Finished!')
    return _nmi
