##This script configures the domains and field of a parcel fabric to meet the data requirements of the MLT staff at DCRA. It also enables attachments. 

##Author/contact: Emma Hatcher, emma.hatcher@alaska.gov

import arcpy
import os
from arcpy import env

#User input 1: geodatabase for the given community's parcel fabric
geodatabase = arcpy.GetParameterAsText(0)

#User input 3: fabric parcel layer
fabric_layer = arcpy.GetParameterAsText(1)

env.workspace = geodatabase

#Create the MLT Domains for the Feature Dataset(mlt class, interest conveyed, disposal type, land use)
MLTdomain = arcpy.CreateDomain_management(geodatabase,"MLT","MLT code for parcel","TEXT","CODED","DEFAULT","DEFAULT")
mlt_dict = {"C12":"Non-MLT", "C3":"MLT", "C4":"DOT Airport"}
for code in mlt_dict:
    arcpy.AddCodedValueToDomain_management(geodatabase, "MLT", code, mlt_dict[code])

interest_domain = arcpy.CreateDomain_management (geodatabase, "Interest", "Interest conveyed", "TEXT", "CODED", "DEFAULT", "DEFAULT")
int_dict = {"1":"fee surface", "2":"less than fee", "3":"equitable"}
for code in int_dict:
    arcpy.AddCodedValueToDomain_management(geodatabase, "Interest", code, int_dict[code])
	
disposal_domain = arcpy.CreateDomain_management (geodatabase, "Disposal", "Disposal type", "TEXT", "CODED", "DEFAULT", "DEFAULT")
disposal_dict = {"1":"lease", "2":"easement" , "3":"other"}
for code in disposal_dict:
    arcpy.AddCodedValueToDomain_management(geodatabase, "Disposal", code, disposal_dict[code])
	
use_domain = arcpy.CreateDomain_management(geodatabase, "Land Use", "Land use", "TEXT", "CODED", "DEFAULT", "DEFAULT")
use_dict = {"1":"airport", "2":"bulk fuel/power", "3":"clinic", "4":"community hall", "5":"council office", "6":"landfill", "7":"landfill/sewage", "8":"maintenance shop", "9":"post office", "10":"public safety", "11":"recreation", "12":"residential", "13":"school", "14":"sewage", "15":"telecommunications", "16":"transportation", "17":"washeteria", "18":"water plant", "19":"other public use", "20":"other commercial use"}
for code in use_dict:
    arcpy.AddCodedValueToDomain_management(geodatabase,"Land Use", code, use_dict[code])

rec_district_domain = arcpy.CreateDomain_management(geodatabase, "RecordDist", "Recording district", "TEXT", "CODED", "DEFAULT", "DEFAULT")
rec_dict = {"1":"Aleutian Islands", "2":"Anchorage", "3":"Barrow", "4":"Bethel", "5":"Bristol Bay", "6":"Cape Nome", "8":"Chitina", "9":"Cordova", "10":"Fairbanks", "11":"Ft Gibbons", "12":"Haines", "13":"Homer", "14":"Iliamna", "15":"Juneau", "16": "Kenai", "17":"Ketchikan", "18":"Kotzebue", "19":"Kuskokwim", "20":"Kvichak", "21":"Manley Hot Springs", "22":"Mt Mckinley", "23":"Nenana", "24":"Nulato", "25":"Palmer", /
"26":"Petersburg", "27":"Rampart", "28":"Seldovia", "29":"Seward", "30":"Sitka", "31":"Skagway", "32":"Talkeetna", "33":"UCC Central", "34":"Valdez", "35":"Wrangell"}
for code in rec_dict:
    arcpy.AddCodedValueToDomain_management(geodatabase, "RecordDist", code, rec_dict[code])
	
#Add the casefile field
casefile = arcpy.AddField_management(fabric_layer, "Casefile", "TEXT", "","",10,"","NULLABLE", "NON_REQUIRED", "")

#Add the plat field
plat = arcpy.AddField_management(fabric_layer, "Plat", "TEXT", "", "", 20, "", "NULLABLE", "NON_REQUIRED", "")

#Add the interest field
interest = arcpy.AddField_management(fabric_layer, "Int_Conv", "TEXT", "", "", 15, "", "NULLABLE", "NON_REQUIRED", "Interest")

#Add the title document field
title_doc = arcpy.AddField_management(fabric_layer, "Title_Doc", "TEXT", "","",20,"","NULLABLE","NON_REQUIRED", "")

#Add the Grantee field
grantee = arcpy.AddField_management(fabric_layer, "Grantee", "TEXT", "", "", 35, "", "NULLABLE", "NON_REQUIRED", "")

#Add the disposal type field
disposal_type = arcpy.AddField_management(fabric_layer, "Disp_Type", "TEXT", "", "", 10, "", "NULLABLE", "NON_REQUIRED", "Disposal")

#Add the date of conveyance field
convey_date = arcpy.AddField_management(fabric_layer, "Convey_Date", "DATE","","","","","NULLABLE", "NON_REQUIRED","")

#Add the revenue field
revenue = arcpy.AddField_management(fabric_layer, "Revenue", "FLOAT", 10, 2,"","","NULLABLE","NON_REQUIRED","")

#Add the reverter field
reverter = arcpy.AddField_management(fabric_layer, "Rev_Date", "DATE", "","","","","NULLABLE", "NON_REQUIRED","")

#Add the hyperlink field
hyperlink = arcpy.AddField_management(fabric_layer, "Hyperlink", "TEXT", "", "", 150, "", "NULLABLE", "NON_REQUIRED", "")

#Add the disposal document
disposal_doc = arcpy.AddField_management(fabric_layer, "Disp_Doc", "TEXT", "", "", 20, "", "NULLABLE", "NON_REQUIRED", "")

#Add the recording district
rec_district = arcpy.AddField_management(fabric_layer, "Rec_Dist", "TEXT", "", "", 20, "", "NULLABLE", "NON_REQUIRED", "")

#Add the disposal date
disposal_date = arcpy.AddField_management(fabric_layer, "Disp_Date", "DATE","","","","", "NULLABLE", "NON_REQUIRED", "")

#Add the land use field
land_use = arcpy.AddField_management(fabric_layer, "Land_Use", "TEXT", "", "", 25, "", "NULLABLE", "NON_REQUIRED", "Land Use")

#Add end of term field
end_term = arcpy.AddField_management(fabric_layer, "End_Term", "DATE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

#Add MLT field
mltclass = arcpy.AddField_management(fabric_layer, "MLT", "TEXT", "", "", 15, "", "NULLABLE", "NON_REQUIRED", "MLT")

#Add status field
status = arcpy.AddField_management(fabric_layer, "Status", "TEXT","","", 200, "", "NULLABLE", "NON_REQUIRED", "")

