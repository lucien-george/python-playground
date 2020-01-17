import csv

data = []
with open ('./test_data.csv', 'r') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=",")

  for row in csv_reader:
    print(' '.join(row))
    row = list(filter(lambda x: x != '', row))
    data.append(row)
print(data)

with open('./test_data.csv', 'w') as csv_file:
  csv_writer = csv.writer(csv_file, delimiter=",")
  csv_writer.writerow(['primary_name', 'category', 'age'])
  for row in data:
    csv_writer.writerow(row)
