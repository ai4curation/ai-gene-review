"""Build two source-grounded family reviews; never mutate fetched family sources."""
import csv
import hashlib
import json
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
FAMILIES = ['PTHR33799', 'PTHR32502']


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def support(ref, text, section=None):
    row = {'reference_id': ref, 'supporting_text': text}
    # Family SupportingText has no record_section slot; provenance is in the consultation.
    return row


def main():
    source_hashes = {}
    for family in FAMILIES:
        p = ROOT / f'interpro/panther/{family}/{family}-review.yaml'
        assert not p.exists(), p
        for suffix in ['metadata.yaml', 'entries.csv', 'paint.tsv']:
            source = p.with_name(f'{family}-{suffix}')
            source_hashes[str(source.relative_to(ROOT))] = sha(source)
    (HERE / 'baseline.json').write_text(json.dumps({'new_reviews_previously_absent': FAMILIES,
                                                  'protected_sources_sha256': source_hashes}, indent=2)+'\n')
    labels = {}
    for stanza in (ROOT / 'interpro/panther/panther.obo').read_text().split('[Term]'):
        lines = stanza.strip().splitlines()
        ids = [v[4:] for v in lines if v.startswith('id: ')]
        names = [v[6:] for v in lines if v.startswith('name: ')]
        if ids and names and any(ids[0].startswith('PANTHER:' + f) for f in FAMILIES):
            labels[ids[0]] = names[0]
    (HERE / 'official-labels.json').write_text(json.dumps(labels, indent=2)+'\n')
    terms = {r['id']: r['name'] for r in json.loads((HERE / 'go-terms.json').read_text())['results']}
    trees = json.loads((HERE / 'trees-compact.json').read_text())
    evidence = ['# Official family evidence and bounded interpretation', '',
                'Official PANTHER tree responses and UniProt JSON are archived with acquisition URLs/hashes in this directory. Cached metadata descriptions are marked llm:true/checked:false and are not treated as functional evidence.', '']
    for family in FAMILIES:
        tree = trees[family]
        evidence += ['## ' + family, f'Current official reference tree contains {len(tree["leaves"])} leaves.']
        for row in csv.DictReader((ROOT / f'interpro/panther/{family}/{family}-paint.tsv').open(), delimiter='\t'):
            members = [tree['leaves'][p] for p in tree['under'].get(row['node'], [])]
            evidence.append(f"{row['node']} / {row['go_id']} spans {len(members)} current leaves: " + '; '.join(f"{m['uniprot']} ({m['symbol']}; {m['subfamily']})" for m in members) + '.')
    evidence += ['', '## Architecture and source limits',
                 'P69797 ManX has separate EIIA and EIIB domains (Pfam PF03610 and PF03830); the curated domains are 2–124 and 157–320, with phosphohistidines at 10 and 175. This is reference-protein architecture, not a universal family residue discriminator.',
                 'P26379 LevD is 146 residues and carries the EIIA-man domain; P69797 ManX is 323 residues and combines EIIA with EIIB. Both occur in PTHR33799:SF1.',
                 'P69801 ManY is PTHR32502:SF4 and P69805 ManZ is PTHR32502:SF5. LevF P26381 and LevG P26382 occur in those same respective subfamilies. Subfamily membership does not distinguish mannose from fructose specificity.',
                 'Official current UniProt places IL1403 PtnAB/PtnC/PtnD Q9CEX8/Q9CEX7/Q9CEX6 in PTHR33799:SF1/PTHR32502:SF25/PTHR32502:SF27; UA159 Q8DSC4/Q8DSC3/Q8DSC2 has the same respective classification. Classification establishes identity/domain placement, not primary assay strain attribution.',
                 'PMID2117666 is abstract-only in the immutable cache. Its explicit report that LevDEFG is not involved in mannose uptake supplies a source-reported substrate boundary, not an inferred absence or an independently inspected full experimental negative assay.',
                 'PMID11976750 is newly normally fetched and abstract-only. It explicitly reports that GatZ/KbaZ support full activity and stability of the catalytic Y subunit. Official curated UniProt FUNCTION statements tie the same positive role to ECO:0000269/PubMed:11976750. No autonomous chaperone-foldase activity is inferred.',
                 'The current root PTN000789828 spans both membrane PTS branches and the downstream carbohydrate-enzyme branches. PTN001287483 covers the seven GatZ/KbaZ-like descendants, separate from the IIC/IID branches.',
                 'The preserved PAINT rows for PTN002845864 and PTN002845871 carry taxon:1385 although the current descendant set includes enterobacterial ManY/ManZ as well as Bacillus LevF/LevG. That metadata is retained as provenance, not used to replace actual tree membership.',
                 'No universal mannose grant, fusion claim, mapped evolutionary loss, new PAINT assertion, or residue-specific scope discriminator is inferred from protein names or from the number of seeds.', '']
    (HERE / 'evidence.md').write_text('\n'.join(evidence))
    evref = 'file:' + str((HERE / 'evidence.md').relative_to(ROOT))
    broad_pts = support('PMID:2117666', 'The levD and levE gene products that form part of\na fructose uptake PTS act as negative regulators of the operon.')
    lev_boundary = support('PMID:2117666', 'genes are not involved in mannose uptake, but form a fructose phosphotransferase\nsystem in B. subtilis.')
    gat_positive = support('PMID:11976750', 'both aldolases required subunits GatZ or\nKbaZ (420 amino acids) for full activity and for good in vivo and in vitro\nstability.')
    arch = support(evref, 'P26379 LevD is 146 residues and carries the EIIA-man domain; P69797 ManX is 323 residues and combines EIIA with EIIB. Both occur in PTHR33799:SF1.')
    gatz_ref = 'file:' + str((HERE / 'P0C8J8-uniprot.json').relative_to(ROOT))
    gatz_function = support(gatz_ref, 'Component of the tagatose-1,6-bisphosphate aldolase GatYZ that is required for full activity and stability of the Y subunit.', 'CC:FUNCTION')
    references = []
    for pmid, notes in [('2117666', 'Abstract explicitly reports LevDEFG fructose uptake and no mannose uptake; full experimental negative assay was not independently available. Used as a reported substrate boundary with curated UniProt and architecture, not a basis to rewrite experimental gene rows.'), ('11976750', 'Normally fetched abstract plus publication-linked curated UniProt FUNCTION support positive GatZ/KbaZ activation/stabilization of aldolase Y. Do not convert chaperone-like speculation into autonomous protein-folding activity.')]:
        content = (ROOT / f'publications/PMID_{pmid}.md').read_text()
        metadata = yaml.safe_load(content.split('---', 2)[1])
        references.append({'id': 'PMID:' + pmid, 'title': metadata['title'], 'full_text_unavailable': True,
                           'reference_review': {'relevance': 'HIGH', 'correctness': 'VERIFIED', 'review_notes': notes}})
    references.append({'id': evref, 'title': 'Official PANTHER tree and curated UniProt architecture evidence',
                       'reference_review': {'relevance': 'HIGH', 'correctness': 'VERIFIED',
                                            'review_notes': 'Computed tree descendants and source-specific identity/domain observations; raw snapshots and provenance are separately archived.'}})
    references.append({'id': gatz_ref, 'title': 'Official curated UniProt P0C8J8 record',
                       'reference_review': {'relevance': 'HIGH', 'correctness': 'VERIFIED',
                                            'review_notes': 'FUNCTION paragraph is explicitly ECO:0000269 with PMID11976750/8955298; no label/ARBA-only inference.'}})
    def protein(a, label, gene, org, path=None):
        value = {'id': 'UniProtKB:' + a, 'label': label, 'gene_symbol': gene, 'organism': org}
        if path:
            value['gene_review'] = path
        return value
    ecx = protein('P69797', 'PTS system mannose-specific EIIAB component', 'manX', 'Escherichia coli K-12', 'genes/ECOLI/manX/manX-ai-review.yaml')
    ecy = protein('P69801', 'PTS system mannose-specific EIIC component', 'manY', 'Escherichia coli K-12', 'genes/ECOLI/manY/manY-ai-review.yaml')
    ecz = protein('P69805', 'PTS system mannose-specific EIID component', 'manZ', 'Escherichia coli K-12', 'genes/ECOLI/manZ/manZ-ai-review.yaml')
    for family in FAMILIES:
        doc = {'family_id': 'PANTHER:' + family, 'family_name': labels['PANTHER:' + family],
               'preferred_name': 'Mannose-family PTS IIA and fused IIAB phosphorelay proteins' if family == 'PTHR33799' else 'PTS IIC/IID and downstream carbohydrate-enzyme superfamily',
               'summary': ('Members participate in sugar-specific phosphoenolpyruvate-dependent phosphotransfer systems. The shared IIA architecture occurs both as a separate soluble phosphorelay protein, exemplified by Bacillus LevD, and fused to an IIB domain, exemplified by Escherichia coli ManX. Substrates include mannose-family system sugars, fructose and sorbose; the fold or single PANTHER subfamily does not define the transported sugar or ensure a fused IIAB protein. Sugar phosphorylation and membrane translocation require compatible partners.' if family == 'PTHR33799' else 'This heterogeneous family combines membrane IIC/IID components of sugar phosphotransfer systems with downstream carbohydrate-metabolic proteins, including GatZ/KbaZ aldolase-support subunits and AgaS-related enzymes. IIC and IID are distinct partnered membrane roles, and their subfamilies include transporters with different sugar specificities. Escherichia coli ManY/ManZ and lactococcal PtnC/PtnD occupy different subfamily pairs. Soluble downstream-enzyme branches do not acquire PTS uptake roles merely because they share this broad evolutionary classification.'),
               'functional_coherence': 'HETEROGENEOUS',
               'coherence_reason': 'Specific sugar, domain fusion and assembled activity differ despite a shared PTS phosphorelay role.' if family == 'PTHR33799' else 'Membrane sugar-uptake components and downstream aldolase-support/deaminase-related proteins occupy distinct branches; neither substrate-specific transport nor membrane location is universal.',
               'reference_protein': ecx if family == 'PTHR33799' else ecy,
               'subfamilies': [], 'node_assessments': [], 'term_assessments': [],
               'references': references, 'review_status': 'COMPLETE', 'reviewed_by': 'codex',
               'review_date': '2026-11-07',
               'notes': 'Bounded family audit for mannose PTS interpretation. All cached PAINT identities, terms, evidence, polarity, seeds and dates are copied unchanged into assessments. No raw source is rewritten. No evolutionary loss or catalytic residue rule is invented; positive target activities remain valid where supported. The subfamily roster below names characterized or directly classified relevant branches and does not pretend every member or every downstream enzyme was experimentally re-reviewed.'}
        if family == 'PTHR33799':
            doc['subfamilies'] = [{'subfamily_id': 'PANTHER:PTHR33799:SF1', 'label': labels['PANTHER:PTHR33799:SF1'],
                                  'description': 'Contains both separate IIA proteins and fused IIAB proteins with different sugar-system specificities; neither fusion nor mannose is encoded by SF1 alone.',
                                  'representative_members': [ecx, protein('P26379', 'PTS system fructose-specific EIIA component', 'levD', 'Bacillus subtilis 168'), protein('Q9CEX8', 'PTS system mannose-specific IIAB component', 'ptnAB', 'Lactococcus lactis IL1403')],
                                  'diverged_from_family': False, 'supported_by': [arch, broad_pts]}]
        else:
            configs = [
                ('SF4', 'IIC branch including ManY, LevF and sorbose-system proteins; exact sugar is not universal.', [ecy, protein('P26381', 'Fructose permease IIC component', 'levF', 'Bacillus subtilis 168')]),
                ('SF5', 'IID branch including ManZ, LevG and AgaD; partner architecture and substrate require independent evidence.', [ecz, protein('P26382', 'Fructose permease IID component', 'levG', 'Bacillus subtilis 168')]),
                ('SF25', 'A distinct IIC branch including directly classified IL1403 PtnC and UA159 reference candidates; strain assay identity is assessed separately.', [protein('Q9CEX7', 'PTS system mannose-specific IIC component', 'ptnC', 'Lactococcus lactis IL1403')]),
                ('SF27', 'A distinct IID branch including directly classified IL1403 PtnD and UA159 reference candidates; no universal sugar grant follows from its name.', [protein('Q9CEX6', 'PTS system mannose-specific IID component', 'ptnD', 'Lactococcus lactis IL1403')]),
                ('SF12', 'GatZ downstream aldolase-support branch, distinct from the membrane PTS uptake step.', [protein('P0C8J8', 'D-tagatose-1,6-bisphosphate aldolase subunit GatZ', 'gatZ', 'Escherichia coli K-12')]),
                ('SF2', 'Includes KbaZ downstream aldolase-support proteins; the broad subfamily is not asserted universally to have one activity.', [protein('P0C8K0', 'D-tagatose-1,6-bisphosphate aldolase subunit KbaZ', 'kbaZ', 'Escherichia coli K-12')]),
            ]
            for sf, desc, members in configs:
                doc['subfamilies'].append({'subfamily_id': 'PANTHER:PTHR32502:' + sf, 'label': labels['PANTHER:PTHR32502:' + sf], 'description': desc, 'representative_members': members, 'diverged_from_family': False})
        for row in csv.DictReader((ROOT / f'interpro/panther/{family}/{family}-paint.tsv').open(), delimiter='\t'):
            term = row['go_id']
            node = {'node_id': 'PANTHER:' + row['node'], 'asserted_term': {'id': term, 'label': terms[term]},
                    'evidence': row['evidence'], 'negated': row['negated'] == 'true', 'paint_snapshot': row['date'],
                    'seeds': [{'id': x} for x in row['seeds'].split('|') if x],
                    'supported_by': [support(f'file:interpro/panther/{family}/{family}-paint.tsv', '\t'.join(row[k] for k in ['family', 'node', 'go_id', 'aspect', 'evidence', 'negated']))]}
            if row['taxon'] != 'taxon:':
                taxid = row['taxon'].split(':')[1]
                node['node_taxon'] = {'id': 'NCBITaxon:' + taxid, 'label': 'Bacteria' if taxid == '2' else 'Bacillales'}
            if family == 'PTHR33799':
                if term == 'GO:0009401':
                    node.update(assessment='SOUND', assessment_reason='The current root covers IIA-family phosphorelay proteins, including fused ManX and separate LevD. Their shared work is sugar-PTS phosphotransfer; substrate and fusion differences do not refute this broad process. Placement is assessed from conserved role and current descendant architecture, not the number of seeds.')
                    node['supported_by'] += [arch, broad_pts]
                elif term == 'GO:0008982':
                    node.update(assessment='UNRESOLVED', assessment_reason='The GO definition names coupled phosphohistidine-to-sugar transfer and transport. ManX supplies fused IIA/IIB catalytic functions in a partner-dependent system, while descendants such as LevD contain IIA only. Broad system contribution is plausible, but a uniform gene-level enabling assertion cannot be inferred from the root across these architectures. No function loss or exact pruning point is inferred.')
                    node['supported_by'] += [arch]
                else:
                    node.update(assessment='UNRESOLVED', assessment_reason='A phosphorelay role does not by itself establish a stable transmembrane-complex location for every separate IIA protein. ManX partner association is positive evidence for the seed, but the current root also includes soluble separate IIA architectures. Their potential transient contributions are not denied; universal complex membership remains unresolved without evidence of physical assembly.')
                    node['supported_by'] += [arch]
            elif term == 'GO:0009401':
                node.update(assessment='TOO_DEEP', assessment_reason='The current 48-leaf root extends beyond the membrane IIC/IID branches into the GatZ/KbaZ branch PTN001287483 and AgaS-related branch. GatZ/KbaZ support downstream tagatose-bisphosphate aldolase activity rather than doing the coupled extracellular uptake/phosphorylation work defined by this process. This is a positive mechanistic distinction, not an inference from missing donor annotations. Restriction to the membrane PTS branches is warranted; no invented replacement PTN is supplied.', affected_subfamilies=[{'id': 'PANTHER:PTHR32502:' + sf, 'label': labels['PANTHER:PTHR32502:' + sf]} for sf in ['SF2', 'SF12']])
                node['supported_by'] += [gat_positive, gatz_function]
            elif term == 'GO:0005886':
                node.update(assessment='UNRESOLVED', assessment_reason='The root spans both multipass IIC/IID proteins and downstream GatZ/KbaZ/AgaS-related proteins. Membrane embedding is supported for the PTS branches but cannot be generalized from their domains to the downstream enzyme branches. The current sources do not establish every member\'s peripheral membrane association or a precise ancestral location-loss event, so no automatic negative member list is manufactured.')
                node['supported_by'] += [gatz_function]
            elif term == 'GO:0008047':
                node.update(assessment='SOUND', assessment_reason='PTN001287483 contains seven GatZ/KbaZ-like current descendants, including both experimental E. coli seeds. The positive biochemical function is enhancement and stabilization of catalytic Y-subunit aldolase activity. This supports enzyme-activator placement at this branch without transferring it to membrane IIC/IID proteins or equating chaperone-like speculation with a proven foldase.')
                node['supported_by'] += [gat_positive, gatz_function]
            else:
                node.update(assessment='UNRESOLVED', assessment_reason='The current descendant set includes the positive E. coli mannose-system seed together with Bacillus LevF/LevG, whose primary abstract explicitly reports fructose transport and no mannose uptake. Thus a uniform mannose-specific grant is not established by this IIC/IID node. The negative full assay was not independently read, and the data do not distinguish later specificity gain from loss or justify an exact pruning point. Preserve the source assertion and positive target activity while leaving scope unresolved. The recorded taxon:1385 is retained rather than used to override the actual mixed descendant tree.')
                node['supported_by'] += [lev_boundary]
            doc['node_assessments'].append(node)
        if family == 'PTHR33799':
            scopes = [('GO:0009401', 'FAMILY_WIDE', 'Conserved participation in the sugar-PTS phosphorelay is shared across the observed IIA and fused IIAB architectures; this broad process does not require mannose specificity.', [broad_pts, arch]),
                      ('GO:0008982', 'UNRESOLVED', 'Partner-dependent system activity and gene-level catalytic completeness differ between separate IIA and fused IIAB proteins; no universal enabling or standalone transport claim.', [arch]),
                      ('GO:0022870', 'UNRESOLVED', 'The same SF1 contains mannose-system ManX and fructose-system LevD; architecture/family alone does not identify substrate.', [lev_boundary, arch]),
                      ('GO:1902495', 'UNRESOLVED', 'Physical transmembrane-complex association is not established for every separate soluble IIA member; no universal absence is inferred.', [arch])]
        else:
            scopes = [('GO:0009401', 'UNRESOLVED', 'Positive membrane PTS members coexist with downstream enzyme-support and deaminase-related branches. Exact characterized members remain licensed, but no universal family assertion or incomplete list implying all other subfamilies are negative is supplied.', [gat_positive]),
                      ('GO:0005886', 'UNRESOLVED', 'Membrane IIC/IID architectures are positive; downstream metabolic branches prevent a universal plasma-membrane inference.', [gatz_function]),
                      ('GO:0022870', 'UNRESOLVED', 'ManY/ManZ and PtnC/PtnD are positive in their demonstrated systems, while shared subfamilies contain other substrate systems. Specificity requires positive target/partner evidence; no whole-subfamily mannose loss is asserted.', [lev_boundary]),
                      ('GO:0008047', 'UNRESOLVED', 'GatZ/KbaZ activation is positive for the assessed branch; it does not license membrane IIC/IID members or every protein assigned to the broad enzyme-related subfamilies.', [gat_positive, gatz_function])]
        for term, scope, reason, supp in scopes:
            doc['term_assessments'].append({'assessed_term': {'id': term, 'label': terms[term]}, 'scope': scope, 'scope_reason': reason, 'supported_by': supp})
        path = ROOT / f'interpro/panther/{family}/{family}-review.yaml'
        doc['references'] = [{'id': r['id'], 'title': r['title']} for r in doc['references']]
        path.write_text(yaml.safe_dump(doc, sort_keys=False, allow_unicode=True, width=100))
    print('Created two family reviews; source files untouched')


if __name__ == '__main__':
    main()
