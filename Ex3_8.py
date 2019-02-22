import arcpy
arcpy.env.workspace = r'C:\Users\rryser\Desktop\Ex3\Exercise_3.gdb\Exercise_3.gdb'

#Q8
#Return the count of records in the CallsforService feature class
lyrfile = r'C:\Users\rryser\Desktop\Ex3\Exercise_3.gdb\Exercise_3.gdb'
result = arcpy.GetCount_management(r'C:\Users\rryser\Desktop\Ex3\Exercise_3.gdb\Exercise_3.gdb\CallsforService')
print(result)
