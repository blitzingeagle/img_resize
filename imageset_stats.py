from __future__ import print_function

import numpy as np
import cv2

import os.path as path
from glob import glob


def image_paths(directory):
    return sorted(glob(path.join(directory, "*")))


def load_images(filepaths):
    return [cv2.imread(filepath) for filepath in filepaths]


if __name__ == "__main__":
    directory = "images"
    paths = image_paths(directory)
    N = len(paths)
    print(N, "images found.")

    images = load_images(paths)
    print(images.shape)
