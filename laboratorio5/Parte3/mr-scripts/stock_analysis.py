from mrjob.job import MRJob
from mrjob.step import MRStep


class StockAnalysis(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer)
        ]

    def mapper(self, _, line):
        row = line.strip().split(",")

        if len(row) == 3:
            company = row[0]
            try:
                price = float(row[1])
                date = row[2]
                yield f"minmax-day-{company}", (date, price)
                yield f"stable-{company}", (date, price)
                yield "black-day", (date, price)
            except ValueError:
                pass

    def reducer(self, key, values):
        min_price = None
        max_price = None
        stable = True
        days = {}

        for date, price in values:
            if min_price is None or price < min_price:
                min_price = price
            if max_price is None or price > max_price:
                max_price = price

            if price < min_price:
                stable = False

            if date in days:
                days[date] += 1
            else:
                days[date] = 1

        if key.startswith("minmax-day"):
            yield key, (min_price, max_price)
        elif key.startswith("stable"):
            if stable:
                yield None, key
        elif key == "black-day":
            min_count = min(days.values())
            black_day = [date for date, count in days.items() if count == min_count]
            yield 'Black Day', (black_day, min_count)


if __name__ == '__main__':
    StockAnalysis.run()
