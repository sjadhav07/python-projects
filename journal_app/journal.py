"""
This is journal module.
"""
import os


def load(name):
    """
    This method creates and loads new journal

    :param name: Base name of journal to load
    :return: New journal data structure populated with file data
    """
    data = []
    filename = get_filepath(name)

    if os.path.exists(filename):
        with open(filename) as f:
            for entry in f.readlines():
                data.append(entry.rstrip())

    return data


def save(name, data):
    print(f'..... saving to: {name}')
    filename = get_filepath(name)

    with open(filename, 'w') as f:
        for entry in data:
            f.write(entry+"\n")


def get_filepath(name):
    return os.path.abspath(os.path.join('.', 'journals', name + '.jrl'))


def add_entry(entry, journal_list):
    journal_list.append(entry)


def clear_file(name):
    filename = get_filepath(name)
    open(filename, "w").close()
