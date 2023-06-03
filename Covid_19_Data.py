"""The code below records answers to the following questions based on Covid case data:

What day was the first Covid case in Harrisonburg city? What about Rockingham county?
What was the day with the most Covid cases recorded in Harrisonburg and Rockingham? How many?
What was the 7-day period with the most Covid cases in either Harrisonburg or Rockingham? How many?

The CovidRecord class and NYT data parsing function were written by Jason Forsyth and the other functions and execution of
them were written by Alex Kreitzer
"""

class CovidRecord:
    """
    A simple class to hold record data from NYT database
    """

    def __init__(self, _date='', _county='', _state='', _fips=0, _cases=0, _death=0):
        """
        Default constructor for transforming each line of the file into data point

        :param _date: Date covid case was recorded
        :param _county: County in which data was recorded
        :param _state: State in which data was recorded
        :param _fips: Federal Information Processing Standards code
        :param _cases: Cumulative number of total cases recorded
        :param _death: Cumulative number of total deaths recorded
        """
        self.date = _date
        self.county = _county
        self.state = _state

        if _fips == '':
            self.fips = 0
        else:
            self.fips = int(_fips)
        self.cases = int(_cases)

        if _death == '':
            self.death = 0
        else:
            self.death = int(_death)


def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of points
    :param file_path: Path to data file
    :return: List of CovidRecord points
    """
    # data point list
    covid_data = list()

    # open the NYT file path
    fin = open(file_path)

    # get rid of the headers
    fin.readline()

    done = False

    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        elements = line.strip().split(",")

        new_point = CovidRecord((elements[0]), (elements[1]), (elements[2]),
                                (elements[3]), (elements[4]), (elements[5]))

        # to reduce file sizes, only grab Virginia points
        if new_point.state == 'Virginia':
            covid_data.append(new_point)

    return covid_data


def find_earliest_date(All_Data, location):
    """Parse the Covid class and returns the date of the first covid case in specified location
    :param All_Data: List of objects which has various type of data about each case of Covid-19
    :param location: String of a location where the data is being requested
    """

    # Creating variables to compare on each iteration
    previous_year = "2025"
    previous_month = "13"
    previous_day = "35"

    # Fetching all the of the dates of covid cases from specified location
    for point in All_Data:
        if point.county == location:

            # parse given date up into day, month, year

            year = point.date[0:4]
            month = point.date[5:7]
            day = point.date[8:10]


            # finding the oldest date in the data
            if year <= previous_year:
                if month <= previous_month:
                    if day <= previous_day:
                        first_case = point.date

            # adjusting old variables for next iteration
            previous_year = year
            previous_month = month
            previous_day = day

    print("The first Covid case in", location, "was", first_case)

    return first_case

def find_greatest_case_day(All_Data, location):
    """Parse the Covid database and return the max number of Covid Cases in a specified location
    as well as the date the max were recorded
    :param All_Data: List of objects which have many attributes related to Covid information
    :param location: String of a location where the data is being requested
    """

    #starting cumulative case number
    previous_case = 0
    max = 0

    # search through all the covid data and look through the points from a county of interest
    for object in All_Data:
        if object.county == location:
            # subtracting total cases from previous cumulative number of cases to find the cases of one day
            case_number = object.cases - previous_case
            # comparing each number of cases to find the maximum & finding date of the max
            if case_number > max:
                max = case_number
                date = object.date

            # replace previous case with the new case total
            previous_case = object.cases

    print("The greatest number of cases in", location, "was", max, "and was recorded on", date)

    return max,date

def sum_list_indexes(nums, x, y):
    """
    Function which finds the sum of specified indeces in a list
    :param nums: list that is being iterated over
    :param x: starting index
    :param y: final index
    :return: sum of elements from x to y
    """

    sum_range = 0
    for i in range(x, y, 1):
        sum_range += nums[i]
    return sum_range
def find_greatest_week(All_Data, location1, location2):

    #lists to hold objects from both locations
    location1_list = list()
    location2_list = list()

    #lists of dates that will connect case values to a date
    list_of_dates_1 = list()
    list_of_dates_2 = list()

    # cumulative case number for each location
    case_count_1 = 0
    case_count_2 = 0


    #finding the objects from location 1 and 2 and placing them in a list
    for value in All_Data:
        if value.county == location1:


            #find cases in one day and place in location1 list
            one_day_1 = value.cases - case_count_1
            location1_list.append(one_day_1)
            case_count_1 = value.cases



            list_of_dates_1.append(value.date)

        elif value.county == location2:

            #Find cases in one day and place in location2 list
            one_day_2 = value.cases - case_count_2
            location2_list.append(one_day_2)
            case_count_2 = value.cases

            #lists of dates that will connect case values to a date
            list_of_dates_2.append(value.date)

    #creating lists to store the sum of 7 day periods
    location_1_seven_day_list = list()
    location_2_seven_day_list = list()

    # go through location list for each 7 day period in the list
    index = 0
    for num in range(0,len(location1_list) - 6):
        seven_day_total = sum_list_indexes(location1_list,index,(index+6))
        location_1_seven_day_list.append(seven_day_total)
        index += 1
    index = 0

    #find total of 7 elements of a list from 0 to the length of the list for location 2
    for num in range(0,len(location2_list) - 6):

        #save the next 7 days of the list and place the sum in a new list
        seven_day_total = sum_list_indexes(location2_list,index,(index+6))
        location_2_seven_day_list.append(seven_day_total)
        index += 1











    #find the largest 7 day period from both locations and compare them
    x = max(location_1_seven_day_list)
    y = max(location_2_seven_day_list)

    if x > y:

        #find where in the data the 7 day period was and record that date
        x_idx = location_1_seven_day_list.index((x))

        start_of_week = list_of_dates_1[x_idx - 1]
        end_of_week = list_of_dates_1[x_idx + 5]

        print(location1, "had the most cases,",x, ", in a 7 day period and it was from", start_of_week, "to", end_of_week)


    if x < y:


        x_idx = location_2_seven_day_list.index(max(location_2_seven_day_list))

        start_of_week_2 = list_of_dates_2[x_idx]
        end_of_week_2 = list_of_dates_2[x_idx + 6]

        print(location2, "has the most cases,",y, "in a 7 day period and it is from", start_of_week_2, "to", end_of_week_2)










if __name__ == "__main__":
    # load covid data as list of CovidRecord objects
    data = parse_nyt_data('us-counties.csv')



    # find the earliest recorded Covid case in Rockingham County
    find_earliest_date(data, "Rockingham")

    # Find the earliest recorded Covid case in Harrisonburg City
    find_earliest_date(data, "Harrisonburg city")

    # Find the day with the most Covid cases in Harrisonburg and how many
    find_greatest_case_day(data, "Harrisonburg city")

    # find the day with the most Covid cases in Rockingham and how many
    find_greatest_case_day(data,"Rockingham")

    # find the week with the most Covid cases in either Harrisonburg or Rockingham
    find_greatest_week(data, "Harrisonburg city", "Rockingham")
