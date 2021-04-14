import os
import shutil

root_dir = 'Ex_01_02/my_project'
for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith('.html'):
            dir_name = os.path.join('templates', os.path.basename(root))
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)
            shutil.copyfile(os.path.join(root, file), os.path.join(dir_name, file))