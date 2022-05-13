from browser import document, html, ajax
from browser.html import TABLE, TR, TH, TD

# Function to check data from server request
def checkData(request):

    # If everything is correct,
    if request.status == 200 and "learningModules" in request.json:

        # Show data in HTML as a table
        lines = [["Name", request.json["studentName"]],
                 ["Family's Name", request.json["familyName"]],
                 ["Course or Workshop", request.json["courseName"]],
                 ["Conferral Date", request.json["date"]],
                 ['Instructor', request.json["instructor"]]]

        # Create table
        table = TABLE()

        # Iterate through each row in list
        for line in lines:
            table <= TR(TD(line[0]) + TD(line[1]))

        document['request-result'].text = ''
        document['request-result'] <= table

    else:
        document["request-result"].html = "ERROR! Address is not correct"

def getCertificate(_):

    # Check if input box has any value
    if document['address-input'].value:

        # Send HTTPS request using Ajax
        ajax.get("https://api.ithacanet.tzkt.io/v1/contracts/" + document['address-input'].value + "/storage", mode="json", oncomplete = checkData)

    # If it is empty
    else:
        document["request-result"].html = "ERROR! Address cannot be empty"

document["get-certificate"].bind("click", getCertificate)
