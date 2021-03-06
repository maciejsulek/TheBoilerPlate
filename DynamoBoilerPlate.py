'''
Python Template for Revit/Dynamo
'''

__author__ = 'Maciej Sulek'
__website__ = 'https://github.com/maciejsulek'
__version__ = '1.0.0'

import clr #This is .NET's Common Language Runtime. It's an execution environment that is able to execute code from several different languages.

import sys #sys is a fundamental Python library - here, we're using it to load in the standard IronPython libraries.
sys.path.append('C:\Program Files (x86)\IronPython 2.7\Lib') #Imports the standard IronPython libraries, which cover everything from servers and encryption through to regular expressions.

import System #The System namespace at the root of .NET.
from System import Array #.NET class for handling array information.
from System.Collections.Generic import * #Lets you handle generics. Revit's API sometimes wants hard-typed 'generic' lists, called ILists. If you don't need these you can delete this line.

#Import Dynamo library for its proxy geometry classes.
clr.AddReference('ProtoGeometry') #You'll only need this if you're interacting with geometry.
from Autodesk.DesignScript.Geometry import * #Loads everything in Dynamo's geometry library.

#Import ToDSType(bool) extension method.
clr.AddReference("RevitNodes") #Dynamo's nodes for Revit.
import Revit #Loads in the Revit namespace in RevitNodes.
clr.ImportExtensions(Revit.Elements) #More loading of Dynamo's Revit libraries.

# Import geometry conversion extension methods.
clr.ImportExtensions(Revit.GeometryConversion) #More loading of Dynamo's Revit libraries. You'll only need this if you're interacting with geometry.

# Import DocumentManager and TransactionManager.
clr.AddReference("RevitServices") #Dynamo's classes for handling Revit documents.
import RevitServices
from RevitServices.Persistence import DocumentManager #An internal Dynamo class that keeps track of the document that Dynamo is currently attached to.
from RevitServices.Transactions import TransactionManager #A Dynamo class for opening and closing transactions to change the Revit document's database.

# Import RevitAPI and RevitAPIUI.
clr.AddReference("RevitAPI") #Adding reference to Revit's API DLLs.
clr.AddReference("RevitAPIUI") #Adding reference to Revit's API DLLs.

import Autodesk #Loads the Autodesk namespace.
from Autodesk.Revit.DB import * #Loading Revit's API classes.
from Autodesk.Revit.UI import * #Loading Revit's API UI classes.

# Standard areas for Current Document, Active UI and application.
doc = DocumentManager.Instance.CurrentDBDocument #Finally, setting up handles to the active Revit document.
uiapp = DocumentManager.Instance.CurrentUIApplication #Setting a handle to the active Revit UI document.
app = uiapp.Application #Setting a handle to the currently-open instance of the Revit application.
uidoc = uiapp.ActiveUIDocument #Setting a handle to the currently-open instance of the Revit UI application.

#########################
### START CODING HERE ###
#########################

# Preparing input from Dynamo to Revit 
input = IN[0]
# or
input = UnwrapElement(IN[0])

# Transaction starts.
TransactionManager.Instance.EnsureInTransaction(doc)

################################
### TRANSACTION DETAILS HERE ###
################################

# End of Transaction
TransactionManager.Instance.TransactionTaskDone()
#TransactionManager.Instance.ForceCloseTransaction()

# Geometric converting between revit and dynamo elements.
# https://github.com/teocomi/dug-dynamo-unchained/tree/master/dynamo-unchained-1-learn-how-to-develop-zero-touch-nodes-in-csharp#wrapping-unwrapping-and-converting

# Output and Changing element to Dynamo for export.
# https://github.com/DynamoDS/Dynamo/wiki/Python-0.6.3-to-0.7.x-Migration#wrapping
# <element>.ToDSType(True), #Not created in script, mark as Revit-owned
# <element>.ToDSType(False) #Created in script, mark as non-Revit-owned

OUT = "Declare output here!"