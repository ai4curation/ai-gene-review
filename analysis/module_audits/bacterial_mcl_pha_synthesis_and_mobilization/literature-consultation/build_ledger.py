"""Build the manually adjudicated literature ledger; verify every quotation."""
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
CACHE = ROOT / '.cache/module-audit-logs/mcl-pha-20261107/literature-consultation'
PRE = CACHE / 'from-preflight'


def record(ref, path, kind, scope, statement, quote, section):
    text = path.read_text()
    assert ' '.join(quote.split()) in ' '.join(text.split()), (ref, quote)
    return {
        'id': ref, 'source_path': str(path.relative_to(ROOT)),
        'source_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
        'publication_type': kind, 'access_scope': scope,
        'reference_review': {'assessment': 'RELEVANT', 'reviewed_by': 'codex',
                             'rationale': statement},
        'findings': [{'statement': statement, 'supporting_text': quote,
                      'reference_section_type': section}],
    }


def pub(pmid):
    return ROOT / f'publications/PMID_{pmid}.md'


rows = [
    record('DOI:10.1007/s10924-024-03474-4', PRE / 'review2025.txt', 'REVIEW',
           'FULL; classification, specificity, and PhaZ sections manually read',
           'Class II synthases are usual mcl-PHA anchors, but class labels are not absolute substrate exclusion rules; the review discusses C. necator class I acceptance of C8/C12 precursors in heterologous E. coli. Intracellular native-granule and extracellular denatured-polymer depolymerases are distinct roles. Publisher calls this OriginalPaper, but its content is a literature review.',
           'the substrate specificity of the different types of PhaCs is less strict than originally thought', 'REVIEW'),
    record('PMID:38845815', pub('38845815'), 'REVIEW',
           'FULL; introduction and producer/feedstock sections manually read',
           'The mcl range is C6–C14, distinct from C3–C5 scl-PHA. Wild-type production reports extend beyond Pseudomonas, but a polymer-production report does not identify the matching synthase/depolymerase pair or license family-only role transfer. Composition depends on feedstock; C8/C10 are frequent, not exclusive.',
           'comprising different monomers containing 6-14 carbon atoms', 'ABSTRACT'),
    record('PMID:28425176', pub('28425176'), 'REVIEW',
           'FULL; phasin roles and Pseudomonas PhaF/PhaI sections manually read',
           'Phasins organize granules and influence accumulation, segregation and enzyme access. These are adjacent granule functions, not additional obligatory chemical reactions in the bounded synthase-plus-intracellular-depolymerase profile; PHB-specific phasin dependencies cannot automatically be transferred to mcl systems.',
           'localization of the granules in the cell', 'REVIEW'),
    record('PMID:35338129', pub('35338129'), 'PRIMARY_RESEARCH',
           'FULL; genetic discrimination and bioprospecting Results read',
           'KT2440 PhaG expressed in E. coli supports forward ACP-to-CoA routing in genetic product-sink comparisons: the product does not depend on FadD reactivation. The paper explicitly lacks direct forward acyl-ACP in-vitro kinetics. Endogenous thioesterases offer an alternative explanation for free hydroxyacids in older experiments. The main subsequent enzyme optimization uses P. koreensis PhaG and is not KT2440 native physiology.',
           'no in vitro data on acyl-ACPs, the substrate in the forward direction is available', 'RESULTS'),
    record('PMID:12200450', pub('12200450'), 'PRIMARY_RESEARCH', 'ABSTRACT_ONLY',
           'Purified/refolded P. putida PhaG was measured transferring hydroxyacyl groups from CoA to ACP: direct reverse-reaction evidence, not a direct forward-ACP assay. Abstract also reports cytosolic localization and substrate-dependent dimerization. Exact target strain/construct requires fuller source bridge.',
           'Kinetic analysis of the 3-hydroxyacyl transfer to ACP', 'ABSTRACT'),
    record('PMID:22101037', pub('22101037'), 'PRIMARY_RESEARCH',
           'FULL; native KT2440 composition/expression and heterologous Results read',
           'This study inferred PhaG thioesterase chemistry from heterologous free hydroxyacid accumulation and increased PHA when PP0763 was coexpressed. It did not isolate PhaG hydrolysis from endogenous CoA-thioester hydrolysis. Preserve the observed phenotype while reassessing that interpretation against the 2022 controls; do not make PP0763 universally required for PhaG routing. Native KT2440 polymer composition is measured separately from recombinant E. coli output.',
           'expression of phaG alone led to the production', 'RESULTS'),
    record('PMID:1989978', pub('1989978'), 'PRIMARY_RESEARCH',
           'ABSTRACT_ONLY; publisher and institutional PDF access returned403',
           'The original GPo1 locus study selected synthase/degradation complementation and sequenced the two synthases and intervening depolymerase. M58445 CDS translations exactly match P26494/P26495/P26496. It does not establish a mandatory sequential C1/C2 division, and the abstract reports no clear specificity difference.',
           'No clear difference in specificity was found for the PHA polymerases.', 'ABSTRACT'),
    record('PMID:11133449', CACHE / '11133449-repository.txt', 'PRIMARY_RESEARCH',
           'FULL institutional publisher-PDF copy; Methods/Results/Figs5–6 read; normal cache remains abstract-only',
           'Native GPo1 and GPo500 phaZ were compared for polymer mobilization, with genetic complementation. The rescuing construct contains phaC1 plus phaZ and their promoter, so it is not purified single-protein reconstitution. The mutant is leaky, not absolute zero turnover. ATP/ppGpp and survival are consequences, not additional PhaZ catalytic functions. The source describes primarily C8/C6 polymer.',
           'slight degradation due to the leak-', 'RESULTS'),
    record('PMID:10713430', pub('10713430'), 'PRIMARY_RESEARCH',
           'ABSTRACT_ONLY; corrected Wiley full URL returned403',
           'PAO1 PhaG supports complementation of a P. putida phaG mutant; the resulting polymer contains C6/C8/C10/C12. Native P. aeruginosa phaG disruption reduces gluconate-supported PHA to about40% of wild type while fatty-acid-supported accumulation remains at wild-type level. This establishes a useful, nonobligatory substrate-routing role, not direct purified target chemistry. AF209711 exactly matches Q51553.',
           'whereas from fatty acids wild-type level PHA accumulation was obtained.', 'ABSTRACT'),
    record('PMID:10952003', pub('10952003'), 'PRIMARY_RESEARCH', 'ABSTRACT_ONLY',
           'Purified His-tagged P. aeruginosa class II PhaC1/PhaC2 synthesize poly(3-hydroxydecanoate) in vitro. Exact modern PAO1 PhaC1 construct identity remains unresolved: historical X66592 C1 is557aa versus current559aa. C2 and depolymerase archive sequences match modern entries, but adding a full PAO1 panel is unnecessary for the present mechanism comparison.',
           'the in vitro synthesis of\npoly(3-hydroxydecanoate)', 'ABSTRACT'),
    record('PMID:41055782', pub('41055782'), 'PRIMARY_RESEARCH',
           'FULL; Methods, Table1, WT Results and interpretation read',
           'Despite KT2440 in its title, the assayed pPAZ3/template derives from KT2442 and protein is expressed in E. coli. GPo1 supplies radiolabeled polymer, not the enzyme. WT PhaZ acts on mcl polymer and pNP ester substrates; commercial polymer is mainly C8 with C6. Do not transfer native KT2440 localization, whole-strain phenotypes or variant kinetics from this paper without identity/context qualification. Extracellular GK13 comparator is a distinct compartmental role.',
           'pQE32 derivative containing phaZ gene from P. putida KT2442', 'METHODS'),
]
(HERE / 'reference-ledger.yaml').write_text(yaml.safe_dump(rows, sort_keys=False, allow_unicode=True, width=100))
(HERE / 'quote-proof.json').write_text(json.dumps({'checked': len(rows), 'passed': len(rows), 'normalization': 'whitespace only', 'manual_full_reviews': 3}, indent=2) + '\n')
print(f'{len(rows)} source-checked findings; 3 full reviews')
