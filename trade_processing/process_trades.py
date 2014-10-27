import csv
import argparse

class CSVHandler(object):

    def read_csv(self, filename):
        with open(filename, 'rb') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                yield row

    def write_csv(self, data, filename):
        with open(filename, 'wb') as csv_file:
            writer = csv.writer(csv_file)
            for row in data:
                writer.writerow(row)

class TradeData(object):
    
    def __init__(self, symbol=None, timestamp=0, quantity=0, price=0):
        self.symbol = symbol
        self.last_traded_time = timestamp
        self.max_gap_in_trade_time = 0
        self.total_volume = quantity
        self.total_value = quantity*price
        self.max_price = price
        #self.weighted_average

    def update_last_traded_time(self, timestamp):
        self.max_gap_in_trade_time = max([(timestamp - self.last_traded_time), 
                                            self.max_gap_in_trade_time])
        self.last_traded_time = timestamp

    def update_total_volume(self, volume):
        self.total_volume += volume

    def update_total_value(self, value):
        self.total_value += value

    def update_max_price(self, price):
        if price > self.max_price:
            self.max_price = price

    def update_data(self, timestamp, quantity, price):
        self.update_last_traded_time(timestamp)
        self.update_total_volume(quantity)
        self.update_total_value(quantity*price)
        self.update_max_price(price)


class TradeProcessor(object):

    def __init__(self):
        self.csv_handler = CSVHandler()
        self.trade_map = {}

    def build_trade_history(self, filename):
        for row in self.csv_handler.read_csv(filename):
            timestamp = int(row[0])
            symbol = row[1]
            quantity = int(row[2])
            price = int(row[3])
            if symbol in self.trade_map:
                self.trade_map[symbol].update_data(timestamp, quantity, price)
            else:
                self.trade_map[symbol] = TradeData(symbol, timestamp, quantity, price)

    def generate_sorted_keys(self):
        return (key for key in sorted(self.trade_map.keys()))
        
    def generate_trade_summary(self):
        for symbol in self.generate_sorted_keys():
            trade = self.trade_map[symbol]
            yield [symbol, 
                    trade.max_gap_in_trade_time,
                    trade.total_volume,
                    int(trade.total_value/trade.total_volume),
                    trade.max_price]

    def output_trade_summary_to_csv(self, filename):
        self.csv_handler.write_csv(self.generate_trade_summary(), filename)

def main(input_filename, output_filename):
    processor = TradeProcessor()
    processor.build_trade_history(input_filename)
    processor.output_trade_summary_to_csv(output_filename)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate the trading information")
    parser.add_argument('--input', '-i', help='input CSV file path',
                        default='input.csv')
    parser.add_argument('--output', '-o', help='output csv file path',
                        default='output.csv')
    args = parser.parse_args()
    main(args.input, args.output)

