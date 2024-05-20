import os
import shutil
from PIL import Image
import matplotlib.pyplot as plt

def create_folders(main_folder, sub_folders):
    if not os.path.exists(main_folder):
        os.mkdir(main_folder)
    for sub_folder in sub_folders:
        path = os.path.join(main_folder, sub_folder)
        if not os.path.exists(path):
            os.mkdir(path)

def move_file(file_path, destination_folder):
    shutil.move(file_path, destination_folder)
    print(f"{os.path.basename(file_path)} moved to {destination_folder}")

def display_image(image_path):
    img = Image.open(image_path)
    plt.imshow(img)
    plt.axis('off')
    plt.show()

def main():
    downloads_folder = "downloads"
    if not os.path.exists(downloads_folder):
        print("Downloads folder does not exist.")
        return
    
    main_folder = input("Input nama main folder: ")
    sub_folders = []
    shortcuts = {}
    i = 1
    
    while True:
        sub_folder = input(f"Input nama sub-folder {i}: ")
        if sub_folder.lower() == 'q':
            break
        sub_folders.append(sub_folder)
        shortcuts[str(i)] = sub_folder
        i += 1
    
    create_folders(main_folder, sub_folders)
    
    undo_stack = []
    
    for filename in os.listdir(downloads_folder):
        file_path = os.path.join(downloads_folder, filename)
        if not os.path.isfile(file_path):
            continue
        
        display_image(file_path)
        print(f"Input shortcut number to move {filename} or 'p' to undo last move:")
        
        while True:
            choice = input().strip().lower()
            
            if choice in shortcuts:
                dest_folder = os.path.join(main_folder, shortcuts[choice])
                move_file(file_path, dest_folder)
                undo_stack.append((file_path, dest_folder))
                break
            elif choice == 'p' and undo_stack:
                last_move = undo_stack.pop()
                shutil.move(last_move[1], downloads_folder)
                print(f"{os.path.basename(last_move[1])} moved back to downloads folder")
                break
            else:
                print("Invalid choice. Try again.")
    
if __name__ == "__main__":
    main()
