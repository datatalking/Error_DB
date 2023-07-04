import os
import csv
from datetime import datetime


class ErrorDB:
    def __init__(self):
        self.db_path = os.path.join("data", "bug_database.csv")
        self.create_database()

    def create_database(self):
        """
        initializes the database by creating the necessary directory and CSV file if they don't exist
        :return:
        """
        if not os.path.exists("data"):
            os.makedirs("data")
        if not os.path.exists(self.db_path):
            with open(self.db_path, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Timestamp", "Error Message", "Source File", "Line Number"])

    def log_error(self, error_message, source_file, line_number):
        """
        appends a new row to the CSV file with the timestamp, error message, source file, and line number
        :param error_message:
        :param source_file:
        :param line_number:
        :return:
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.db_path, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, error_message, source_file, line_number])


# Example usage
if __name__ == "__main__":
    error_db = ErrorDB()
    try:
        # Code that might generate errors
        1 / 0
    except Exception as e:
        error_db.log_error(str(e), "script.py", 10)
