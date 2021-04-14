import os
from pathlib import Path

with open('config.yaml','r',encoding='utf-8') as f:
    root = Path.cwd()
    currentLevel = 0
    lastLevel = 0
    direction = 0
    for line in f.readlines():
        objectName = line.strip(' -:\n\r')
        currentLevel = int(line.find('-') / 4)
        if line.endswith(':\n'):
            if currentLevel == 0:
                currentPath = os.path.join(root, objectName)
            elif currentLevel > lastLevel:
                currentPath = os.path.join(currentPath, objectName)
            elif currentLevel == lastLevel:
                currentPath = os.path.join(Path(currentPath).parents[0], objectName)
            else:
                currentPath = os.path.join(Path(currentPath).parents[lastLevel - currentLevel], objectName)
            # print(currentPath)
            lastLevel = currentLevel
            if not os.path.exists(currentPath):
                os.mkdir(currentPath)
        else:
            if lastLevel - currentLevel < 0:
                fileName = os.path.join(currentPath, objectName)
            else:
                fileName = os.path.join(Path(currentPath).parents[lastLevel-currentLevel], objectName)
            if not os.path.exists(fileName):
                open(fileName, 'w').close()
