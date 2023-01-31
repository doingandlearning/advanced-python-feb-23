import os

results = dict()


def search_directory(directory_name):
    print("Begun search of " + directory_name)
    paths = []
    for dir, subdirs, files in os.walk(directory_name):
        paths.append(dir)
        for file in files:
            paths.append(os.path.join(dir, file))
    results[directory_name] = paths
    print("ENDED SEARCH OF " + directory_name)


def ask_user_for_directory_names():
    directory_names = []
    while True:
        directory_name = input("Enter a directory name (or 'done'): ").lower()
        if directory_name == "done":
            break
        elif directory_name in directory_names:
            print("Directory already specified!")
        elif not os.path.isdir(directory_name):
            print("Directory does not exist!")
        else:
            directory_names.append(directory_name)
    return directory_names


def start_all_searches(directory_names):
    for directory_name in directory_names:
        search_directory(directory_name)


def list_searches():
    print("Here is a list of all directories searched:")
    for directoryName in results:
        print("  " + directoryName)


def show_search_result():
    directory_name = input("Enter a directory name: ")
    paths = results.get(directory_name.lower())
    if paths is None:
        print("No search results available for " + directory_name)
    else:
        print("Entries in directory " + directory_name)
        for path in paths:
            print(("  [D] " if os.path.isdir(path) else "  [F] ") + path)


def display_results():
    while True:
        option = input("""
Choose an option from the menu:
1. List directories searched
2. Show search results
3. Exit
==> """)
        if option == "1":
            list_searches()
        elif option == "2":
            show_search_result()
        elif option == "3":
            break
    print("Goodbye!")


def main():
    directory_names = ask_user_for_directory_names()
    tasks = start_all_searches(directory_names)
    display_results()


if __name__ == "__main__":
    main()
