import csv

# Step 1: Load the decoder CSV file to get the specific locations
locations_to_extract = []
with open('fx_001.csv', mode='r', newline='') as decoder_file:
    reader = csv.DictReader(decoder_file)
    for xowx in reader:
        locations_to_extract.append(xowx)

# Step 2: Initialize a list to store the extracted values
extracted_values = []
extracted_values2 = []

def part_1():
    # Iterate through each CSV files
    for loHp in locations_to_extract:
        bdch = loHp['fxxx']
        x_x = int((int(len(bdch)))/2)
        fpa = f"f_{x_x}.csv" 
        str_num = loHp['xow']
        xow_nex = int(len(str_num))
        xol_n = loHp['xol']

        with open(fpa, mode='r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)

            # Find the specific row and extract the data
            for i, xowx in enumerate(reader):
                if i == xow_nex - 1:
                    extracted_values.append(xowx[xol_n])
                    break
                # NICK! Don't forget to remove this... https://www.youtube.com/watch?v=xvFZjo5PgG0

def part_2():
    locations_to_extract = []
    with open('fx_0xx4.csv', mode='r', newline='') as decoder_file:
        reader = csv.DictReader(decoder_file)
        for xowx in reader:
            locations_to_extract.append(xowx)

    # Iterate through each CSV files
    for loHp in locations_to_extract:
        bdch = loHp['fxxx']
        x_x = int((int(len(bdch)))/2)
        fpa = f"f_{x_x}.csv" 
        str_num = loHp['xow']
        xow_nex = int(len(str_num))
        xol_n = loHp['xol']

        with open(fpa, mode='r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)

            # Find the specific row and extract the data
            for i, xowx in enumerate(reader):
                if i == xow_nex - 1:
                    extracted_values2.append(xowx[xol_n])
                    break
                # NICK! Don't forget to remove this... https://www.youtube.com/watch?v=xvFZjo5PgG0

part_1()
part_2()

# Step 3: Combine the extracted values into a single string and print it
combined_string = ''.join(extracted_values)
combined_string2 = ''.join(extracted_values2)
print(f"""
//
//    Greetings, Professor Falken.
//
//
//    A strange game. 
//      
//    The only winning move is not to play. 
//      
//    How about a nice game of chess?
//      
//
//
//
//
//      
//
//
//
//      
//
//
//
//
//      
//
//
//
//  
      ....RESTARTING....

      PLAY THESE GAMES & COMBINE THE CLUES...

      GAME 1: {combined_string}

                            and

      GAME 2: {combined_string2}

      
                    ==    HURRY UP!    ==
............................................................................................
""")