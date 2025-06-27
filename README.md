# Telemetry Data Merge

This project loads telemetry data from two different formats (`data-1.json` and `data-2.json`) and merges them into a unified format as shown in `data-result.json`.

## Files

- `main.py`: Contains the merging logic and unit tests.
- `data-1.json`: Format 1 - device-wise grouped data with timestamps in milliseconds.
- `data-2.json`: Format 2 - flat list with ISO 8601 timestamps.
- `data-result.json`: Final target format.

## How to Run

```bash
python main.py
```

Make sure Python 3 is installed. All tests should pass if the solution is correct.