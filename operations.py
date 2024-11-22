import running_list
from data import CountyDemographics


#def fields(str):


   # pass




#not finished -- Returns a nicer formatted county
def prettify_county(county:CountyDemographics):
    pretty_county = ""
    pretty_county += county.county
    return pretty_county

#FINISHED -- Prints out the contents of the memory file to console
def display():
    """try:
        memory_file = open("Memory_County_List", "r")
    except FileNotFoundError:
        return "error: file not found"""
    for n in running_list.running_list:
        print(prettify_county(n))

def filter_state(state_abbreviation:str):
    output_list = []
    for n in running_list.running_list:
        if n.state == state_abbreviation:
            output_list.append(n)
    running_list.running_list = output_list
    return None



