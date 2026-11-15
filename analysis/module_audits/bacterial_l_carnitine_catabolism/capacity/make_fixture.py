"""Author the finite evidence fixture independently of module topology and review actions."""
from pathlib import Path
import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
DEST = ROOT / 'modules/bacterial_l_carnitine_catabolism-source-analysis/evidence-fixture.yaml'

REACTIONS = {
    'oxidation': {'go': 'GO:0047728', 'rhea': 'RHEA:19265',
                  'substrates': ['L-carnitine', 'NAD+'],
                  'products': ['3-dehydrocarnitine', 'NADH', 'proton'],
                  'sources': ['pao1_oxidation', 'rhime_biochemistry', 'IFP206']},
    'cleavage': {'go': 'GO:0016747', 'rhea': 'RHEA:47044',
                 'substrates': ['3-dehydrocarnitine', 'acetyl-CoA'],
                 'products': ['betainyl-CoA', 'acetoacetate'],
                 'sources': ['pao1_cleavage', 'rhime_biochemistry', 'target_screen']},
    'hydrolysis': {'go': 'GO:0016289', 'rhea': 'RHEA:45716',
                   'substrates': ['betainyl-CoA', 'water'],
                   'products': ['glycine betaine', 'CoA', 'proton'],
                   'sources': ['pao1_hydrolysis', 'rhime_biochemistry']},
    'import': {'go': 'GO:0015226',
               'substrates': ['L-carnitine outside', 'ATP', 'water'],
               'products': ['L-carnitine inside', 'ADP', 'phosphate'],
               'required_unit_roles': ['carnitine_recognition', 'translocation', 'ATP_coupling'],
               'sources': ['transport_primary', 'pao1_scope']},
}
SOURCES = {
    'transport_primary': {'path': 'publications/PMID_19919675.md',
                          'kind': 'PRIMARY_FULL_CACHE',
                          'quotes': ['In addition to the core transporter comprised of a transmembrane protein (CbcW) and an ATPase (CbcV)',
                                     'carnitine uptake (Table 5)'],
                          'scope': 'Pseudomonas native mutants and constructs; Table5 combines P.syringae CaiX with PAO1 CbcWV in E.coli. Not an all-native KT2440 assay.'},
    'pao1_scope': {'path': 'analysis/module_audits/bacterial_l_carnitine_catabolism/pseae-consultation/primary-scope.md',
                   'kind': 'SOURCE_IDENTITY_CONSULTATION',
                   'quotes': ['The paper\'s Table 5 CaiX reconstitution uses a P. syringae B728a substrate-binding protein with the PAO1 core'],
                   'scope': 'Separates PAO1 constructs, PA14/native genetics and heterologous-host uptake.'},
    'pao1_oxidation': {'path': 'genes/PSEAE/cdhA/cdhA-uniprot.txt',
                       'kind': 'CURATED_PRIMARY_LINKED_REACTION',
                       'quotes': ['Reaction=carnitine + NAD(+) = 3-dehydrocarnitine + NADH + H(+);'],
                       'scope': 'Publication-linked curated PAO1 reaction, with primary specificity paper not independently available in full.'},
    'pao1_cleavage': {'path': 'genes/PSEAE/cdhC/cdhC-uniprot.txt',
                      'kind': 'CURATED_PRIMARY_LINKED_REACTION',
                      'quotes': ['Reaction=3-dehydrocarnitine + acetyl-CoA = N,N,N-trimethylglycyl-CoA + acetoacetate;'],
                      'scope': 'ECO0000269 curated reaction cites24240508; accessible screen is not a PAO1 assay.'},
    'pao1_hydrolysis': {'path': 'genes/PSEAE/cdhB/cdhB-uniprot.txt',
                        'kind': 'CURATED_PRIMARY_LINKED_REACTION',
                        'quotes': ['Reaction=N,N,N-trimethylglycyl-CoA + H2O = glycine betaine + CoA + H(+);'],
                        'scope': 'ECO0000269 curated reaction cites24240508; exact target assay details not independently exposed in accessible supplement.'},
    'psepk_evidence': {'path': 'analysis/module_audits/bacterial_l_carnitine_catabolism/psepk-consultation/evidence.md',
                       'kind': 'QUALIFIED_COMPARATIVE_ANALYSIS',
                       'quotes': ['Global BLOSUM62 alignment', 'No alignment establishes native flux'],
                       'scope': 'Target sequence/locus/domain support, qualified by specific ortholog activity and strain boundaries.'},
    'target_screen': {'path': 'analysis/module_audits/bacterial_l_carnitine_catabolism/psepk-consultation/results.yaml',
                      'kind': 'PRIMARY_DATASET_ACCESSION_MAPPING',
                      'quotes': ['BKACE_511', 'Q88R31', "Activity_T1_A_dehydrocarnitine: '146.407'"],
                      'scope': 'Direct target pre-process screening values. Positive-call cutoff and target kinetics unresolved; combines with independent comparative chemistry.'},
    'rhime_biochemistry': {'path': 'genes/RHIME/bcoE-bcoF/bcoE-bcoF-source-analysis/primary-scope.md',
                           'kind': 'PRIMARY_FULL_TEXT_AND_SEQUENCE_BRIDGE',
                           'quotes': ['Purified full-length Smc01638 performs NAD-dependent carnitine oxidation',
                                      'BcoG/Smc01637 was kinetically assayed for dehydrocarnitine plus acetyl-CoA conversion',
                                      '496/496 residues'],
                           'scope': '3D0a2 recombinant proteins identical to Rm2011, and independently sequence-identical1021 representatives. Intact fusion assays, not isolated domains. Does not transfer strain growth.'},
    'IFP206': {'path': 'publications/PMID_3058208.md', 'kind': 'PRIMARY_ABSTRACT',
               'quotes': ['Pseudomonas putida IFP 206', 'the carnitine dehydrogenase is specific for L-carnitine and NAD+'],
               'scope': 'Reaction support in IFP206; not a KT2440 target experiment.'},
    'native_pseudomonas': {'path': 'publications/PMID_19406895.md', 'kind': 'PRIMARY_ABSTRACT_WITH_FULL_CONSULTATION',
                           'quotes': ['We used a genetic screen of the P. aeruginosa PA14 transposon mutant library'],
                           'scope': 'Growth/locus evidence; full consultation separates PAO1 insertions and PA14 deletions. Growth is not exact isolated enzyme chemistry.'},
    'CJ25': {'path': 'publications/PMID_40853000.md', 'kind': 'PRIMARY_FULL_CACHE',
             'quotes': ['Future work, including gene cloning, enzyme purification, and assays, will be crucial to confirm their activity'],
             'scope': 'GB production and proteomics nominate Fad homologs, not validated CdhC/betainyl-CoA enzyme realization.'},
    'alternative_route_scope': {'path': 'modules/bacterial_l_carnitine_catabolism-source-analysis/alternative-route-scope.md',
                                'kind': 'PRIMARY_ABSTRACT_AND_CACHED_BOUNDARY_REVIEW',
                                'quotes': ['Heterologous overexpression of cntAB enables Escherichia coli to produce TMA'],
                                'scope': 'PMID24591617 primary abstract read on PubMed; CntAB outcome differs from the three canonical reactions. No native negative or accession invented.'},
    'alternative_fates': {'path': 'publications/PMID_9037756.md', 'kind': 'REVIEW_ABSTRACT',
                          'quotes': ['degrade only the carbon backbone, with formation of trimethylamine.', 'via \ncrotonobetaine, to gamma-butyrobetaine'],
                          'scope': 'Comparative route/product boundary; not evidence that CntAB or Cai enzymes perform the three reactions in this module.'},
}


