# What the script is
This is a script that parses technical metadata from an xml file to a csv sheet. This format allows us to more easily ingest technical information gathered from our AV vendor as metadata into our digital repostiory. This script and directions are intended for terminal use on MacOS. This script and procedures were written by Willow Germs.
## Why CA-R uses it
Our vendor creates an xml file in which they record technical information about the av material as they inspect it for digitization. We wanted to be able to more easily ingest this information into our repository. This includes information such as running speed, stock, condition notes, transfer comments, duration, etc. The vendor usually includes multiple partners from a particular grant cycle on a hard drive, based on the original shipments we sent to them. These batches are then given a job number and the associated hard drive is named after that job number. The script is run on the hard drive and is able to go through each folder, find the vendor-md.xml file, gather particular information from that file, and put it into a csv file that we can use to copy and paste from into an ingestible spreadsheet for our repository.
## Workflow timelines
This script is used on the hard drives that we receive from MediaPreserve post-digitization and before QCing. Prior to this script, we were manually opening the PBCore xml files for each object, searching through the file, and copying over some of the information into a spreadsheet. This script reduces repetitive manual work and human error. It's also helpful for reviewing this metadata on a batch level.
# Procedures
- You will need python3 to be able to run this script
- Download the script from this github: xml_parse_csv.py
- Create a folder called "scripts" in your Documents folder. Move xml_parse_csv.py to this folder.
- Plug in the hard drive from the vendor.
-Run dot_clean to remove hidden files. If you don't do this, you will likely encounter an error. Here is the beginning of the command, which will be followed by the full pathway to the hard drive:
```
dot_clean /Volumes/[name-of-harddrive]/
```
Example:
```
dot_clean /Volumes/CAR3924/
```
- Note: pathways are case-sensitive. Type out the name of the hard drive as it shows in Finder and make sure that you add a forward slash at the end of the hard drive name.
- Open terminal and change your directory (cd) to the scripts folder. You can use the command below to do so.
```
cd Documents/scripts/
```
- Now you are ready to use the script to create the csv. Here is the beginning of the command, which will then be followed by the pathway to the hard drive. Follow the same steps laid out for the dot_clean section above.
```
python3 xml_parse_csv.py /Volumes/[Name-of-harddrive]/
```
Example:
```
python3 xml_parse_csv.py /Volumes/CAR3924/
```
- When you press enter, the terminal will print when the csv and headers are written, how many vendor-md.xml files it found, the pathways to each file, and if any errors came up along the way.
- If successful, you should now find a file in the hard drive directory with the name of the hard drive followed by "_vendor-md.csv" i.e. CAVP5081D1_vendor-md.xml
## Side note
See the expand-collapse-lines GitHub for transferring sheets with multi-item objects.