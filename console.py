#!/usr/bin/python3
"""Module to be used as the entry point of the comand interpreter"""


import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""

    prompt = '(hbnb) '

    def emptyline(self):
        """handles empty line"""

        pass

    def do_EOF(self, line):
        """hanldes EOF"""

        return True

    def help_EOF(self):
        """help for EOF"""

        print("CTRL + D to exit the program")
        print()

    def do_quit(self, line):
        """handles quit command"""

        return True

    def help_quit(self):
        """help for quit command"""

        print("Quit command to exit the program")
        print()

    def do_create(self, class_name):
        if(class_name is None):
            print("** class name missing **")
        else if (class_name != 'BaseModel'):
            
        


if __name__ == '__main__':
    HBNBCommand().cmdloop()
