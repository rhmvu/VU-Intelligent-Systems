import sys
import os
import platform

is_dev = sys.argv[1] == "dev" if len(sys.argv) > 1 else False


if not sys.version_info >= (2,7,13):
    requirements = "requirements.txt"
else:
    raise AssertionError("only support for Python 2.7")


if __name__ == "__main__":
    if platform.system() == "Linux":
        print("Please enter your UNIX sudo password if necessary to give permission for the installation:")
        os.system("sudo pip2 install -r %s" % requirements)
    else:
        os.system("pip2 install -r %s" % requirements)
