import arcpy
from arcpy import env

# Question Number 5
env.overwriteOutput = True

#set variables
out_folder_path = r"D:\MAS-GIS\610\Assignments\Ex3"

out_name = "Rasputin"
featureList = ['CapitalCities', 'Landmarks', 'HistoricPlaces', 'StateNames', 'Nationalities', 
'Rivers'] 

#create gdb
arcpy.CreateFileGDB_management (out_folder_path, out_name)

#create feature classes
for feature in featureList:
    arcpy.CreateFeatureclass_management (r"D:\MAS-GIS\610\Assignments\Ex3\Rasputin.gdb", feature, "POINT")
      
print("Success")



