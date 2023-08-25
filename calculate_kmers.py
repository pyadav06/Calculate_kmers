# Author: Pooja Yadav, UNL
# Date created : 08/24/2023
# Date modified : 08/24/2023

import os
from Bio import SeqIO
import csv
import time
import argparse  # Import argparse module to handle command-line arguments

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Calculate k-mer frequencies from DNA sequences.")
parser.add_argument('--kmer', type=int, required=False, default=5, help='Length of k-mers')
parser.add_argument('--assembly_folder', type=str, default='assembly/', help='Path to the assembly folder')
parser.add_argument('--output', type=str, default='', required=False, help='Path to the output folder')
parser.add_argument('--logfile', type=str, default='', required=False, help='Path to the log file')
args = parser.parse_args()


length_kmer = args.kmer
fasta_dir_path = args.assembly_folder
output = args.output
log = args.logfile
# If output_folder is not specified, use assembly_folder or default input directory
if not output:
    output = os.path.join(args.assembly_folder, 'outfile')
os.makedirs(output, exist_ok=True)
# If output_folder is not specified, use assembly_folder or default input directory
if not log:
    log = os.path.join(args.assembly_folder, 'log')
os.makedirs(log, exist_ok=True)

# create a log file to record results and run times
# string format the time
fa = open(log+'/log_kmer_'+time.strftime('%Y%m%d %H:%M:%S')+'.txt', 'a')
fa.write('\n==== '+time.strftime('%Y-%m-%d %H:%M:%S')+' ====\n')
fa.write('##Find_kmers.py started##\n')
fa.write('##calculate_kmers_frequency started##\n' )

# main body
def calculate_kmers_frequency(sequence, length_of_kmer):
    kmer_freq = {}
    for i in range(len(sequence) - length_of_kmer + 1):
        kmer = str(sequence[i: i + length_of_kmer])
        if kmer in kmer_freq:
            kmer_freq[kmer] += 1
        else:
            kmer_freq[kmer] = 1
    return kmer_freq


# update the log
fa.write('\n==== '+time.strftime('%Y-%m-%d %H:%M:%S')+' ====\n')
fa.write('##calculate_kmers_frequency completed##\n')
fa.write('##dictionary_to_tsv started##\n')


def dictionary_to_tsv(kmer_output, kmer_freq):
    with open(kmer_output, 'w', newline='', encoding='utf-8') as tsvfile:
        writer = csv.writer(tsvfile, delimiter='\t')
        writer.writerow(['5-mer', 'frequency'])
        for key, value in kmer_freq.items():
            writer.writerow([key, value])


# update the log
fa.write('\n==== '+time.strftime('%Y-%m-%d %H:%M:%S')+' ====\n')
fa.write('##dictionary_to_tsv completed##\n')
fa.write('##convert_fasta_to_tsv started##\n')


def convert_fasta_to_tsv(fasta_dir):
    for filename in os.listdir(fasta_dir):
        if filename.endswith('.fasta') or filename.endswith('.fa'):
            fa.writelines("Processing " + filename + "\n")
            fasta_file_path = os.path.join(fasta_dir, filename)
            with open(fasta_file_path, "r") as fasta_files:
                for seq_record in SeqIO.parse(fasta_files, "fasta"):
                    cur_sequence = seq_record.seq
                    kmer_freq_dict = calculate_kmers_frequency(cur_sequence, length_kmer)
                    kmer_output_file = os.path.join(output, filename
                                                    + 'kmer_output.tsv')  # change the output folder path
                    dictionary_to_tsv(kmer_output_file, kmer_freq_dict)


convert_fasta_to_tsv(fasta_dir_path)
# update the log
fa.writelines('\n==== '+time.strftime('%Y-%m-%d %H:%M:%S')+' ====\n')
fa.write('##Find k-mer has been completed##\n')

