# %%
# import math
import markdown
import os

# %%
# Parse Markdown file to HTML
with open ("text.md", 'r') as f:
     mdata = f.read()
     f.close()
# %%
# Add contence to new.html
def buildMD (html):
     html = "<!DOCTYPE html> \n <head> \n <title>\"Test\"</title> \n <link rel=\"stylesheet\" href=\"style.css\">\n</head>\n<html>\n<body>" + html + \
     "\n</body>\n<html>"

     with open ("new.html", 'w') as f:
        f.write(html)
        f.close()

# %%
# main
html = markdown.markdown(mdata)
buildMD(html)
# print(html)