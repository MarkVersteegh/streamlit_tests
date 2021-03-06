from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import streamlit as st
import random

def write():
    # Magic commands
    col1, col2 = st.beta_columns([1,2])

    # Cached function that returns a mutable object with a random number in the range 0-100
    @st.cache(allow_output_mutation=True)
    def seed():
        return {'seed': random.randint(0, 100)} # Mutable (dict)

    # Random state for points generation randomly selected by calling the cached function seed()
    # In this way the points distribution generated by make_blobs is conserved when app is rerun
    random_state = seed()

    # Button to reset points by mutating the cached dict value
    if col1.button('Reset points', key='123'):
        random_state['seed'] = random.randint(0, 100) # Mutated cached value

    # Showing the current random_state
    #col1.write('Seed = ', random_state['seed'])
    col1.markdown('Random seed = ' + str(random_state['seed']))

    # Slider to select the standard deviation of clusters generated by make_blobs generator
    cluster_std = col1.slider('Dispersion', 0.2, 3.0, 0.2, 0.2)

    # Points generator
    N=col1.slider(label='Actual number of clusters',min_value=1,max_value=10,step=1,value=3)
    x, _ = make_blobs(n_samples=200, n_features=2, centers=N, cluster_std=cluster_std, shuffle=True, random_state=random_state['seed'])

    # Dropdown list to select number of clusters
    n_clusters = col1.selectbox('Number of clusters', range(1, 10))

    # k-means algorithm 
    kmeans = KMeans(n_clusters=n_clusters, init='random', n_init=10, max_iter=300, random_state=111)
    y_kmeans = kmeans.fit_predict(x)

    # Plotting colored clusters 
    fig, ax = plt.subplots(figsize=(12,8))
    plt.scatter(x[:, 0], x[:, 1], s=100, c=kmeans.labels_, cmap='Set1')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=400, marker='*', color='k')
    col2.pyplot(fig)

    col2.write("""
    **NOTES**:
    - The number of point centers generated is set to 3 by default and can be set by the slider
    - The clusters found by the k-means algorithm are identified by colors
    - The stars indicate the centroids of the clusters
    - Code available in this github [repo](https://github.com/arielcedola/kmeans)
    """)


if __name__=='__main__':
    write()
