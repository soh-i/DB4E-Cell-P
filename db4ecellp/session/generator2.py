import re
import os.path

import species2


class PromoterDecGenerator(object):

    def __init__(self, input_filename, output_filename):
        self.__input_filename = input_filename
        self.__output_filename = output_filename

    def reformat(self, data):
        if data[2] in "forward":
            return (data[0], "+1", data[3], data[3], "promoter", data[5])
        else:
            return (data[0], "-1", data[3], data[3], "promoter", data[5])

    def save(self):
        with open(self.__output_filename, "w") as fout:
            with open(self.__input_filename, "r") as fin:
                while True:
                    line = fin.readline()
                    if line is None or line == "":
                        break
                    elif line.isspace() or re.match('^#', line):
                        continue

                    line = line.rstrip()

                    data = line.split("\t")
                    if not len(data) == 7:
                        continue
                    fout.write("%s\n" % ("\t".join(self.reformat(data))))

    def generate(self, session):
        # if not os.path.isfile(self.__output_filename):
        if True:
            self.save() # save cache

        with open(self.__output_filename, 'r') as fin:
            while True:
                line = fin.readline()
                if line is None or line == "":
                    break

                data = line[: -1].split("\t")
                obj = species2.PromoterDec(*data)
                session.add(obj)

        session.commit()
