import journal


def main():
    print_header()
    run_event_loop()


def print_header():
    print("--------------------------------------")
    print("        PERSONAL JOURNAL APP          ")
    print("--------------------------------------")


def clear_entries(journal_name):
    journal.clear_file(journal_name)


def run_event_loop():
    print("What do you want to do? ")
    cmd = "not_blank"
    journal_name = "default"
    journal_data = journal.load(journal_name)

    while cmd != 'x' and cmd:
        cmd = input("[L]list, [A]dd, E[x]it or [C]lear? ")
        cmd = cmd.lower().strip()
        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entries(journal_data)
        elif cmd == 'c':
            clear_entries(journal_name)
            journal_data = journal.load(journal_name)
        elif cmd != 'x' and cmd:
            print(f"Sorry, we didn't understand {cmd}")

    print("Done, Goodbye")
    journal.save(journal_name, journal_data)


def list_entries(journal_data):
    print(f"Your {len(journal_data)} entries")
    journal_data = reversed(journal_data)
    for idx, item in enumerate(journal_data):
        print(f"{idx+1}. {item}")


def add_entries(journal_data):
    entry = input("Enter your journal entry: ")
    journal.add_entry(entry, journal_data)


if __name__ == "__main__":
    main()
