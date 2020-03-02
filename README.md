# dkpd

dkpd is a small python module that downloads data from the [historical data feed] of Dukascopy
and stores it locally on the disk.
It can decompress the data and load them into a Pandas DataFrame for processing.

[historical data feed]: https://www.dukascopy.com/swiss/english/marketwatch/historical/

## Usage

Use `download_ticks(start_date, end_date, instr_type, instr_name )` to download the data files to the local data directory.
Use `convert_ticks(start_date, end_date, instr_type, instr_name)` to load the data from the downloaded files and convert them to a Pandas DataFrame.

## License

Dukapd is distributed under the terms of the MIT License.

See [LICENSE](LICENSE) for details.
