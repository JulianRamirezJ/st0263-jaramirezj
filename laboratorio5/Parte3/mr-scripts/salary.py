from mrjob.job import MRJob


class SalaryStats(MRJob):

    def mapper(self, _, line):
        idemp, sececon, salary, _ = line.strip().split(',')
        
        yield sececon, float(salary)
        yield idemp, float(salary)
        yield idemp, sececon

    def reducer_avg_salary_by_sececon(self, sececon, salaries):
        total_salary = 0
        num_salaries = 0

        for salary in salaries:
            total_salary += salary
            num_salaries += 1

        avg_salary = total_salary / num_salaries
        yield sececon, avg_salary

    def reducer_avg_salary_by_employee(self, idemp, salaries):
        total_salary = 0
        num_salaries = 0

        for salary in salaries:
            total_salary += salary
            num_salaries += 1

        avg_salary = total_salary / num_salaries
        yield idemp, avg_salary

    def reducer_num_sececon_by_employee(self, idemp, sececons):
        unique_sececons = set(sececons)
        num_sececons = len(unique_sececons)
        yield idemp, num_sececons

    def steps(self):
        return [
            self.mr(mapper=self.mapper,
                    reducer=self.reducer_avg_salary_by_sececon),
            self.mr(mapper=self.mapper,
                    reducer=self.reducer_avg_salary_by_employee),
            self.mr(mapper=self.mapper,
                    reducer=self.reducer_num_sececon_by_employee)
        ]


if __name__ == '__main__':
    SalaryStats.run()
