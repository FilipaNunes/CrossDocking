import os
import pandas as pd
import jedi

data = pd.read_excel('data.xlsx')

# define data as a matrix
data.as_matrix()

i=0
j=0
same_client = [1] * len(data)

# the following cycle determines the number of packages to be delivered to a specific city
while i < len(data) - 1:
    # if the next iteration is verified it means that the packages are to be delivered to the same city
    if (data.iloc[i,1] == data.iloc[i+1,1]):
        # if the next iteration is verified it means that the packages are to be delivered to the same client
        if (data.iloc[i,2] == data.iloc[i+1,2]):
            # if the next iteration is verified then the arrival times of the packages are arriving with more than one day difference.
            # if this happen then the one with earliest EDD needs to have its dispatch delayed (a package can never spend more than 24 hours in the cross-dock)
            if(abs(data.iloc[i,3] - data.iloc[i+1,3])) > 1:
                #???????????????
                print(i)
            else:
                same_client[j] = same_client[j] + 1
        else:
            j = j + 1
        i = i + 1
    else:
        i = i + 1

print(same_client[:])
