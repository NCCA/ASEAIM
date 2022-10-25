#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import PIL.Image
import scipy.cluster
import sklearn.cluster


def process_image(filename):
    image = PIL.Image.open(filename)
    data_array = np.asarray(image)
    shape = data_array.shape
    data_array = data_array.reshape(np.product(shape[:2]), shape[2]).astype(float)
    kmeans = sklearn.cluster.MiniBatchKMeans(
        n_clusters=10, init="k-means++", max_iter=20, random_state=1000
    ).fit(data_array)
    codes = kmeans.cluster_centers_
    vecs, _dist = scipy.cluster.vq.vq(data_array, codes)  # assign codes
    counts, _bins = np.histogram(vecs, len(codes))  # count occurrences

    colours = []
    for index in np.argsort(counts)[::-1]:
        colours.append(tuple([int(code) for code in codes[index]]))

    f, ax = plt.subplots(1, 2, figsize=(8, 8), constrained_layout=True)
    [axi.set_axis_off() for axi in ax.ravel()]
    image_from_file = plt.imread(filename)
    ax[0].imshow(image_from_file)
    ax[0].set_title(filename)
    ax[1].imshow([[(colours[0][0], colours[0][1], colours[0][2])]])
    ax[1].set_title(f"RGB({colours[0][0]} {colours[0][1]} {colours[0][2]})")
    plt.savefig(filename + ".out1.png")

    f, ax = plt.subplots(1, len(colours), figsize=(10, 10))
    index = 0
    for c in colours:
        ax[index].set_axis_off()
        ax[index].imshow([[(c[0], c[1], c[2])]])
        index += 1

    plt.savefig(filename + ".out.png")


if __name__ == "__main__":
    process_image("test.0000.png")
