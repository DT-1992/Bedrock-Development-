


Function:
============================

this software should provide an easy way to do these things if it gets finished:

  Addon Scans for:
    
    ->  Compability (can addon be combined without merging files etc)
    
    ->  JSON validation
  
  Addon update/changes:
  
    ->  Because Bedrock is a hell in case of version updates in code for developers
        its often the case that users cant run their addons anymore,
        so this tool will try to update the json files with help of the newest samples from bedrock(https://github.com/Mojang/bedrock-samples/releases)
        
     -> let jsbeautify run over your addon so files become formatet and readable,
        so you can better read and understand whats inside
        https://github.com/beautify-web/js-beautify
        
     
  Build An lib of your Addons for further use:
    
    ->  Create an Lib from your addons and changed addons,
        with some extra data to make the compilation out of it
    ->  Feature for running updates for lib in init 
  
  Create an Addon Compilatation from your lib:
    
    ->  Create an Addon based on the newest bedrock sample of your choise,
        containing the choosen addons of your lib (consoles have problem running multiple packs on servers so i needed a way to fuse them)
    
    ->  files will be placed in subfolders for each addon so no conflicts with as example differnt car.json 
        can occour
    
    ->  some file will not be placed in subfolders because they manipulate vanilla things so we have to merge these 
        i will try to to do this using [merge](https://pypi.org/project/jsonmerge/)
    
    ->  Options to Choose as Compilation Extras:
        texturepack
        shader
        subpacks 
        etc
        
everything controlled from an simply gui   

Work in Progress....


Progress:
============================

Projekt structure:first tests done
create a gui: first tests done but some errors with pathdeclarations and input of textfields so just like a picture and some things are missing

functions:(at the moment more or less ideas what and how)
  
  base functions:first few functions for base tasks implemented but some errors still
    ---------------------------
  import pack from:
    zip/mcaddon/mcpack: import to workfolder works 
    folder:  import to workfolder works (if run as admin)
    ---------------------------   
   export pack to:
    zip/mcaddon/mcpack:
    folder:
    ---------------------------
   checks:
    Compability: needs changes
    validate: needs testing
    manifest:
    packname_readable:
     ---------------------------    
  updates:
    jsbeautify:needs testing
    version_update:
    code_version_update:
      ---------------------------
  lib management:
    import pack from workdir:
    create files to store additional information: 
    define additional informations:
    implement autoupdate when update is done
        ---------------------------   
  build compilation:
    set_packname:
    set_author:
    set_description:
    load_base:
    add info from base to description and in seperat compilation.txt file:
    select packs:
    load packs to copilation and doing the things to combine the base pack and selected packs:
    add option for prim texture pack:
    add option for prim shader pack:
    add option for API Addition:
    

inspiration and at the moment main source:
============================
https://github.com/RavinMaddHatter/Bedrock-Addon-Compatiblity-Tool
https://github.com/DauntlessStudio/Bedrock-Developments/tree/main

etc:
============================
 free to use for everyone :D 
 feel also free in helping and commenting as you see early development and i am relative new to py and bedrock development :D 
 i think a lot of us want this and maybe i or we together can make it or someone builds on some ideas and we can make it even better than i even hoped or planed.
 feel also free to yell at my english, its not the yellow from the egg i would say ;)
