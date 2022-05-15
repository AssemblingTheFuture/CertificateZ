from browser import document, ajax
from browser.html import A, B, TABLE, TR, TH, TD

# List of workshops and courses
linkCourse = {"Numerical Methods with Engineering Applications" : "https://bit.ly/NumericZ",
              "Control of Dynamical Systems" : "https://bit.ly/zControl",
              "Robotics: from Kinematics to Control" : "https://bit.ly/RoboticZ",
              "Basic Robot Programming with Python" : "https://bit.ly/CertificateZ"}

# List of instructors
instructors = {"zDynamics" : "https://zdynamics.org/about/",
               "David Zenteno-Lara" : "https://zdynamics.org/about/zenteno"}

# API to request the smart contracts
contractsAPI = "https://api.ithacanet.tzkt.io/v1/contracts/"

# URL for smart contract overview
contractsURL = "https://ithacanet.tzkt.io/"

# Function to check data from server request
def checkData(request):

    # If everything is correct,
    if request.status == 200 and "learningModules" in request.json:
        
        # Assign links to some values in table
        course = A(request.json["courseName"], href = linkCourse[request.json["courseName"]], target = "_blank")
        
        # Show data in HTML as a table
        lines = [["Name", request.json["studentName"]],
                 ["Family's Name", request.json["familyName"]],
                 ["Issued", request.json["date"]],
                 ["Course or Workshop", course],
                 ["Instructor", A(request.json["instructor"], href = instructors[request.json["instructor"]], target = "_blank")],
                 ["File", A('Click here to download!', href = "#")],
                 ["Smart Contract", A('Validate on ꜩ Blockchain', href = contractsURL + document['address-input'].value + "/storage/", target = "_blank")]]
        
        # Create table
        table = TABLE()
        
        # Create a row
        row = TR() 
        
        # Add header cells
        row <= TH("Data")
        row <= TH("Content")
        
        # Add content to table
        table <= row

        # Iterate through each row in list
        for line in lines:
            table <= TR(TD(line[0]) + TD(line[1]))

        document['request-result'].clear()
        document['request-result'] <= table

    else:
        document['request-result'].html = "ERROR! Address is not correct"

def getCertificate(_):

    # Check if input box has any value
    if document['address-input'].value:

        # Send HTTPS request using Ajax
        ajax.get(contractsAPI + document['address-input'].value + "/storage", mode="json", oncomplete = checkData)

    # If it is empty
    else:
        document['request-result'].html = "ERROR! Address cannot be empty"

document["get-certificate"].bind("click", getCertificate)
