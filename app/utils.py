def read_csv(file_path):
    import csv

    data = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Skip the header row
        for row in csv_reader:
            data.append(dict(zip(header, row)))
    return data