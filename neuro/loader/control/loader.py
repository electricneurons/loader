import pandas as pd
import matplotlib.pyplot as plt

from neuro.utils.parse.cmdline import db_cmdline
from neuro.utils import file_utils

def main():
    ret_val = None

    parser = db_cmdline.db_parser('bin/loader', url_required=False)
    parser.add_argument(
        '--data_dir', '--data', '-data', '-dd',
        required=True,
        help="Directory of .csv files..."
    )
    cmdline = parser.parse_args()
    files = file_utils.find_files(cmdline.data_dir, ".csv", True)
    for f in files:
        df = pd.read_csv(f, header=None, skiprows=5)
        print(df.loc[0,2])
        print(df)
        ret_val = df
        break

def plot():
    #df = main()
    headers = ['Student', 'RollNumber', 'Grade']
    students = {'Student': ['Amit', 'Cody', 'Darren', 'Drew'], 
        'RollNumber': [1, 5, 10, 15],
        'Grade': ['A', 'C', 'F', 'B']
    }
    df = pd.DataFrame(students, columns = headers)

    # displaying the original DataFrame
    print("Original DataFrame")
    print(df)
    
    # saving as a CSV file
    df.to_csv('Students.csv', sep ='\t')    

    plt.rcParams["figure.figsize"] = [7.50, 3.50]
    plt.rcParams["figure.autolayout"] = True

    df = pd.read_csv('Students.csv', names=headers)
    df.set_index('Student').plot()
    plt.show()
