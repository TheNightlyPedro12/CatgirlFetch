#!/usr/bin/python3
import os, getpass, random
from datetime import datetime

print("        .^~^.              .:^!!.        " + "User: " + getpass.getuser())
print("        ^!!7?!:.  ...... .^7?7!!^        "+ "Kernel: " + os.uname()[2])
print("       .~!7!!J?~~?JJYJJ?7!?7~!7!~        " + "OS Name: " + os.name)
print("        ~!!~!!JJY555555555YJ?~!!^        " + "Date: " + datetime.today().strftime('%Y-%m-%d'))
print("        ~!~!55?J555YJJ55JY55Y57~:        " + "Random number: " + str(random.randint(0, 32767)))
print("        :~?5P??P55Y77!PPY~Y5Y757.        " + "CPUS-s: " + str(os.cpu_count()))
print("        .?5JY!Y?7!^7J755?7!!Y7J5^  ^.    ")
print("        ~5?JY!YJJJJPB7JJP#GY?!?J: .YY.   ")
print("        7J!YJ!Y??JJP#GGB5JJJP!!:  :PB7   ")
print("       :7Y7YY?PYG#BG##BGG#B55!?.  ~GBP   ")
print("       ~Y?7YY7GPGJ5GGGPPP5GPG~J^  JGB5   ")
print("      :Y5Y!55!Y##55#####JY#BY!Y7 .5GB?   ")
print("     ^?J5J!5Y7~!JPGGGGGGGPY7~YJ?:^GGB~   ")
print("   .!7!Y5~!5Y7^^:~Y??777~^!?!JY~77BBG.   ")
print("  :7~!Y57!~Y5J^~!?5GGY^^~J7^~JJ~^!7?7    ")
print("  ~^7Y57?^^~?JJ?7???YGY!JJ?!!7!~^~!^     ")
print(" .:!?J?77~??????J^!!!7?!!7!^7^^YJ5PG?    ")
print("  ^?!J7J~JYYJ?J?!?J7!JY?77??7?^7?PPBJ    ")
print("  :^^!~~^777!!~!!77~~777~~7!^7^.^^?J.    ")
