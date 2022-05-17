from browser import document
from browser.html import TABLE, TR, TD
from browser.local_storage import storage
from browser.template import Template
from browser.widgets.dialog import InfoDialog
import json

# Get values of current certificate as JSON
certificate = json.loads(storage['certificate'])
URLs = json.loads(storage['URLs'])

def createTable(place, values):

    # Create table
    table = TABLE()
    
    # Iterate through each value in list
    for value in values:
            
        # Set value of each cell in column
        table <= TR(TD(value))

    # Delete section in HTML
    document[place].clear()
    
    # Add created table
    document[place] <= table

# Add date to template
Template(document["date"]).render(date = certificate["date"])

# Add student's to template
Template(document["studentCompleteName"]).render(studentCompleteName = certificate["studentName"] + " " + certificate["familyName"])

# Add short description to template
Template(document["shortDescription"]).render(shortDescription = certificate["shortDescription"])

# Add course or workshop to template
Template(document["courseName"]).render(courseName = certificate["courseName"])
Template(document["courseURL"]).render(courseURL = URLs["courseURL"], name = certificate["courseName"])

# Add long description to template
Template(document["longDescription"]).render(longDescription = certificate["longDescription"])

# Add instructor's name
Template(document["instructor"]).render(instructor = certificate["instructor"])
Template(document["instructorURL"]).render(instructorURL = URLs["instructorURL"], name = certificate["instructor"])

# Add instructor's position
Template(document["instructorPosition"]).render(instructorPosition = certificate["instructorPosition"])

# Add instructor's position
Template(document["contractAddress"]).render(contractAddress = URLs["contractAddress"])
Template(document["contractURL"]).render(contractURL = URLs["contractURL"], name = certificate["instructor"])

# Add learning modules
createTable(place = 'learningModules', values = certificate["learningModules"])
