"""Reproduce source checks and identity receipts; scientific judgments are authored below."""
import hashlib
import json
import re
from pathlib import Path

import yaml
from bs4 import BeautifulSoup

A = Path(__file__).resolve().parent
ROOT = A.parents[3]
C = ROOT / '.cache/module-audit-logs/mannose-20261107/literature-consultation'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalized(path):
    text = path.read_text()
    if path.suffix == '.html':
        text = BeautifulSoup(text, 'html.parser').get_text(' ', strip=True)
    return re.sub(r'\s+', ' ', text).strip()


# PMID, type, read scope, source, section, short exact excerpt, manual finding.
RECORDS = [
 ('17158705', 'REVIEW', 'FULL_TEXT_RELEVANT_SECTIONS', '2006-review.txt', 'INTRODUCTION',
  'the four proteins (domains) forming the PTS phosphorylation cascade (EI, HPr, EIIA, and EIIB)',
  'Distinguishes the PEP/EI/HPr/EIIA/EIIB phosphorelay from its extensive regulatory interactions. Supports an EII group-translocation boundary downstream of phospho-HPr, not a module that includes all PTS signaling. Its passing description of Bacillus Lev as mannose/fructose-specific is contradicted for mannose by primary2117666 and is not used for substrate scope.'),
 ('16339738', 'REVIEW', 'FULL_TEXT_RELEVANT_SECTIONS', '2005-review.txt', 'INTRODUCTION',
  'one additional membrane-spanning protein or domain, called IID',
  'A PubMed-indexed review with comparative-genomic analyses: mannose-class EII includes A/B relay and C/D membrane components, with variable fusion organization and frequent strain-level variation. Its older unknown-biochemical-role description of IID does not override the later ManYZ structure. Phylogenetic membership or a partial cassette alone cannot establish matched mannose transport capacity.'),
 ('18647176', 'REVIEW', 'FULL_TEXT_RELEVANT_SECTIONS', '2008-review-full.txt', 'Lactobacillus',
  'the IIA and IIB domains are encoded by separate genes',
  'The Streptococcus/Enterococcus/Lactococcus and Lactobacillus sections document broad glucose/mannose-class uptake, fused and split relay architectures, and alternate non-PTS uptake. ManO is not universal and was of unresolved function in the cited Lactobacillus context. The review supports taxon discovery, while exact substrates and strains require primary evidence.'),
 ('2117666', 'PRIMARY_RESEARCH', 'ABSTRACT_ONLY', None, 'ABSTRACT',
  'not involved in mannose uptake, but form a fructose phosphotransferase system',
  'The abstract explicitly distinguishes Bacillus subtilis LevDEFG from mannose uptake despite homologous components. This is a source-positive negative control for mannose specificity, not a claim that all related families lack mannose activity. Full text was not acquired.'),
 ('2681202', 'PRIMARY_RESEARCH', 'ABSTRACT_ONLY', None, 'ABSTRACT',
  'between domains on different subunits of the dimer',
  'E. coli ManX/IIIMan has two phosphorylated domains; transfer is reported within a subunit, between isolated domains and between subunits. Phospho-HPr feeds His10, then His175 donates to sugar with membrane partners. A strictly intramolecular relay is false. Full-text attempts are recorded separately by the Ecoli consultant.'),
 ('8262947', 'PRIMARY_RESEARCH', 'ABSTRACT_ONLY', None, 'ABSTRACT',
  'of the same as well as of different subunits',
  'Independent biochemical analysis confirms intra- and intersubunit ManX phosphoryl transfer in a dimer. This soluble phosphorelay stoichiometry is distinct from membrane ManYZ stoichiometry and does not imply a fixed whole-assembly ratio.'),
 ('31209249', 'PRIMARY_RESEARCH', 'FULL_TEXT_RELEVANT_SECTIONS', '.shared-2019', 'RESULTS',
  'Each protomer is composed of a ManY and ManZ',
  'The 2019 structure describes a trimer of ManY/ManZ protomers, hence three copies of each membrane component. The supplementary counterflow experiment is not complete PEP/HPr/ManX group translocation. Do not carry the older membrane-dimer model or infer a matched soluble-ManX stoichiometry.'),
 ('17284603', 'PRIMARY_RESEARCH', 'FULL_TEXT_RELEVANT_SECTIONS', '2007-lactococcus.txt', 'RESULTS',
  'reduced ability of the mutant (B464) to grow on glucose or mannose',
  'Native Lactococcus lactis IL1403 ptnAB/C/D deletion reduces growth on glucose/mannose; the same paper explicitly names genome AE005176 and the three genes. Reintroduction and isolated-C/D experiments shown here primarily test bacteriocin receptor behavior, so receptor restoration is not relabeled as a complete sugar-transport reconstitution.'),
 ('38047704', 'PRIMARY_RESEARCH', 'FULL_TEXT_RELEVANT_SECTIONS', '2023-lactococcus.txt', 'RESULTS AND DISCUSSION / Fig4',
  'the growth rate of all mutants, except for mutants 1 and 5, was negatively affected',
  'Native IL1403 membrane-component variants have impaired mannose/glucose growth in Fig4, with cellobiose control and exceptions retaining sugar utilization. Bacteriocin resistance is separable from transport. This reinforces native C/D participation without claiming every variant abolishes transport or that all glucose uptake uses this system.'),
 ('12902269', 'PRIMARY_RESEARCH', 'FULL_TEXT_RELEVANT_SECTIONS', '2003-mutans.txt', 'ABSTRACT; RESULTS; Fig1',
  'grew more slowly than the wild-type strain in glucose but grew faster in mannose',
  'UA159 ManL contributes to PEP-dependent glucose/mannose uptake, while inducible alternative mannose transport explains the mutant growth result. Operon Fig1 identifies manL/M/N by flanking loci and the text gives manL length0.99kb. Genetic/regulatory phenotypes do not prove sole-route necessity or separate catalytic measurements for every membrane subunit.'),
 ('17951382', 'PRIMARY_RESEARCH', 'FULL_TEXT_RELEVANT_SECTIONS', 'ua159-locus-primary.txt', 'RESULTS / Table1',
  'manL (SMU.1877) and manM (SMU.1878)',
  'This independent UA159 primary explicitly equates manL with SMU.1877 and manM with SMU.1878. It supports the nomenclature bridge rather than adding new transport measurements. manN is mapped through the adjacent third CDS in the original2003 operon figure and official genome cross-references.'),
 ('24928869', 'PRIMARY_RESEARCH', 'FULL_TEXT_RELEVANT_SECTIONS', '2014-mutans.txt', 'ABSTRACT; RESULTS',
  'the glucose/mannose enzyme II permease encoded by manLMN playing a dominant role',
  'Native UA159 assays extend the system to glucosamine/N-acetylglucosamine uptake; downstream ManO modulates amino-sugar uptake. This is broader cargo context, not justification to require ManO for the bacterial mannose module or to add downstream amino-sugar catabolism to the transport mechanism.'),
 ('9004509', 'PRIMARY_RESEARCH', 'FULL_TEXT_RELEVANT_SECTIONS', '1996-curvatus.txt', 'ABSTRACT; METHODS; sequence analysis',
  'shown to be involved in glucose and mannose transport',
  'The assayed Lactobacillus curvatus strain is CECT904. The deposited U28163 fragment encodes separate complete IIA/IIB/IIC and only partial IID. Heterologous ManB complementation provides relay-function support, but does not establish arbitrary cross-species cassette compatibility. Original UniProt IDs are now inactive; no complete active quartet is asserted.'),
 ('40135874', 'PRIMARY_RESEARCH', 'FULL_TEXT_RELEVANT_SECTIONS', None, 'RESULTS / Fig3',
  'the complementation of manLMN restored the mutant strains’ capability',
  'Native Streptococcus pyogenes MGAS8232 experiments distinguish complete-manLMN from ManL-only complementation for mannose/galactose/GlcNAc utilization. The reported additional background mutations make the complementation comparison important. Antimicrobial production and host colonization are downstream context, not core transport roles. Exact accession bridge not established in this consultation, so no representative IDs proposed.'),
]


