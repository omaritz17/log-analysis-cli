import re
from pathlib import Path
from typing import Generator

#Parses logs 

BASE_DIR = Path("/var/log")
TEST_BASE_LOG_FILE = Path.cwd().parent.parent / "logs" / "linux_sample.log"
print(f"Test Base Dir: {TEST_BASE_LOG_FILE}")


def log_parser(logfile: Path) -> Generator[dict[str,str | list [str]]] :
    log_file = BASE_DIR / logfile
    PID_PATTERN = r"\[([^\]]+)\]"
    print(f"LogFile: {log_file}")
    try:
        with open(log_file, "r") as f:
            for line in f:
                parsed_line = line.split()
                month = parsed_line[0]
                day = parsed_line[1]
                time = parsed_line[2]
                component = parsed_line[4].strip(':')
                pid = re.findall(PID_PATTERN, parsed_line[4])
                message = line.split("]:")[1]

                yield {
                    "Raw Line": line,
                    "Month": month,
                    "day": day,
                    "time": time,
                    "component": component,
                    "pid": pid,
                    "message" : message
                }
    except FileNotFoundError:
        print("File not found")

gen = log_parser(TEST_BASE_LOG_FILE)

print(f"Output: {next(gen)}")