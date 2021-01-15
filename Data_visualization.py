"""
Created on Wed Dec 23 14:25:37 2020

@author: Gunjan Gautam
"""

'''------------------------------------------------------------------------
 Import necessary libraries for the application 
---------------------------------------------------------------------------
'''
from sys import exit # imported for exit function to exit the application 
import pandas as pd  #  imported for dataframe processing 
from matplotlib import pyplot as plt #  imported using plot fucntions 
import seaborn as sns  #  imported using plot fucntions 


# Making dataframes from the given CSV databases
input_df1 = pd.read_csv("C:/Project/ProjectSpec_Dataset/NhanesDemoAdapted.csv")
input_df2 = pd.read_csv("C:/Project/ProjectSpec_Dataset/NhanesFoodAdapted.csv")


# Remove null values from the dataframes to avoid errors 
input_df1.dropna(inplace = True)
input_df2.dropna(inplace = True)

# Make a copies of the dataframes for safety
df1=input_df1
df2=input_df2

# Use describe function to familiarise with the contents of each dataframe.
df1.describe()
df2.describe()

# View top rows of dataframes
print(df1.head())
print(df2.head())

# Display the column names of the dataframes
print(df1.columns)
print(df2.columns)


'''--------------------------------------------------------------------------
Implement functions for the application to be called in the main function 
----------------------------------------------------------------------------
''' 

'''--------------------------------------------------------------------------
MENU OPTION 1
----------------------------------------------------------------------------
''' 

# Function to investigate the relationship between the average HouseholdIncome and ethnicity
def Household_income_per_ethnicity():
    
    # Use describe method to check the unique values in Ethnicity variable
    desc = df1["Ethnicity"].describe()
    # display
    print("\n Describe Ethnicity \n")
    print(desc)
    
    # Get the unique number of ethnities and print that 
    ethnicities = df1['Ethnicity'].nunique()
    print("\nNumber of ethenicities in the dataset:",ethnicities)
        
    # Print the sorted list of number of respondents per ethenicity:
    print("\n Number of respondents per ethenicity: ")    
    print(df1.groupby('Ethnicity')['Ethnicity'].count().sort_values(ascending=False))
    
    # Generate the newdataframe containing information only for adults based on age >=20
    newdf_adults = df1[df1['Age']>=20]    
          
    # Ontain the data for x-axis data point which denotes the average HouseholdIncome per ethnicity
    xaxis_data = newdf_adults.groupby('Ethnicity')['HouseholdIncome'].mean()
    
    # Ontain the data for y-axis
    yaxis_data = ['Asian','Black','Mexican-American','Other Hispanic','Others','White']
    
    # Plotting the horizontal bar graph  showing average HouseholdIncome per ethnicity
    plt.barh(yaxis_data, xaxis_data, color='orange',edgecolor='blue' )
    
    # Set a title of the current axes.
    plt.title('Average Household Income per ethnicity for only adult respondents')
    
    # Set the x and y labels.
    plt.xlabel("Household Income")
    plt.ylabel("Ethnicity")
        
    # Display a figure.
    plt.show() 
    
    
'''--------------------------------------------------------------------------
MENU OPTION 2
----------------------------------------------------------------------------
'''   
def Marital_status():    
    
    # New dataframe with respondents only aged 20 and over.
    newdf = input_df1[input_df1['Age']>19]    
    print('\n List of respondents only aged 20 and over')
    print('\n')
    
    # Display the sorted list indicating the number of respondents per marital status category.
    print(newdf.groupby('Marital Status')['Marital Status'].count().sort_values())  
    
    # Obtain the the points in 1st Quartile
    df_25 =  newdf.groupby('Marital Status')['Age'].quantile(.25)
    
    # Obtain the points in 2nd Quartile
    df_50 =  newdf.groupby('Marital Status')['Age'].quantile(.50)
    
    # Obtain the points in 3rd Quartile
    df_75 =  newdf.groupby('Marital Status')['Age'].quantile(.75)
    
    xaxis = ['1','2','3','4','5','6']
    
    # plotting the points in 1st Quartile
    plt.plot(xaxis, df_25, linewidth=2,linestyle =  'dashed', label = "1st Quartile") 
    
    # plotting the points in 2nd Quartile
    plt.plot(xaxis, df_50, linewidth=2, linestyle =   'dashdot',label = "2nd Quartile")
    
    # plotting the points in 3rd Quartile
    plt.plot(xaxis, df_75, linewidth=2, linestyle =  'solid',label = "3rd Quartile")
    
    # Set the x and y labels.    
    plt.xlabel('Marital Status')    
    plt.ylabel('Age')
    
    # Set a title of the current axes.
    plt.title('Line graph to display the 1st, 2nd, and 3rd quartiles of Age for each Marital Status')
    
    # show a legend on the plot
    plt.legend()
    
    # Display a figure.
    plt.show()
    