def main():
    ledger = []
    quotes = []
    sources = {}
    for pmid, kind, scope, source, section, quote, finding in RECORDS:
        if source == '.shared-2019':
            p = ROOT / '.cache/module-audit-logs/mannose-pts-20261107/ecoli-review/31209249-pmc.html'
        else:
            p = C / source if source else ROOT / f'publications/PMID_{pmid}.md'
        assert quote in normalized(p), (pmid, quote)
        metadata = yaml.safe_load((ROOT / f'publications/PMID_{pmid}.md').read_text().split('---')[1])
        sources[str(p.relative_to(ROOT))] = sha(p)
        ledger.append(dict(id=f'PMID:{pmid}', title=metadata['title'], manual_publication_type=kind,
                           access_scope=scope, consulted_source=str(p.relative_to(ROOT)),
                           section=section, finding=finding, supporting_text=quote,
                           immutable_cache_full_text_available=metadata['full_text_available']))
        quotes += [f'## PMID:{pmid}', f'Source: {p.relative_to(ROOT)}', f'Section: {section}',
                   f'Access: {scope}', f'> {quote}', '', finding, '']
    (A / 'evidence-ledger.yaml').write_text(yaml.safe_dump(ledger, sort_keys=False, allow_unicode=True))
    (A / 'source-excerpts.md').write_text('# Consulted source excerpts\n\nWhitespace is normalized for matching. External full texts are held in the ignored acquisition cache; normal publication caches remain unchanged. Each excerpt below is checked against the cited acquisition, not against an abstract-only cache.\n\n' + '\n'.join(quotes))

    candidates = json.loads((A / 'uniprot-candidates.json').read_text())
    exact = json.loads((A / 'exact-proteins.json').read_text())
    identity = []
    for organism, accession, gene, locus, family, genome, protein in [
        ('IL1403', 'Q9CEX8', 'ptnAB', 'L1762179', 'PTHR33799:SF1', 'AE005176', 'AAK05804.1'),
        ('IL1403', 'Q9CEX7', 'ptnC', 'L146623', 'PTHR32502:SF25', 'AE005176', 'AAK05805.1'),
        ('IL1403', 'Q9CEX6', 'ptnD', 'L147466', 'PTHR32502:SF27', 'AE005176', 'AAK05806.1'),
        ('UA159', 'Q8DSC4', 'manL', 'SMU_1877', 'PTHR33799:SF1', 'AE014133', 'AAN59494.1'),
        ('UA159', 'Q8DSC3', 'manM', 'SMU_1878', 'PTHR32502:SF25', 'AE014133', 'AAN59495.1'),
        ('UA159', 'Q8DSC2', 'manN', 'SMU_1879', 'PTHR32502:SF27', 'AE014133', 'AAN59496.1'),
    ]:
        obj = next(x for x in candidates['IL1403']['response']['results'] if x['primaryAccession'] == accession) if organism == 'IL1403' else exact[accession]['response']
        assert obj['organism']['taxonId'] == {'IL1403': 272623, 'UA159': 210007}[organism]
        assert locus in json.dumps(obj['genes'])
        refs = obj['uniProtKBCrossReferences']
        assert any(x['database'] == 'PANTHER' and x['id'] == family for x in refs)
        assert any(x['database'] == 'EMBL' and x['id'] == genome and protein in json.dumps(x) for x in refs)
        actual_length = obj['sequence']['length']
        # Exact source length is reported, not imposed from a presumed gene model.
        identity.append(dict(strain=organism, accession=accession, source_gene=gene,
                             official_gene=obj['genes'], locus=locus, length=actual_length,
                             genome=genome, protein_id=protein, family=family,
                             sequence_sha256=hashlib.sha256(obj['sequence']['value'].encode()).hexdigest(),
                             primary_bridge=['17284603'] if organism == 'IL1403' else ['12902269 Fig1', '17951382'],
                             evidence_limit='Locus and strain bridge; no claim of independently sequenced experimental construct.'))
    embl = (A / 'U28163.embl').read_text()
    parts = re.split(r'^FT   CDS\s+', embl, flags=re.M)[1:]
    split = []
    for part in parts:
        gene = re.search(r'/gene="([^"]+)"', part).group(1)
        protein = re.search(r'/protein_id="([^"]+)"', part).group(1)
        seq = re.search(r'/translation="([^"]+)"', part).group(1)
        seq = re.sub(r'\s|FT', '', seq)
        accession = re.search(r'/db_xref="UniProtKB/TrEMBL:([^"]+)"', part).group(1)
        assert exact[accession]['response']['entryType'] == 'Inactive'
        split.append(dict(gene=gene, protein_id=protein, inactive_uniprot=accession,
                          location=part.splitlines()[0].strip(), length=len(seq),
                          partial='>' in part.splitlines()[0], sequence_sha256=hashlib.sha256(seq.encode()).hexdigest()))
    assert len(split) == 4 and split[-1]['partial'] and split[-1]['length'] == 87
    proteome = json.loads((C / 'curvatus-proteome.json').read_text())
    assert proteome['strain'] == 'WDN19'
    (A / 'identity-proof.json').write_text(json.dumps(dict(verified_panels=identity,
        split_CECT904=dict(deposit='U28163', primary='PMID:9004509', proteins=split,
                          limitation='No active complete four-protein panel established; current reference proteome WDN19 is not the assayed CECT904 strain.'),
        no_seed_substitution=['No WDN19 replacement for CECT904', 'No complete IID inferred from87aa fragment'],
        strain_aliases='Official CECT catalogue: CECT904 = ATCC25601 = DSM20019 = JCM1096; aliases do not prove a sequence match.')) + '\n')
    baseline = json.loads((A.parent / 'baseline.json').read_text())
    protected = baseline['protected_files_sha256']
    assert all(sha(ROOT / path) == digest for path, digest in protected.items())
    for p in A.glob('*.json'):
        if p.name not in {'validation.json', 'handoff.json', 'source-sha256.json'}:
            sources[str(p.relative_to(ROOT))] = sha(p)
    for p in C.iterdir():
        if p.is_file():
            sources[str(p.relative_to(ROOT))] = sha(p)
    for pmid in {row[0] for row in RECORDS} | {'32710850', '31214989', '16006479', '41432198'}:
        p = ROOT / f'publications/PMID_{pmid}.md'
        sources[str(p.relative_to(ROOT))] = sha(p)
    for name in ['baseline.json', 'provider-attempt.json', 'discovery-root.json', 'discovery-followup.json']:
        p = A.parent / name
        sources[str(p.relative_to(ROOT))] = sha(p)
    (A / 'source-sha256.json').write_text(json.dumps(sources, indent=2) + '\n')
    report = dict(result='PASS', manually_read_full_reviews=3, findings=len(ledger),
                  exact_quote_checks=len(ledger), verified_current_protein_bridges=len(identity),
                  archival_split_components=len(split), protected_original_sources=len(protected),
                  protection='All original source bytes exactly match root baseline; curated records owned by other agents are not compared.',
                  limitation='Quote/identity/preservation checks do not establish assay equivalence, native necessity, substrate specificity from family membership, or universal interfaces.')
    (A / 'validation.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
