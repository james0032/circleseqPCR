import gzip
import re

def fqReader(fqfile):
    if re.search('.gz$', fqfile):
        fastq = gzip.open(fqfile, 'rb')
    elif re.search('.fastq$', fqfile) or re.search('.fq$', fqfile):
        fastq = open(fqfile, 'r')


    with fastq as f:
        while True:
            l1 = f.readline().rstrip('\n')
            if not l1:
                break
            elif re.search('^@', l1):
                continue
            l2 = f.readline().rstrip('\n')
            l3 = f.readline().rstrip('\n')
            l4 = f.readline().rstrip('\n')
            yield [l1 ,l2, l3, l4]
