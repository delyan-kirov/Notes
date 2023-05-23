# %%
import markdown
import os

# %%
#Do something in this block. 
# def readMD (mdFile):
#      path = "./data/" + mdFile
#      with open (path, 'r') as f:
#           mdata = f.read()
#           f.close()
#      return mdata

#%%
# Styling
cssFile = ""
with open("./templates/styles.css", "r") as f:
    cssFile = f.read()
    f.close()

cssStyle = "    <head>\
        <style> " + cssFile + "\n </style>\
    </head>\n"
# %%
#Do something in this block. 
def buildMD (mdata, name:str):

     mdata = markdown.markdown(mdata, extensions=['markdown.extensions.tables'])
     path = "./templates/" + name + ".html"
     print("the path was made: " + path)
     print (name)
     with open (path, 'w') as f:
        f.write(cssStyle + mdata)
        print(f)
        f.close()
        
     print("successfully created file.")
        
# %%
# # main
# mdFile = input("Enter the name of the markdown file. \n ")
# name = input("Provide the name of the html file. \n")
# mdata = readMD(mdFile)
# html = markdown.markdown(mdata, extensions=['markdown.extensions.tables'])
# buildMD(html, name)
