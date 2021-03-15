import pandas as pd
import csv
import os, inspect, glob
import numpy as np






def combine_csv(path):
    os.chdir()
    extension = 'csv'
    all_filenames = [i for i in glob.glob('*.{extension}'.format(extension=extension))]
    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
    combined_csv.to_csv("combined_csv.csv", index=False, encoding='utf-8-sig')






def main():
    data = pd.read_csv("combined_csv.csv")
    columns = ['c_asn', 'c_bytes_all', 'c_durat', 'c_first_abs', 'c_ip', 'c_isint',
       'c_pkts_all', 'c_port', 'c_type', 's_asn', 's_bytes_all', 's_durat',
       's_first_abs', 's_ip', 's_isint', 's_pkts_all', 's_port', 's_type',
       'service']
    data['c_asn'] = pd.to_numeric(data['c_asn'], errors='coerce')
    data['s_asn'] = pd.to_numeric(data['s_asn'], errors='coerce')
    print(data.dtypes)



if __name__ == '__main__':
    main()
