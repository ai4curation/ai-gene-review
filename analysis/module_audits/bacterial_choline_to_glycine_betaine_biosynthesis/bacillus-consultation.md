# Bacillus OpuB and GbsAB review findings

All six records are COMPLETE. Identity, original payload and raw-source preservation are in bacillus-baseline.yaml and bacillus-preservation.yaml; exact deliverables/actions/new rows/families are in bacillus-manifest.yaml. The 35 seeded rows are preserved, with 10 appended NEW rows and no retired rows. All six normal Falcon attempts failed HTTP403; no provider report was fabricated.

| Gene | Accession | Core activity / role | PANTHER classification from frozen UniProt |
|---|---|---|---|
| opuBA | Q45460 | ATPase GO0016887; contributes to ABC choline import GO0033266 | PTHR43117:SF3 CHOLINE TRANSPORT ATP-BINDING PROTEIN OPUBA |
| opuBB | Q45461 | contributes to ABC choline import GO0033266; membrane translocation | PTHR30177:SF28 CHOLINE TRANSPORT SYSTEM PERMEASE PROTEIN OPUBB |
| opuBC | Q45462 | choline binding GO0033265; contributes to ABC choline import GO0033266 | PTHR30024:SF44 CHOLINE-BINDING PROTEIN |
| opuBD | P39775 | contributes to ABC choline import GO0033266; membrane translocation | PTHR30177:SF4 OSMOPROTECTANT IMPORT PERMEASE PROTEIN OSMW |
| gbsA | P71016 | betaine-aldehyde dehydrogenase (NAD+) GO0008802 | PTHR43860:SF2 BETAINE ALDEHYDE DEHYDROGENASE-RELATED |
| gbsB | P71017 | acceptor-unspecified choline dehydrogenase GO0008812 | PTHR11496:SF102 ALCOHOL DEHYDROGENASE 4 |

OpuB is the distinct native choline-specific ABC system. Its subunits share family/subfamily classifications with OpuC, so family match alone cannot identify the native complex or predict its cargo. The primary JH642-derived mutant uptake experiments (PMID10216873) distinguish OpuB from OpuC and report that OpuB components match the genome-project sequences. The system has four subunit types, not four polypeptides: the standard architecture includes two ATPase copies, two distinct membrane components and one lipoprotein binding component. No individual subunit enables autonomous ABC import.

The OpuBA glycine-betaine MF and OpuBB glycine-betaine BP ancestral nodes were traced through cached IBD.gaf and PANTHER trees and include both OpuB and OpuC branches. Direct native substrate discrimination supports MODIFY to choline rather than donor-count criticism. OpuBC sulfate-starvation REMOVE agrees with the existing PTHR30024 family review's TOO_DEEP assessment for PTN001246788/SF44. No family files were changed.

PMID21658392 directly measures OpuBC choline binding and solves its structure. The JH642 construct lacks signal/lipid-anchor sequence and has a reported terminal Cys-to-Gly substitution. Deposited3R6U entity1 matches reference Q45462 residues23–306 but retains the cysteine; the discrepancy is preserved. Binding-domain evidence applies without calling this an unmodified full-length native construct or silently mapping mechanistic residue numbers.

PMID8752328 links the GbsAB route to native isotope-labeled precursor conversion, differential precursor rescue and heterologous complementation. Its original JH642 U47861 record exactly matches reference GbsA. The deposited GbsB CDS is the393-aa shorter alternative; translation from the experimentally observed upstream start exactly matches402-aa P71017. These initiation forms are preserved, with no erroneous current canonical gene model asserted.

GbsA purified-enzyme data (PMID9297465) establish betaine-aldehyde oxidation, NAD preference, measurable NADP turnover and a homodimer. The tested negative substrates were propionaldehyde, pivalaldehyde, isovaleraldehyde, acetaldehyde and benzaldehyde. They do not disprove the three aminoaldehyde IBA terms; those remain UNDECIDED. Salt activation does not prove a metal-binding site. Aldehyde detoxification is retained as non-core because GbsA actually consumes the toxic precursor.

GbsB is typeIII alcohol-dehydrogenase-family, not GMC BetA. GO0008812/RHEA17433 specify generic acceptor A, so the same GO term can cover the alternative implementation without identical electron acceptors. RHEA33051 specifies NAD+ and is recorded by UniProt with inferred ECO0000305 evidence from the genetics paper. Existing GO0004022 is retained as inherited/curated NAD-linked capability; purified GbsB cofactor preference, metal requirement and any second betaine-aldehyde reaction remain unknown. The core does not invent FAD, quinone, oxygen or peroxide coupling.

The two Gbs NEW biosynthetic-process proposals reflect enzymes performing the reactions, not necessity alone. Same-role E.coliBetB carries current GO0031456; BetA lacks the current term but has an older specific-process history discussed in its review. No systematic convention excludes these catalysts. No redundant generic osmotic-response or biosynthesis ancestor BP was added.

Normal publication acquisition supplied8752328,9297465,21658392;10216873 was reused byte-for-byte from the genuinely fetched sibling cache after HTTP429, as authorized. Author-hosted full text was read for all four papers; PDFs/text remain in ignored source-downloads, with source provenance retained in gene analysis artifacts. GenBank and RCSB identity checks are reproducible with genes/BACSU/gbsB/gbsB-source-analysis/verify_identity.py.
