"""Rebuild the explicit curated evidence ledger from frozen member/source records."""
from pathlib import Path
import hashlib
import re

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
ROLES = {
    'iscS': ('GO:0031071', 'TIGR01006'),
    'iscU': ('GO:0140132', 'TIGR01999'),
    'fdx': ('GO:0009055', 'TIGR02007'),
    'hscB': ('GO:0001671', 'IPR004640'),
    'hscA': ('GO:0016887', 'TIGR01991'),
    'iscA': ('GO:0140132', 'TIGR02011'),
}
PRIMARY = {
    'ECOLI': {'iscS': ['11577100'], 'iscU': ['15964837', '39870763'],
              'fdx': ['23682711', '25688831'], 'hscA': ['15485839', '18986169'],
              'hscB': ['10869428', '15485839'], 'iscA': ['11319236', '15964837']},
    'AZOVI': {'iscS': ['9582371', '16165131'], 'iscU': ['18562278', '16964969'],
              'fdx': ['10542283', '16936042', '25688831'], 'hscA': ['16964969'],
              'hscB': ['16964969'], 'iscA': ['16936042']},
}
RATIONALES = {
    'ECOLI': {
        'iscS': 'Direct sulfur handoff to IscU, not generic desulfurase similarity.',
        'iscU': 'Measured cluster scaffold/delivery chemistry; iron-loading evidence is distinct.',
        'fdx': 'Target-organism Fdx redox transfer and NADPH/FNR/Fdx-supported IscS/IscU assembly.',
        'hscA': 'Dedicated HscA ATPase cycle and ATP-dependent IscU cluster transfer.',
        'hscB': 'HscB activation of HscA and cognate IscU recruitment.',
        'iscA': 'Purified cluster loading/delivery, not iron donation alone; native ordering unresolved.',
    },
    'AZOVI': {
        'iscS': 'Exact AF010139 identity and native desulfurase/sulfur-transfer evidence.',
        'iscU': 'Native scaffold and target-organism cluster-delivery reconstitution.',
        'fdx': 'Native FdIV redox biophysics, specific ISC signatures and native ISC dependence support '
               'inference from E. coli donor chemistry. PMID16964969 uses Fdx as recipient, not donor.',
        'hscA': 'Target-organism HscA ATPase and HscB-dependent cluster-transfer assay.',
        'hscB': 'Target-organism HscB-dependent activation/transfer, not generic J-domain inference.',
        'iscA': 'Broad binding and native oxygen-dependent participation do not establish GO0140132 '
                'delivery. NifIscA experiments are not evidence for O31271.',
    },
}


