# Enter script code
import subprocess
from subprocess import call


def getCurrentWorkspaceIndex():
    currentWorkspaceCmd = "wmctrl -d | grep -w '*'"
    ps = subprocess.Popen(currentWorkspaceCmd, shell=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = ps.communicate()[0]
    return output.decode().split(None, 3)[0]


def getWindowsByName(name):
    getWindowsByNameCmd = "wmctrl -l -x | grep " + name
    ps = subprocess.Popen(getWindowsByNameCmd, shell=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return ps.communicate()[0].splitlines()


currentWorkspaceIndex = getCurrentWorkspaceIndex()


def focusWindowHex(hex):
    call(['wmctrl', '-i', '-a', hex])


def windowExistsInWorkspace(target):
    for line in subprocess.check_output(['wmctrl', '-i', '-l', '-x']).splitlines():
        windowName = line.split(None, 3)[2].decode()
        windowsWorkspaceIndex = line.split(None, 3)[1].decode()
        if windowName == target and windowsWorkspaceIndex == currentWorkspaceIndex:
            return True
    return False


def focusWindowIfInCurrentWorkspace(windowName):
    for windowLine in getWindowsByName(windowName):
        windowHex = windowLine.split(None, 3)[0].decode()
        windowWorkspaceIndex = windowLine.split(None, 3)[1].decode()
        if windowWorkspaceIndex == currentWorkspaceIndex:
            focusWindowHex(windowHex)


if windowExistsInWorkspace("code.Code"):
    focusWindowIfInCurrentWorkspace('Code')
else:
    call(['code'])
