# LnsAB independent gene consultation

The full cached primary papers PMID32723923 (2020) and PMID42580408 (2026), including Results, Discussion and Methods, were read. The genuine 2026 supplementary PDF was retrieved through Europe PMC and read separately; it has not been substituted into or used to overwrite the publication cache. Source URLs, archive paths and hashes are in source-provenance.json.

## Reviewed target panel

| Target | Exact identity | Direct experimental scope |
|---|---|---|
| STAA8 SAOUHSC_00822 / LnsA | Q2G006, NCBITaxon93061,189aa | NCTC8325 cloned sequence; native deletion/complementation in named derivatives; mutation-defined catalytic center; signal peptide cleavage, membrane fractionation and live-cell external accessibility; purified LnsA32–189 with LnsB. |
| STAA8 SAOUHSC_02761 / LnsB | Q2FVF3, NCBITaxon93061,249aa | Same cloned-sequence/native-background distinction; membrane partner required in purified reconstitution; physical crosslinking to LnsA; tested CPBP motif substitutions retain activity. |

Both normal-fetch seeds contained zero annotation rows. Three NEW assertions per target cover non-amino-acyltransferase activity (LnsB explicitly contributes_to), lipoprotein biosynthetic process, and experimentally supported location. LnsA's external side of plasma membrane assignment rests on fractionation plus membrane-impermeant SCAM accessibility, not merely its signal peptide. LnsB is assigned plasma membrane as a multipass membrane partner. No process of immune response, cytokine production, virulence, protein export, generic proteolysis or folding is added from downstream phenotypes or family names.

The 2020 source distinguishes NCTC8325 HG003-derived TM226 mutants, RN4220 and USA300 JE2 panels. Its Methods explicitly traces complementation inserts to NCTC8325 genomic DNA. The 2026 host TXM1576 derives from the RN4220 ΔlnsAB lineage (TXM1500 in2020; printed TM1500 in the2026 table), with spa and sbi deletions. It is not silently equated with TM226 or untouched NCTC8325 stock. The supplement confirms the exact source DNA and pairing constructs.

## Chemistry and contribution

The 2026 paper states: “both recombinant LnsA and LnsB are required, along with a phospholipid donor source”. Recombinant expression used the E. coli BL21(DE3) derivative TXM2540 lacking endogenous Lnt. The reconstituted proteins are LnsA32–189 and LnsB; natural LnsA signal cleavage after27 and the recombinant32–189 truncation are distinct observations.

LnsA H60A/C143A and Y129A lose activity in the cellular assay, with expression assessed. H60/Y129/C143 map to the current189aa target sequence. One source sentence prints Tyr29; the Results, Discussion and actual mutant table identify Tyr129, and no Tyr29 claim is authored. The data locate the catalytic center; a covalent acyl-enzyme intermediate was not directly trapped. LnsB is represented as an obligatory interacting contributor, not an independently demonstrated acyltransferase. Physical cysteine crosslinks and purified reconstitution support actual complex work. A substrate-presenter mechanism remains a hypothesis; the multimeric arrangement is supported but exact subunit stoichiometry remains unresolved.

Defined donor mixtures, asymmetric PG, and product MS/MS establish preferential transfer from PG sn-1 for the purified **S. aureus pair**. Preference is not exclusive donor use, physiological flux quantification, or a purified S. epidermidis assay. The enzyme pair's PG-derived chain transfer is distinct from Lnb's unresolved donor and from acetyl-CoA-dependent lysine acetylation.

Eight target LnsB substitutions (C167A,Q168A,R172A,E196A,Y200A,Y201A,Q238A,I242A) retain N-acylation. The primary says: “None of the mutations affected TA-LP synthesis”. CPBP ancestry and the ProtNLM metalloprotease label are therefore not grounds to annotate proteolysis. This finding does not prove the absence of every possible secondary activity, nor a family-wide loss.

## S. epidermidis controls: exact identity, unavailable current UniProt records

