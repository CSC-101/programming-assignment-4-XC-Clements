import running_list
from data import CountyDemographics


def fields(field:str, county:CountyDemographics):
    field_prop = ""
    if field == "Education.Bachelor's Degree or Higher":
        field_prop = county.education["Bachelor's Degree or Higher"]
    elif field == "Education.High School or Higher":
        field_prop = county.education["High School or Higher"]
    elif field == "Ethnicities.American Indian and Alaska Native Alone":
        field_prop = county.ethnicities["American Indian and Alaska Native Alone"]
    elif field == "Ethnicities.Asian Alone":
        field_prop = county.ethnicities["Asian Alone"]
    elif field == "Ethnicities.Black Alone":
        field_prop = county.ethnicities["Black Alone"]
    elif field == "Ethnicities.Hispanic or Latino":
        field_prop = county.ethnicities["Hispanic or Latino"]
    elif field == "Ethnicities.Native Hawaiian and Other Pacific Islander Alone":
        field_prop = county.ethnicities["Native Hawaiian and Other Pacific Islander Alone"]
    elif field == "Ethnicities.Two or More Races":
        field_prop = county.ethnicities["Two or More Races"]
    elif field == "Ethnicities.White Alone":
        field_prop = county.ethnicities["White Alone"]
    elif field == "Ethnicities.White Alone, not Hispanic or Latino":
        field_prop = county.ethnicities["White Alone, not Hispanic or Latino"]
    elif field == "Income.Persons Below Poverty Level":
        field_prop = county.income["Persons Below Poverty Level"]
    return field_prop






#not finished -- Returns a nicer formatted county
def prettify_county(county:CountyDemographics):
    pretty_county = ""
    pretty_county += county.county
    return pretty_county

#FINISHED -- Prints out the contents of the memory file to console
def display():
    for n in running_list.running_list:
        print(n.county + ", " + n.state)
        print("\tPopulation: {}".format(n.population["2014 Population"]))

        print("\tAge:")
        print("\t\t<5: {}%".format(n.age['Percent Under 5 Years']))
        print("\t\t<18: {}%".format(n.age['Percent Under 18 Years']))
        print("\t\t>65: {}%".format(n.age['Percent 65 and Older']))

        print("\tEducation:")
        print("\t\t Bachelor's Degree or Higher: {}%".format(n.education["Bachelor's Degree or Higher"]))
        print("\t\t High School Diploma or Higher: {}%".format(n.education['High School or Higher']))

        print("\tEthnicity:")
        print("\t\t {}".format(n.ethnicities))
        print("\t\t American Indian and Alaska Native Alone: {}%".format(n.ethnicities['American Indian and Alaska Native Alone']))
        print("\t\t Asian Alone: {}%".format(n.ethnicities['Asian Alone']))
        print("\t\t Black Alone: {}%".format(n.ethnicities['Black Alone']))
        print("\t\t Hispanic or Latino: {}%".format(n.ethnicities['Hispanic or Latino']))
        print("\t\t Native Hawaiian and Other Pacific Islander Alone: {}%".format(n.ethnicities['Native Hawaiian and Other Pacific Islander Alone']))
        print("\t\t Two or More Races: {}%".format(n.ethnicities['Two or More Races']))
        print("\t\t White Alone: {}%".format(n.ethnicities['White Alone']))
        print("\t\t White Alone, not Hispanic or Latino: {}%".format(n.ethnicities['White Alone, not Hispanic or Latino']))

        print("\tIncome:")
        print("\t\t Per Capita Income: {}%".format(n.income['Per Capita Income']))
        print("\t\t Persons Below Poverty Level: {}%".format(n.income['Persons Below Poverty Level']))
        print("\t\t Median Household Income: {}%".format(n.income['Median Household Income']))




#FINISHED
def filter_state(state_abbreviation:str):
    output_list = []
    filtered_count = 0
    for n in running_list.running_list:
        if n.state == state_abbreviation:
            output_list.append(n)
            filtered_count += 1
    running_list.running_list = output_list
    print("Filter: state == {} ({} entries)".format(state_abbreviation, filtered_count))
    return None

def filter_gt(field:str, number:int):
    output_list = []
    for n in running_list.running_list:
        field_prop = fields(field, n)
        if field_prop > number:
            output_list.append(n)
    running_list.running_list = output_list
    return None

def filter_lt(field:str, number:int):
    output_list = []
    for n in running_list.running_list:
        field_prop = fields(field, n)
        if field_prop < number:
            output_list.append(n)
    running_list.running_list = output_list
    return None

def population(field:str):
    output_population = 0
    for n in running_list.running_list:
        field_prop = fields(field, n)
        output_population += n.population['2014 Population'] * (field_prop / 100.0)
    print("2014 {} population: {}".format(field, output_population))
    return output_population

def percent(field:str):
    total_population = 0
    for n in running_list.running_list:
        total_population += n.population['2014 Population']
    portion_population = 0
    for n in running_list.running_list:
        field_prop = fields(field, n)
        portion_population += n.population['2014 Population'] * (field_prop / 100.0)
    percent_portion = (portion_population / total_population)
    print("2014 {} percentage: {}".format(field, percent_portion))
    return percent_portion



def population_total():
    total_population = 0
    for n in running_list.running_list:
        total_population += n.population['2014 Population']
    print("2014 population: {}".format(total_population))
    return total_population




