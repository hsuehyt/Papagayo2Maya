import maya.cmds as cmds

# Path to the .dat file (update this path as needed)
file_path = 'path/to/your/dat/file.dat'

# Mapping phonemes to controller attributes
phoneme_to_attr = {
    'aaa': 'ctrlPhonemes_M.aaa',
    'eh': 'ctrlPhonemes_M.eh',
    'ahh': 'ctrlPhonemes_M.ahh',
    'ohh': 'ctrlPhonemes_M.ohh',
    'uuu': 'ctrlPhonemes_M.uuu',
    'iee': 'ctrlPhonemes_M.iee',
    'rrr': 'ctrlPhonemes_M.rrr',
    'www': 'ctrlPhonemes_M.www',
    'sss': 'ctrlPhonemes_M.sss',
    'fff': 'ctrlPhonemes_M.fff',
    'tth': 'ctrlPhonemes_M.tth',
    'mbp': 'ctrlPhonemes_M.mbp',
    'ssh': 'ctrlPhonemes_M.ssh',
    'schwa': 'ctrlPhonemes_M.schwa',
    'gk': 'ctrlPhonemes_M.gk',
    'lntd': 'ctrlPhonemes_M.lntd'
}

# Function to set keyframe values
def set_keyframe_values(start, end, phoneme):
    attr = phoneme_to_attr.get(phoneme.lower(), None)
    if attr:
        cmds.setKeyframe(attr, time=start, value=10)
        cmds.setKeyframe(attr, time=end, value=0)

def process_phoneme_file(file_path):
    """
    Processes the phoneme data file and sets keyframes accordingly.
    
    :param file_path: Path to the .dat file containing phoneme data
    """
    # Read and process the .dat file
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Initialize all controller attributes to 0 at the beginning
    for attr in phoneme_to_attr.values():
        cmds.setKeyframe(attr, time=0, value=0)
    
    # Process each phoneme and set the corresponding attribute values
    for i in range(1, len(lines) - 1):  # Start from 1 to skip header and go to len(lines) - 1 to avoid index out of range
        current_line = lines[i].strip().split()
        next_line = lines[i + 1].strip().split()
    
        # Ensure the line contains exactly two elements
        if len(current_line) == 2 and len(next_line) > 0:
            start = float(current_line[0])
            phoneme = current_line[1]
            end = float(next_line[0])
            
            # Set all other attributes to 0 at the start frame
            for attr in phoneme_to_attr.values():
                if attr != phoneme_to_attr.get(phoneme.lower(), None):
                    cmds.setKeyframe(attr, time=start, value=0)
            
            # Set the current phoneme attribute to 10
            set_keyframe_values(start, end, phoneme)
    
    print("Keyframes have been set.")

# Run the script with the specified file path
process_phoneme_file(file_path)
