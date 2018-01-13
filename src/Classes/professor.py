"""
Professor Class

"""

import random
import json

from assignment import Assignment
from datetime import date


class DateEncoder(json.JSONEncoder):
    """JSON Encoder for Date Class"""
    def default(self, obj):
        if isinstance(obj, date):
            return str(obj.year) + " " + str(obj.month) + " " + str(obj.day)
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)


class Professor(object):
    """Professor class
Attributes:
Name: The name of the professor.

"""

    def __init__(self, name="Sohee Kang"):
        """Initializes the Professor class"""
        self.name = name
        self.directory = open("directory.json", 'a')

    def __str__(self):
        """String representation of Professor Object.
Returns:
    outp: The string representation of Professor Object.
"""

        outp = "Name: {};".format(self.name)
        return outp

    def make_assignment(self):
        """Creates a new Assignment object and calls
        Assignment.build_assignment()"""
        a_id = int(input("Please enter the ID of this assignment."))
        a_syear = int(input("Please enter the startdate of this assignment."))
        a_smonth = int(input())
        a_sday = int(input())
        a_dyear = int(input("Please enter the duedate of this assignment."))
        a_dmonth = int(input())
        a_dday = int(input())
        assignment_in_works = Assignment(
            a_id, start_date=date(a_syear, a_smonth, a_sday),
            due_date=date(a_dyear, a_dmonth, a_dday))
        assignment_in_works.build_assignment()
        self.directory.write(json.dumps(a_id)+'\n'+
                             json.dumps(date(a_syear, a_smonth, a_sday), cls=DateEncoder)+
                             '\n'+json.dumps(date(a_dyear, a_dmonth, a_dday), cls=DateEncoder)+'\n')

if __name__ == '__main__':
    prof = Professor()
    while(True):
        command = input("Enter MA to create an assignment, and EX to exit.")
        if (command == "EX"):
            break
        elif (command == "MA"):
            prof.make_assignment()
