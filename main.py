import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import click


@click.command(no_args_is_help=True)
@click.option('--inputfile', type=click.Path(exists=True), required=True, help='Path to the CSV input file.')
@click.option('--outputdir', type=click.Path(), required=True, help='Directory where the Parquet file will be saved.')
def convert_csv_to_parquet(inputfile, outputdir):
    # Read the CSV file
    df = pd.read_csv(inputfile, sep=";")

    # Convert the DataFrame to a Parquet file
    df.to_parquet(outputdir)

if __name__ == '__main__':
    convert_csv_to_parquet()
