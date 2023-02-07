def powerset(inputSet, subset=[]): #creating another subset
    #if the inputset is empty returns the subset 
    if not inputSet:
        return [subset]