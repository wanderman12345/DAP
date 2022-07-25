
def checkElementID(str,uniqueElements):
    ID = str[0]
    if int(ID) > 0:
        if int(ID) not in uniqueElements:
            uniqueElements.append(int(ID))
        else:
            raise ValueError("ID is duplicate")
    else:
        raise ValueError("ID is negative")


def checkCustomerID(str):
    

    return
def checkCustomerFirstName(str):
    return
def checkCustomerLastName(str):
    return
def checkStartWatchTime(row):
    return
def checkEndWatchTime(row):
    return
def checkChannelNumber(row):
    return
def checkCustomerAge(row):
    return
