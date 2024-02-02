import subprocess
import datetime

filename = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".txt"

try:
    with open(filename, "a") as file:
        process = subprocess.Popen(["candump", "can0"], stdout=subprocess.PIPE, text=True)

        for line in process.stdout:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            line_with_timestamp = f"{line.strip()} {timestamp}"
            print(line_with_timestamp)
            file.write(line_with_timestamp + "\n")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    process.terminate()
    process.wait()
