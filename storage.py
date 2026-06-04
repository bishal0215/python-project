import csv 
import os
def save_to_csv(filename,data,headers):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    file_exists = os.path.exists(filename)

    with open(filename,"a",newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(headers)
        writer.writerow(data)

def read_csv(filename):
    if not os.path.exists(filename):
        return []
    with open(filename,"r",newline="") as file:
        reader = csv.reader(file)
        return list(reader)
    


