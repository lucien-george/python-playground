# import csv

# data = []
# with open ('./test_data.csv', 'r') as csv_file:
#   csv_reader = csv.reader(csv_file, delimiter=",")

#   for row in csv_reader:
#     print(' '.join(row))
#     row = list(filter(lambda x: x != '', row))
#     data.append(row)
# print(data)

# with open('./test_data.csv', 'w') as csv_file:
#   csv_writer = csv.writer(csv_file, delimiter=",")
#   csv_writer.writerow(['primary_name', 'category', 'age'])
#   for row in data:
#     csv_writer.writerow(row)

import csv

data = []
id = 1
with open ('./test_data.csv', 'r') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=",")
  next(csv_reader)
  for row in csv_reader:
    row.append(id)
    data.append(row)
    modified_row = row.copy()
    modified_row[0] = modified_row[0][:2] + '  ' + modified_row[0][2:]
    data.append(modified_row)
    id += 1

with open('./test_data.csv', 'w') as csv_file:
  csv_writer = csv.writer(csv_file, delimiter=",")
  csv_writer.writerow(['primary_name', 'category', 'id'])
  for row in data:
    csv_writer.writerow(row)
