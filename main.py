from FileManagerModule import CheckDuplicate

from HwpModule import *

from KakaoModule import *

from NotionModule import LoadDatabase
from NotionModule import SearchDirectory

import sys
import os
import shutil
import time



#This is Main Function. The Ultimate Start Point of WhaleOS.
def main():
    print(
        "WhaleOS version 1.0.0-221019-1 (linux edition)\n"
        "Copyright (c) 2022 Chaemin Lim\n"
        "The Ultimate Operating System for Team Management\n"
        "Type 'help' for more detail."
    )

    while True:
        cmd = input("WhaleOS> ")

        if cmd == "exit":
            print("Exiting WhaleOS...")
            break

        elif cmd == "help":
            print(
                "WhaleOS Help\n"
                "exit -> exit function\n"
                "help -> print this message")
        
        else:
            print("unknown command...Type 'help' for information.")

main()