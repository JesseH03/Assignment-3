import arcpy
from arcpy import env

# Question Number 13

#set variables
env.overwriteOutput = True
arcpy.env.workspace = r"D:\MAS-GIS\610\Assignments\Exercise 3\Question 13\Question 13"

out_folder_path = r"D:\MAS-GIS\610\Assignments\Exercise 3\Question 13\Question 13"
out_name = "Extra_Credit"
in_features = ['tl_2018_04_tract.shp', 'tl_2018_us_county.shp']
out_location = r"D:\MAS-GIS\610\Assignments\Exercise 3\Question 13\Question 13\Extra_Credit.gdb"
#create gdb
arcpy.CreateFileGDB_management (out_folder_path, out_name)

#copy feature class to gdb
arcpy.FeatureClassToGeodatabase_conversion(in_features, out_location)

# change workspace to geodatabase
arcpy.env.workspace = r"D:\MAS-GIS\610\Assignments\Exercise 3\Question 13\Question 13\Extra_Credit.gdb"

#select maricopa county from the county shapefile for the clip
arcpy.MakeFeatureLayer_management ("tl_2018_us_county", "tempcounty")
arcpy.SelectLayerByAttribute_management ("tempcounty", "NEW_SELECTION", "NAME = 'Maricopa' ")

# perform the clip

arcpy.Clip_analysis(arcpy.env.workspace + r"\tl_2018_04_tract", "tempcounty", "Maricopa_tracts")

print("Everyone has a plan until they get punched in the mouth. - Mike Tyson")

