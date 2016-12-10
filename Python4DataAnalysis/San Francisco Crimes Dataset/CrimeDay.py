#Crimes by day of week

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt



class CrimeDay:
    def __init__(self, data,larceny,assault,drug,vehicle,vandalism,burglary):
        self.data=data
        self.larceny=larceny
        self.assault=assault
        self.drug=drug
        self.vehicle=vehicle
        self.vandalism=vandalism
        self.burglary=burglary
    
    def getYvalues(self):
        y0 = self.larceny.groupby('DayOfWeek').size().get_values()
        y1 = self.assault.groupby('DayOfWeek').size().get_values()
        y2 = self.drug.groupby('DayOfWeek').size().get_values()
        y3 = self.vehicle.groupby('DayOfWeek').size().get_values()
        y4 = self.vandalism.groupby('DayOfWeek').size().get_values()
        y5 = self.burglary.groupby('DayOfWeek').size().get_values()
        return y0,y1,y2,y3,y4,y5
        
    def PlotCrimeDay(self):
        
        sns.set_style("darkgrid")
        plt.style.use('ggplot')

        daysOfWeekIdx = self.data.groupby('DayOfWeek').size().keys()
        daysOfWeekLit = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        occursByWeek = self.data.groupby('DayOfWeek').size().get_values()

        # Linear plot for all crimes
        ax1 = plt.subplot2grid((3,3), (0,0), colspan=3)
        ax1.plot(daysOfWeekIdx, occursByWeek, 'ro-', linewidth=2)
        ax1.set_xticklabels(daysOfWeekLit)
        ax1.set_title ('All Crimes', fontsize=20)
        # ensure that ticks are only at the bottom and left parts of the plot
        ax1.get_xaxis().tick_bottom()
        ax1.get_yaxis().tick_left()

        # Bar plot
        y = np.empty([6,7])
        h = [None]*6
        width = 0.1

        ax2 = plt.subplot2grid((3,3), (1,0), colspan=3)
        y[0],y[1],y[2],y[3],y[4],y[5]=self.getYvalues()
        color_sequence = ['#1f77b4', '#ff7f0e', '#2ca02c','#d62728', '#9467bd', '#8c564b']

        for i in range(0,6):
            h[i] = ax2.bar(daysOfWeekIdx + i*width, y[i], width, color=color_sequence[i], alpha = 0.7)

        ax2.set_xticks(daysOfWeekIdx + 3*width)
        ax2.set_xticklabels(daysOfWeekLit)
        # ensure that ticks are only at the bottom and left parts of the plot
        ax2.get_xaxis().tick_bottom()
        ax2.get_yaxis().tick_left()

        ax2.legend((item[0] for item in h), 
                ('Larceny', 'Assault', 'Drug', 'Vehicle', 'Vandalism', 'Burglary'), 
                bbox_to_anchor=(0.88, 1), loc=2, borderaxespad=0., frameon=False)

        ax1.set_title("San Fransisco Crime Occurence by the Day of Week", x=0.5, y=1, fontsize=35)



        plt.show()