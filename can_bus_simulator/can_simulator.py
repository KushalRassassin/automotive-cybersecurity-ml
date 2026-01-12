import csv
import random
import time

#Basic CAN message structure
class CANMessage:
  def __init__(self, can_id, data, timestamp):
    self.can_id = can_id
    self.data = data
    self.timestamp = timestamp

  def to_row(self):
    return [self.timestamp, hex(self.can_id), self.data]

def generate_can_message():
  """
  Generate a normal CAN message
  """
  can_id = random.randint(0x100,0x1FF) #typical ECU range
  data = [random.randint(0, 255) for _ in range(8)]
  timestamp = time.time()
  return CANMessage(can_id, data, timestamp)

def main():
  messages = []

  for _ in range(20):
    msg = generate_can_message()
    messages.append(msg)
    time.sleep(0.05)\

  with open("can_traffic.csv", "w", newline = "") as f;
    writer = csv.writer(f)
    writer.writerow(["timestamp", "can_id", "data"])
    for msg in messages:
      writer.writerow(ms.to_row())


  print("Generated normal CAN traffic and saved to can_traffic.csv)

if __name__= "__main__"
  main()
