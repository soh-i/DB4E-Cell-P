import re
import os.path

import species2


class PromoterDecGenerator(object):

    def __init__(self, filename):
        self.__filename = filename

    def reformat(self, data):
        if data[2] in "forward":
            return (data[0], "+1", data[3], data[3], "promoter", data[5])
        else:
            return (data[0], "-1", data[3], data[3], "promoter", data[5])

    def generate(self, session):
        with open(self.__filename, "r") as fin:
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

                # fout.write("%s\n" % ("\t".join(self.reformat(data))))
                obj = species2.PromoterDec(*self.reformat(data))
                session.add(obj)
        session.commit()

class TerminatorDecGenerator(object):

    def __init__(self, filename):
        self.__filename = filename

    def reformat(self, data):
        if data[3] in "forward":
            return (data[0], "+1", data[1], data[2], "terminator", data[4])
        else:
            return (data[0], "-1", data[1], data[2], "terminator", data[4])

    def generate(self, session):
        with open(self.__input_filename, "r") as fin:
            while True:
                line = fin.readline()
                if line is None or line == "":
                    break
                elif line.isspace() or re.match('^#', line):
                    continue

                line = line.rstrip()

                if not re.match('^\S',line):
                    continue

                data = line.split("\t")
                # fout.write("%s\n" % ("\t".join(self.reformat(data))))
                obj = species2.TerminatorDec(*self.reformat(data))
                session.add(obj)
        session.commit()
