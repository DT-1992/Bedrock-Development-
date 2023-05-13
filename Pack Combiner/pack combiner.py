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
from jsbeautifier import beautify_file
from jsonmerge import merge
from jsonschema import validate

"""
Do Things with files Definitions
"""
def files_in_path(path):
    result = []
    for root, dirs, files in os.walk(path):
        result.append(os.path.join(root))
    return result

def find_all_in(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result

def unzip_from_to(path_in,name,path_out ):
    for root, path_in, files in os.walk(path_in):
        if name in files:
            with ZipFile(path_in, 'r') as  zip_ref:
                zip_ref.extractall(path_out)

def beautify_files(path_in,name,path_out ):
    for root, path_in, files in os.walk(path_in):
        if name in files:
            with beautify_file(path_in, 'r') as  beauty_ref:
                beauty_ref.extractall(path_out)

def merge_files(path_in,name,path_in1,name1,path_out ):
    for root, path_in, files in os.walk(path_in):
        if name in files:
            for root, path_in1, files in os.walk(path_in1):
                if name1 in files:
                    json_str1 = json.dumps({"a": [1, 2]})
                    json_str2 = json.dumps({"a": [3, 4]})
                    dct1 = json.loads(json_str1)
                    dct2 = json.loads(json_str2)
                    res_merge = merge(dct1, dct2)

def validate_files(path_in,name,path_out ):
    for root, path_in, files in os.walk(path_in):
        if name in files:
            res_vali=validate(path_in)

"""
Copy files for BP
"""

def copy_animation_controllers(path_to_bp,ac_name):
    path_to_a_c=join(path_to_bp,"animation_controllers") 
    if not(os.path.isdir(path_to_a_c)):
        os.mkdir(path_to_a_c)
    copyfile(join("lookups",ac_name),join(path_to_a_c,ac_name))

def copy_animation(path_to_bp,ani_name):
    path_to_animations=join(path_to_bp,"animations") 
    if not(os.path.isdir(path_to_animations)):
        os.mkdir(path_to_animations)
    copyfile(join("lookups",ani_name),join(path_to_animations,ani_name))

def copy_entities(path_to_bp,entities_name):
    path_to_entities=join(path_to_bp,"entities") 
    if not(os.path.isdir(path_to_entities)):
        os.mkdir(path_to_entities)
    copyfile(join("lookups",entities_name),join(path_to_entities,entities_name))

def copy_functions(path_to_bp,fun_name):
    path_to_functions=join(path_to_bp,"functions") 
    if not(os.path.isdir(path_to_functions)):
        os.mkdir(path_to_functions)
    copyfile(join("lookups",fun_name),join(path_to_functions,fun_name))

def copy_items(path_to_bp,items_name):
    path_to_items=join(path_to_bp,"items") 
    if not(os.path.isdir(path_to_items)):
        os.mkdir(path_to_items)
    copyfile(join("lookups",items_name),join(path_to_items,items_name))

def copy_scripts(path_to_bp,scripts_name):
    path_to_scripts=join(path_to_bp,"items") 
    if not(os.path.isdir(path_to_scripts)):
        os.mkdir(path_to_scripts)
    copyfile(join("lookups",scripts_name),join(path_to_scripts,scripts_name))

def copy_structures(path_to_bp,structures_name):
    path_to_structures=join(path_to_bp,"structures") 
    if not(os.path.isdir(path_to_structures)):
        os.mkdir(path_to_structures)
    copyfile(join("lookups",structures_name),join(path_to_structures,structures_name))

"""
Edit files for BP
"""

def edit_manifests_BP(path_to_bp , packs):
    with open(join(path_to_bp,"manifest.json"), 'r+') as f:
        data = json.load(f)
        data["header"]["description"]+=", Created BP Pack includes: {}".format(packs)
        
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate() 

def add_a_c_to_player(path_to_bp,a_c_handle,ac_common_handle,addtoscript=True):
    result = [y for x in os.walk(path_to_bp) for y in glob(os.path.join(x[0], '*.json'))]
    found=False
    for file in result:
        print(file)
        with open(file, 'r+') as f:
            data=""
            for line in f:
                data+=line
            data=re.sub("\/\/[^\n]*\n", '', data )
            data = json.loads(data)
            if type(data) is dict:
                if "minecraft:entity" in data.keys():
                    if data["minecraft:entity"]["description"]["identifier"]=="minecraft:player":
                        found=True
                        if "scripts" not in data["minecraft:entity"]["description"].keys() and addtoscript:
                            data["minecraft:entity"]["description"]["scripts"]={"animate":[]}
                        if "animations" not in data["minecraft:entity"]["description"].keys():
                            data["minecraft:entity"]["description"]["animations"]={}
                        if addtoscript:
                            data["minecraft:entity"]["description"]["scripts"]["animate"].append(ac_common_handle)
                        data["minecraft:entity"]["description"]["animations"][ac_common_handle]=a_c_handle
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
    print(found)
    if not found:
        path_to_a_c=join(path_to_bp,"entities") 
        if not(os.path.isdir(path_to_a_c)):
            os.mkdir(path_to_a_c)
        copyfile(join("lookups","player.json"),join(path_to_a_c,"player.json"))

"""
Copy files for RP
"""

def copy_animation_controllers(path_to_rp,ac_name):
    path_to_a_c=join(path_to_rp,"animation_controllers") 
    if not(os.path.isdir(path_to_a_c)):
        os.mkdir(path_to_a_c)
    copyfile(join("lookups",ac_name),join(path_to_a_c,ac_name))

def copy_animation(path_to_rp,ani_name):
    path_to_animations=join(path_to_rp,"animations") 
    if not(os.path.isdir(path_to_animations)):
        os.mkdir(path_to_animations)
    copyfile(join("lookups",ani_name),join(path_to_animations,ani_name))

def copy_entity(path_to_rp,entities_name):
    path_to_entity=join(path_to_rp,"entity") 
    if not(os.path.isdir(path_to_entity)):
        os.mkdir(path_to_entity)
    copyfile(join("lookups",entities_name),join(path_to_entity,entities_name))

def copy_atachables(path_to_rp,atachables_name):
    path_to_atachables=join(path_to_rp,"atachables") 
    if not(os.path.isdir(path_to_atachables)):
        os.mkdir(path_to_atachables)
    copyfile(join("lookups",atachables_name),join(path_to_atachables,atachables_name))

def copy_font(path_to_rp,font_name):
    path_to_font=join(path_to_rp,"font") 
    if not(os.path.isdir(path_to_font)):
        os.mkdir(path_to_font)
    copyfile(join("lookups",font_name),join(path_to_font,font_name))

def copy_models(path_to_rp,models_name):
    path_to_models=join(path_to_rp,"models") 
    if not(os.path.isdir(path_to_models)):
        os.mkdir(path_to_models)
    copyfile(join("lookups",models_name),join(path_to_models,models_name))

def copy_particles(path_to_rp,particles_name):
    path_to_particles=join(path_to_rp,"particles") 
    if not(os.path.isdir(path_to_particles)):
        os.mkdir(path_to_particles)
    copyfile(join("lookups",particles_name),join(path_to_particles,particles_name))

def copy_render_controllers(path_to_rp,render_controllers_name):
    path_to_render_controllers=join(path_to_rp,"render_controllers") 
    if not(os.path.isdir(path_to_render_controllers)):
        os.mkdir(path_to_render_controllers)
    copyfile(join("lookups",render_controllers_name),join(path_to_render_controllers,render_controllers_name))

def copy_sound(path_to_rp,sound_name):
    path_to_sound=join(path_to_rp,"sound") 
    if not(os.path.isdir(path_to_sound)):
        os.mkdir(path_to_sound)
    copyfile(join("lookups",sound_name),join(path_to_sound,sound_name))

def copy_text(path_to_rp,text_name):
    path_to_text=join(path_to_rp,"text") 
    if not(os.path.isdir(path_to_text)):
        os.mkdir(path_to_text)
    copyfile(join("lookups",text_name),join(path_to_text,text_name))

def copy_textures(path_to_rp,textures_name):
    path_to_textures=join(path_to_rp,"textures") 
    if not(os.path.isdir(path_to_textures)):
        os.mkdir(path_to_textures)
    copyfile(join("lookups",textures_name),join(path_to_textures,textures_name))

def copy_ui(path_to_rp,ui_name):
    path_to_ui=join(path_to_rp,"ui") 
    if not(os.path.isdir(path_to_ui)):
        os.mkdir(path_to_ui)
    copyfile(join("lookups",ui_name),join(path_to_ui,ui_name))

def copy_sub_packs(path_to_rp,sub_packs_name):
    path_to_sub_packs=join(path_to_rp,"sub_packs") 
    if not(os.path.isdir(path_to_sub_packs)):
        os.mkdir(path_to_sub_packs)
    copyfile(join("lookups",sub_packs_name),join(path_to_sub_packs,sub_packs_name))

def ran_ids(path_to_rp,ran_ids_name):
    path_to_ran_ids=join(path_to_rp,"ran_ids") 
    if not(os.path.isdir(path_to_ran_ids)):
        os.mkdir(path_to_ran_ids)
    copyfile(join("lookups",ran_ids_name),join(path_to_ran_ids,ran_ids_name))

"""
Edit files for RP
"""

def edit_manifests_RP(path_to_rp , packs):
    with open(join(path_to_rp,"manifest.json"), 'r+') as f:
        data = json.load(f)
        data["header"]["description"]+=", Created RP Pack includes: {}".format(packs)
        
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate() 

"""
Handle Json
"""
def loadJsonKillComments(jsonFile):
    data=""
    with open(jsonFile, 'r+') as f:
        
        for line in f:
            data+=line
    data=re.sub("\/\/[^\n]*\n", '', data )
    data = json.loads(data)
    return data

def get_recursively(search_dict, field):
    """
    Takes a dict with nested lists and dicts,
    and searches all dicts for a key of the field
    provided.
    """
    fields_found = []
    keys=[]

    for key, value in search_dict.items():

        if key == field:
            fields_found.append(value)
            keys.append([key])

        elif isinstance(value, dict):
            results,recurKeys = get_recursively(value, field)
            for result in results:
                fields_found.append(result)
            for recurKey in recurKeys:
                tempKey=[key]
                tempKey+=recurKey
                keys.append(tempKey)

        elif isinstance(value, list):
            for ind in range(len(value)):
                item=value[ind]
                if isinstance(item, dict):
                    more_results,more_recurKeys = get_recursively(item, field)
                    
                    for another_result in more_results:
                        fields_found.append(another_result)
                    for more_recurkey in more_recurKeys:
                        tempKey=[ind]
                        tempKey+=more_recurkey
                        keys.append(tempKey)
                        

    return fields_found, keys

"""
Def Functions
"""
def check_compatiblity(Base,Cross):
    path_to_base="base"
    path_to_cross="Cross"
    with ZipFile(Base, 'r') as zipObj:
        zipObj.extractall(path_to_base)
        
    with ZipFile(Cross, 'r') as zipObj:
        zipObj.extractall(path_to_cross)
    result = [y for x in os.walk(path_to_base) for y in glob(os.path.join(x[0], '*.json'))] 
    base_handles=[]
    for file in result:
        print(file)
        data=loadJsonKillComments(file)
        try:
            fields_found, keys=get_recursively(data,"identifier")
        except:
            fields_found=[]
            keys=[]
        base_handles+=fields_found
    result2 = [y for x in os.walk(path_to_cross) for y in glob(os.path.join(x[0], '*.json'))] 
    cross_handles=[]
    for file in result2:
        print(file)
        data=loadJsonKillComments(file)
        try:
            fields_found, keys=get_recursively(data,"identifier")
        except:
            fields_found=[]
            keys=[]
        cross_handles+=fields_found
    print(base_handles)
    print(cross_handles)
    shutil.rmtree(path_to_base)
    shutil.rmtree(path_to_cross)
    return set(base_handles).intersection(set(cross_handles))

"""
copy files from selected pack to workdir 
"""
def add_Pack(packPath):
    cwd = os.getcwd()
    path_to_save="temp/pack/"
    with ZipFile(path, 'r') as zipObj:
        zipObj.extractall(path_to_save)
    """
    Erkenne BP und speicher path und benenne nach path
    """
    manifests=find_all_in("manifest.json",path_to_save)
    path_to_bp=""
    for mani in manifests:
        with open(mani) as f:
            packmani = json.load(f)
        for sub in packmani["modules"]:
            if "data"== sub["type"]:
                path_to_bp=os.path.dirname(mani)
                bp_name=ntpath.basename(path_to_bp)
                shutil.move(path_to_save, "/Packs/BPs/")
                print("packs BP import is completed"+bp_name)
    """
    Erkenne RP und speicher path benenne nach path
    """
    manifests=find_all_in("manifest.json",path_to_save)
    path_to_rp=""
    for mani in manifests:
        with open(mani) as f:
            packmani = json.load(f)
        for sub in packmani["modules"]:
            if "recources"== sub["type"]:
                path_to_rp=os.path.dirname(mani)
                rp_name=ntpath.basename(path_to_rp)
                shutil.move(path_to_save, "/Packs/RPs/")
                print("packs RP import is completed"+rp_name)

"""
run beautify over selected pack folder files 
"""
def beautify_Pack(folderPath):
    b_files=find_all_in("*.json",folderPath)
    for bs in b_files:    
        beautify_files(folderPath,bs,folderPath )
    
"""
run validate over selected pack folder files 
"""
def validate_Pack(folderPath):
    b_files=find_all_in("*.json",folderPath)
    for bs in b_files:    
        validate(folderPath,bs,folderPath )
    
"""
create Addon
"""
def create_AddonPack(basePath):
    """
    Get Files and Path for BP
    """
    BP_path_to_base=basePath+"behavior_pack/"
    BP_path_to_packs="/Packs/BPs/"
    BP_path_to_temp="/temp/Addon/BP/"
    BP_path_to_save="/Output/BP/"

    cwd = os.getcwd()
    pack =""

    temp_path=join(cwd,BP_path_to_save)
    os.chdir(temp_path)
    pack_name=ntpath.basename(path)
    file_paths = []
    
    for directory,_,_ in os.walk(temp_path):
        files=glob(os.path.join(directory, "*.*"))
        for file in files:
            print(os.getcwd())
            print(file)
            file_paths.append(file.replace(os.getcwd()+"\\",""))
    with ZipFile(pack_name, 'x') as zip:
        for file in file_paths:
            print(file)
            zip.write(file)
    os.chdir(cwd)
    copyfile(join(BP_path_to_save,pack_name),"BP_"+pack_name)
    shutil.rmtree(BP_path_to_save)
    print("packs have been merged and processing is completed, please use BP_"+pack_name)
    


    """
    Get Files and Path for RP
    """
    RP_path_to_base=basePath+"resource_pack/"
    RP_path_to_packs="/Packs/RPs/"
    RP_path_to_temp="/temp/Addon/RP/"
    RP_path_to_save="/Output/BP/"

    cwd = os.getcwd()
    pack =""
    temp_path=join(cwd,RP_path_to_save)
    os.chdir(temp_path)
    pack_name=ntpath.basename(path)
    file_paths = []   
    for directory,_,_ in os.walk(temp_path):
        files=glob(os.path.join(directory, "*.*"))
        for file in files:
            print(os.getcwd())
            print(file)
            file_paths.append(file.replace(os.getcwd()+"\\",""))
    with ZipFile(pack_name, 'x') as zip:
        for file in file_paths:
            print(file)
            zip.write(file)
    os.chdir(cwd)
    copyfile(join(RP_path_to_save,pack_name),"RP_"+pack_name)
    shutil.rmtree(RP_path_to_save)
    print("packs have been merged and processing is completed, please use RP_"+pack_name)
    


"""
MAIN-LOOP
"""
if __name__ == "__main__":
    from tkinter import ttk
    from tkinter import filedialog
    from tkinter import messagebox
    from tkinter import StringVar, Button, Label, Entry, Tk, Checkbutton, END, ACTIVE
    from tkinter import filedialog, Scale,DoubleVar,HORIZONTAL,IntVar,Listbox, ANCHOR
    



    """
    GUI
    """
    root = Tk()
    root.title("Addon Pack Combiner")   
    Bedrock_Preview_check =IntVar ()
    packPath =StringVar ()
    folderPath = StringVar ()
    basePath= StringVar ()

    def browse_pack():
        #browse for a structure file.
        packPath.set(filedialog.askopenfilename(filetypes=(
            ("addon", "*.mcaddon *.MCADDON *.MCPACK *mcpack"),("zip", "*.zip *.ZIP") )))
        
    
    def preview_pack():
        if Bedrock_Preview_check==1:
            with ZipFile("/base_packets/bedrock-samples-1.20.0.22-preview.zip", 'r') as zipObj:
                zipObj.extractall("/temp/base/preview/")
                basePath.set("/temp/base/preview/") 
        else:
            with ZipFile("/base_packets/bedrock-samples-1.19.80.2.zip", 'r') as zipObj:
                zipObj.extractall("/temp/base/normal/")
                basePath.set("/temp/base/normal/") 


    def add_pack_from_gui():
        add_Pack(packPath.get())
    def browse_folder():
        #browse for a structure file.
        folderPath.set(filedialog.askopenfilename(
            ))
    def nicer_code():
        bfolder_pack=folderPath.get()
        beautify_Pack(bfolder_pack)

    def validate_code():
        vfolder_pack=folderPath.get()
        validate_Pack(vfolder_pack)

    def crossCheckPacksGui():
        base_pack=basePath.get()
        cross_pack=packPath.get()
        if len(base_pack)>0:
            intersections=check_compatiblity(base_pack,cross_pack)
            print(intersections)
            if len(intersections)!=0:
                printInt="\n".join(intersections)
                messagebox.showerror("Not Compatible by default","The two packs are not compatible because they both modify the following game features: \n{}\n i will try to combine them if you let me".format(printInt))
            else:
                messagebox.showinfo("Compatible","The two packs are likely compatible,i will try to combine them if you let me")
            
        else:
            messagebox.showerror("No Base Pack", "You must first select a base pack to check compatiblity")


    def make_pack_from_gui():
        create_AddonPack(basePath)


    base_pack=Label(root, text="Base Pack - Select if Preview or not")
    Bedrock_Preview = Checkbutton(root, text="Bedrock_Preview", variable=Bedrock_Preview_check, onvalue=1, offvalue=0)
    
    add_pack=Label(root, text="Select File to add to Projekt:")

    path_entry = Entry(root, textvariable=packPath, width=30)
    browsButton = Button(root, text="Browse", command=browse_pack)
    
    addButton = Button(root, text="add Pack to Projekt", command=add_pack_from_gui)
    
    edit_pack=Label(root, text="Select Folder to run changes on:")
    
    path_folder = Entry(root, textvariable=folderPath, width=30)
    browsfulButton = Button(root, text="Browse Addon folder ", command=browse_folder)


    Cross_check = Button(root, text="Cross Check a Pack", command=crossCheckPacksGui)
    vali_date = Button(root, text="validate_pack", command=validate_code)
    beauti_button = Button(root, text="beautify_pack", command=nicer_code)
    pack_out=Label(root, text="Press Buton to create Addonpack from all Sources in /Packs/ on the selected base version:")
    packButton = Button(root, text="Create Addon", command=make_pack_from_gui)
    
    r=0
    base_pack.grid(row=r, column=0,columnspan=2)
    r+=1
    Bedrock_Preview.grid(row=r, column=0,columnspan=2)
    r+=1
    add_pack.grid(row=r, column=0,columnspan=2)
    r+=1
    path_entry.grid(row=r, column=0)
    browsButton.grid(row=r, column=1)
    r+=1
    addButton.grid(row=r, column=0,columnspan=2)
    r+=1
    edit_pack.grid(row=r, column=0,columnspan=2)
    r+=1
    path_folder.grid(row=r, column=0)
    browsfulButton.grid(row=r, column=1)
    r+=1
    Cross_check.grid(row=r, column=0)
    vali_date.grid(row=r, column=1)
    r+=1
    beauti_button.grid(row=r, column=0,columnspan=2)
    r+=1
    pack_out.grid(row=r, column=0,columnspan=2)
    r+=1
    packButton.grid(row=r, column=0,columnspan=2)
    
    root.mainloop()
    root.quit()
