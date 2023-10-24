#!/usr/bin/env python3

import csv
import sys


## Takes in the object's format and duration and converts it to a price bundle.
## Both arguments expected as strings. Returns a string.
def get_price_bundle(object_format, duration):

    video_cassette_formats = ['VHS', 'MiniDV', 'Video8', 'Hi8', 'DVCAM', 'U-matic', 'U-matic: S', 'U-matic: SP',
                              'VHS: S-VHS', 'VHS: VHS-C', 'Betamax', 'Betamax: ED', 'Betacam', 'Betacam: SP' ]
    film_formats = ['8mm film', 'Super 8mm film', '16mm film', 'Super 16mm film', '35mm film']
    audio_formats = ['Audio cassette', '1/4 inch audio tape', 'Micro-cassette', 'DAT']

    bucket=''   # bucket of time, exact value will depend on format
    seconds = get_time_seconds(duration) # converts the duration from hh:mm:ss to seconds
    
    if object_format in video_cassette_formats: # if the format is one of the video cassette formats
        bucket = get_video_bucket(seconds)
        return "Video Cassette" + bucket
    elif object_format in film_formats: # if the format is one of the film formats
        bucket = get_film_bucket(seconds)
        return "Film 2k" + bucket
    elif object_format in audio_formats:    # if the format is one of the audio formats
        bucket = get_audio_bucket(seconds)
        return "Audiotape" + bucket;

    return "unrecognized format"    # if not any of the pre-defined formats, returns "unrecognized format"
      

## Takes in time as a hh:mm:ss and returns it as total seconds (int)
## If the input is not in hh:mm:ss, returns "invalid time"
def get_time_seconds(time):
    timeSplit = time.split(':')
    if len(timeSplit)!= 3:
        return " invalid time"

    totalSeconds = int(timeSplit[0])*60*60 + int(timeSplit[1])*60 + int(timeSplit[2])

    return totalSeconds

## Takes in the seconds and returns the duration as a range according to the AV Price bundles controlled vocabulary.
## For "Video Cassette"
def get_video_bucket(seconds):
    if type(seconds)==str:
        return seconds

    if seconds <= 1830:
        return " 0-30 min"
    elif seconds <= 3630:
        return " 30-60 min"
    elif (seconds <= 5430):
        return " 60-90 min"
    elif (seconds <= 7230):
        return " 90-120 min"
    elif (seconds <= 9030):
        return " 120-150 min"
    elif (seconds <= 10830):
        return " 150-180 min"
    elif (seconds <= 12630):
        return " 180-210 min"
    elif (seconds <= 14430):
        return " 210-240 min"
    elif (seconds <= 16230):
        return " 240-270 min"
    elif (seconds <= 18030):
        return " 270-300 min"
    return " >300 min"

## Takes in the seconds and returns the duration as a range according to the AV Price bundles controlled vocabulary.
## For "Audiotape"
def get_audio_bucket(seconds):
    if type(seconds)==str:
        return seconds

    if (seconds <= 2430):
        return " 0-40 min"
    elif (seconds <= 5430):
        return " 40-90 min"
    elif (seconds <= 7230):
        return " 90-120 min"
    elif (seconds <= 9030):
        return " 120-150 min"
    elif (seconds <= 10830):
        return " 150-180 min"
    elif (seconds <= 12630):
        return " 180-210 min"
    elif (seconds <= 14430):
        return " 210-240 min"
    elif (seconds <= 16230):
        return " 240-270 min"
    elif (seconds <= 18030):
        return " 270-300 min"
    elif (seconds <= 19830):
        return " 300-330 min"
    elif (seconds <= 21630):
        return " 330-360 min"
    elif (seconds <= 23430):
        return " 360-390 min"
    elif (seconds <= 25230):
        return " 390-420 min"
    return " >420 min";


## Takes in the seconds and returns the duration as a range according to the AV Price bundles controlled vocabulary.
## For "Film 2k"
def get_film_bucket(seconds):
    if type(seconds)==str:
        return seconds

    if (seconds <= 390):
        return " 0-6 min"
    elif (seconds <= 1230):
        return " 6-20 min"
    elif (seconds <= 2430):
        return " 20-40 min"
    elif (seconds <= 3630):
        return " 40-60 min"
    return " >60 min"

## Takes in a header row and returns the index of the column containing the item's format
def get_format_col(header):
    for index, heading in enumerate(header):
        if "obj_av_item_parts__ip_gauge_and_format" in heading:
            return index

## Takes in a header row and returns the index of the column containing the object's duration
def get_length_col(header):
    for index, heading in enumerate(header):
        if "obj_prsv_duration_string" in heading:
            return index

## Takes in a header row and returns the index of the column containing the object's price bundle
def get_bundle_col(header):
     for index, heading in enumerate(header):
        if "obj_av_item_parts__ip_price_bundle" in heading:
            return index
    
def write_price_bundles():
    all_items = []  # temporary array to hold the altered data

    with open(sys.argv[1]) as csvfile:      # open the csv supplied by user
            reader = csv.reader(csvfile)
            header_row = next(reader)   
            all_items.append(header_row)

            format_col = get_format_col(header_row)
            time_col = get_length_col(header_row)
            bundle_col = get_bundle_col(header_row)

            # for each row in the csv, get the price bundle and update the row
            for row in reader:
                price_bundle = get_price_bundle(row[format_col], row[time_col])
                row[bundle_col] = price_bundle
                all_items.append(row)

    with open(sys.argv[2], 'w',newline='') as csvfile:      # write the array to the user-specified file
        csv_writer = csv.writer(csvfile)
        for item in all_items:
            csv_writer.writerow(item)
                
def main():
    write_price_bundles()
    print("finished writing price bundles")

if __name__== "__main__":
    main()
    
  
