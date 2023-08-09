# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"14AQ.00","system":"readv2"},{"code":"G57y900","system":"readv2"},{"code":"12375.0","system":"med"},{"code":"1297.0","system":"med"},{"code":"1536.0","system":"med"},{"code":"18357.0","system":"med"},{"code":"23647.0","system":"med"},{"code":"29491.0","system":"med"},{"code":"35124.0","system":"med"},{"code":"4940.0","system":"med"},{"code":"51845.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('supraventricular-tachycardia-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["supraventricular-tachycardia---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["supraventricular-tachycardia---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["supraventricular-tachycardia---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
