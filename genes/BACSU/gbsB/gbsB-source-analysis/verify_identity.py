"""Verify original JH642 GbsA/B sequences and the deposited OpuBC binding domain."""
from pathlib import Path
import json
import re
from Bio import SeqIO

HERE = Path(__file__).resolve().parent
BACSU = HERE.parents[1]

def canonical(gene):
    text = (BACSU / gene / (gene + '-uniprot.txt')).read_text()
    return ''.join(re.findall('[A-Z]+', text.split('SQ   SEQUENCE')[1].split('\n', 1)[1].split('//')[0]))

record = SeqIO.read(HERE / 'U47861.gb', 'genbank')
products = {f.qualifiers.get('product', [''])[0]: f for f in record.features if f.type == 'CDS'}
assert products['GbsA'].qualifiers['translation'][0] == canonical('gbsA')
assert products['GbsB'].qualifiers['translation'][0] == canonical('gbsB')[9:]
assert str(record.seq[2751:3960].translate(table=11, to_stop=True)) == canonical('gbsB')
entity = json.loads((BACSU / 'opuBC/opuBC-source-analysis/3R6U-entity1.json').read_text())
assert entity['entity_poly']['pdbx_seq_one_letter_code_can'] == canonical('opuBC')[22:]
print('PASS: GbsA exact, GbsB long/short starts, deposited OpuBC binding-domain mapping')
print('OpuBC caveat: paper methods report terminal Cys-to-Gly engineering; the deposited entity retains Cys.')
