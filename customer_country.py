import csv

def main():
    infile_name = 'customers.csv'
    outfile_name = 'customers_country.csv'

    infile = open(infile_name, 'r')
    reader = csv.reader(infile)

    fields = next(reader)

    outfile = open(outfile_name, 'w', newline = '')
    writer = csv.writer(outfile)

    writer.writerow(['Full Name', 'Country'])

    for row in reader:
        customer_name = row[1] + ' ' + row[2]
        country = row[4]

        writer.writerow([customer_name, country])

    infile.close()
    outfile.close()

main()