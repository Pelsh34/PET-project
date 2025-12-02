import os
import shutil

def sort_files_by_format(directory_path):
    """
    Сортируем файлы в директории в подпапки по их формату:

    Sorts files in a given directory into subdirectories based on their format.

    Args:
    
        directory_path (str): The path to the directory containing the files to sort.
    """

    file_types = {
        "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv"],
        "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
        "Pictures": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
        "Text": [".txt", ".pdf", ".doc", ".docx", ".rtf"],
        "Others": [] # For files that don't match any of the above categories
    }

    if not os.path.isdir(directory_path):
        print(f"Error: Directory '{directory_path}' does not exist.")
        return

    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()
            moved = False

            for folder_name, extensions in file_types.items():
                if file_extension in extensions:
                    destination_folder = os.path.join(directory_path, folder_name)
                    os.makedirs(destination_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(destination_folder, filename))
                    print(f"Moved '{filename}' to '{folder_name}'")
                    moved = True
                    break
            
            if not moved:
                destination_folder = os.path.join(directory_path, "Others")
                os.makedirs(destination_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(destination_folder, filename))
                print(f"Moved '{filename}' to 'Others'")


if __name__ == "__main__":
    target_directory = input("Введите путь к папке, файлы в которой необходимо сортировать по форматам \n (Enter the path of the directory to sort): ")
    sort_files_by_format(target_directory)
    print("Сортировка файлов окончена (File sorting complete)")