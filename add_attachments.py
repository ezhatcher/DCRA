#Using a file folder with attachments that have a common naming scheme (with the unique identifier separated by an underscore), this script creates a match csv table, then joins the files in a folder 
#to a layer file as attachments. Note: this script is only configured for files with a single underscore delineating the unique identifier. It must be modified for additional underscores or other 
#separator character as appropriate. Inputs: attachments folder, layer, the field from the layer on which the join will be based, and the matching join field to be created in the csv file. 

#Author/contact: Emma Hatcher/emma.hatcher@alaska.gov


import arcpy
import csv
import os
from arcpy import env
from os import listdir

#Inputs: folder with attachments, the layer to attach to, the name of the attribute field the match is based on
attachments_folder = arcpy.GetParameterAsText(0)
attachments_layer = arcpy.GetParameterAsText(1)

#Define match field on which to base join
match_field = arcpy.GetParameterAsText(2)
f_id_name = arcpy.GetParameterAsText(3)

#Enable Attachments
arcpy.EnableAttachments_management(attachments_layer)

attachments_table = attachments_folder + "\\" + "attachments_Table.csv"

#Parse file names to extract unique identifier (must be separated from file name structure by an '_'), then write csv table
with open(attachments_table, 'wb') as output:
    writer = csv.writer(output, delimiter=",")
    writer.writerow([str(f_id_name), 'Attachment'])

    for f in os.listdir(attachments_folder):
        file_name, file_ext = os.path.splitext(f)
        f_file, f_id = file_name.split('_')
        if str(f).find('.pdf') > -1:
            writer.writerow([f_id, f])

#Add attachments
arcpy.AddAttachments_management(attachments_layer, match_field, attachments_table, f_id_name, "Attachment", attachments_folder)
