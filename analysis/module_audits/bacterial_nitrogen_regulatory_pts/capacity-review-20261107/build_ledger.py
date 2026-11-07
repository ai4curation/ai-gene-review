"""Record manually assessed primary edges independently of module declarations."""
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
A = OUT.parent
panel = [('ECOLI', 'ptsP'), ('ECOLI', 'ptsO'), ('ECOLI', 'ptsN'),
         ('PSEPK', 'ptsP'), ('PSEPK', 'ptsH'), ('PSEPK', 'ptsN'),
         ('CAUVN', 'ptsP'), ('CAUVN', 'ptsH'), ('CAUVN', 'ptsN'),
         ('ECOLI', 'ptsI'), ('ECOLI', 'ptsH'), ('BACSU', 'ptsH')]
members = {}
for organism, gene in panel:
    path = f'genes/{organism}/{gene}/{gene}-ai-review.yaml'
    doc = yaml.safe_load((ROOT / path).read_text())
    members[doc['id']] = {'review': path, 'organism': organism, 'taxon': doc['taxon']['id'],
                          'uniprot': f'genes/{organism}/{gene}/{gene}-uniprot.txt'}

def ev(pmid, quote, limit):
    return {'source': f'publications/PMID_{pmid}.md', 'quote': quote, 'scope': limit}

ecoli1 = ev('10473571', 'EI(Ntr) phosphorylated NPr but not HPr',
             'Abstract explicitly reports purified E. coli enzyme specificity. Not a universal cross-system prohibition.')
ecoli2 = ev('7876255', 'Purified IIANtr and NPr exchange phosphate',
             'Abstract reports purified protein phosphate exchange, including cross-system reactions; native exclusivity is not claimed.')
psepk = ev('18296519', 'the primary flow of phosphate through the N/C-sensing PTS proceeds from PEP to EI(Ntr) to NPr to EIIA(Ntr)',
            'Native KT2440-derived MAD2 phosphorylation genetics; canonical cache contains abstract/discussion, not complete primary methods.')
cauvn = ev('27109061', 'Besides ptsP (EINtr), we found a unique HPr homologue (ptsH, CCNA_00241) and another nitrogen-related PTSNtr component, EIIANtr (ptsN, CCNA_03710).',
            'NA1000 native genetics and phosphostate experiments plus heterologous relay complementation; not purified binary transfer kinetics.')
output = {
 'P69829': ev('19400808', 'interacts with sensor kinase KdpD and stimulates kinase', 'Direct E. coli kinase-activation output; other outputs are not required.'),
 'Q88PA0': ev('21236318', 'the non-phosphorylated form of PtsN is the protein species that inhibits PDH', 'Target association and cell-extract activity, not purified binary inhibition.'),
 'A0A0H3CDT8': ev('27109061', 'these findings demonstrate that EIIANtr∼P inhibits hydrolase activity of SpoT', 'Phosphostate BTH and engineered native hydrolase dissection; no isolated inhibition kinetics.')}
edges = []
for organism, taxon, proteins, sources in [
 ('ECOLI', 'NCBITaxon:83333', ('P37177','P0A9N0','P69829'), (ecoli1,ecoli2)),
 ('PSEPK', 'NCBITaxon:160488', ('Q88CN5','Q88PA2','Q88PA0'), (psepk,psepk)),
 ('CAUVN', 'NCBITaxon:565050', ('A0A0H3C823','A0A0H3C344','A0A0H3CDT8'), (cauvn,cauvn))]:
    edges += [{'donor': proteins[0], 'acceptor': proteins[1], 'donor_role': 'entry', 'acceptor_role': 'carrier', 'organism': organism, 'taxon': taxon, 'relation': 'native_relay_transfer', 'evidence': sources[0]},
              {'donor': proteins[1], 'acceptor': proteins[2], 'donor_role': 'carrier', 'acceptor_role': 'terminal', 'organism': organism, 'taxon': taxon, 'relation': 'native_relay_transfer', 'evidence': sources[1]}]
ledger = {'members': members, 'native_edges': edges, 'terminal_outputs': output,
 'controls': {'P08839': 'Carbohydrate EI: measured PEP-protein chemistry does not make it native Ntr PtsP.',
              'P0AA04': 'E. coli HPr: in-vitro exchange exists; EI(Ntr) discriminates against HPr in 10473571. Not proof all bypasses are impossible.',
              'P08877': 'B. subtilis carbohydrate HPr shares SF2 with native NPr carriers and the same core chemical genus; no matched native Ntr partner evidence here.'},
 'bypass': ev('18296519', 'in the presence of fructose, unlike in the presence of succinate, EIIA(Ntr) can be phosphorylated in a ptsP strain but not in a ptsP fruB double mutant', 'A condition-specific alternative input; failure of the canonical route is not failure of every possible PtsN phosphorylation route.'),
 'unknown_policy': 'Unlisted members or absent native partner evidence are UNRESOLVED, not experimentally inactive.',
 'function_anchors': {'entry': [{'source_id':'PMID:10473571', 'quote':'EI(Ntr) phosphorylated NPr but not HPr'}], 'carrier': [{'source_id':'PMID:7876255','quote':'Purified IIANtr and NPr exchange phosphate'}], 'terminal': [{'source_id':'PMID:19400808','quote':'stimulates kinase activity'}, {'source_id':'PMID:21236318','quote':'the enzyme activity was measured in extracts of isogenic ptsN(+)/ptsN(-)P. putida strains'}]},
 'role_chemistry': {'entry':'GO:0008965','carrier':'GO:0016775','terminal':'GO:0098772'}}
(OUT / 'evidence-ledger.json').write_text(json.dumps(ledger, indent=2)+'\n')
