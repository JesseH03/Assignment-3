import arcpy

#Question 7

#set variables

arcpy.env.workspace = r"D:\MAS-GIS\610\Assignments\EX3\Exercise_3.gdb"

InFeature = "CallsforService"
outLocation = r"D:\MAS-GIS\610\Assignments\EX3\Exercise_3.gdb"
outFeatureClass = "Selected_Crimes"
delimitedField = arcpy.AddFieldDelimiters(arcpy.env.workspace, "CFSType")
expression = delimitedField + " = 'Subject Down Call'"

# Execute FeatureClassToFeatureClass
arcpy.FeatureClassToFeatureClass_conversion(InFeature, outLocation, outFeatureClass, expression)


print("almost done dummy!")





