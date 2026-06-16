import re
import os


def extract_emails(input_file, output_file="extracted_emails.txt"):
    if not os.path.exists(input_file):
        print(f"Error: '{input_file}' not found.")
        return

    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, content)

    unique_emails = sorted(set(emails))

    if not unique_emails:
        print("No email addresses found.")
        return

    with open(output_file, "w", encoding="utf-8") as f:
        for email in unique_emails:
            f.write(email + "\n")

    print(f"Found {len(unique_emails)} unique email(s).")
    print(f"Saved to '{output_file}'.")


if __name__ == "__main__":
    input_path = input("Enter path to the .txt file to scan: ").strip()
    extract_emails(input_path)
