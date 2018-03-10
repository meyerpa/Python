"""
16.10 Living People
Given a list of people with their birth and eath years, implement a method to
compute the year with the most number of people alive. You may assume that
all people were born between 1900 and 2000 (inclusive). If a person was alive
during any portion of that year, they should be included in that year's count.
For example, Person (birth = 1908, death = 1909) is included in the counts
for both 1908 and 1909.
"""

rateChange = {
    1900: 0,
    1901: 0,
    1902: 0,
    1903: 0,
    .
    .
    .
}

def updateYears(yearInfo, peopleInfo):
    """Updates yearInfo with the change in people each year"""
    for person in peopleInfo:
        # update birth year
        yearInfo[person.birth] += 1
        # update year following a death
        yearInfo[person.death + 1] -= 1
    return yearInfo

def maxPeople(yearInfo, peopleInfo):
    """Returns the year with the most people. If no change in population,
    returns 1900."""

    # update yearInfo with the population
    yearInfo = updateYears(yearInfo, peopleInfo)
    # iterate through the years, to find the maximum population
    current = 0
    maxPop = 0
    maxYear = 1900
    for year, change in yearInfo.items():
        current += change
        if current > maxPop:
            maxPop = current            # update maximum
            maxYear = year              # update current maximum year
    return maxYear
