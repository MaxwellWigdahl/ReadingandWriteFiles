import csv

def main():
    infile_name = r'C:\Users\maxww\Documents\AdvPython\readandwritefiles\employee_data.csv'
    infile = open(infile_name, 'r', newline='')

    reader = csv.reader(infile)
    fields = next(reader)

    highly_efficient = []
    low_efficiency = []
    worker_40s = []
    worker_30s = []
    worker_20s = []

    for row in reader:
        employee_ID = row[0]
        name = row[1]
        age = int(row[2])
        salary = float(row[3])
        hours_worked = int(row[4])
        productivity = int(row[5])
        team = row[6]
        bonus = float(row[7])

        efficiency = productivity / hours_worked

        if efficiency > 2: 
            highly_efficient.append(name)
        elif efficiency < 1:
            low_efficiency.append(name)

        if age >= 40:
            worker_40s.append(name)
        elif age >= 30:
            worker_30s.append(name)
        else:
            worker_20s.append(name)

        

    print("Highly Efficient Indiviuals")
    for name in highly_efficient:
        print(name)

    print()

    print("Low Efficiency Indiviuals:")
    for name in low_efficiency:
        print(name)
    print()


    print("Employees in their 40s")
    for name in worker_40s:
        print(name)
    print("Total number of employees in their 40s: " , len(worker_40s))
    print()

    print("Employees in their 30s")
    for name in worker_30s:
        print(name)
    print("Total number of employees in their 30s: " , len(worker_30s))
    print()

    print("Employees in their 20s")
    for name in worker_20s:
        print(name)
    print("Total number of employees in their 20s: " , len(worker_20s))

main()