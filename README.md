# Data-Visualization-using-Python

In this application the user is given few options to select that explores the National Health and Nutrition Examination Survey (NHANES) datasets. As the application begins running, first it provides the description of the two input datasets  followed by the display to different options to be performed on the datasets. As the dataset does contain some missing values; we first remove them before proceeding with the plots and visualization otherwise it might generate erroneous results. Notably, these two datasets contain demographic details and dietry details for individuals. This report analyses the relationship among different variables of these datasets. There are total five tasks to be implemented; results and explanation for each of them is given as follows: 

# Menu Option 1
In this option, first the the number of ethnicities are displayed followed by a sorted list of number of respondents per ethnicity. Afterwards, a horizontal
bar graph for average Household Income per ethnicity (only considering adult respondents) is displayed

# Menu Option 2
This menu option investigates the relationship between Age and Marriage for only adult respondents
which are aged 20 and over. First, it displays a sorted list showing the number of
respondents per marital status category is displayed. Afterwards, it shows a line graph; which includes the information about
1st , 2nd , and 3rd quartiles of age for each marriage status.

# Menu Option 3 
This menu option investigates the the correlation between education and income based on IncomePovertyRatio or HouseholdIncome (entered byt user)


# Menu Option 4
This menu is implemented based on a function that accepts two dataframes as input: (1) demographic
data,(2) dietary data. 

It first reduces the food dataset to the average
food intake per meal per individual. Then this new dataframe is merged with the demographic dataframe. Then Boxplots is generated for the categories of Gender, Ethnicity and Education. Scatter plot is generated for comparing with HouseholdIncome, and comparing
with Age.

# Menu Option 5
Exits the application
