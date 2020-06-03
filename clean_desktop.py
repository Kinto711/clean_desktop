import os
import shutil
desktop_content = []
import time
import logging
import json

Documents = [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods", 
                 ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox", 
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", 
                  "pptx", ".pdf", ".txt", ".in", ".out", ".pptx"] 
Media = [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg", 
               ".heif", ".psd", ".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", 
               ".qt", ".mpg", ".mpeg", ".3gp", ".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", 
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma", ".PNG"] 
Programming = [".py"]

desktop = os.chdir('C:\\Users\\aliak\\Desktop')

path_to_desktop = 'C:\\Users\\aliak\\Desktop'
folder_destination = 'C:\\Users\\aliak\\Desktop\\Alexander'
desktop_content=os.listdir('C:\\Users\\aliak\\Desktop')

documents_path = 'C:\\Users\\aliak\\Desktop\\Alexander\\Documents'
media_path = 'C:\\Users\\aliak\\Desktop\\Alexander\\Media'
other_path = 'C:\\Users\\aliak\\Desktop\\Alexander\\Other'
programming_path = 'C:\\Users\\aliak\\Desktop\\Alexander\\Programming'
duplicate = 'C:\\Users\\aliak\\Desktop\\Alexander\\Duplicates'

logging.basicConfig(filename='clean_desktop_log.log', level=logging.DEBUG)



def sort_desktop():
    for x in desktop_content:
        i = 1
        f_name, f_extention = os.path.splitext(x)
        new_file_name = f_name + "_duplicate" + str(i) + f_extention
        
        if x != 'Alexander':
            try:
                if f_extention in Documents:
                    shutil.move(x, documents_path)
                    logging.debug(x + " has been moved to the Documents folder")
                elif f_extention in Media:
                    shutil.move(x, media_path)  
                    logging.debug(x + " has been moved to the Media folder")
                elif f_extention in Programming:
                    shutil.move(x, programming_path)
                    logging.debug(x + " has been moved to the Programming folder")
                elif os.path.isdir(x):
                    if x == "Alexander":
                        continue
                    else:
                        shutil.move(x, other_path)
                        logging.debug(x + " has been moved to the Other folder")
            except FileNotFoundError:
                i += 1
                os.rename(x, new_file_name)
                if new_file_name in Documents:
                    shutil.move(new_file_name, documents_path)
                elif new_file_name in Media:
                    shutil.move(new_file_name, media_path)  
                elif new_file_name in Programming:
                    shutil.move(new_file_name, programming_path)
                elif os.path.isdir(x):
                    if new_file_name == "Alexander":
                        continue
                    else:
                        shutil.move(new_file_name, other_path)
            except Exception:
                i += 1
                os.rename(x, new_file_name)
                if new_file_name in Documents:
                    shutil.move(new_file_name, documents_path)
                elif new_file_name in Media:
                    shutil.move(new_file_name, media_path)  
                elif new_file_name in Programming:
                    shutil.move(new_file_name, programming_path)
                elif os.path.isdir(x):
                    if new_file_name == "Alexander":
                        continue
                    else:
                        shutil.move(new_file_name, other_path)


while True:
    sort_desktop()
    sleep = 60
            
              
        
    
        
        
      
            
        
   
      
   
    