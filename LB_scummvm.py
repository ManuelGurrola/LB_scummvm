import sys
import configparser
import string

# Check that command is of type "LB_scummvm.py scummvm.ini"
args_len = len(sys.argv)
if args_len != 2:
    print("\nArgument must be only the path to 'scummvm.ini'")
    quit()

# Parse scummvm.ini file
scummvm_ini = configparser.ConfigParser()
scummvm_ini.read(sys.argv[1])

# For each game section in the file, create a .scummvm file (except for the 
# scummvm section which is the core's configuration)
for game in scummvm_ini.sections():
    if game != "scummvm":
        path = scummvm_ini[game]['path']
        desc = scummvm_ini[game]['description']
        filename = desc + ".scummvm"
        for ch in ['<', '>', ':', '"', '/', '\\', '|', '?', '*']:
            if ch in filename:
                filename = filename.replace(ch, " ")
        print("\nCreating " + filename + " for " + game + " in " + path)
        full_path = path + filename
        scummvm_file = open(full_path, "w+")
        scummvm_file.write(game)
        scummvm_file.close()
