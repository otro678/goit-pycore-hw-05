import sys

def parse_log_line(line: str) -> dict:
    parts = line.split(' ', 3)
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': parts[3]
    }

def read_log(file_path: str) -> list:
    records = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                records.append(parse_log_line(line.strip()))
    except FileNotFoundError:
        print(f"Файл не знайдено: {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Невідома помилка при читанні файлу: {e}")
        sys.exit(1)
    return records

def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda log: log['level'] == level, logs))

def count_logs_by_level(logs: list) -> dict:
    counts = {}
    for log in logs:
        level = log['level']
        if level in counts:
            counts[level] += 1
        else:
            counts[level] = 1
    return counts

def display_log_counts(counts: dict):
    print("Тип логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")


if len(sys.argv) < 2:
    print("Використання: python main.py /шлях/до/файла.log [level]")
    sys.exit(1)

log_file_path = sys.argv[1]
logs = read_log(log_file_path)
counts = count_logs_by_level(logs)

display_log_counts(counts)

if len(sys.argv) > 2:
    level = sys.argv[2].upper()
    filtered_logs = filter_logs_by_level(logs, level)
    if filtered_logs:
        print(f"\nЛоги для рівня '{level}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")
    else:
        print(f"\nНемає записів рівня '{level}'.")