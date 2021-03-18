import os 
import argparse


dirs = [
    os.path.join ("data","raw") ,
     os.path.join ("data","processed"),
    "noteboooks",
    "saved_models" , 
    "src"
]

# exist_pk =True , if dir_ already exist it'll not throw error
# create .gitkeep file init 
for dir_ in dirs:
    os.makedirs(dir_ ,exist_ok = True)
    with open (os.path.join(dir_ ,".gitkeep"),"w") as f :
        pass 

files = [
   " dvc.yaml" ,
    "params.yaml" ,
    ".gitignore" ,
    os.path.join("src" , "__init__.py")
]

for file_ in files:   
    with open (file_ , "w") as f :
        pass 
    