'''--------------------------------------------------------------------------
MENU OPTION 3
----------------------------------------------------------------------------
'''
    
def Income_and_education_level():
    
    # Ask user's integer choice for IncomePovertyRatio or HouseholdIncome for further processing 
    choice = int(input("For the plot enter 1 for IncomePovertyRatio or 2 for HouseholdIncome :\n"))
    
    # Create a list that inlcudes each possible education level in the dataset
    ed_level = ['0','1','2','3','4','5']
    
    # Generate simple bar graph based on the choice entered by user 
    if (choice == 1): #  Represents IncomePovertyRatio as the entered choice
    
        # Obtain data points that represents average IncomePovertyRatio for each education level
        option1 = df1.groupby('Education')['IncomePovertyRatio'].mean()        
        
        # Generate simple bar graph to show average IncomePovertyRatio for each education level
        plt.bar(ed_level,option1,color='green',edgecolor='blue')   
        
        # Set a title of the current axes.
        plt.title('Correlation between Education and Income Poverty Ratio')
        
        # Set the x and y labels.  
        plt.xlabel("Education levels")
        plt.ylabel("Income Poverty Ratio")  
        
        # Display a figure.
        plt.show()
        
    elif(choice == 2): #  Represents HouseholdIncome as the entered choice
    
        #Obtain data points that represents average HouseholdIncome for each education level
        option2 = df1.groupby('Education')['HouseholdIncome'].mean()
        
        # Generate simple bar graph to show average HouseholdIncome for each education level
        plt.bar(ed_level,option2, color='pink',edgecolor='red')
        
        # Set a title of the current axes.
        plt.title('Correlation between Education and Household Income')
        
        # Set the x and y labels.  
        plt.xlabel("Education levels")
        plt.ylabel("Household Income")
        
        # Display a figure.
        plt.show()
        
    else:
        print('Run again and Please enter 1 or 2  as per the above choice')
        
'''--------------------------------------------------------------------------
MENU OPTION 4
----------------------------------------------------------------------------
'''
    
