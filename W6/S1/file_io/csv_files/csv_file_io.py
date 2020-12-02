from csv import reader, writer

# Reading and Writing CSV Files

# Reading Resources
# * https://docs.python.org/3/library/csv.html

# Writing a CSV file

# > Open the CSV file for writing
fp = open("movies.csv", "w")

# > Create a CSV writer
csv_writer = writer(fp)

# > Write rows into file
csv_writer.writerow(["ID","MOVIE", "RATING"]) 
csv_writer.writerow([0,"Monty Python and the Holy Grail", 8])
csv_writer.writerow([1,"Monty Python's Life of Brian", 8.5])
csv_writer.writerow([2,"Monty Python's Meaning of Life", 7])

# > Close the file
fp.close()

# Reading a CSV file

# > Open the CSV file for reading
fp = open("movies.csv")

# > Create a CSV reader
csv_reader = reader(fp)

# > Iterate over the record and print them
for record in csv_reader:
    print(f"Movie #{record[0]} - '{record[1]}' has a rating of {record[2]}.")

# > Close the file
fp.close()