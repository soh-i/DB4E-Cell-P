import re


class PromoterDecGenerator(object):

    def __init__(self, filename):
        self.__input_filename = filename

    def reformat(self, data):
        if data[2] in "forward":
            return (data[0], "1", data[3], data[3], "promoter", data[5])
        else:
            return (data[0], "-1", data[3], data[3], "promoter", data[5])

    def generate(self, filename):
        with open(filename, "w") as fout:
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

#     def __mapping_promoter(self):
#         with open(self.PROMOTOR_OUT, 'r') as f:
#             for line in f:
#                 (name, strand, start, end, feature, sequence) = line[:-1].split("\t")
#                 obj = species2.PromoterDec(name, strand, start, end, feature, sequence)
#                 print obj
#                 # obj = species.Promoter(name, strand, start, end, feature, sequence)
#                 self.session.add(obj)
#         self.session.commit()
