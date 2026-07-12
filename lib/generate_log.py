from datetime import datetime
import os


def generate_log(data):
    """
    Writes a list of log entries to a text file with today's date.

    Args:
        data (list): List of log entries.

    Returns:
        str: The name of the generated log file.

    Raises:
        ValueError: If data is not a list.
    """

    # STEP 1: Validate input
    if not isinstance(data, list):
        raise ValueError("Input must be a list.")

    # STEP 2: Generate filename
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # STEP 3: Write log entries to the file
    with open(filename, "w", encoding="utf-8") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # STEP 4: Print confirmation
    print(f"Log written to {filename}")

    # Return filename for testing
    return filename


if __name__ == "__main__":
    sample_logs = [
        "User logged in",
        "User updated profile",
        "Report exported"
    ]

    generate_log(sample_logs)