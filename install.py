import sys

print("Running installer...")

try:
    import hcsr04
except ImportError:
    print("hcsr04 package not installed, installing")
    import upip
    upip.install(['mPython-hcsr04'])

print("Installer ready")