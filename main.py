import sys
import operations
import running_list
from operations import prettify_county
from running_list import init_running_list


def can_opener():
    #Initalizes the running list of counties to then be modified
    running_list.init_running_list()

    #Tries to open the operations file
    try:
        op_file = open(sys.argv[1], "r")
    except IndexError:
        return "error: no argument provided"
    except FileNotFoundError:
        return "error: file not found"

    #Splits into each operation and executes
    for line in op_file:
        better_line = line.replace("-", "_")
        stripped_line = better_line.strip("\n")
        split_line = stripped_line.split(":")
        #Finds all the arguments in the line and converts them into a string to run
        args = []
        try:
            for n in range(1, len(split_line)):
                args.append(split_line[n])
        except IndexError:
            pass
        args_str = ", ".join(args)
        command = ("operations." + split_line[0] + "(" + str(args_str) + ")")
        new_command = "operations.filter_state('CA')"
        eval(new_command)


def hello(abc:str):
    print(abc)
if __name__ == '__main__':
    running_list.init_running_list()
    arg = "CA"
    eval("operations.filter_state(arg)")
    can_opener()