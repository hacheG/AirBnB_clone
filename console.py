#!/usr/bin/python3

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
#import time
#import shlex
from models import theClasses
import cmd

class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_EOF(self, args):
        """end_of_file"""
        print("end of file")
        return True

    def do_quit(self, args):
        """Quit command to exit the program"""
        print("chao bye")
        return True

    def emptyline(self):
        """don't make nothing"""
        pass
       
    def do_create(self, args):
        #creates a new instance
        #print(type(args))
        if len(args) == 0:
            print("** class name missing **")
            return
        
        token = args.split()

        try:
            newInstance = eval(token[0])()
            #time.sleep(2)
            newInstance.save()
            #time.sleep(2)
            print(newInstance.id)
        except:
            print("** class doesn't exist **")
    


    def do_show(self, args):
        """Prints the string representation of an instance"""
        token = args.split()

        if len(args) == 0:
            print("** class name missing **")
            return
        
        if token[1] == 0:
            print("** instance id missing **")
        
        #print(token[0])
        #print(token[1])

        try:
            eval(token[0])
        except:
            print("** class doesn't exist **")

        objDict = storage.all()
        keyId = token[0] + "." + token[1]

        try:
            value = objDict[keyId]
            print(value)
        except:   
            print("** no instance found **")    

    def do_destroy(self, args):
        """Deletes an instance based on the class name"""
        token = args.split()

        if len(args) == 0:
            print("** class name missing **")
            return
        
        if token[1] == 0:
            print("** instance id missing **")

        try:
            eval(token[0])
        except:
            print("** class doesn't exist **")
        
        objDict = storage.all()
        keyId = token[0] + "." + token[1]  

        try:
            del objDict[keyId]
        except:   
            print("** no instance found **")
        storage.save()
    """
    def do_all(self, args):
        Prints all string representation of all instances
        token = args.split()

        try:
            eval(token[0])
        except:
            print("** class doesn't exist **")
        
        newList = []
        objDict = storage.all()

        for key, val in objDict.items():
            if len(args) != 0:
                if type(val) is eval(val):
                    newList.append(val)
            else:
                newList.append(val)
        print(newList)
    """
    def do_all(self, arg):
        """ Prints string represention of all instances of a given class """

        if not arg:
            print("** class name missing **")
            return

        token = arg.split(' ')

        if token[0] not in theClasses:
            print("** class doesn't exist **")
        
        else:
            all_objs = storage.all()
            newList = []

            for key, val in all_objs.items():
                ob_name = val.__class__.__name__
                if ob_name == token[0]:
                    newList += [val.__str__()]
            print(newList)





    def do_update(self, args):
        pass    

    
if __name__ == "__main__":
    console = HBNBCommand()
    console.cmdloop()