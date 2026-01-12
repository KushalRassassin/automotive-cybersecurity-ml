import csv
import time

"""
Replay attack:
Re-Sending previously captured CAN messages
"""

def load_can_messages(csv_file):
    messages = []
    with open(csv_file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            messages.append(row)
        return messages

def replay_attack(messages, delay=0.02):
    print("Starting CAN replay attack...")
    for msg in messages:
        print(f"Replaying->ID:{msg['can_id']} | Data: {msg['data']} | Time: {time.time()}")
        time.sleep(delay)

def main():
    csv_file = "can_traffic.csv"
    messages = load_can_messages(csv_file)
    replay_attack(messages)

if __name__ == "__main__":
    main()