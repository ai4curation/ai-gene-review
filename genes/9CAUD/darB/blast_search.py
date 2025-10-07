from Bio import Entrez, SeqIO
from Bio.Blast import NCBIWWW, NCBIXML

Entrez.email = "your@email.com"

# Search for qsuB homologs
print("Searching for qsuB (3-dehydroshikimate dehydratase) homologs in UniProt...")

# Read the sequence
with open('qsuB_sequence.fasta', 'r') as f:
    sequence = ''.join(f.readlines()[1:]).replace('\n', '')

# Run BLAST against nr database
print("Running BLAST (this may take a minute)...")
result_handle = NCBIWWW.qblast("blastp", "nr", sequence, 
                               entrez_query="txid1306[ORGN]",  # Limit to Corynebacterium
                               hitlist_size=10)

# Parse results
blast_records = NCBIXML.parse(result_handle)
blast_record = next(blast_records)

print(f"\nFound {len(blast_record.alignments)} hits for qsuB:")
for i, alignment in enumerate(blast_record.alignments[:5], 1):
    print(f"\n{i}. {alignment.title[:100]}")
    print(f"   Length: {alignment.length}")
    for hsp in alignment.hsps[:1]:
        print(f"   E-value: {hsp.expect:.2e}")
        print(f"   Identity: {hsp.identities}/{hsp.align_length} ({100*hsp.identities/hsp.align_length:.1f}%)")
        print(f"   Score: {hsp.score}")
