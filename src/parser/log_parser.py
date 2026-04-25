from pathlib import Path
#Parses logs 

BASE_DIR = Path("/var/log")


def log_parser(logfile: str):
    log_file = BASE_DIR / logfile
    print(f"LogFile: {log_file}")
    try:
        with open(log_file, "r") as f:
            for line in f:
                parsed = line.split()
                yield parsed
    except FileNotFoundError:
        print("File not found")

gen = log_parser("system.log")

print(f"Output: {next(gen)}")