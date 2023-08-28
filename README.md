# Calculate_kmers

This script calculates the frequency of k-mers (subsequences of length k) in DNA sequences stored in FASTA files. It uses the Biopython library to process DNA sequences and provides the flexibility to customize the k-mer length and input assembly folder.

## Features

- Calculate k-mer frequencies from DNA sequences in FASTA files.
- Command-line interface for easy customization.
- Option to specify the k-mer length and input assembly folder.
- Creates an output folder to store k-mer frequency results.
- Logs the execution process, including start and completion times.

## Getting Started

1. **Prerequisites:** Ensure you have Python 3.11 installed on your system.

2. **Installation:** Clone this repository to your local machine:

   ```bash
   git clone https://github.com/pyadav06/Calculate_kmers
   cd Calculate_kmers
   
3. **Usage:** Run the script with the desired options. 
   --kmer: Length of k-mers to calculate (default: 5).
   --assembly_folder: Path to the folder containing input FASTA files (default: assembly/).
   --output_folder: Path to the folder to store k-mer frequency results (default: "outfile" folder within --assembly_folder).
   Here's an example command:
   ```bash
   python calculate_kmers.py --kmer 5 --assembly_folder "Path/to/the/genome/assembly/folder" --output_folder "Path/to/the/output/folder"
  
5. **Results:** The script will generate TSV files containing k-mer frequencies in the specified output folder.

6. **Example:** To demonstrate the script's functionality, the repository includes sample DNA sequences in the assembly folder. The expected output is stored in outfile and logfile comprises the log. You can run the script with the following 
   command:
      ```bash
      python calculate_kmers.py --kmer 6 --assembly_folder "Path/to/the/genome/assembly/folder" --output_folder "Path/to/the/output/folder"

