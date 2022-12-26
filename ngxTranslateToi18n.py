import os 
from tkinter import filedialog
import tqdm
import json
import re

"""
This script has been written in a rush and not code cleanup or bugfixing has been performed. It just worked for the relevant angular apps 
All errors have been wrapped in try excepts and solved manually later on 
This script has been written to move from ngx-translate in angular to the new i18n
 The scripts first asks for a json file that contains the translation
 Then it demands a directory and after that all files in the directory are parsed and the corresponding strings replaced
 To minimalise the impact on the application the following replacements are performed: 
{{ 'PAGES.HOME.CTA' | translate }}    -replaced with->     json['PAGES']['HOME']['CTA']  
"""

#json_path = filedialog.askopenfilename(title='Please chose a json file containg the translations')
json_path = "C:/Users/micro/Documents/coding/homie/frontend/src/assets/i18n/en.json"
# path = filedialog.askdirectory(title='Please chose a directory file')
path = "C:/Users/micro/Documents/coding/homie/frontend/src/app"
# Extract basename and pathname to save new pages
print("Recursively replacing ", path, " with values from ", json_path)
with open(json_path) as f:
  translations = json.load(f)

translation_regex = "{{ *\n* *['|\"][A-z.\d]+['|\"] *\n* *\|*\n* *translate *\n* *}}"
translation_capture = "{{ *\n* *['|\"]([A-z.]+)['|\"] *\n* *\|*\n* *translate *\n* *}}"

# Recursively oop through each directory
for dname, dirs, files in os.walk(path):
    # Loop through the corresponding files 
    for fname in files:
      try:
          # Open the file and store the content in a variable 
          fpath = os.path.join(dname, fname)
          if (fpath.endswith(".html")):
            
            with open(fpath) as f:
              content = f.read()
            # Find corresponding matches
            matches = re.findall(translation_regex, content)
            for match in matches:
              capture_keys = re.search(translation_capture, match)
              if (capture_keys):
                  json_keys = capture_keys.groups()[0].split('.')
              else:
                try:
                  json_keys = match.split('\' |')[0].split('{{ \'')[1].split('.')
                except IndexError:
                  continue
              current_json = translations
              keyError = False
              for key in json_keys:
                try: 
                  current_json = current_json[key]
                except KeyError:
                  keyError = True
                  break
              if keyError:
                print("**********************************************************")
                print("Translation not found for ", match)
                print("**********************************************************")
                continue
              translation = current_json
              content = content.replace(match, translation)
              
            
            # Write the new content to the file again 
            with open(fpath, "w") as f:
                f.write(content)
          else: 
            continue
      except UnicodeDecodeError:
            continue