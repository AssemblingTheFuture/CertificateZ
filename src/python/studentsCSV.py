import os
import csv
from re import L
from browser import document, aio
from browser.html import A, TABLE, TR, TH, TD

# Get CSV paths
numericalCSV = os.path.dirname(__file__) + "/csv/numerical.csv"
controlCSV = os.path.dirname(__file__) + "/csv/control.csv"
roboticsCSV = os.path.dirname(__file__) + "/csv/robotics.csv"
pythonCSV = os.path.dirname(__file__) + "/csv/python.csv"

# List of workshops and courses
linkCourse = {"Numerical Methods with Engineering Applications" : "https://bit.ly/NumericZ",
              "Control of Dynamical Systems" : "https://bit.ly/zControl",
              "Robotics: from Kinematics to Control" : "https://bit.ly/RoboticZ",
              "Basic Robot Programming using Python" : "https://bit.ly/CertificateZ"}

# Create empty dictionary for students with already finished trainings
certificates = {}

# Get name of each course
courses = [key for key in linkCourse]

# Read any CSV
def readCSV(csvURL, certificates, course):

    # Open CSV file for Numerical Methods
    with open(csvURL) as csv_file:
        
        # Read data as dictionary
        csv_reader = csv.DictReader(csv_file, delimiter = ',')

        # Iterate through all rows
        for rows in csv_reader:
            
            # If current student has finished the course
            if "100" in rows['Progress']:
                
                # Get the name
                name = rows['Student Name']
                
                # If student is already in the dictionary
                if name in certificates:
                    
                    # Add the address of the contract in the current course
                    certificates[name][course] = "Z"
                
                # Otherwise
                else:

                    # Store it as key in the certificate's dictionary and include the direction of the certificate
                    certificates[name] = {course : "Z"}
        
    return certificates

# Sort students by name
def sortStudents(certificates):
    
    # Sorted Dictionary
    sortedDictionary = {}
    
    # Names
    names = [key for key in certificates.keys()]
    
    # Iterate through each sorted name
    for name in names.sort():
        
        # Assign its value to sorted dictionary
        sortedDictionary[name] = certificates[name]
        
    return sortedDictionary

# Show data as table in HTML
def showData(certificates):
    
    # Create table
    table = TABLE()
        
    # Create a row
    row = TR() 
        
    # Add header cells
    row <= TH("Student's Name")
    
    # Add courses' names
    for course in courses:
        
        # Assign links to some values in table
        row <= TH(A(course, href = linkCourse[course], target = "_blank"))
        
    # Add content to table
    table <= row
    
    # Iterate through each student
    for name in certificates:
        
        # Create a row
        row = TR()
        
        # Add student's name
        row <= TD(name)
        
        # Add courses' data
        for course in courses:
            
            # If current student has finished the current course
            if course in certificates[name]:
                
                # Get the addresses of the smart contracts if the current student took the course
                row <= TD(A(certificates[name][course], href = "#", target = "_blank"))
            
            # Otherwise
            else:
                
                # Set an empty cell
                row <= TD("Not enrolled or finished yet UwU")
        
        # Add values of current student
        table <= row
        
    # Delete everything in current section
    document['students-data'].clear()
            
    # Add table
    document['students-data'] <= table

# Read Numerical Methods course
certificates = readCSV(numericalCSV, certificates, courses[0])

# Read Control course
certificates = readCSV(controlCSV, certificates, courses[1])

# Read Robotics course
certificates = readCSV(roboticsCSV, certificates, courses[2])

# Read Python Robotics course
certificates = readCSV(pythonCSV, certificates, courses[3])

# Create table in HTML (sorted by students' names)
showData(sortStudents(certificates))