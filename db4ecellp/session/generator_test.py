from generators import Genbank
from generators import Promoter
from generators import Terminator

def generator_test():
    gb = Genbank()
    gb.generate_genbank_file()
    print "Finished gbk file"

    tm = Terminator()
    tm.generate_terminator_file()
    print "Finished terminator file"
    
    pr = Promoter()
    pr.generate_promoter_file()
    print "Finisehd promoter file"

if __name__ == '__main__':
    generator_test()