def member(org, gene, accession, roles, orthologs=()):
    return {'organism': org, 'gene': gene, 'accession': accession,
            'review_path': f'genes/{org}/{gene}/{gene}-ai-review.yaml',
            'raw_path': f'genes/{org}/{gene}/{gene}-uniprot.txt',
            'orthologs_of': list(orthologs), 'roles': roles}


def claim(tier, sources, scope):
    return {'tier': tier, 'sources': sources, 'scope': scope}


def main():
    members = {}
    pao1 = [('cdhA', 'Q9HTH8', 'oxidation', 'pao1_oxidation'),
            ('cdhC', 'Q9HTH7', 'cleavage', 'pao1_cleavage'),
            ('cdhB', 'Q9HTH9', 'hydrolysis', 'pao1_hydrolysis')]
    for gene, acc, role, source in pao1:
        members[acc] = member('PSEAE', gene, acc, {role: claim('CURATED_PRIMARY', [source, 'native_pseudomonas'],
                                                            'Exact reaction curated from primary; native genetics is contextual, not an isolated substrate assay.')})
    for gene, acc, role in [('Q9HTH6', 'Q9HTH6', 'carnitine_recognition'),
                            ('cbcW', 'Q9HTI7', 'translocation'), ('cbcV', 'Q9HTI8', 'ATP_coupling')]:
        members[acc] = member('PSEAE', gene, acc,
                              {role: claim('ORTHOLOG_SUPPORTED_ASSEMBLY' if role == 'carnitine_recognition' else 'CONSTRUCT_ASSAY',
                                           ['transport_primary', 'pao1_scope'],
                                           'Construct/ortholog participation in functional transport; no purified ATPase or binding-constant claim.')},
                              ['Q9HTH6'] if role == 'carnitine_recognition' else [])
    for gene, acc, role, source in [('lcdH', 'Q88R32', 'oxidation', 'pao1_oxidation'),
                                    ('PP_0303', 'Q88R31', 'cleavage', 'pao1_cleavage'),
                                    ('PP_0301', 'Q88R33', 'hydrolysis', 'pao1_hydrolysis')]:
        sources = ['psepk_evidence', source]
        if role == 'cleavage':
            sources.append('target_screen')
        if role == 'oxidation':
            sources.append('IFP206')
        members[acc] = member('PSEPK', gene, acc,
                              {role: claim('TARGET_SCREEN_PLUS_INFERENCE' if role == 'cleavage' else 'QUALIFIED_INFERENCE',
                                           sources, 'Conserved target sequence/locus plus specific characterized ortholog chemistry; target screen is not a kinetic constant.')})
    for gene, acc, role in [('caiX', 'Q88R30', 'carnitine_recognition'),
                            ('cbcW', 'Q88R39', 'translocation'), ('cbcV', 'Q88R40', 'ATP_coupling')]:
        members[acc] = member('PSEPK', gene, acc,
                              {role: claim('QUALIFIED_INFERENCE', ['psepk_evidence', 'transport_primary'],
                                           'Conserved locus/domain/ortholog evidence; no native KT2440 uptake assay.')},
                              ['Q9HTH6'] if role == 'carnitine_recognition' else [])
    members['Q92NF5'] = member('RHIME', 'bcoE-bcoF', 'Q92NF5', {
        role: claim('SEQUENCE_IDENTICAL_ASSAY', ['rhime_biochemistry'],
                    'Intact3D0a2 fusion assayed; complete1021 target sequence match; no isolated-domain or native1021 growth inference.')
        for role in ['oxidation', 'hydrolysis']}, ['Q92NF5'])
    members['Q92NF6'] = member('RHIME', 'bcoG', 'Q92NF6', {
        'cleavage': claim('SEQUENCE_IDENTICAL_ASSAY', ['rhime_biochemistry'],
                          'Intact3D0a2 BcoG kinetically assayed and complete1021 target sequence match; no invented BcoG knockout.')})
    panels = {
        'PAO1': {'taxon': 'NCBITaxon:208964', 'members': ['Q9HTH8', 'Q9HTH7', 'Q9HTH9', 'Q9HTH6', 'Q9HTI7', 'Q9HTI8'],
                 'native_phenotype': 'Native PAO1 insertion/growth and PA14 deletion evidence reported; this enzyme-capacity calculation does not itself predict growth.'},
        'KT2440': {'taxon': 'NCBITaxon:160488', 'members': ['Q88R32', 'Q88R31', 'Q88R33', 'Q88R30', 'Q88R39', 'Q88R40'],
                   'native_phenotype': 'No native carnitine-growth conclusion follows from this finite audit; reported GBB-growth failure is an upstream, different-substrate phenotype.'},
        'RHIME1021': {'taxon': 'NCBITaxon:266834', 'members': ['Q92NF5', 'Q92NF6'],
                      'native_phenotype': '1021 GBB-growth failure remains separate from exact-sequence protein chemistry and positive3D0a2/Rm2011 GBB growth; no native1021 carnitine-growth claim.'},
    }
    assemblies = [
        {'panel': 'PAO1', 'members': ['Q9HTH6', 'Q9HTI7', 'Q9HTI8'],
         'tier': 'ORTHOLOG_SUPPORTED_ASSEMBLY', 'sources': ['transport_primary', 'pao1_scope'],
         'scope': 'Cognate assembly inferred using native P.aeruginosa genetics and PAO1-core reconstitution with P.syringae CaiX; not all-native PAO1 complex assay.'},
        {'panel': 'KT2440', 'members': ['Q88R30', 'Q88R39', 'Q88R40'],
         'tier': 'QUALIFIED_INFERENCE', 'sources': ['transport_primary', 'psepk_evidence'],
         'scope': 'Target cognate-core assembly supported by conserved functions/locus, not directly reconstituted.'},
    ]
    fixture = {'purpose': 'Finite, source-grounded enzyme-capacity and optional uptake audit; not genome-wide prediction or native-growth assay.',
               'required_reactions': ['oxidation', 'cleavage', 'hydrolysis'], 'optional_reactions': ['import'],
               'reactions': REACTIONS, 'sources': SOURCES, 'members': members, 'panels': panels,
               'assemblies': assemblies,
               'profiles': {'qualified': ['CURATED_PRIMARY', 'QUALIFIED_INFERENCE', 'TARGET_SCREEN_PLUS_INFERENCE',
                                           'SEQUENCE_IDENTICAL_ASSAY', 'CONSTRUCT_ASSAY', 'ORTHOLOG_SUPPORTED_ASSEMBLY'],
                            'direct_or_identical': ['SEQUENCE_IDENTICAL_ASSAY', 'CONSTRUCT_ASSAY']},
               'negative_descriptor_controls': [
                   {'id': 'Hbd_like_descriptor', 'family': 'PANTHER:PTHR48075:SF5', 'go': 'GO:0016491',
                    'known_reaction': '3-hydroxybutyryl-CoA redox chemistry; no specific carnitine claim',
                    'source': 'interpro/panther/PTHR48075/PTHR48075-entries.csv', 'scope': 'Synthetic evidence descriptor, not a measured negative of every Hbd enzyme'},
                   {'id': 'Kce_like_descriptor', 'family': 'PANTHER:PTHR37418:SF2', 'go': 'GO:0016747',
                    'known_reaction': 'KAH cleavage only; no dehydrocarnitine claim',
                    'source': 'interpro/panther/PTHR37418/PTHR37418-entries.csv', 'scope': 'Synthetic incomplete evidence descriptor; does not deny promiscuity'},
                   {'id': 'other_hydrolase_descriptor', 'family': 'PANTHER:PTHR31793:SF2', 'go': 'GO:0016289',
                    'known_reaction': 'Generic acyl-CoA hydrolysis; betainyl-CoA specificity unestablished',
                    'source': 'interpro/panther/PTHR31793/PTHR31793-entries.csv', 'scope': 'Adversarial broad-parent/family descriptor, not an invented gene or native negative'},
               ]}
    DEST.write_text(yaml.safe_dump(fixture, sort_keys=False, width=100))
    print(DEST.relative_to(ROOT))


if __name__ == '__main__':
    main()
