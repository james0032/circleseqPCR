import argparse
import gzip
import itertools

from Bio.Seq import Seq
from utility import fqReader

itertools??
break

def mergeRead(read1, read2, outfile):
    fastq1 = fqReader(read1)
    fastq2 = fqReader(read2)

    with gzip.open(outfile, 'wb') as o:
        for r1, r2 in itertools.zip_longest(fastq1, fastq2):
            seq1 = Seq(r1[1])
            merged_seq = seq1.reverse_complement() + r2[1]
            merged_quality = r1[3][::-1] + r2[3]
            o.write(r1[0])
            o.write(merged_seq)
            o.write('+')
            o.write(merged_quality)

def main():
    des = "Usage:\nMerge Circle-Seq reads from paired-end fastq files\n\n" \
          "Append reverse-complemented R1 to R2 read so that the sequence \nwould be continuously in line with reference sequence."
    parser = argparse.ArgumentParser(description=des, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-r1', '--read1', help='Read 1 fastq filename', required=True)
    parser.add_argument('-r2', '--read2', help='Read 2 fastq filename', required=True)
    parser.add_argument('-o',  '--out', help='output filename', required=True)

    args = parser.parse_args()

    mergeRead(args.read1, args.read2, args.out)

if __name__ == "__main__":
    main()