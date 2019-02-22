import arcpy



# Question Number 8


arcpy.env.workspace = r'D:\MAS-GIS\610\Assignments\EX3\Exercise_3.gdb'
numberRows = arcpy.GetCount_management("CallsforService")

print("There are " + str(numberRows) + " records in the CallsforService feature class.")

