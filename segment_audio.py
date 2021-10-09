import argparse
from pyAudioAnalysis import audioBasicIO as aIO
from pyAudioAnalysis import audioSegmentation as aS
import scipy.io.wavfile as wavfile
import os

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
    segment.add_argument("-o", "--output", help="Output folder")
    return segment.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    input = args.input
    t = args.threshold
    s = args.smooth
    o = args.output

    # If folder doesn't exist, then create it.
    if not os.path.isdir(o):
        os.makedirs(o)
        print("Created output folder : ", o)

    else:
        print(o, "Output folder already exists.")

    fs, x = aIO.read_audio_file(input)
    segs = aS.silence_removal(x, fs, 0.04, 0.02, smooth_window=s,
                              weight=t, plot=True)
    for s in segs:
        print(s)
        name = os.path.join(o,
                            f'{os.path.basename(input).replace(".wav", "")}_{s[0]}_{s[1]}.wav')
        wavfile.write(name, fs,
                      x[int(fs * s[0]):int(fs * s[1])])
