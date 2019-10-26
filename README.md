# Do_your_stuffs_with_Python
Use Python to automate some of your dailystuffs

This repository is a collection of python scripts that run using commandline as these take command line arguments as parameter to work upon...
___
Instructions to use:

1 Paste these files in some folder and add that folder to Environment Variables Path to ease the process of accessing

2 further create batch files for the script with the same name as the script

the content of the batch files should be as:

@py.exe /bsolute/address/of/the script/ %*

@pause 

the second line is required to pause the command prompt use this as per requirements
___
#### Autotext
Autotext is an amazing script it will automate the keyboard of your device to type some text for you

It takes the text copied to the clipboard to do so...

It starts writing the text with a 10 seconds delay..

Beware while using this script as this will start typing anywhere and can lead to hazards..

#### Capture
This script helps you to take quick screenshots

Just pass in the name for the image and the current screen will be captured and will be saved as a png image in your pc

The commandline needs not to be paused for this script

#### ColorPalleteGenerator
This script generates a color pallete from an image

Arguments: `<imagepath> <num colors>`

The commandline needs to be paused for this script

#### Dict
This Script is for quick dictionary

It uses a json file "data.json" as its database
so edit the path of the json file in the script

Just pass the word you want to search as the commandline argument

#### MCB
This Script is for a Multi Clip Board

> Copy any Text and save to it the multiclipboard by passing the commandline arguments:
  `save <key for accessig the clip>`

> to access the clip pass the arguments the clip corresponding to the clip will be copied:
  `<key>`

> to delete any clip use the arguments:
  `delt <key>`

> to know all the clips in the multiclipboard a list of keys of all saved clips will be copied:
  `list`

> to delete all the clips:
  `dall`

shevle is used to store all the data to change the path of the shelve in the script

The commandline need not to be paused for this script

#### pdf
This Script is for various pdf utilities which are:
>  merge cut watermark encrypt decrypt

`merge <source1> <source2> <destination>`

`watermark <source> <marksrc> <destination>`

`encrypt <source> <password> <destination>`

`decrypt <source> <password> <destination>`

`cut <source> <start>-<end> <destination>`

The commandline need not to be paused for this script

#### RPlace
This is a quick replace all script

Copy the text in which you want to make replacements
Run the scripts with the following keyword arguments:

   `<Replace what> ~ <Replace with>`

The text after the replacements will be copied to the clipboard

The commandline need not to be paused for this script

#### Speak
This module read out text data for you

The commandline terminal needs to be paused for this script

You can optionally pass the text to be read as the commandline aguments if not provived it will read the text copied to the clipboard

#### Stopwatch
This Script is a quick stopwatch

The commandline needs to be paused for this script
 
#### Syntax
This Script lets you search you online for some syntax

Just pass the query as the commandline arguments and you will be redirected to the syntaxdb website with your query already being searched

The commandline needs not to be paused for this script

#### Wiki
This script parses data directy fro the wikipedia

The commandline terminal needs to paused for this script

the commandline arguments are as follows

`~ <optional query>` parses the entire wikipedia page for the requested query

`search <optional query> or Search <optional query>` parses a list if results for the requested page

`summary <optional query> or Summary <optional query>` parses the summary of the requested page

note that the query arguments are optional as if they are not mentioned the script will parse information about the text from the clip board

#### WordCloud
This script quickly creates cool wordclouds for you

The commandline terminal need not to be paused for this script

The commandline arguments are as follows:

`<width in pixels> <height in pixels> <background color> <optional max words default 200>`

#### WordCloudCustom
This script quickly creates cool masked wordclouds for you

The commandline terminal need not to be paused for this script

The commandline arguments are as follows:

`<width in pixels> <height in pixels> <background color> <universal path of the masking image>`

#### xl2txt
This script lets you to export an entire excel workbook to text files one for each worksheet

The commanline arguments are as follows: 

`<source_file_path> <destination_folder>`

The commandline needs not to be paused for this script