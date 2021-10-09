import argparse
from pyAudioAnalysis import audioBasicIO as aIO
from pyAudioAnalysis import audioSegmentation as aS


def parse_arguments():
    segment = argparse.ArgumentParser(description="Audio segment")
    segment.add_argument("-s", "--smooth", type=float, default=0.1,
                         help="Probability smoothing window: the higher"
                              "this param is, the more difficult is to "
                              "detect small changes in the signal. "),
    segment.add_argument("-t", "--threshold", default=0.5, type=float,
                         help="Thresholding weight. The higher this value is"
                              "the fewer the segments that survive in the "
                              "final segmentation")
    segment.add_argument("-i", "--input", help="Input WAV file")
    return segment.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    input = args.input
    t = args.threshold
    s = args.smooth
    fs, x = aIO.read_audio_file(input)
    segs = aS.silence_removal(x, fs, 0.04, 0.02, smooth_window=s,
                              weight=t, plot=True)
    for s in segs:
        print(s)
