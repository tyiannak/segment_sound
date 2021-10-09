import argparse
from pyAudioAnalysis import audioBasicIO as aIO
from pyAudioAnalysis import audioSegmentation as aS


def parse_arguments():
    segment = argparse.ArgumentParser(description="Audio segment")
#    record_analyze.add_argument("-w", "--win_size",
#                                  type=float, choices=[0.25, 0.5, 0.75, 1, 2],
#                                  default=1, help="Recording block size")
#    record_analyze.add_argument("-fs", "--samplingrate", type=int,
#                                  choices=[4000, 8000, 16000, 32000, 44100],
#                                  default=8000, help="Recording block size")
#    record_analyze.add_argument("--chromagram", action="store_true",
#                                  help="Show chromagram")
    segment.add_argument("-i", "--input", help="Input WAV file")
    return segment.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    input = args.input
    fs, x = aIO.read_audio_file(input)
    segs = aS.silence_removal(x, fs, 0.05, 0.01, smooth_window=0.1,
                              weight=0.02, plot=True)
    for s in segs:
        print(s)
