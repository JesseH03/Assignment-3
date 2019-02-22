import arcpy

#Question 9


workspace_path = r"D:\MAS-GIS\610\Assignments\Ex3\Rasputin.gdb"

#first add the feature class to the gdb I created in question 5
arcpy.CreateFeatureclass_management (workspace_path, 'Popcorn', "POINT")

#add a field to the feature class I just created
arcpy.AddField_management(r"D:\MAS-GIS\610\Assignments\Ex3\Rasputin.gdb\Popcorn", "Color", "TEXT")

#now add domain
arcpy.CreateDomain_management(workspace_path, 'Color', 'Color choice', 'SHORT', 'CODED', 'DUPLICATE', 'DEFAULT')

#add values to domain
arcpy.AddCodedValueToDomain_management(workspace_path, 'Color', 0, 'Black')
arcpy.AddCodedValueToDomain_management(workspace_path, 'Color', 1, 'Red')
arcpy.AddCodedValueToDomain_management(workspace_path, 'Color', 2, 'Blue')
arcpy.AddCodedValueToDomain_management(workspace_path, 'Color', 3, 'Yellow')
arcpy.AddCodedValueToDomain_management(workspace_path, 'Color', 4, 'Green')


print("Your domains are created!")