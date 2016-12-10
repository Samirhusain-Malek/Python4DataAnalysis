#Crimes by hour
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

#sns.set_style("darkgrid")

class CrimeHr:
    def __init__(self, data,larceny,assault,drug,vehicle,vandalism,burglary):
        self.data=data
        self.larceny=larceny
        self.assault=assault
        self.drug=drug
        self.vehicle=vehicle
        self.vandalism=vandalism
        self.burglary=burglary
        
    
    def PlotCrimeHr(self):

        with plt.style.context('fivethirtyeight'):
            ax1 = plt.subplot2grid((3,3), (0,0), colspan=3)
            ax1.plot(self.data.groupby('Hour').size(), 'ro-')
            ax1.set_title ('All crimes')
            start, end = ax1.get_xlim()
            ax1.xaxis.set_ticks(np.arange(start, end, 1))
            
            ax2 = plt.subplot2grid((3,3), (1, 0))
            ax2.plot(self.larceny.groupby('Hour').size(), 'o-')
            ax2.set_title ('Larceny/Theft')
            
            ax3 = plt.subplot2grid((3,3), (1, 1))
            ax3.plot(self.assault.groupby('Hour').size(), 'o-')
            ax3.set_title ('Assault')
        
            ax4 = plt.subplot2grid((3,3), (1, 2))
            ax4.plot(self.drug.groupby('Hour').size(), 'o-')
            ax4.set_title ('Drug/Narcotic')
        
            ax5 = plt.subplot2grid((3,3), (2, 0))
            ax5.plot(self.vehicle.groupby('Hour').size(), 'o-')
            ax5.set_title ('Vehicle')
    
            ax6 = plt.subplot2grid((3,3), (2, 2))
            ax6.plot(self.vandalism.groupby('Hour').size(), 'o-')
            ax6.set_title ('Vandalism')
        
            ax7 = plt.subplot2grid((3,3), (2, 2))
            ax7.plot(self.burglary.groupby('Hour').size(), 'o-')
            ax7.set_title ('Burglary')
  
            sns.gcf().text(0.5, 1, 
                    'San Franciso Crime Occurence by Hour',
                     horizontalalignment='center',
                     verticalalignment='top', 
                     fontsize = 18)    
        #plt.tight_layout(1)
        plt.show()

