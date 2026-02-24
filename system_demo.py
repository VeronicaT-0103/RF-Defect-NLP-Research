import pandas as pd
import time
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# --- PART 1: THE AI BRAIN (Software) ---
print("--- INITIALIZING AI SYSTEM ---")
df = pd.read_csv('data/rf_logs.csv', encoding='utf-8-sig')
df.columns = df.columns.str.strip()

vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2))
X = vectorizer.fit_transform(df['Text (Technical Log / Inspection Note)'])
y = df['Label (Defect Category)']

model = LogisticRegression(class_weight='balanced')
model.fit(X, y)
print("AI Model Trained and Ready.")

# --- PART 2: THE HARDWARE INTERFACE (Simulation) ---
class RFTestBench:
    def __init__(self):
        self.equipment = "Keysight PNA-X VNA"
        
    def run_sweep(self):
        print(f"\n[HARDWARE]: Connecting to {self.equipment}...")
        time.sleep(1)
        print("[HARDWARE]: Running 10MHz to 20GHz Sweep...")
        time.sleep(2)
        # This is the "Simulated" signal failure
        return "Return loss exceeds 10dB at 12.5GHz"

# --- PART 3: THE INTEGRATED SYSTEM DEMO ---
print("\n=== STARTING INTEGRATED RF-AI DEMO ===")
bench = RFTestBench()

# 1. Hardware generates data
captured_log = bench.run_sweep()
print(f"[SYSTEM]: Data Received: '{captured_log}'")

# 2. Software analyzes data
print("[SYSTEM]: Analyzing with NLP Model...")
time.sleep(1)
prediction = model.predict(vectorizer.transform([captured_log]))

# 3. Final Result
print(f"\n[FINAL DIAGNOSIS]: {prediction[0]}")
print("========================================")