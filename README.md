# DCRA
Contains scripts for ArcGIS toolboxes that are specific to the needs of DCCED/DCRA. All of the tools here can be edited to be more generalized for similar purposes. Contact emma.hatcher@alaska.gov for help with customization.

ArcGIS properies configuration:

MLT Parcel Fabric:
  - Tool: Update Fields and Domains
      - Overview: This tool configures domains and fields of a parcel fabric to meet the inventory requirements of the MLT staff at       
      DCRA. It additionally enables attachments. 
      - Input Parameters (2):
         -Display Name: Parcel Fabric Geodatabase, Data Type: Workspace
         -Display Name: Parcel Layer, Data Type: Feature Layer

DCRA:
  - Tool: DCRA Add Attachments:
      - Overview: Using a file folder with attachments that have a common naming scheme (with the unique identifier separated by an 
      underscore), this script creates a match csv table, then joins the files in a folder to a layer file as attachments. Note: 
      this script is only configured for files with a single underscore delineating the unique identifier. It must be modified for 
      additional underscores or other separator character as appropriate. Inputs: attachments folder, table, the field from the 
      layer on which the join will be based (entered as text), and the matching join field to be created in the csv file (entered 
      as text). 
      - Input Parameters (4):
         - Display Name: Attachments Folder, Data Type: Workspace
         - Display Name: Input Layer, Data Type: Table
         - Display Name: Match Field (from Layer), Data Type: Any value
         - Display Name: Join Field (created in attachment table): Any value
