# Imports smartpy library
import smartpy as sp

# Object
class Certificate(sp.Contract):

    # Object creation
    def __init__(self,
                 courseName : str,
                 studentName : str,
                 familyName : str,
                 date : str,
                 shortDescription : str,
                 longDescription : str,
                 learningModules : list,
                 instructor : str,
                 instructorPosition : str,
                 instructorLicenses : list):

        # Set the variables
        self.update_initial_storage(courseName = courseName)
        self.update_initial_storage(studentName = studentName)
        self.update_initial_storage(familyName = familyName)
        self.update_initial_storage(date = date)
        self.update_initial_storage(shortDescription = shortDescription)
        self.update_initial_storage(longDescription = longDescription)
        self.update_initial_storage(learningModules = learningModules)
        self.update_initial_storage(instructor = instructor)
        self.update_initial_storage(instructorPosition = instructorPosition)
        self.update_initial_storage(instructorLicenses = instructorLicenses)

    @sp.entry_point(lazify = True)
    def setName(self, parameters):
        """This function sets the full name of the student in the smart contract

        Args:
            name (str): first and second name (if any)
            familyName (str): family's name
        """       
        
        self.data.studentName = parameters.studentName
        self.data.familyName = parameters.familyName
    
    @sp.entry_point(lazify = True)
    def setCourseWorkshop(self, parameters : str):
        """This function sets the name of the course or workshop

        Args:
            courseWorkshop (str): first and second name (if any)
        """       
         
        self.data.courseName = parameters.courseName

    @sp.entry_point(lazify = True)
    def setDate(self, parameters : str):
        """This function sets the accomplishment date of the training

        Args:
            date (str): accomplishment date of the training
        """       
        
        self.data.date = parameters.date
    
    @sp.entry_point(lazify = True)
    def setShortDescription(self, parameters : str):
        """This function sets the course or workshop short description

        Args:
            shortDescription (str): course or workshop short description
        """
        
        self.data.shortDescription = parameters.shortDescription

    @sp.entry_point(lazify = True)   
    def setLongDescription(self, parameters : str):
        """This function sets the course or workshop long description

        Args:
            longDescription (str): course or workshop long description
        """
        
        self.data.longDescription = parameters.longDescription
    
    @sp.entry_point(lazify = True)
    def setLearningModules(self, parameters : str):
        """This function sets the learning modules of the course or workshop

        Args:
            learningModules (list): course or workshop learning modules
        """
        
        self.data.learningModules = parameters.learningModules

    @sp.entry_point(lazify = True)
    def setInstructor(self, parameters):
        """This function sets the instructor's signature

        Args:
            instructor (str): instructor's name
            
        """
        
        self.data.instructor = parameters.instructor
        self.data.instructorPosition = parameters.instructorPosition
        self.data.instructorLicenses = parameters.instructorLicenses

# Contract testing
@sp.add_test(name = "TeZt")
def test():

    # Define a test scenario
    scenario = sp.test_scenario()

    date = "October 4, 2021"
    studentName = "Astrid"
    familyName = "Torres"
    shortDescription = "has successfully completed the +5 hours Profesional Training"
    courseName = "Numerical Methods with Engineering Applications"
    longDescription = "This certificate acknowledges that students developed and improved their skills in Numerical Methods and Algorithms. They acquired theoretical and hands-on experience in numerical mathematics, flow charts, pseudocodes, optimization, curve fitting and numerical solvers. This included the use of Python for several assignments where they solved real-life engineering problems, using basic algorithms up to advanced simulations"
    learningModules = ["Flow charts", "Mathematical Modelling", "Optimization", "Curve Fitting", "Numerical Solvers", "Git", "GitHub"]
    instructor = "David Zenteno-Lara"
    instructorPosition = "Founder"
    instructorLicenses = ["11598263"]

    # Creates a certificate
    certificate = Certificate(courseName, studentName, familyName, date, shortDescription, longDescription, learningModules, instructor, instructorPosition, instructorLicenses)

    # Add certificate to scenario
    scenario += certificate

    # Set contract
    """
    certificate.setName(name = "Bob", familyName = "el Trompas")
    certificate.setShortDescription(shortDescription = "has successfully completed the +10 hours Profesional Training")
    certificate.setCourseWorkshop(courseWorkshop = "Robotics: from Kinematics to Control")
    certificate.setLongDescription(longDescription = "This certificate acknowledge that students developed and improved their skills in Robotics. They acquired theoretical and hands-on experience on kinematics, dynamics and control of robotic systems using MATLAB, Simulink and Python after completing several assignments about solving real-life problems, using basic algorithms up to advanced simulations")
    certificate.setLearningModules(learningModules = ["Kinematics", "Dual Quaternions", "Dynamics"])
    certificate.setInstructor(instructor = "David Zenteno-Lara", instructorPosition = "Founder", instructorLicenses = ["ABC - 123"])
    certificate.setDate(date = "September 29, 1994")
    """
