import argparse
import json
import csv

parser = argparse.ArgumentParser(description='Define a parser')

parser.add_argument('good_variable_name', help='Operation with good variable name that does something')

# Sum
parser.add_argument('numbers', default=0, type=int, nargs='*', help='Parser that is used for storage of entered values')

# Generate
parser.add_argument('--start', dest='start', type=int, help='Start the sequence from this term')
parser.add_argument('--stop', dest='stop', type=int, help='Stops the sequence once we get to this value')
parser.add_argument('--step', dest='step', type=int, default=1, help='the common difference between terms')

# Convert
parser.add_argument('--input', dest='input', help='Enter the input file')
parser.add_argument('--output ', dest='output', help='Enter the output file')

# parse (read) the arguments
args = parser.parse_args()

if args.good_variable_name == 'sum':
    accumulated_numbers = sum(args.numbers)
    print(f'Sum: {accumulated_numbers}')

elif args.good_variable_name == 'generate':
    n = 1
    generated_List = []
    while 1:
        a_n = args.start + args.step * (n - 1)  # a_n is the nᵗʰ term in the sequence
        n = n + 1
        # checking if input is equal or greater then args.stop:
        if a_n >= args.stop:  # if it is, printing the list and breaking the constant loop
            print("Generated:", *generated_List)
            break
        else:  # if it is not, adding the value in the back of the list
            generated_List.append(a_n)

elif args.good_variable_name == 'convert':
    column_name = ['userId', 'id', 'title', 'body']

    # Open the file and create object root that will be used later
    with open(args.input) as json_file:  # open json file
        root = json.load(json_file)

    with open(args.output, 'w') as csv_file:  # open csv file
        writer = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(column_name)  # the names of each column are given in the assignment
        for item in root:
            writer.writerow([item['userId'], item['id'], item['title'], item['body']])
            # go through the root and writing attributes of each item in the given sequence