def main():
    members = {}
    inputs = set()
    panels = {}
    for org in ['ECOLI', 'PSEPK', 'AZOVI']:
        panels[org] = {}
        for gene, (function, signature) in ROLES.items():
            review = Path(f'genes/{org}/{gene}/{gene}-ai-review.yaml')
            raw = Path(f'genes/{org}/{gene}/{gene}-uniprot.txt')
            doc = yaml.safe_load((ROOT / review).read_text())
            text = (ROOT / raw).read_text()
            # IscS entries consistently carry the specific HAMAP rule; avoid assuming TIGR version.
            if gene == 'iscS':
                signature = 'MF_00331'
            assert signature in text, (org, gene, signature)
            families = ['PANTHER:' + x for x in re.findall(r'DR   PANTHER; ([^;]+);', text)]
            if accession := doc.get('id'):
                if accession == 'P0A6Z1':
                    classification = yaml.safe_load((HERE / 'classification-provenance.yaml').read_text())
                    assert classification['accession'] == accession
                    families.append(classification['classification'])
            tier = 'DIRECT_ROLE_ASSAY' if org != 'PSEPK' else 'QUALIFIED_INFERENCE'
            if org == 'AZOVI' and gene == 'fdx':
                tier = 'QUALIFIED_INFERENCE'
            if org == 'AZOVI' and gene == 'iscA':
                tier = 'ROLE_UNRESOLVED'
            sources = PRIMARY.get(org, PRIMARY['ECOLI'])[gene]
            rationale = RATIONALES.get(org, {}).get(gene,
                'KT2440 isc-locus identity and specific curated/domain signatures support a cognate '
                'conserved-role inference from bacterial primary assays; no KT2440 assay is asserted.')
            accession = doc['id']
            panels[org][gene] = accession
            members[accession] = {
                'organism': org, 'taxon': doc['taxon']['id'], 'role': gene,
                'review_path': str(review), 'raw_path': str(raw), 'family_ids': families,
                'specific_signature': signature, 'required_function': function,
                'role_tier': tier, 'role_sources': ['PMID:' + p for p in sources],
                'rationale': rationale,
                'core_functions': [c['molecular_function']['id'] for c in doc['core_functions']
                                   if c.get('molecular_function')],
            }
            inputs.update([review, raw])
            inputs.update(Path(f'publications/PMID_{p}.md') for p in sources)
    interfaces = []
    for org, panel in panels.items():
        for edge, genes in [('sulfur_handoff', ['iscS', 'iscU']),
                            ('ferredoxin_donor', ['fdx', 'iscS', 'iscU']),
                            ('assisted_transfer', ['iscU', 'hscB', 'hscA'])]:
            tier = 'QUALIFIED_INFERENCE' if org == 'PSEPK' else 'DIRECT_ROLE_ASSAY'
            if org == 'AZOVI' and edge == 'ferredoxin_donor':
                tier = 'QUALIFIED_INFERENCE'
            edge_sources = {
                'ECOLI': {'sulfur_handoff': ['11577100'],
                          'ferredoxin_donor': ['23682711', '25688831'],
                          'assisted_transfer': ['10869428', '15485839', '18986169']},
                'AZOVI': {'sulfur_handoff': ['16165131'],
                          'ferredoxin_donor': ['10542283', '16936042', '25688831'],
                          'assisted_transfer': ['16964969']},
            }
            source_panel = 'ECOLI' if org == 'PSEPK' else org
            sources = edge_sources[source_panel][edge]
            inputs.update(Path(f'publications/PMID_{p}.md') for p in sources)
            interfaces.append({'organism': org, 'edge': edge,
                               'members': [panel[g] for g in genes], 'tier': tier,
                               'sources': ['PMID:' + p for p in sources],
                               'mechanism_source_panel': ('ECOLI' if org == 'PSEPK' or
                                                          (org == 'AZOVI' and edge == 'ferredoxin_donor')
                                                          else org),
                               'scope': ('Cognate compatibility inferred, not reconstituted.'
                                         if tier == 'QUALIFIED_INFERENCE' else
                                         'Cognate components assayed; no simultaneous five-role flux claim.')})
    inputs.update([
        Path('analysis/module_audits/bacterial_isc_iron_sulfur_cluster_assembly/'
             'final-boundary-consultation.md'),
        Path('analysis/module_audits/bacterial_isc_iron_sulfur_cluster_assembly/'
             'azotobacter-consultation/member-map.yaml'),
        Path('interpro/panther/PTHR10093/PTHR10093-review.yaml'),
        HERE.relative_to(ROOT) / 'classification-provenance.yaml',
        HERE.relative_to(ROOT) / 'interface-evidence.yaml',
        Path('genes/PSEPK/dnaK/dnaK-ai-review.yaml'),
        Path('genes/PSEPK/dnaK/dnaK-uniprot.txt'),
        Path('publications/PMID_26560204.md'),
    ])
    ledger = {
        'scope': 'Curated finite-panel oracle, not proteome prediction or native flux validation.',
        'profiles': {'supported_or_inferred': ['DIRECT_ROLE_ASSAY', 'QUALIFIED_INFERENCE'],
                     'assay_only': ['DIRECT_ROLE_ASSAY']},
        'panels': panels, 'members': members, 'interfaces': interfaces,
        'interface_evidence': yaml.safe_load((HERE / 'interface-evidence.yaml').read_text()),
        'source_sha256': {str(p): hashlib.sha256((ROOT / p).read_bytes()).hexdigest()
                          for p in sorted(inputs)},
    }
    (HERE / 'evidence-ledger.yaml').write_text(yaml.safe_dump(ledger, sort_keys=False, width=100))


if __name__ == '__main__':
    main()
