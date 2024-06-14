import os
import shutil
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import simpledialog, messagebox

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

def delete_file(file_path):
    os.remove(file_path)
    print("{} deleted".format(os.path.basename(file_path)))

class ImageMoverApp:
    def __init__(self, root, main_folder, sub_folders):
        self.root = root
        self.main_folder = main_folder
        self.sub_folders = sub_folders
        self.shortcuts = {str(i+1): sub_folder for i, sub_folder in enumerate(sub_folders)}
        self.undo_stack = []
        self.downloads_folder = "downloads"
        self.current_file = None
        self.files = [f for f in os.listdir(self.downloads_folder) if os.path.isfile(os.path.join(self.downloads_folder, f))]

        self.label = tk.Label(root)
        self.label.pack()
        
        self.button_frame = tk.Frame(root)
        self.button_frame.pack()
        
        self.create_buttons()
        self.bind_keys()

        self.next_image()

    def create_buttons(self):
        for key, sub_folder in self.shortcuts.items():
            button = tk.Button(self.button_frame, text=f"{key} - {sub_folder}", command=lambda k=key: self.move_image(k))
            button.pack(side=tk.LEFT)
        
        undo_button = tk.Button(self.button_frame, text="Undo", command=self.undo_last_move)
        undo_button.pack(side=tk.LEFT)
        
        delete_button = tk.Button(self.button_frame, text="Delete", command=self.delete_image)
        delete_button.pack(side=tk.LEFT)

    def bind_keys(self):
        for key in self.shortcuts.keys():
            self.root.bind(key, self.key_move_image)
        
        self.root.bind('u', self.key_undo_last_move)
        self.root.bind('d', self.key_delete_image)

    def key_move_image(self, event):
        self.move_image(event.char)

    def key_undo_last_move(self, event):
        self.undo_last_move()

    def key_delete_image(self, event):
        self.delete_image()

    def next_image(self):
        self.label.config(image='')
        if self.files:
            self.current_file = os.path.join(self.downloads_folder, self.files.pop(0))
            img = Image.open(self.current_file)
            img.thumbnail((400, 400))
            self.img = ImageTk.PhotoImage(img)
            self.label.config(image=self.img)
        else:
            messagebox.showinfo("Info", "No more images in the downloads folder.")
            self.root.quit()

    def delete_image(self):
        if self.current_file:
            delete_file(self.current_file)
            self.next_image()

    def move_image(self, shortcut):
        if self.current_file and shortcut in self.shortcuts:
            dest_folder = os.path.join(self.main_folder, self.shortcuts[shortcut])
            move_file(self.current_file, dest_folder)
            self.undo_stack.append((os.path.join(dest_folder, os.path.basename(self.current_file)), self.downloads_folder))
            self.next_image()

    def undo_last_move(self):
        if self.undo_stack:
            last_move = self.undo_stack.pop()
            shutil.move(last_move[0], last_move[1])
            self.files.insert(0, os.path.basename(last_move[0]))  # Reinsert file at the beginning of the list
            self.next_image()
        else:
            print("Nothing to undo")

def main():
    downloads_folder = "downloads"
    if not os.path.exists(downloads_folder):
        print("Downloads folder does not exist.")
        return
    
    main_folder = input("Input nama main folder: ")
    sub_folders = []
    i = 1
    
    while True:
        sub_folder = input("Input nama sub-folder {}: ".format(i)) 
        if sub_folder.lower() == 'q':
            break
        sub_folders.append(sub_folder)
        i += 1
    
    create_folders(main_folder, sub_folders)
    
    root = tk.Tk()
    app = ImageMoverApp(root, main_folder, sub_folders)
    root.mainloop()

if __name__ == "__main__":
    main()
