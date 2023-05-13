import os
import platform
import subprocess
from cat_factory import cat_fetcher


def main():
    print_header()
    folder = create_folder()
    download_cats(folder)
    display_cats(folder)


def print_header():
    print('-------------------------------------------')
    print('           CAT FACTORY APP                 ')
    print('-------------------------------------------')


def create_folder():
    base_folder = os.path.dirname(__file__)
    folder = 'cat_pics'
    full_path = os.path.abspath(os.path.join(base_folder, folder))

    # create a folder if it doesn't exist
    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print(f'Creating new directory at {full_path}')
        os.mkdir(full_path)
    return full_path


def download_cats(folder):
    while True:
        try:
            num_of_cats = int(input("How many cat pics do you want?: "))
            if num_of_cats <= 0:
                raise ValueError("Please enter a positive integer")
            break
        except ValueError as e:
            print("Error:", e)

    for i in range(1, num_of_cats+1):
        name = f'cat_pic {i}'
        print(f'Downloading cat {name}')
        cat_fetcher.get_cat(folder, name)


def display_cats(folder):
    print('Displaying cats')
    # determining os platform you're working on
    if platform.system() == 'Darwin':
        subprocess.call(['open', folder])
    elif platform.system() == 'Linux':
        subprocess.call(['xdg-open', folder])
    elif platform.system() == 'Windows':
        subprocess.call(['explorer', folder])
    else:
        print("Sorry!, we currently support only Windows, Linux and OS X.")


if __name__ == '__main__':
    main()
