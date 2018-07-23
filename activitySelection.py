#!/usr/bin/env python

"""
You are given n activities with their start and finish times.
Select the maximum number of activities that can be performed by a single person,
assuming that a person can only work on a single activity at a time.
The greedy choice is to always pick the next activity whose finish time is least among the remaining activities
and the start time is more than or equal to the finish time of previously selected activity.
We can sort the activities according to their finishing time so that we always consider the next activity as minimum finishing time activity.
"""

class Activity:
    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.finish = end

    def __str__(self):
        return "Name: " + self.name + "\t" + "Start: " + str(self.start) + "\t" + "Finish: " + str(self.finish)


class Greedy:
    def __init__(self):
        self.activities = []
    
    def add_activity(self, activity):
        self.activities.append(activity)
    
    def select_activities(self):
        sorted(self.activities, key=lambda x: x.finish)
        print self.activities[0]

        i = 0
        for j in range(1, len(self.activities)):
            if self.activities[i].finish <= self.activities[j].start:
                print self.activities[j]
                i = j

if __name__ == "__main__":
    a1 = Activity("A1", 1, 2)
    a2 = Activity("A2", 3, 4)
    a3 = Activity("A3", 0, 6)
    a4 = Activity("A4", 5, 7)
    a5 = Activity("A5", 8, 9)
    a6 = Activity("A6", 5, 9)
    greedy = Greedy()
    greedy.add_activity(a1)
    greedy.add_activity(a2)
    greedy.add_activity(a3)
    greedy.add_activity(a4)
    greedy.add_activity(a5)
    greedy.add_activity(a6)
    greedy.select_activities()
