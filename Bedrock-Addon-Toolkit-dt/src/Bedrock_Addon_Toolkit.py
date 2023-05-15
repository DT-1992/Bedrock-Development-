"""
import Dependencies
"""
import json
import os
import shutil
from os import listdir
from os import path
from os.path import isfile, join
from zipfile import ZipFile 
from shutil import copyfile
from glob import glob
import ntpath
import threading
import re
import sys


"""
imports Functions
"""

"""from .functions.init import *"""
from functions.load_pack import *
from functions.check_pack import * 
"""from .functions.update_pack import * """
"""from .functions.return_pack import * """
"""from .functions.add_to_lib import * """
"""from .functions.create_compilation import * """



"""
MAIN-LOOP
"""
if __name__ == "__main__":
    from tkinter import ttk
    from tkinter import filedialog
    from tkinter import messagebox
    from tkinter import StringVar, Button, Label, Entry, Tk, Checkbutton, END, ACTIVE
    from tkinter import filedialog, Scale,DoubleVar,HORIZONTAL,IntVar,Listbox, ANCHOR
    from tkinter import *



    """
    GUI
    """
    """
    GUI-predefs
    """
    
    root = Tk()
    root.title("Addon Pack Combiner")   
    Bedrock_Preview_check =IntVar ()
    basePath =StringVar ()
    packPath =StringVar ()
    folderPath = StringVar ()
    tempPath= StringVar ()
    
    """
    GUI-defs
    """
    def browse_workdir_from_gui():
        tempPath.set(filedialog.askdirectory())
    def set_workdir_from_gui():
        tempPath.set(filedialog.askdirectory())

    def preview_pack():
        if Bedrock_Preview_check==1:
            with ZipFile("/base_packets/bedrock-samples-1.20.0.22-preview.zip", 'r') as zipObj:
                zipObj.extractall("/temp/base/")
                basePath.set("/temp/base/") 
        else:
            with ZipFile("/base_packets/bedrock-samples-1.19.80.2.zip", 'r') as zipObj:
                zipObj.extractall("/temp/base/")
                basePath.set("/temp/base/")

    def browse_pack():
        #browse for a structure file.
        packPath.set(filedialog.askopenfilename(filetypes=(
            ("addon", "*.mcaddon *.MCADDON *.MCPACK *mcpack"),("zip", "*.zip *.ZIP") )))
    def load_pack_zip_from_gui():
        load_pack_zip(packPath.get(),tempPath.get())
    
    def browse_pack_folder():
        #browse for a structure file.
        folderPath.set(filedialog.askdirectory())
    def load_pack_folder_from_gui():
        load_pack_folder(folderPath.get(),tempPath.get())
    
    def check_compability_from_gui():
        check_compatiblity("/temp/base/","/temp/pack/")
    
    def check_validate_from_gui():
        validate_Pack("/temp/pack/") 

    def update_version_from_gui():
        validate_Pack("/temp/pack/")

    def update_beautify_from_gui():
        validate_Pack("/temp/pack/") 

    def add_to_lib_from_gui():
        validate_Pack("/temp/pack/") 
        
    def build_compilation_from_gui():
        validate_Pack("/temp/pack/") 
    """
    GUI-ui
    """
    temp_l=Label(root, text="Select to work in:")
    path_temp_l = Entry(root, textvariable=tempPath, width=30)
    browworkButton = Button(root, text="Browse workdir", command=browse_workdir_from_gui)
    settemp= Button(root, text="set workdir", command=set_workdir_from_gui)

    base_pack=Label(root, text="Base Pack - Select if Preview or not")
    Bedrock_Preview = Checkbutton(root, text="Bedrock_Preview", variable=Bedrock_Preview_check, onvalue=1, offvalue=0)


    add_pack=Label(root, text="Select File to add to work:")
    path_entry = Entry(root, textvariable=packPath, width=30)
    browsButton = Button(root, text="Browse", command=browse_pack)
    addButton = Button(root, text="load Pack", command=load_pack_zip_from_gui)

    add_pack_folder=Label(root, text="Select Folder to add to work:")
    path_entry_folder = Entry(root, textvariable=folderPath, width=30)
    browsButton_folder = Button(root, text="Browse", command=browse_pack_folder)
    addButton_folder = Button(root, text="load Pack folder", command=load_pack_folder_from_gui)

    check_pack=Label(root, text="run checks on work:")
    check_Comp_Button = Button(root, text="Compability", command=check_compability_from_gui)
    check_valid_Button = Button(root, text="Validate JSON", command=check_validate_from_gui)
    
    update_pack=Label(root, text="run changes on work:")
    update_version_Button = Button(root, text="update_version", command=update_version_from_gui)
    update_beautify_Button = Button(root, text="beautify JSON", command=update_beautify_from_gui)

    add_lib_pack=Label(root, text="add work to lib:")
    add_lib_Button = Button(root, text="add to lib", command=add_to_lib_from_gui)

    build_pack=Label(root, text="build from lib:")
    build_pack_Button = Button(root, text="build compilation", command=build_compilation_from_gui)
    """
    GUI-structure
    """
    
    r=0
    temp_l.grid(row=r, column=0,columnspan=2)
    r+=1
    path_temp_l.grid(row=r, column=0)
    browworkButton.grid(row=r, column=1)
    r+=1
    settemp.grid(row=r, column=0,columnspan=2)
    r+=2
    base_pack.grid(row=r, column=0,columnspan=2)
    r+=1
    Bedrock_Preview.grid(row=r, column=0,columnspan=2)
    r+=2
    add_pack.grid(row=r, column=0,columnspan=2)
    r+=1
    path_entry.grid(row=r, column=0)
    browsButton.grid(row=r, column=1)
    r+=1
    addButton.grid(row=r, column=0,columnspan=2)
    r+=2

    add_pack_folder.grid(row=r, column=0,columnspan=2)
    r+=1
    path_entry_folder.grid(row=r, column=0)
    browsButton_folder.grid(row=r, column=1)
    r+=1
    addButton_folder.grid(row=r, column=0,columnspan=2)
    r+=2
    check_pack.grid(row=r, column=0,columnspan=2)
    r+=1
    check_Comp_Button.grid(row=r, column=0)
    check_valid_Button.grid(row=r, column=1)
    r+=1
    update_pack.grid(row=r, column=0,columnspan=2)
    r+=1
    update_version_Button.grid(row=r, column=0)
    update_beautify_Button.grid(row=r, column=1)
    r+=1
    add_lib_pack.grid(row=r, column=0,columnspan=2)
    r+=1
    add_lib_Button.grid(row=r, column=0,columnspan=2)
    r+=1
    build_pack.grid(row=r, column=0,columnspan=2)
    r+=1
    build_pack_Button.grid(row=r, column=0,columnspan=2)
    r+=1
    """
    ending
    """
    root.mainloop()
    root.quit()
