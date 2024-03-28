from binance_historical_data import BinanceDataDumper
import argparse
import os
from datetime import date




DIR = os.path.dirname(os.path.abspath(__file__))




def main():

    parser = argparse.ArgumentParser(description="Download and dump binance historical data from binance.com/en/landing/data")
    parser.add_argument(
        "--dump_path", 
        metavar="dump_path", 
        help=f"Absolute path to dump files.  Default: {DIR}", 
        default=DIR)
    parser.add_argument(
        "--asset_class", 
        metavar="asset_class",
        help="Asset class: spot, usdt margined, or coin margined.  Acceptable arguments: spot, um, cm.  Default: 'spot'.",
        default="spot")
    parser.add_argument(
        "--data_type",
        metavar="data_type",
        help="Data type.  Acceptable arguments: [aggTrades, klines, trades] for spot, [aggTrades, klines, trades, indexPriceKlines, markPriceKlines, premiumIndexKlines, metrics] for futures (metrics only supported for um).  Default: 'klines'.",
        default="klines")
    parser.add_argument(
        "--data_frequency",
        metavar="data_frequency",
        help="Granularity of ticker data.  Acceptable arguments: 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d.  Default: '1h'.",
        default="1h")
    parser.add_argument(
        "-tickers",
        metavar="tickers",
        help="(list) Trading pairs for which to dump data.  If equals None, all USDT pairs will be used.  Acceptable argument: raw strings separated by spaces, e.g. BTCUSDT ETHUSDT AVAXUSDT.  Default: None.",
        nargs="+",
        default=None
    )
    parser.add_argument(
        "--date_start",
        metavar="date_start",
        help="(string, iso format (e.g. 2020-12-30)) The date from which to start dump.  If equals None, every trading pair will be dumped from the early begining (the earliest is 2017-01-01).  Default: None.",
        default=None
    )
    parser.add_argument(
        "--date_end",
        metavar="date_end",
        help="(string, iso format (e.g. 2020-12-30)) The last date for which to dump data.  If equals to None, Today's date will be used.  Default: None",
        default=None
    )
    parser.add_argument(
        "--update_existing",
        metavar="update_existing",
        help="(bool) Flag if you want to update the data if it already exists.  Default: False.",
        default=False
    )
    parser.add_argument(
        "--excluded_tickers",
        metavar="excluded_tickers",
        help="(list) Tickers to exclude from dump.  Acceptable arguments: raw strings separated by spaces, e.g. UST USDT USDC.  Default: ['UST']",
        nargs="+",
        default=["UST"]
    )

    args = parser.parse_args()

    start = None if args.date_start is None else date.isoformat(args.date_start)
    end = None if args.date_end is None else date.isoformat(args.date_end)


    data_dumper = BinanceDataDumper(
        path_dir_where_to_dump = args.dump_path,
        asset_class = args.asset_class,  # spot, um, cm
        data_type = args.data_type,  # aggTrades, klines, trades
        data_frequency= args.data_frequency,
    )   


    data_dumper.dump_data(
        tickers = args.tickers,
        date_start = start,
        date_end = end,
        is_to_update_existing = args.update_existing,
        tickers_to_exclude = args.excluded_tickers,
    )




if __name__ == "__main__":
    main()