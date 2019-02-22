import arcpy
arcpy.env.workspace = r'C:\Users\rryser\Desktop\Ex3\Exercise_3.gdb\Exercise_3.gdb'
arcpy.env.overwriteOutput = True
print('success')

#Create a layer from GeneralOffense feature class
arcpy.MakeFeatureLayer_management(r"C:\Users\rryser\Desktop\Ex3\Exercise_3.gdb\Exercise_3.gdb\General_Offense","General_Offense_lyr")
print('created layer')

#Select all assault offenses from the new General Offense layer
AssaultOffenses = arcpy.SelectLayerByAttribute_management("General_Offense_lyr",'NEW_SELECTION',"OffenseCustom = 'ASSAULT'")
print("selected by attribute")

# Write the selected features to a different feature class
arcpy.CopyFeatures_management(AssaultOffenses, 'CallsforService')
print("copied features to CallsforService")



#Q8 Return the count of records in the CallsforService feature class
lyrfile = r'C:\Users\rryser\Desktop\Ex3\Exercise_3.gdb\Exercise_3.gdb'
result = arcpy.GetCount_management('CallsforService')
#print('{} has {} records'.format('CallsforService', result[0]))...

#Q9 create a domain with 5 coded values, not 5 separate records in a table/fc. Q12 will be changed for the query.