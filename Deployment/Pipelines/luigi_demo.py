import luigi
import numpy as np

class One(luigi.Task):
    def input(self):
        i1 = 'data/data.csv'
        return luigi.LocalTarget(i1)

    def output(self):
        o1 = 'data/output_One.txt'
        return luigi.LocalTarget(o1)

    def run(self):
        with self.input().open("r") as input_file:
            results = np.loadtxt(input_file).sum()

        with self.output().open("w") as output_file:
            output_file.write(str(results))


class Two(luigi.Task):
    def requires(self):
        return One()

    def output(self):
        o2 = 'data/output_Two.txt'
        return luigi.LocalTarget(o2)

    def run(self):
        with self.input().open("r") as input_file:
            read_value = np.loadtxt(input_file)

        with self.output().open("w") as output_file:
            if read_value > 25:
                final_result = 'OK'
            else:
                final_result = 'KO'

            output_file.write(final_result)