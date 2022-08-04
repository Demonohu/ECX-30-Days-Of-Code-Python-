import os

def convert_to_lowercase_and_turn_space_to_underscore(folder_name):
    """
        Takes a string and converts it to lowercase and turns spaces into underscores.
        @param folder_name: string
        @return: string

        @example:
        convert_to_lowercase_and_turn_space_to_underscore('This is a test')
        returns 'this_is_a_test'
        convert_to_lowercase_and_turn_space_to_underscore('Day 22.py')
        returns 'day_22.py'
    """
    folder_name = folder_name.lower().replace(' ', '_')
    return folder_name

def rename_folder(folder_name):
    """
        Renames a folder by converting it to lowercase and turning spaces into underscores.
        @param folder_name: string
        @return: string -> new folder name
    """
    new_folder_name = convert_to_lowercase_and_turn_space_to_underscore(folder_name)
    os.rename(folder_name, new_folder_name)
    return new_folder_name

def rename_folders_in_directory(directory='.'):
    """
        Renames all folders in a directory.
        @param directory: string
        @return: None
    """
    for folder in os.listdir(directory):
        if os.path.isdir(folder):
            if folder.startswith('.'):
                print('Skipping hidden folder:', folder)
                continue
            rename_folder(folder)
            print(f'{folder} renamed to {folder}')
        else:
            print(f'{folder} is not a folder')
            continue

if __name__ == '__main__':
    rename_folders_in_directory()
