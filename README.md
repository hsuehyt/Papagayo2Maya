# Papagayo2Maya

Map and set lip-sync keyframes from Papagayo to Advanced Skeleton Facial Rigging in Maya.

## Introduction

This script sets keyframes for viseme controller in Autodesk Maya based on phoneme data exported from Papagayo. The viseme controller is part of facial rigging by Advanced Skeleton.

## Usage

1. Place the `phoneme_keyframe_setter.py` script in your Maya scripts directory or a directory of your choice.
2. Update the `file_path` variable in the script to point to your `.dat` file containing the phoneme data.
3. Update the `phoneme_to_attr` dictionary to map your phonemes to the corresponding controller attributes in your Maya scene.
4. Run the script in Maya's script editor or as a Python script.

### Example Phoneme Data File Format

The `.dat` file should contain lines with start times and phonemes. Example format:

- MohoSwitch1
- 1 rest
- 19 E
- 20 O
- 21 MBP
- 22 WQ

## Installation

Clone this repository to your local machine using the following command: `git clone https://github.com/hsuehyt/Papagayo2Maya.git`

## Links

- [Papagayo](https://www.lostmarble.com/papagayo/)
- [Advanced Skeleton](https://www.animationstudios.com.au/advanced-skeleton)

## License

This project is licensed under the MIT License.
