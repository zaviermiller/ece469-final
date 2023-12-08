import sys
from typing import Literal, Union, List
import scipy.io.wavfile as wavfile

SAMPLE_RATE=44100
FILE_FORMAT="1.10"
HIGH_LEVEL=5
LOW_LEVEL=-5
CHANNEL='left'

class ArbFile:
    def __init__(self, sample_rate: int, file_format: str, high_level: int, low_level: int, channel: Union[Literal["left"], Literal["right"]], data: List[int]):
        self.sample_rate = sample_rate
        self.file_format = file_format
        self.high_level = high_level
        self.low_level = low_level
        self.channel_count = 2 if channel == 'both' else 1
        self.data = data
    def print(self) -> None:
        print(f"File Format:{self.file_format}")
        print(f"Channel Count:{self.channel_count}")
        print("Sample Rate %.6f" % float(self.sample_rate))
        print("High Level: %.6f" % float(self.high_level))
        print("Low Level: %.6f" % float(self.low_level))
        print(f"Data Points:{len(self.data)}")
        print("Data:")
        [print(row) for row in self.data]


def stereo_to_mono(data):
    return [row[0 if CHANNEL == "left" else 1] for row in data]

def normalize(data):
    d_max = max([abs(d) for d in data])
    return [row / d_max for row in data]

def create_arb_from_wav(wav_filename) -> ArbFile:
    (sample_rate, data) = wavfile.read(wav_filename)

    # check if file contains two channels, and convert to one channel if so
    if isinstance(data[0], list):
        data = stereo_to_mono(data)

    # get data between -32767 and 32767
    data = normalize(data)
    data = [int(row * 32767) for row in data]

    return ArbFile(sample_rate, FILE_FORMAT, HIGH_LEVEL, LOW_LEVEL, CHANNEL, data)


def graph_waveform(data) -> None:

    # use matplot lib to graph the wav file
    import matplotlib.pyplot as plt
    plt.plot(data)
    plt.show()


def main():
    if len(sys.argv) < 2:
        print("Usage: python create_arb.py <csv filename>")
        sys.exit(1)
    elif not sys.argv[1].endswith(".wav"):
        print("Usage: python create_arb.py <csv filename>")
        sys.exit(1)
    arb = create_arb_from_wav(sys.argv[1])
    arb.print()
    # graph_wav_file(sys.argv[1])


main()
