import sys

def parse_log_line(line: str) -> dict:
    parts = line.strip().split(" ", 3)
    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2].upper(),
        "message": parts[3]
    }

def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, 'r', encoding ='utf-8') as file:
            for line in file:
                print(f"Reading: {repr(line)}")
                if line.strip():
                    try:
                        log_entry = parse_log_line(line)
                        print(f"Parsed: {log_entry}")
                        logs.append(log_entry)
                    except Exception as e:
                        print(f"Failed to parse line: {line.strip()} | Error:{e}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
        return []
    return logs
    
def filter_logs_by_level(logs: list, level: str) -> list:
    level = level.upper()
    return [log for log in logs if log["level"] == level]

def count_logs_by_level(logs: list) -> dict:
    all_levels = ['DEBUG', 'ERROR', 'INFO', 'WARNING']
    counts = {level: 0 for level in all_levels}
    for log in logs:
        lvl = log["level"]
        if lvl in counts:
            counts[lvl]+=1
    return counts

def display_log_counts(counts: dict) -> None:
    print("Рівень логування|Кількість")
    print("----------------|-----------")
    for level in ["INFO", "DEBUG", "ERROR", "WARNING"]:
        print(f"{level < 16} | {counts.get(level, 0)}")

def display_filtered_logs(logs: list, level: str) -> None:
    if not logs:
        print(f"\nNo logs found for level '{level.upper()}'.")
        return
    print(f"\nДеталі логів для рівня '{level.upper()}':")
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")
                     
def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_logfile> [log_level]")
        sys.exit(1)

    file_path = sys.argv[1]
    filter_level = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path)
    if not logs:
        print("No valid log entries found.")
        return

    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if filter_level:
        filtered = filter_logs_by_level(logs, filter_level)
        display_filtered_logs(filtered, filter_level)

if __name__ == "__main__":
    main()