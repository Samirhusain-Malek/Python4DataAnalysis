#Crimes by month

import pylab
import numpy as np
import matplotlib.pyplot as plt

#sns.set_style("darkgrid")

class CrimeMonth:
    def __init__(self, data,larceny,assault,drug,vehicle,vandalism,burglary):
        self.data=data
        self.larceny=larceny
        self.assault=assault
        self.drug=drug
        self.vehicle=vehicle
        self.vandalism=vandalism
        self.burglary=burglary
    
    def getYvalues(self):
        y0 = self.larceny.groupby('Month').size().get_values()
        y1 = self.assault.groupby('Month').size().get_values()
        y2 = self.drug.groupby('Month').size().get_values()
        y3 = self.vehicle.groupby('Month').size().get_values()
        y4 = self.vandalism.groupby('Month').size().get_values()
        y5 = self.burglary.groupby('Month').size().get_values()
        return y0,y1,y2,y3,y4,y5
        
    def PlotCrimeMonth(self):
        pylab.rcParams['figure.figsize'] = (16.0, 8.0)

        monthsIdx = self.data.groupby('Month').size().keys() - 1
        monthsLit = ['January', 'February', 
                    'March', 'April', 'May', 
                    'June', 'July','August', 
                    'September', 'October', 'Novemeber', 'December']
        occursByMonth = self.data.groupby('Month').size().get_values()

        # Linear plot for all crimes
        ax1 = plt.subplot2grid((3,3), (0,0), colspan=3)
        ax1.plot(monthsIdx, occursByMonth, 'ro-', linewidth=2)

        ax1.set_title ('All Crimes', fontsize=20)

        start, end = ax1.get_xlim()
        ax1.xaxis.set_ticks(np.arange(start, end, 1))
        ax1.set_xticklabels(monthsLit)
        # ensure that ticks are only at the bottom and left parts of the plot
        ax1.get_xaxis().tick_bottom()
        ax1.get_yaxis().tick_left()

        # Linear normalized plot for 6 top crimes
        ax2 = plt.subplot2grid((3,3), (1,0), colspan=3, rowspan=2)

        y = np.empty([6,12])
        y[0],y[1],y[2],y[3],y[4],y[5]=self.getYvalues()

        crimes = ['Larceny/theft', 'Assault', 'Drug', 'Vehicle', 'Vandalism', 'Burglary']
        color_sequence = ['#1f77b4', '#ff7f0e', '#2ca02c','#d62728', '#9467bd', '#8c564b']
    
        h=[None]*6
        for i in range(0,6):
            y[i]= (y[i]-min(y[i]))/(max(y[i])-min(y[i]))  # normalization
            h[i] = ax2.plot(monthsIdx, y[i],'o-', color=color_sequence[i], lw=2)

        ax2.set_ylabel("Crime occurences by month, normalized")

        ax2.xaxis.set_ticks(np.arange(start, end+2, 1))
        ax2.set_xticklabels(monthsLit)

        ax2.legend((item[0] for item in h), 
            crimes, 
            bbox_to_anchor=(0.87, 1), loc=2, borderaxespad=0., frameon=False)

        pylab.gcf().text(0.5, 1.00, 
                'San Franciso Crime Occurence by Month',
                horizontalalignment='center',
                verticalalignment='top', 
                fontsize = 28)
        plt.show()
        