from collections import Counter

class IsRansomNotePossible(object):
    def __init__(self):
        print("Init")
    def returnPossiblity(self, magazine, ransomenote):
        magazineCountofWords = Counter(magazine.split())
        ransomenoteCountofWords = Counter(ransomenote.split())
        print(magazineCountofWords)
        print(ransomenoteCountofWords)
        print(ransomenoteCountofWords - magazineCountofWords)
        if  not (ransomenoteCountofWords - magazineCountofWords):
            return "Yes"
        else:
            return "No"