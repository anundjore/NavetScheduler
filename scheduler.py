from collections import defaultdict

## Program laget for å hente ut datoer fra .TSV filen med svar på arrangementer for IFI-navet
## Legg til scheduler.py og .TSV filen i samme mappe, og gi filen navn 'skjema.tsv', eller endre variabelnavnet



def main(csv):
    file = open(csv)
    dictionary_date_and_companies = defaultdict(list)
    toggle = False

    for line in file:
        line = line.split("\t")

        dates = line[13].split(",")
        company = line[2]

        if toggle:
            for date in dates:
                dictionary_date_and_companies[date].append(company)
        toggle = True

    new_list = dictionary_date_and_companies

    file_path = "output.txt"

    with open(file_path, "w") as file:
        for key, value in new_list.items():
            file.write(f"{key}: {value}\n")

    print(
        """
    _   _                 _    
    | \ | | __ ___   _____| |_  
    |  \| |/ _` \ \ / / _ \ __| 
    | |\  | (_| |\ V /  __/ |_  
    |_| \_|\__,_| \_/ \___|\__| 
        """
    )

    print("Semesterplanen er lagret som output.txt")


if __name__ == "__main__":
    main("skjema.tsv")
