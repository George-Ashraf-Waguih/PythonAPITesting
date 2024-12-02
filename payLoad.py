from utilities.configurations import *


def addBookPayload(isbn, aisle):
    body = {

        "name": "Learn Appium Automation with Java",
        "isbn": isbn,
        "aisle": aisle,
        "author": "Geo Ash"
    }
    return body


def buildPayLoadFromDB(query):
    # add payload from db instead of hardcoded

    addBody = {}
    tp = getQuery(query)
    addBody['name'] = tp[0]
    addBody['isbn'] = tp[1]
    addBody['aisle'] = tp[2]
    addBody['author'] = tp[3]
    return addBody