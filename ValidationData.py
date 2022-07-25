
def checkElementID(str,uniqueElements):
    ID = str[0]
    if int(ID) > 0:
        if int(ID) not in uniqueElements:
            uniqueElements.add(int(ID))
        else:
            raise ValueError("ID is duplicate")
    else:
        raise ValueError("ID is negative")

def checkCustomerID(str):
    CustID = str[1]
    if int(CustID) < 0:
        raise ValueError("CustID is negative")

def checkCustomerFirstName(str):
    FirstName = str[2]
    for eachChar in FirstName:
        if len(FirstName) > 30:
            raise ValueError("The Name is longer than 30 characters")
        if not eachChar.isalpha():
            raise ValueError("There can be no special Characters")

def checkCustomerLastName(str):
    LastName = str[3]
    for eachChar in LastName:
       if len(LastName) > 30:
            raise ValueError("The Name is longer than 30 characters")
       if not eachChar.isalpha():
            raise ValueError("There can be no special Characters")

def checkChannelNumber(str):
    ChannelNumber = int(str[4])
    if ChannelNumber < 0:
        raise ValueError("ChannelNumber is negative")
    elif ChannelNumber < 100 or ChannelNumber > 1500:
        raise ValueError("ChannelNumbe not within valid range")

def checkStartWatchTime(str):
    startTime = int(str[5])
    if startTime < 0 or startTime > 2359:
        raise ValueError("StartWatchTime is invalid")

def checkEndWatchTime(str):
    EndTime = int(str[6])
    if EndTime < 0 or EndTime > 2359:
        raise ValueError("EndWatchTime is invalid")

def checkCustomerAge(str):
    age = int(str[7])
    if age < 0:
        raise ValueError("Age is negative")
    elif age < 15 or age > 121:
        raise ValueError("Age not in valid range")

