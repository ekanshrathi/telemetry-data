import json
import unittest
from datetime import datetime, timezone
import calendar

with open("data-1.json", "r") as f:
    jsonData1 = json.load(f)
with open("data-2.json", "r") as f:
    jsonData2 = json.load(f)
with open("data-result.json", "r") as f:
    jsonExpectedResult = json.load(f)

def convertFromFormat1(jsonObject):
    result = {"readings": []}
    for device, readings in jsonObject.items():
        for entry in readings:
            result["readings"].append({
                "device": device,
                "timestamp": entry["timestamp"],
                "value": entry["value"]
            })
    result["readings"].sort(key=lambda x: x["timestamp"])
    return result

def convertFromFormat2(jsonObject):
    result = {"readings": []}
    for entry in jsonObject:
        dt = datetime.strptime(entry["timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        timestamp_ms = calendar.timegm(dt.timetuple()) * 1000 + dt.microsecond // 1000
        result["readings"].append({
            "device": entry["device"],
            "timestamp": timestamp_ms,
            "value": entry["value"]
        })
    result["readings"].sort(key=lambda x: x["timestamp"])
    return result

def main(jsonObject):
    if isinstance(jsonObject, dict) and "device" not in jsonObject:
        return convertFromFormat1(jsonObject)
    return convertFromFormat2(jsonObject)

class TestSolution(unittest.TestCase):
    def test_dataType1(self):
        self.assertEqual(main(jsonData1), jsonExpectedResult)

    def test_dataType2(self):
        self.assertEqual(main(jsonData2), jsonExpectedResult)

if __name__ == '__main__':
    unittest.main()