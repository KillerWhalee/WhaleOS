from cmd import Cmd
import sys
import os
import shutil
import time

import FileManagerModule as FileManager
import HwpModule as Hwp
import KakaoModule as Kakao
import NotionModule as Notion

#This is Main Function. The Ultimate Start Point of WhaleOS.
class Prompt(Cmd):
    # Cmd Module functions
    # Variables
    prompt = "WhaleOS> "
    intro = "WhaleOS version 1.0.0-221019-1 (linux edition)\n" + \
            "Copyright (c) 2022 Chaemin Lim\n" + \
            "The Ultimate Operating System for Team Management\n" + \
            "Type 'help' for more detail.\n"
    ruler = ""

    # Functions
    def default(self, line):
        print(f"Unknown command : {line}\nType 'help' for help.")


    # Helper functions
    # checkargv
    def checkargv(self, argv, argc, more = True, less = True):
        """
        Check number of argument is correct.
        If correct, return True and False if not correct.
        Set 'more' option False to ignore argument overflow.
        Set 'less' option False to ignore argument underflow.
        """

        argn = len(argv.split())
        
        if argn > argc and more:
            print(f"*** too many arguments : takes {argc} but {argn} were given")
            return False
        if argn < argc and less:
            print(f"*** too few arguments : takes {argc} but {argn} were given")
            return False
        
        return True


    # Main command functions
    # exit
    def help_exit(self):
        print("exits the WhaleOS")
        print("usage : exit <no args>")

    def do_exit(self, argv):
        print("exit")
        return True
    
    # dupcheck
    def help_dupcheck(self):
        print("check duplication of file")
        print("usage : dupcheck <directory> [<directory> ... <directory>]")

    def do_dupcheck(self, argv):
        if not self.checkargv(argv, 1, more = False):
            return
        
        FileManager.checker.checkDuplicate(argv.split(), {}, None)

Prompt().cmdloop()