# Function that takes two dataframes (demographic data and dietary data as input
def Diet_analysis(input_df1,input_df2): 
    
    # Create new dataframe (from dietary data) that contains average food intake per meal per individual
    new_diet_data = input_df2.groupby('SEQN')[['dGRMS','dKCAL','dPROT','dCARB','dSUGR','dFIBE','dTFAT','dSFAT','dCHOL','dVITC','dVITD','dCALC','dCAFF','dALCO']].mean() 
    
    # Merge the newly created dataframe to the existing demographic dataframe
    merged_df = pd.merge(input_df1, new_diet_data,on='SEQN')
    
    # Write the merged dataframe to a csv file in the current directory with no additional index
    merged_df.to_csv('Gunjan_Gautam_merged.csv', sep=',',index=False)
    
    # Create a list of avalable nutrients 
    nutrients = ['dGRMS','dKCAL','dPROT','dCARB','dSUGR','dFIBE','dTFAT','dSFAT','dCHOL','dVITC','dVITD','dCALC','dCAFF','dALCO']
    
    # Create index for each avalable nutrients 
    valid_index = list(range(0,15))
    
    # Obtain the number of avalable nutrients 
    count = len(nutrients)
    
    # Display the list of nutrients and asked the user to select a category based on index
    print('\n The following nutrients are available: ') 
    for i in nutrients:
        print(count-14,i)
        count = count+1
    print('\n Which above categories do you wish, please enter the number :')     
    
    # Initialize variable to store user's choice 
    nutrients_choice = None
    
    # Continue asking user to enter a valid value based on the above index until the correct choice is not entered
    while nutrients_choice not in valid_index:
        input_value = input() 
        try:
            nutrients_choice = int(input_value)            
        except ValueError:
             # tell the user off
             print("{input} is not a valid number , please enter a number from the index".format(input=nutrients_choice))
             
    # Obtain the the variable for y-axis based on user's entered choice
    y_var = nutrients[nutrients_choice]  
    
    # Create a new figure     
    plt.figure()
    sns.boxplot(y=merged_df[y_var], x=merged_df['Gender'],data=merged_df,palette="colorblind",hue='Gender').set(title='Gender-wise nutrients status via Boxplot')
    
    # Create a new figure 
    plt.figure()    
    sns.boxplot(y=merged_df[y_var], x=merged_df['Ethnicity'],data=merged_df,palette="dark",hue='Ethnicity').set(title='Ethnicity-wise nutrients status via Boxplot')
    
    # Create a new figure 
    plt.figure()    
    sns.boxplot(y=merged_df[y_var], x=merged_df['Education'],data=merged_df,palette="Set2",hue='Education').set(title='Education level wise nutrients status via Boxplot')
       
    # Create a new figure 
    plt.figure() 
    
    # Single scatter plot to visualize  the selected category vs HouseholdIncome and Age
    plt.scatter(merged_df[y_var], merged_df['HouseholdIncome'], color='r', edgecolors='blue')
    plt.scatter(merged_df[y_var], merged_df['Age'], color='g', edgecolors='black')
    
    # Set the title of the plot
    plt.title('Scatter plot for the selected nutrient to compare with HouseholdIncome and Age'),
    
    # Set the x and y labels 
    plt.xlabel('Age')
    plt.ylabel('Household Income')
    
    # Display the figures
    plt.show()  
    
    # Create a new figure 
    plt.figure() 
    
    # Scatter plot for comparing HouseholdIncome and Age    
    plt.scatter( merged_df['Age'], merged_df['HouseholdIncome'], color='orange', edgecolors='purple')
    
    # Set the title of the plot 
    plt.title('Scatter plot to visualize HouseholdIncome vs Age'),
    
    # Set the x and y labels 
    plt.xlabel('Age')
    plt.ylabel('Household Income')
    
    # Display the figures
    plt.show()
    
'''--------------------------------------------------------------------------
MENU OPTION 5
----------------------------------------------------------------------------
'''
    
# Function to exit the application based on choice 
def Exit():
    print('Option 5 selected that exits the application')
    exit()
    

# Default function if the entry is wrong 
def default():
    print("Invalid_Entry_function")
    return ("Invalid Entry")

# Using dictionary to create switch case for user input
def switch_Nhanes(i):
    switcher={
        '1': Household_income_per_ethnicity,
        '2': Marital_status,
        '3': Income_and_education_level,
        '4': lambda: Diet_analysis(input_df1,input_df2), # Use lambda function to implemenent a function that  accepts two arguments.
        '5': Exit
    }
    return switcher.get(i,default)()


# Main function
if __name__ == "__main__": # To confirm that the code is under main function
     while True:   # While loop to continuously ask user to re-enter the choice until the entered choice is correct 
         num = input('Please select one of the following options :  \n 1: Household_income_per_ethnicity    \n 2: Marital_status    \n 3: Income_and_education_level    \n 4: Diet_analysis     \n 5: Exit\n')
         print('\n')
         print (switch_Nhanes(num))
         print('\n')
         if(switch_Nhanes(num) != "Invalid Entry"):
             break




