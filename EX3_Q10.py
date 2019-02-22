import arcpy

#Question 10

#set variables
target_features = r"D:\MAS-GIS\610\Assignments\EX3\Exercise_3.gdb\Tracts"
join_features = r"D:\MAS-GIS\610\Assignments\EX3\Exercise_3.gdb\General_Offense"
out_feature_class = r"D:\MAS-GIS\610\Assignments\EX3\Exercise_3.gdb\General_Offense_in_Tracts"

arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class)

print("San Dimas High School Football Rules!")