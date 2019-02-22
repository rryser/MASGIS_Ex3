#Q10
#Perform a spatial join between the census tracts feature class and the general offense feature class.
                          
import arcpy
arcpy.env.workspace = r'C:\Users\rryser\Desktop\Ex3\Exercise_3.gdb\Exercise_3.gdb'
arcpy.env.overwriteOutput = True
print('success')

arcpy.SpatialJoin_analysis(target_features='Tracts'
                           , join_features='General_Offense'
                           , out_feature_class='GeneralOffense_Tracts'
                           , join_operation='JOIN_ONE_TO_MANY')

print('Finished')
