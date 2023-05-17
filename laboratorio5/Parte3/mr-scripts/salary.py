from mrjob.job import MRJob
from mrjob.step import MRStep

class Salary(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer)
        ]

    def mapper(self, _, line):
        row = line.replace(" ", "").split(",")

        try:
            idemp = int(row[0])
            sector = int(row[1])
            salary = float(row[2])
            year = int(row[3])
        except ValueError:
            return

        yield f"sector-{sector}-avg", salary
        yield f"employee-{idemp}-avg", salary
        yield f"employee-count-{idemp}", sector

    def reducer(self, key, values):
        if key.startswith("employee-count-"):
            count = len(set(values))
            yield key, count
        else:
            values = list(values)
            avg_salary = sum(values) / len(values)
            yield key, avg_salary


if __name__ == "__main__":
    Salary.run()
