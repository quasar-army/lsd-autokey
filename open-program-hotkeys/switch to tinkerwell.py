# Enter script code
import subprocess
from subprocess import call

def winexists(target):
    for line in subprocess.check_output(['wmctrl', '-l', '-x']).splitlines():
        window_name = line.split(None, 3)[2].decode()
        if window_name == target:
            return True
    return False
    
if winexists("tinkerwell.Tinkerwell"):
    window.activate("tinkerwell.Tinkerwell", switchDesktop=True, matchClass=True)