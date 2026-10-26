# DNAJC21 (Q5F1R6) research notes

J-domain (HSP40) co-chaperone of the HSP70 system acting in **ribosome biogenesis**,
specifically maturation of the large (60S) ribosomal subunit. Also named DNAJA5.

## Architecture
- N-terminal J-domain (HPD motif) that recruits/stimulates HSP70 ATPases.
- Two C2H2 zinc fingers within an otherwise disordered C-terminal region.
- Human counterpart of the yeast 60S-maturation J-protein Jjj1.

## Function / localization
- Localizes to cytoplasm, nucleus and especially the **nucleolus**; associates with
  precursor 45S rRNA. [UniProt Q5F1R6 subcellular location]
- Works with the HSP70 chaperone **HSPA8** and cofactors **PA2G4** (60S nuclear-export
  factor) and **ZNF622** to drive late nucleolar rRNA processing and cytoplasmic
  maturation/recycling of the 60S subunit. [PMID:27346687]

## Disease
- Biallelic loss-of-function variants cause a cancer-prone **bone marrow failure
  syndrome (BMFS3)**, Shwachman–Diamond-like — establishing DNAJC21 as a ribosomopathy
  gene. [PMID:27346687]

## Curation calls
- Core MFs: HSP70 (HSPA8) co-chaperone binding (GO:0051087) driving 60S maturation;
  RNA binding (GO:0003723) to precursor rRNA.
- Bare high-throughput `protein binding` to HTT/MTERF1 and domain-only nucleic-acid
  binding marked over-annotated; folding terms kept non-core (co-chaperone, not foldase).


## 2026-10-17 evidence-based augmentation

This appendix supersedes the earlier curation calls and any implication that human HSPA8 ATPase stimulation was directly measured. It preserves the earlier journal text as provenance. All 15 source annotation dictionaries remain unchanged; the current genuine QuickGO snapshot has the same assertions, so no retirement or source replacement is required. The preceding review was introduced in PR #1434 and updated in PR #1456; those historical bot approvals are preserved and are not a new campaign sign-off.

The review now contains 4 ACCEPT, 3 KEEP_AS_NON_CORE, 6 MODIFY and 2 UNDECIDED decisions. Broad nucleic-acid binding becomes RNA binding. Nucleus and cytoplasm are refined consistently to the independently supported nucleolar and cytosolic pools, without excluding other nuclear regions, reinterpreting the original broad fractionation, or discarding actinomycin-D redistribution. The two screened HTT and MTERF1 associations remain positive non-core annotations under the [user's explicit project binding instruction](https://github.com/ai4curation/ai-gene-review/blob/16996128f5e52475aeffd6b3a573cdb94b1ff9bc/projects/CLINGEN_MENDELIAN.md#curation-instructions). Their fragment, display and verification limits are stated individually.

The two cores distinguish RNA association from Hsp70-partner binding. The latter is specified as GO:0030544, without a second redundant chaperone-binding core. Human native rRNA co-IP is distinct from the independent UV-dependent mRNA-capture experiment; neither implies RNA catalysis. The human study supports HSPA8 association and assembly-factor recycling, whereas its ATPase discussion invokes yeast precedent and HPD-motif inference. No NEW annotation is added merely to fill a process slot.

The NAS ribosome and protein-folding assertions remain unresolved because the target-specific full text of PMID:16952052 was not accessible through the attempted original routes. This is not evidence of a miscitation, an absent assay, or an incorrect function. The former shorthand contrasting co-chaperone with foldase was insufficient: the GO folding definition includes assisted polypeptide and multisubunit assembly.

Three official sequences reconstruct to 531, 576 and 544 residues. Their insertions preserve the J domain but do not establish equivalent function; the historical 531-residue clone has a documented residue-509 sequence conflict. Genuine provider attempts failed through authentication/quota errors, which were recorded without inventing a report. The new PMID:15067379 cache is a genuine abstract-only fetch. Existing downloaded caches and PN notes are preserved.

See the [evidence guide](DNAJC21-evidence-guide.md) for original Methods/Figure/Table locators, exact pair and RNA-capture records, source-access limitations, PAINT ancestry, HPA evidence, product boundaries, and the distinction between the partial protected PMID:27346687 cache and its separately recovered complete original.

## 2026-10-17 review follow-up: process participation and reproducible sources

The Hsp70-partner core now includes GO:0042273, ribosomal large subunit biogenesis. This is supported by the combined human evidence in [PMID:27346687](https://pmc.ncbi.nlm.nih.gov/articles/PMC5005432/), not by disease necessity alone: nuclease-resistant partner associations and P32A discrimination (Figure 3C–D), PA2G4 retention in 60S/80S fractions and altered traffic after DNAJC21 loss (Figure 4), and restoration of traffic by wild-type DNAJC21 (Figure 5G). These observations support a co-chaperone/assembly-factor contribution. They do not directly measure human ATP hydrolysis or reconstituted PA2G4 release. The relevant Methods are Immunostudies, Polysome Analysis, and Cell Death and Rescue by Wild-Type DNAJC21. The protected cache still omits these experimental sections; they were read in the separately recovered original.

The process is recorded once on the cytoplasmic Hsp70-partner core. The RNA core retains its nucleolar location: 45S is a common precursor, and the RNA-association experiment does not isolate a large-subunit-specific RNA step. No nucleolar gene-level pool is discarded. Neither a duplicated process attachment nor an extra NEW Hsp70-binding row is needed to make the existing core evidence explicit.

The broad NAS protein-folding assertion is now KEEP_AS_NON_CORE. Its positive basis is the integrated human assembly evidence and the GO definition's inclusion of assisted multisubunit assembly, rather than HSPA8 binding alone or an assumed autonomous foldase. This does not claim a defined folding substrate, purified refolding assay or direct human ATPase measurement. The target-specific full text of the original 2006 review remains inaccessible. The NAS ribosome location remains UNDECIDED because the human gradients assay PA2G4 and RPL7, not DNAJC21; precursor-rRNA association and maturation-factor function do not settle mature-ribosome localization. These statements supersede the earlier two-UNDECIDED rationale without changing any imported source identity.

The supplementary tables, exact IntAct pair records, PAINT paths/IBD, HPA location records and InterPro match are now preserved as [literal source extracts](DNAJC21-bioinformatics/source-extracts.json), with [public source URLs and original hashes](DNAJC21-bioinformatics/source-manifest.json) and a [working reproduction script](DNAJC21-bioinformatics/reproduce.py). The script was replayed against all nine genuine saved raw inputs; no measurement was transcribed from a conclusion or invented. The 725 original target workbook cells and eight IntAct records are retained. The source extract is cited only for the underlying data it actually contains; the prose evidence guide is no longer cited as independent support.

Five short exact anchors were added once each while preserving all three inherited excerpts. Duplicate rows retain reference-only support, and combined quotations remain below 25 words per source. The positive nucleus/cytoplasm propagation mappings are now labelled NO_FAILURE_CORE; the more specific target-level refinements remain intact. Final actions are 4 ACCEPT, 4 KEEP_AS_NON_CORE, 6 MODIFY and 1 UNDECIDED across the same 15 source objects. All three product descriptions and source caches are unchanged. Status remains DRAFT pending the normal computed-status check; resolving one UNDECIDED does not remove the two generic-binding advisories.
