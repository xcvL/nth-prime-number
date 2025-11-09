from prime_func import segmented_sieve_n
from typing import List
import json
import os
import pickle
import winsound

def _load_dafault(path: str) -> int:
    with open(path, "rb") as f:
        return pickle.load(f)[0]

def _save_dafault(path: str, data: List[int]) -> None:
    with open(path, "wb") as f:
        pickle.dump(data, f)

base_dir = os.path.dirname(os.path.abspath(__file__))
start_path = os.path.join(base_dir, "..", "default", "start.pkl")
start_key_path = os.path.join(base_dir, "..", "default", "start_key.pkl")
numbering_path = os.path.join(base_dir, "..", "default", "numbering.pkl")

count = 2000

for i in range(count):
    n = 5000
    start = _load_dafault(start_path)
    start_key = _load_dafault(start_key_path)
    numbering = _load_dafault(numbering_path)

    json_path = os.path.join(base_dir, "..", "prime_number_json", f"prime_numbers{numbering}.json")

    prime_numbers_list = list(segmented_sieve_n(start, n))
    prime_numbers = dict(zip(list(range(start_key, start_key + n)), prime_numbers_list))

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(prime_numbers, f, ensure_ascii=False, indent=2)

    _save_dafault(start_path, [prime_numbers_list[-1] + 1])
    _save_dafault(start_key_path, [start_key + n])
    _save_dafault(numbering_path, [numbering + 1])

winsound.Beep(2000, 1000) # End sound

# Current number of prime number data : 2000 * 5000 = 10_000_000