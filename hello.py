import os
path = "C:/Users/Lee/git_tutorial"

os.access(path, os.F_OK & os.R_OK & os.W_OK & os.E_OK)


print ("Hello world")
print ("Tell Your world")
