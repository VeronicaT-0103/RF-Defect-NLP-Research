import time
import random

# List of "Hardware Events" our VNA and Microscope might detect
hardware_events = [
    "VNA detects VSWR of 3.1 at the input port",
    "Microscope shows a bridge between R1 and R2",
    "SMA connector torque is below 8 in-lbs",
    "Visual check shows a crack in the alumina substrate"
]

print("--- RF HARDWARE SIMULATOR STARTING ---")
print("Connecting to Keysight PNA-X...")
time.sleep(2) # Simulating hardware connection time

def generate_log():
    # Pick a random hardware event to simulate a real test
    event = random.choice(hardware_events)
    print(f"\n[HARDWARE ALERT]: {event}")
    return event

# This is where the hardware "talks" to your AI
current_log = generate_log()
print(f"Sending log to NLP Classifier...")