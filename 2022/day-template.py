import re
import json
import math
import random
import operator

# Load sample data
sample_1 = """
sample_input_goes_here
"""
sample_2 = """
sample_input_goes_here
"""
sinput_1 = sample_1.strip()
sinput_2 = sample_2.strip()

# Load input file
input = open("inputs/day-01.txt", 'r').read().strip()

print(f"{' Start Pt I ':#^60}")
print(f"{' Wrong Answers Only ':-^60}")
wrong_answers_only = {
    "too high":  []
    , "too low": []
    , "other":   []
}
print(json.dumps(wrong_answers_only, sort_keys=False, indent=4))
print(f"{' End Pt I ':=^60}\n")

print(f"{' Start Pt II ':#^60}")
print(f"{' Wrong Answers Only ':-^60}")
wrong_answers_only = {
    "too high":  []
    , "too low": []
    , "other":   []
}
print(json.dumps(wrong_answers_only, sort_keys=False, indent=4))
print(f"{' End Pt II ':=^60}\n")
