import luigi
import numpy as np

class One(luigi.Task):
    def input(self):
        i = 'data/data.csv'
        return luigi.LocalTarget(i)

    def output(self):
        s = 'data/output_One.txt'
        return luigi.LocalTarget(s)

    def run(self):
        with self.input().open("r") as input_file:
            results = np.loadtxt(input_file).sum()

        with self.output().open("w") as output_file:
            output_file.write(str(results))


# class Two(luigi.Task):
#   def requires(self):
#       pass

#   def output(self):
#       pass

#   def run(self):
#       with self.input().open("r") as input_file