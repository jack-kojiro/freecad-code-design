"""
Goal: Create a simple box and understand basic Python syntax
Learning: Variables, basic FreeCAD commands, viewing objects
"""
import FreeCAD as App
import Part
from FreeCAD import Gui

# Clear any open documents
if App.activeDocument():
    App.closeDocument(App.activeDocument().Name)

# Create new document
doc = App.newDocument("Project1")

# Create a box with variables
width = 50   # Try changing these numbers!
length = 30  # and see what happens
height = 20  # to the box

my_first_box = Part.makeBox(width, length, height)

# Add to document
box_obj = doc.addObject("Part::Feature", "MyBox")
box_obj.Shape = my_first_box

# Update view
doc.recompute()
Gui.SendMsgToActiveView("ViewFit")
print("I created my first box!")
