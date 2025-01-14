# See "Writing benchmarks" in the asv docs for more information.
# https://asv.readthedocs.io/en/latest/writing_benchmarks.html
import numpy as np
from scipy import ndimage as ndi
from skimage import color, data, feature, util


class FeatureSuite:
    """Benchmark for feature routines in scikit-image."""
    def setup(self):
        # Use a real-world image for more realistic features, but tile it to
        # get a larger size for the benchmark.
        self.image = np.tile(color.rgb2gray(data.astronaut()), (4, 4))
        self.image_ubyte = util.img_as_ubyte(self.image)

    def time_canny(self):
        result = feature.canny(self.image)

    def time_glcm(self):
        pi = np.pi
        result = feature.greycomatrix(self.image_ubyte, distances=[1, 2],
                                      angles=[0, pi/4, pi/2, 3*pi/4])
