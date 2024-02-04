import csv

def main():
    infile_name = r'C:\Users\maxww\Documents\AdvPython\readandwritefiles\employee_data.csv'

    # Explicitly open the file
    infile = open(infile_name, 'r', newline='')

    # CSV reader
    reader = csv.reader(infile)
    fields = next(reader)

    # Process data
    for row in reader:
        employee_ID = row[0]
        name = row[1]
        age = row[2]
        salary = float(row[3])
        hours_worked = int(row[4])
        productivity = row[5]
        team = row[6]
        bonus = float(row[7])

        bonus_amt = bonus * salary
        total_salary = bonus_amt + salary

        print(f"Name: {name}")
        print(f"Salary: $ {salary:,.2f}")
        print(f"Bonus:  $  {bonus_amt:,.2f}")
        print(f"Pay:    $ {total_salary:,.2f}")
        print()

    infile.close()

main()