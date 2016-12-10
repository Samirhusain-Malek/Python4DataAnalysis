from Analysis1_CrimeCatg import CrimeCatg

import CrimeHr
import CrimeDay
import CrimeMon
import CrimeYear
import pandas as pd
import matplotlib.pyplot as plt


def readData(filepath):
        filename=filepath+"train.csv"
        data = pd.read_csv(filename, parse_dates=['Dates'], index_col='Dates')
        return data

#sys.path.append(os.path.abspath('C:/Userssaura/OneDrive/Documents/rohit/Analysis1_CrimeCatg'))

# Add new features to the dataset: Weekday (Monday, Tuesday...)
# Hour of day, Month, Year, Day of month
def updateData(data):
    data['DayOfWeek'] = data.index.dayofweek
    data['Hour'] = data.index.hour
    data['Month'] = data.index.month
    data['Year'] = data.index.year
    data['DayOfMonth'] = data.index.day
    
def typeOfCrime(data):
    larceny = data[data['Category'] == "LARCENY/THEFT"]
    assault = data[data['Category'] == "ASSAULT"]
    drug = data[data['Category'] == "DRUG/NARCOTIC"]
    vehicle = data[data['Category'] == "VEHICLE THEFT"]
    vandalism = data[data['Category'] == "VANDALISM"]
    burglary = data[data['Category'] == "BURGLARY"]
    return larceny,assault,drug,vehicle,vandalism,burglary
    

def main(): 
     
    print("\n\nChoose below options to run the specific distribution : \n")
    print("1. Crime Category report")
    print("2. Crime occurence per hour report")
    print("3. Crime occurence per day report")
    print("4. Crime occurence per month report")
    print("5. Crime occurence per year report")
    choice=input("Enter your response: ")  
       
    data=readData("/Users/rohitsingh/Documents/")
    #crimeCat = CrimeCatg.CrimeCatg(data)

    updateData(data)
    larceny,assault,drug,vehicle,vandalism,burglary = typeOfCrime(data)
    #crimeHr = CrimeHr.CrimeHr(data,larceny,assault,drug,vehicle,vandalism,burglary)    
    
    #crimeDay=CrimeDay.CrimeDay(data,larceny,assault,drug,vehicle,vandalism,burglary)
    #plt.figure(3)
    
    #crimeMonth=CrimeMon.CrimeMonth(data,larceny,assault,drug,vehicle,vandalism,burglary)
    
    #crimeYear=CrimeYear.CrimeYear(data,larceny,assault,drug,vehicle,vandalism,burglary)  
    
  
    
    if (choice=='1'):
        plt.figure(1)
        crimeCat = CrimeCatg.CrimeCatg(data)
        crimeCat.plotCrimeCat()
        main()
    elif (choice=='2'):
        plt.figure(2)
        crimeHr = CrimeHr.CrimeHr(data,larceny,assault,drug,vehicle,vandalism,burglary)   
        crimeHr.PlotCrimeHr()
    elif (choice=='3'):
        plt.figure(3)
        crimeDay=CrimeDay.CrimeDay(data,larceny,assault,drug,vehicle,vandalism,burglary)
        crimeDay.PlotCrimeDay()
    elif (choice=='4'):
        plt.figure(4)
        crimeMonth=CrimeMon.CrimeMonth(data,larceny,assault,drug,vehicle,vandalism,burglary)
        crimeMonth.PlotCrimeMonth()
    elif (choice=='5'):
        plt.figure(5)
        crimeYear=CrimeYear.CrimeYear(data,larceny,assault,drug,vehicle,vandalism,burglary)
        crimeYear.PlotCrimeYear()
    else:
        print("Sorry! wrong response")

'''
    for i in range(0,100):
        if (choice=='1'):
            plt.figure(1)
            crimeCat = CrimeCatg.CrimeCatg(data)
            crimeCat.plotCrimeCat()
            return
        elif (choice=='2'):
            plt.figure(2)
            crimeHr = CrimeHr.CrimeHr(data,larceny,assault,drug,vehicle,vandalism,burglary)   
            crimeHr.PlotCrimeHr()
        elif (choice=='3'):
            plt.figure(3)
            crimeDay=CrimeDay.CrimeDay(data,larceny,assault,drug,vehicle,vandalism,burglary)
            crimeDay.PlotCrimeDay()
        elif (choice=='4'):
            plt.figure(4)
            crimeMonth=CrimeMon.CrimeMonth(data,larceny,assault,drug,vehicle,vandalism,burglary)
            crimeMonth.PlotCrimeMonth()
        elif (choice=='5'):
            plt.figure(5)
            crimeYear=CrimeYear.CrimeYear(data,larceny,assault,drug,vehicle,vandalism,burglary)
            crimeYear.PlotCrimeYear()
        else:
            print("Sorry! wrong response")
        
        
        print("\n\nChoose below options to run the specific distribution : \n")
        print("1. Crime Category report")
        print("2. Crime occurence per hour report")
        prin t("3. Crime occurence per day report")
        print("4. Crime occurence per month report")
        print("5. Crime occurence per year report")
        choice=raw_input("Enter your response: ") 
        
        if choice=='q':
            break;

'''


main()            
             
        
        
    





