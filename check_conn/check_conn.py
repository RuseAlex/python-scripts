import csv
import sys
import requests

status_dict= {"Website":"Status"}

def main(createCSV):
    with open("websites.txt", "r") as txtFile:
        for line in txtFile:
            website = line.strip()
            status = requests.get(website).status_code
            status_dict[website] = "working" if status == 200 else "not working"
        print(status_dict)
        if createCSV:
            with open("website_status.csv", "w", newline="") as csvFile:
                csv_writers = csv.writer(csvFile)
                for key in status_dict.keys():
                    csv_writers.writerow([key, status_dict[key]])
            

    if __name__ == "__name__":
        if len(sys.argv) >= 2:
            main(True)
        else:
            main()