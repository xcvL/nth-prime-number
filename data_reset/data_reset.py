import os
import pickle
import winsound

def _reset_default(path):
    with open(path, "wb") as f:
        pickle.dump([1], f)

def _remove_file_in_folder(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

base_dir = os.path.dirname(os.path.abspath(__file__))
start_path = os.path.join(base_dir, "..", "default", "start.pkl")
start_key_path = os.path.join(base_dir, "..", "default", "start_key.pkl")
numbering_path = os.path.join(base_dir, "..", "default", "numbering.pkl")
json_path = os.path.join(base_dir, "..", "prime_number_json")

_reset_default(start_path)
_reset_default(start_key_path)
_reset_default(numbering_path)
_remove_file_in_folder(json_path)

winsound.Beep(2000, 1000) # End Sound