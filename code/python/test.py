from feature_extraction import feature_core
import numpy a np

def test():
    a = np.arange(0, 10).reshape((10, 1))
    print(feature_core.sequence_feature(a, 0, 4))  # without window
    print(feature_core.sequence_feature(a, 5, 4))  # with window
    # example output:
    # [4.5         4.5         2.87228132  0.          9.          0.          9.
    #  9.          0.          2.66666667  1.55555556  1.24721913 - 1.14074074
    #  - 1.14074074  3.          2.          1.41421356  0. - 1.3]
    # [[2.          2.          1.41421356  0.          4.          0.          4.
    #   4.          0.          0.66666667  0.22222222  0.47140452 - 0.07407407
    #   - 0.07407407  1.5         0.25        0.5         0. - 2.]
    #  [6.          6.          1.41421356  4.          8.          4.          5.
    #  4.          4.          0.54545455  0.24793388  0.4979296 - 0.02253944
    #  - 0.02253944  5.5         0.25        0.5         0. - 2.]]

if __name == '__main__':
	test()