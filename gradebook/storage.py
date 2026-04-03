import json
import os
import logging

DATA_FILE = "data/gradebook.json"

os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            logging.info("Data loaded successfully")
            return data

    except FileNotFoundError:
        logging.info("File not found. Starting with empty data.")
        return {
            "students": [],
            "courses": [],
            "enrollments": []
        }

    except json.JSONDecodeError:
        logging.error("JSON file is corrupted.")
        print("Warning: Data file is corrupted. Starting fresh.")
        return {
            "students": [],
            "courses": [],
            "enrollments": []
        }


def save_data(data):
    try:
        os.makedirs("data", exist_ok=True)

        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)

        logging.info("Data saved successfully")

    except Exception as e:
        logging.error(f"Error saving data: {e}")
        print("Error saving data:", e)