import sys
from preprocess import extract_failure_lines
from analyze import analyze_failure

def main():
    if len(sys.argv) < 2:
        file_path = ".\/sample_logs\/failure.log"
    else:
        file_path = sys.argv[1]

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            log = f.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return

    failures = extract_failure_lines(log)
    result = analyze_failure(failures)
    print("\n=== AI Analysis ===")
    print(result)

if __name__ == "__main__":
    main()