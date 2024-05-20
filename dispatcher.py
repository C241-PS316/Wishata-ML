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
    print("{} moved to {}".format(os.path.basename(file_path), destination_folder))

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
        sub_folder = input("Input nama sub-folder {}: ".format(i)) 
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
        print("Input shortcut number to move {} or 'p' to undo last move or 'l' to skip:".format(filename))

        while True:
            choice = input().strip().lower()
            
            if choice in shortcuts:
                dest_folder = os.path.join(main_folder, shortcuts[choice])
                move_file(file_path, dest_folder)
                undo_stack.append((os.path.join(dest_folder, filename), downloads_folder))
                break
            elif choice == 'p' and undo_stack:
                last_move = undo_stack.pop()
                shutil.move(last_move[0], last_move[1])
                print("{} moved back to downloads folder".format(os.path.basename(last_move[0])))
                break
            elif choice == 'l':
                print("Skipped {}".format(filename))
                break
            else:
                print("Invalid choice. Try again.")
    
if __name__ == "__main__":
    main()
