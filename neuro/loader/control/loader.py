import pandas
from neuro.utils.parse.cmdline import db_cmdline
from neuro.utils import file_utils

def main():
    parser = db_cmdline.db_parser('bin/loader', url_required=False)
    parser.add_argument(
        '--data_dir', '--data', '-data', '-dd',
        required=True,
        help="Directory of .csv files..."
    )
    cmdline = parser.parse_args()
    files = file_utils.find_files(cmdline.data_dir, ".csv", True)
    for f in files:
        df = pandas.read_csv(f, header=None, skiprows=5)
        print(df.loc[0,2])
        print(df)
        break
