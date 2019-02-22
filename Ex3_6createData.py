#Q6
import arcpy
arcpy.env.workspace = r'C:\Users\rryser\Desktop\Ex3\Exercise_3.gdb\Exercise_3.gdb'
arcpy.env.overwriteOutput = True

#Add crime explanation field here
arcpy.AddField_management('CallsforService','Crime_Explanation','TEXT')
print('Added new field')

fc = r'C:\Users\rryser\Desktop\Ex3\Exercise_3.gdb\Exercise_3.gdb\CallsforService'
fields = ['Crime_Explanation', 'CSFType']

# Create update cursor for feature class 
with arcpy.da.UpdateCursor(fc, fields) as cursor:
    for row in cursor:
        if (row[1] == 'Burglary'):
            row[0] = 'This is a burglary'
        cursor.updateRow(row)


