# %%
# import math
import markdown
import os

# %%
#Do something in this block. 
with open ("text.md", 'r') as f:
     mdata = f.read()
     f.close()
# %%
#Do something in this block. 
def buildMD (mdata):
     with open ("new.html", 'w') as f:
        f.write(mdata)
        f.close()

# %%
# main
html = markdown.markdown(mdata)
buildMD(html)
# print(html)