| Named primary locus | Exact ATCC12228 sequence bridge | Latest known UniProt accession |
|---|---|---|
| SE_0583 | NP_764138.1 / AAO04180 / UPI00000E4D7C,184aa | A0A0H2VFI9 (earlierQ8CTC1), inactive |
| SE_2027 | NP_765582.1 / AAO05668 / UPI00000E5019,272aa | A0A0H2VI84 (earlierQ8CR74), inactive |

Official NCBI records identify taxon176280 and the locus; UniParc sequences are checked for exact equality with those records. UniParc explicitly records the matching strain/locus and inactive UniProt accessions, last updated2026-01-28. The original EMBL crossrefs are active. No identical-sequence RP62A record is substituted for ATCC12228. The normal fetch helper returned exit0 for the verified deleted accessions but wrote **zero-byte UniProt files** and generic species-taxonomy stubs. All six generated files were moved intact into acquisition-failures after confirming these were new untracked targets; there are no failed Se stubs under genes/. These are acquisition-failure evidence, not curated reviews or module representatives. The incomplete acquisition is explicit despite the successful process exit.

The supplement states the cloned Se DNA came from ATCC12228. Its Methods prose says SE_2727, whereas main Figure2, TableS1, the phylogenetic labels and official sequence bridge identify SE_2027. The discrepancy is retained in supplement-excerpts, not used to invent another accession. No native S. epidermidis mutant was tested here.

The construct outcomes are encoded in pairing-evidence.json:

| LnsA | LnsB | Product in S. aureus complementation host | Purified donor assay |
|---|---|---|---|
| Sa | Sa | Yes | Yes: PG sn-1 preferred |
| Sa | Se | Yes | Not measured |
| Se | Sa | No, despite SeA expression | Not measured |
| Se | Se | Yes | Not measured |

The failed reciprocal pairing is a tested-construct boundary, not a universal claim that all strains or evolved variants are incompatible. Model confidence did not distinguish the active and inactive mixed pairs. Loop4 exchange partially restores activity and supports interface specificity; homology or shared family membership cannot override the actual pairing result.

## Family identifiers and annotation conventions

Official InterPro metadata identifies **families** IPR056567 “Lipoprotein N-acylation protein LnsA-like” and IPR056566 “CPBP family lipoprotein N-acylation protein LnsB-like”. Both target raw records corroborate the matching NCBIfam signatures NF041769/NF041768. LnsA also carries PF28265 and the broader papain-like IPR038765. No PANTHER family is present. The PAINT-loss tool therefore cannot assess lineage losses; it does not establish an absence of losses.

The exact Se UniParc sequences independently carry the corresponding NCBIfam/InterPro family features. SeB additionally has the broad PF02517/IPR003675 CPBP domain; that broad domain is not a specificity selector. SaA's automatic “Orthopoxovirus protein” name and SaB's automatic “metalloprotease” name are not biological evidence.

The BP proposals rest on direct catalytic or obligatory complex work, not the proteins merely being consumed or required. Exact-term Lnt comparator responses P23930/Q88DN4 establish use of GO0042158 for terminal N-acylation catalysts. Lnt is not an exact-role accessory-subunit comparator for LnsB; LnsB's proposal instead rests on its demonstrated physical/functional complex contribution. No claim of a systematic annotation oversight is made. Current official GO definitions and ancestry support the selected terms; there is no second redundant BP. GO-CAM index checks find no target or comparator entries and are not treated as positive biological evidence.

## Checks and limits

Two real Falcon calls failed HTTP403; logs and the research receipt are retained without fabricated provider reports. Both focused gene validators pass, including source quotations. Generated histories, HTML rendering, standard record-section backfill and the PAINT diagnostic accompany the reviews. The reproducible verify.py checks all original identity fields, zero-row seeds, six protected raw/publication sources, new-row activity qualifiers, all primary quotes, exact residues, official classifications, exact Se sequence identity, archived failed-output hashes and assay-specific pairing boundaries. No module/family/project edits, commit, push or full-corpus validation are part of this consultation.
