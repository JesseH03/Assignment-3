import arcpy

# Question Number 6
arcpy.env.workspace = r"D:\MAS-GIS\610\Assignments\EX3\Exercise_3.gdb"
#add field
arcpy.AddField_management("CallsforService", "Crime_Explanation", "TEXT")

# set variables
fc = r"D:\MAS-GIS\610\Assignments\EX3\Exercise_3.gdb\CallsforService"
fields = ['CFSType', 'Crime_Explanation']
# update fields based on burglaries
with arcpy.da.UpdateCursor(fc, fields) as cursor:
    for row in cursor:
        if row[0] == 'Burglary Call':
           row[1] = 'This is a burglary'
           cursor.updateRow(row)


print("It's done!")
