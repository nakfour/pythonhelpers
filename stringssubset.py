class StringSubset(object):
    def __init__(self):
        print("Init")
    def IsStringASubset(self, String1, String2):
        isContined =  False
        for char in String1:
            for char2 in String2:
                if char == char2:
                    isContined = True
        return isContined