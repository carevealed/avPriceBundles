
#!/usr/bin/env python

import os
import csv
from xml.etree import ElementTree
import optparse


#DEFINE ARGUMENTS#
directory_default = '/Volumes/CAR4372/'

header_defaults = ['Item Identifier',
                   'Title',
                   'Format',
                   'Reel Size: Additional Technical Notes',
                   'Stock Manufacturer',
                   'Total Running Time',
                   'Frame Rate',
                   'Track Standard',
                   'Colors',
                   'Channel Configuration',
                   'Video Sound 1',
                   'Video Sound 2',
                   'Running Speed',
                   'Aspect Ratio',
                   'Notes from Vendor',
                   ]

search_string_default = 'vendor-md.xml'

element_defaults = ["AssetIdentifier",
                    "Markings",
                    "FormatType",
                    "ReelSize",
                    "StockBrand", 
                    "RunningTime",
                    "FrameRate",
                    "VideoStandard",
                    "ColorAttributes",
                    "SoundField",
                    "SoundFieldLevel1",
                    "SoundFieldLevel2",
                    "RecordingSpeed",
                    "AspectRatio",
                    "TransferComments", 
                    ]
                    

#HELPER FUNCTIONS START HERE

#MAKE A LIST OF THE FILES AND FILE PATHS
def file_list(directory, string):
    '''
    returns a list of strings representing filenames in directory that contain string
    '''
    
    file_list = []
    for root, _, files in os.walk(directory):
        for file in files:
            if string in file:
                file_list.append(os.path.join(root,file))
                
    return file_list

#EXTRACTING INFO WE WANT FROM XMLS
def process_file(file, element_names):
    xml = ElementTree.parse(file)

    for Original in xml.findall("Original"):
        if(Original):
            csvline = [ Original.find(name).text if Original.find(name) is not None else Original.find(name) for name in element_names ]
    
    return csvline

#GENERATES INPUTS FOR FUNCTIONS IN OUR MAIN SCRIPT
def parse_arguments():
    parser = optparse.OptionParser()
    (options, args) = parser.parse_args()
    dirs = str(args[0])
    print(dirs)

    
    return dirs, header_defaults, search_string_default, element_defaults

#TAKES IN THE HDD DIRECTORY STRING AND RETURNS THE NAME OF THE HARD DRIVE. ASSUMES NAME IS "/VOLUMES/NAME/..."
def get_hd_name(hdd_directory):
    
    name = hdd_directory.split('/')[2]
    
    return name

#MAIN SCRIPT STARTS HERE
def run_script():
    #PARSE ARGUMENTS
    hdd_directory, header_list, file_search_string, elements = parse_arguments()
    
    #CREATE CSV
    
    csvfile = open(hdd_directory+get_hd_name(hdd_directory)+'_vendor-md.csv', 'w', encoding='utf-8')
    csv_writer = csv.writer(csvfile)
    print("===============================================================")
    print('csv created')
    csv_writer.writerow(header_list)
    print('header written')
    #GENERATE FILE LIST of VALID FILES
    valid_files = file_list(hdd_directory, file_search_string )
    print("===============================================================")
    print('found',len(valid_files),'files')
    print("===============================================================")
    #ADD ROWS FROM FILES

    #For Each File in the list of valid files
    for file in valid_files:
        print(file)
        #generate a row of csv data from the file
        csvline = process_file(file, elements)
        #write the row of csv data to the csv file
        csv_writer.writerow(csvline)
        

    csvfile.close()
    print("===============================================================")
    print('xml parsed to csv in hdd main directory')
    print("===============================================================")
    return

if __name__ == "__main__":
    run_script()
