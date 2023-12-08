# ECE 469 Final Project Code
The only code in this project will convert a WAV audio file into a file that can be understood by a [Keysight waveform generator](https://rfmw.em.keysight.com/spdhelpfiles/33500/webhelp/us/content/_Programming%20Examples_/06%20-%20Configure%20an%20Arbitrary%20Waveform.htm).

## Prereqs
To use this project you must have Python 3 installed.
You will also need to install `scipy` using the following command:
```bash
pip install scipy
```

## Usage
To use this file, clone the repository and run the following command
```bash
python create_arb.py <wav filename>
```

This will output the new file to `stdout`. You can redirect this output stream to a file to save it a file.

## Configuration
You can also configure the following parameters in the Python file (the defaults are listed below as well)
```python
SAMPLE_RATE=44100
FILE_FORMAT="1.10"
HIGH_LEVEL=5
LOW_LEVEL=-5
CHANNEL='left'
```
