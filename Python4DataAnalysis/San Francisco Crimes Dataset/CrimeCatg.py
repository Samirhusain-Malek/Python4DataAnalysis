import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


class CrimeCatg:
    def __init__(self, data):
        self.data=data
    
    
    def plotCrimeCat(self):
        crimes_rating = self.data['Category'].value_counts()
        print (crimes_rating)
        y_pos = np.arange(len(crimes_rating[0:18].keys()))
        plt.barh(y_pos, crimes_rating[0:18].get_values(),  align= 'center', alpha= 1, color = 'blue')
        plt.yticks(y_pos, map(lambda x:x.title(),crimes_rating[0:18].keys()), fontsize = 10)
        plt.xlabel('Number of occurences', fontsize = 14)
        plt.title('San Franciso Crimes', fontsize = 28)
        plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
        plt.show()

    



    
    
        

        
