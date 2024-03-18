# What the script is
This script looks at the duration and format of item-level information and returns the associated controlled vocabulary terms that California Revealed uses to track the cost of digitization.
## Why CA-R uses it
We are working on ways to automate our processes and one of the most important tasks of post-digitization work is tracking our costs of digitization.
## Workflow timelines
This script can be used to track our digitization costs post-digitization. This script is meant to be used on csv export sheets from the California Revealed repository. The sheets need to be item level; this means they either need to have 1 item per object (or row) or, if each object has multiple items in it, you will need to use expandLines.py on the csv sheet to make our exported metadata sheets item-level. Once we gather the item level duration information from the vendor, we can use this script to fill out the "Price Bundle", collapse the sheet if applicable with collapseLines.py, and ingest the object-level metadata into the California Revealed repository. Please see the xml_parse_csv.py GitHub to see how to gather item level duration from the hard drives.
## Troueblshooting note
This script only accomodates our most common MediaPreserve price bundles for audiotape, videotape, and film. It will need to be updated if the controlled vocabularies change for format or price bundle. If it does not recognize the format, it will return "unrecognized format" in the sheet. If the duration format isn't in hh:mm:ss format, it will return "invalid time" in the sheet. Once we update the csv sheets and ingest them into our repository, our repository has the ability to calculate item, object, and partner set level price bundles based on our controlled vocabularies.
# Procedures
- You will need python3 to be able to run this script
- Download the script from this github: avPriceBundles.py
- Create a folder called "scripts" in your Documents folder. Move avPriceBundles.py to this folder.
- Open terminal and change your directory (cd) to the scripts folder. You can use the command below to do so.
```
cd Documents/scripts/
```
- Now you are ready to use the script to create a new csv with the price bundles. Here is the beginning of the command, which will then be followed by the pathway to the original csv, followed by the path to the new csv you will create. 
```
python3 avPriceBundles.py [pathway/to/file.csv] [pathway/to/newfile.csv]
```
Example:
```
python3 avPriceBundles.py ./Desktop/capdhs_2021-2022_AV_QC.csv ./Desktop/capdhs_2021-22_pricebundle.csv 
```
- When you press enter, a new csv file will be created following the pathway you determined in the terminal. 
