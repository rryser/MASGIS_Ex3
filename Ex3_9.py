#Q9
#Set up environment in gdb from Q5
import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r'C:\Users\rryser\Desktop\Ex3\Exercise3.gdb'
fc_name = 'benches'
out_path = r'C:\Users\rryser\Desktop\Ex3\Exercise3.gdb'
fc_path = out_path + '\\'  + fc_name
domName = "BenchMaterial12"
SRDefinition="PROJCS['WGS_1984_Web_Mercator_Auxiliary_Sphere',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Mercator_Auxiliary_Sphere'],PARAMETER['False_Easting',0.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',0.0],PARAMETER['Standard_Parallel_1',0.0],PARAMETER['Auxiliary_Sphere_Type',0.0],UNIT['Meter',1.0]];-22041257.773878 -33265068.6042249 10000;-100000 10000;-100000 10000;0.001;0.001;0.001;IsHighPrecision"
print('Success')

#Create a feature class 
arcpy.CreateFeatureclass_management(out_path
                                    , out_name=fc_name
                                    , geometry_type="POINT"
                                    , template=""
                                    , has_m="DISABLED"
                                    , has_z="DISABLED"
                                    , spatial_reference=SRDefinition
                                    , config_keyword=""
                                    , spatial_grid_1="0"
                                    , spatial_grid_2="0"
                                    , spatial_grid_3="0"
                                    )
print('Done creating feature class')
    
#Add data field to new feature class
arcpy.AddField_management(fc_path,'BenchType','SHORT','','','','','NULLABLE','NON_REQUIRED','')
print('Added new field to feature class')

#Add a domain to the field you just created field
arcpy.CreateDomain_management(out_path,domName,'','SHORT','CODED','DEFAULT','DEFAULT')
print ('Domain created')

#Add coded values to domain
arcpy.AddCodedValueToDomain_management(out_path, 'BenchMaterial', 1, 'Wood')
arcpy.AddCodedValueToDomain_management(out_path, 'BenchMaterial', 2, 'Plastic')
arcpy.AddCodedValueToDomain_management(out_path, 'BenchMaterial', 3, 'Metal')
arcpy.AddCodedValueToDomain_management(out_path, 'BenchMaterial', 4, 'Concrete')
arcpy.AddCodedValueToDomain_management(out_path, 'BenchMaterial', 5, 'Other')
print('Added 5 coded domains')

#Assign field to domain
arcpy.AssignDomainToField_management(fc_path, 'BenchType', 'BenchMaterial')
print('Done adding field information')