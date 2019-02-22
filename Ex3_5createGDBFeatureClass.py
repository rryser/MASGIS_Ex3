#File name: Ex3createGPSFeatureClass.py
#Author: RRyser
#Python Version: 2.7 or 3.5 or greater
#Description : creates a fgdb and feature classes, in the current working directory

import os
import sys
import arcpy

from arcpy import env
env.overwriteOutput = True

#list your feature class names here
featureList = ['CapitalCities', 'Landmarks', 'HistoricPlaces', 'StateNames', 'Nationalities', 'Rivers']

current_dir = os.getcwd() 
fgdb_name = 'Exercise3.gdb'
workspace_path = current_dir + '\\' +fgdb_name
    
#SR Definition
SRDefinition="PROJCS['WGS_1984_Web_Mercator_Auxiliary_Sphere',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Mercator_Auxiliary_Sphere'],PARAMETER['False_Easting',0.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',0.0],PARAMETER['Standard_Parallel_1',0.0],PARAMETER['Auxiliary_Sphere_Type',0.0],UNIT['Meter',1.0]];-22041257.773878 -33265068.6042249 10000;-100000 10000;-100000 10000;0.001;0.001;0.001;IsHighPrecision"

#create a gdb
arcpy.CreateFileGDB_management(current_dir, fgdb_name)
        
print('Done creating gdb')

#Create the Feature Classes

#CapitalCities
arcpy.CreateFeatureclass_management(out_path=workspace_path
                                    , out_name=featureList[0]
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
print('Done creating CapitalCities')
    
#Landmarks
arcpy.CreateFeatureclass_management(out_path=workspace_path
                                    , out_name=featureList[1]
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
print('Done creating Landmarks')

#HistoricPlaces
arcpy.CreateFeatureclass_management(out_path=workspace_path
                                    , out_name=featureList[2]
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
print('Done creating HistoricPlaces')

#StateNames
arcpy.CreateFeatureclass_management(out_path=workspace_path
                                    , out_name=featureList[3]
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
print('Done creating StateNames')

#Nationalities
arcpy.CreateFeatureclass_management(out_path=workspace_path
                                    , out_name=featureList[4]
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
print('Done creating Nationalities')

#Rivers
arcpy.CreateFeatureclass_management(out_path=workspace_path
                                    , out_name=featureList[5]
                                    , geometry_type="POLYLINE"
                                    , template=""
                                    , has_m="DISABLED"
                                    , has_z="DISABLED"
                                    , spatial_reference=SRDefinition
                                    , config_keyword=""
                                    , spatial_grid_1="0"
                                    , spatial_grid_2="0"
                                    , spatial_grid_3="0"
                                    )
print('Done creating Rivers')

print('All done. Your fgdb was created at ' + workspace_path)
