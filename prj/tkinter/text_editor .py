#!/usr/bin/env python3
#          23 : tkinter Text editor
# https://www.youtube.com/watch?v=6-1XRnEl9pE&list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt&index=23
# http://www.newthinktank.com/2016/09/learn-program-23/

from tkinter import *
import tkinter.filedialog


class TextEditor:
    # Quits the TkInter app when called
    @staticmethod  # Static method
    def quit_app(event=None):
        root.quit()

    def open_file(self, event=None):

        txt_file = tkinter.filedialog.askopenfilename(parent=root,
                                initialdir='/root/Desktop/d')

        if txt_file:  # if file  selected
            self.text_area.delete(1.0, END)

            # Open file and put text in the text widget
            with open(txt_file) as _file:
                self.text_area.insert(1.0, _file.read())
                root.update_idletasks() # Update the text widget

    def save_file(self, event=None):

        # Opens the save as dialog box
        file = tkinter.filedialog.asksaveasfile(mode='w')
        if file != None:
            # Get text in the text widget and delete the last newline
            data = self.text_area.get('1.0', END + '-1c')

            # Write the text and close
            file.write(data)
            file.close()

    def __init__(self, root):

        self.text_to_write = ""
        root.title("Text Editor")
        root.geometry("600x550")
        frame = Frame(root, width=600, height=550)
        scrollbar = Scrollbar(frame)

        # yscrollcommand connects scroll bar to text area
        self.text_area = Text(frame, width=600, height=550,
                              yscrollcommand=scrollbar.set,
                              padx=10, pady=10)

        # Call yview when the scrollbar is moved
        scrollbar.config(command=self.text_area.yview)

        # Put scroll bar on the right and fill in the Y direction
        scrollbar.pack(side="right", fill="y")

        # Pack on the left and fill available space
        self.text_area.pack(side="left", fill="both", expand=True)
        frame.pack()
        the_menu = Menu(root)

        # Create a pull down menu that can't be removed
        file_menu = Menu(the_menu, tearoff=0)

        # Add items to the menu that show when clicked
        # compound allows you to add an image
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Quit", command=self.quit_app)

        # Add the pull down menu to the menu bar
        the_menu.add_cascade(label="File", menu=file_menu)

        # Display the menu bar
        root.config(menu=the_menu)


root = Tk()

text_editor = TextEditor(root)

root.mainloop()
