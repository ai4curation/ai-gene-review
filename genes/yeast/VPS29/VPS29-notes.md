# VPS29 (YHR012W, P38759) curation notes

## Session 2026-11-21: provenance of the research

- Hosted deep research (falcon, perplexity) is not configured in this environment, so no
  `VPS29-deep-research-<provider>.md` exists and `just deep-research*` was not run. The
  notes below are my own reading of the cached publications and the UniProt record.
- `just mod-description-deep-research yeast VPS29` succeeded (`VPS29-deep-research-sgd.md`,
  fetched 2026-11-21).
- `just paint-losses yeast VPS29`: "No IRD or IKR loss on this gene's lineage."
- PubMed E-utilities searches were run together with PEP8 (same session; queries listed in
  `genes/yeast/PEP8/PEP8-notes.md`), in particular
  `Vps29[tiab] AND (yeast[tiab] OR cerevisiae[tiab] OR Saccharomyces[tiab])` (34 hits) and
  the yeast retromer query (72 hits).
- Cached for VPS29 in addition to the PEP8 set: PMID:9105038, PMID:38598303, PMID:22046480
  (abstract only).
- Family review: `interpro/panther/PTHR11124/PTHR11124-review.yaml` (COMPLETE) assesses the
  three PAINT IBDs at PTN000122547 (cargo adaptor activity, retromer complex, retrograde
  transport endosome to Golgi) as SOUND for the VPS29 subfamily. Phosphoric diester
  hydrolase activity is scoped to the bacterial YfcE subfamily only.

## Identity and structure

- 282 aa; aliases PEP11, VPT6. The ORF has an intron
  [PMID:9105038 "Sequence analysis revealed that the VPS29 ORF was interrupted by an intron."].
- Metallophosphoesterase-like fold: InterPro IPR000979 (Phosphodiesterase_MJ0936/Vps29),
  IPR029052, Pfam PF12850 Metallophos_2, NCBIfam TIGR00040 yfcE. For the mammalian protein
  [PMID:15965486 "mVps29 can coordinate metals in a similar manner but has no detectable phosphoesterase activity in vitro, suggesting a unique specificity or function."].
  There is no catalytic data for yeast Vps29 and GOA carries no hydrolase row, which is
  correct; PTHR11124 scopes phosphodiesterase activity to bacterial YfcE.
- The yeast protein (282 aa) is longer than human VPS29 (182 aa, `genes/human/VPS29`
  UniProt record) and has a predicted disordered region at 173..242 (MobiDB-lite) with
  two acidic/basic compositional-bias segments. Harbour and Seaman argue from VPS29
  sequence variation that the stable S. cerevisiae heteropentamer is not representative
  of other eukaryotes [PMID:22046480, abstract only; the specific insertion argument is in
  the full text, which is not cached].
- Cryo-ET of C. thermophilum retromer: Vps29 sits at the apex of the Vps35 arch
  [PMID:30224749 "Vps29 resides at the apex where it is free to interact with regulatory factors"].

## Complex membership and partners

- Retromer: [PMID:9700157 "By genetic and biochemical means we now show that Vps35p and Vps29p interact and form part of a multimeric membrane-associated complex that also contains Vps26p, Vps17p, and Vps5p."].
- Vps29-Vps35: overexpressed VPS29 suppresses the dominant-negative vps35dn allele
  [PMID:9700157 "Only cells overexpressing VPS29 were able to suppress the CPY sorting defect caused by the vps35dn allele"];
  binding needs Vps35 R98 and residues 733-944 [PMID:17892535].
- Vps29 is needed for the trimer to bind the SNX-BARs:
  [PMID:9700157 "When a lysate of the vps35Δ strain was cross-linked and Vps29p was immunoprecipitated, Vps29p was not cross-linked to Vps5p/Vps17p"]
  and in vps29Δ "Vps35p no longer cross-linked to Vps5p/Vps17p or Vps26p" [PMID:9700157].
  The Vps5 N-terminus binds Vps29 at two sites
  [PMID:38598303 "the N-terminus of Vps5 interacts with the retromer subunit Vps29 at two sites, including a conserved hydrophobic pocket in Vps29 that engages other accessory proteins in humans."];
  [PMID:40234461 "A Pro-Leu (PL) motif in Vps5 binds Vps29 and is required for association with Retromer on membrane tubules in vitro, and for the proper recycling of the Vps10 cargo in Saccharomyces cerevisiae."];
  [PMID:40234461 "previous studies in S. cerevisiae that have shown the interaction of Retromer with the Vps5–Vps17 proteins requires Vps29 but not Vps26"].
- Snx3/Grd19: [PMID:17420293 "However, when DSP was added to intact spheroplasts before lysing the cells, both Grd19p and Vps17p copurified with Vps29p"].
- Ypt7-GTP beads capture Vps26, Vps29 and Vps35 [PMID:22593205].
- CROP (with Atg18) [PMID:35466426]; Atg21-retromer
  [PMID:42135947 "While Vps29-6xHA co-precipitates with GFP-Atg21 in wt, but not in a vps35∆ strain."].

## Location

- Mostly soluble: [PMID:9700157 "it was found to be a predominantly soluble protein, but ∼20% of Vps29p was associated with the 100,000 g particulate fraction (P100) that contains Vps35p"];
  membrane association needs Vps35 [PMID:9700157 "demonstrating that Vps35p is required for membrane association of Vps29p."];
  no Vps29 in the vacuole/ER/mitochondria/PM P13 fraction [PMID:9700157].
- Cytosolic Vps35-Vps29 complex [PMID:9700157 "In addition we have found that Vps35p assembles into a high molecular weight complex in the cytosol, and this assembly is dependent upon Vps29p."].
- Endosomal dots: [PMID:36644906 "The pre‐vacuolar compartment recruits SNX‐BARs and retromer (Burda et al, 2002; Liu et al, 2012)."]
  and "Vps17yomCherry or Vps29yomCherry appeared as scattered dots" [PMID:36644906].

## Processes

- Vps10 retrieval and CPY sorting [PMID:9105038 "Together, the data indicate that the VPS29, VPS30, and VPS35 gene products are required for the normal recycling of Vps10p from the prevacuolar endosome back to the Golgi where it can initiate additional rounds of vacuolar hydrolase sorting."].
- Recycling of endocytosed Ftr1 (Snx3-retromer, via the Golgi) [PMID:17420293] and Chs3
  [PMID:28362258 "deletion of the gene encoding each retromer subunit also confers resistance to CFW (Figure 4A) and Chs3-GFP is localized prominently to the vacuole lumen"].
- Vacuole fission via CROP [PMID:35466426 "the CSC mutants vps26Δ, vps29Δ and vps35Δ showed fewer and larger vacuoles than the wild type"].

## GO-CAMs

- No production GO-CAM in `gocams/index.tsv` contains S. cerevisiae Vps29 (SGD:S000001054,
  P38759). S. pombe vps29 (SPAC15E1.06) is a has_part of the GO:0030906 complex that enables
  GO:0140312 cargo adaptor activity in gomodel:693b3c0900002174 (activity
  693b3c0900002175; occurs_in endosome; part_of GO:0042147). See PEP8 notes for details.

## Decisions summary

- ACCEPT: endosome (IBA, IPI), retromer complex (IBA, IMP, IPI x2), cargo-selective complex
  (IPI), retrograde transport endosome to Golgi (IBA, IPI, NAS), cargo adaptor activity
  contributes_to (IBA, IMP, IPI), CROP complex (IDA).
- KEEP_AS_NON_CORE: cytosol (IEA), endosome to plasma membrane transport (NAS).
- TOO_GENERAL: endomembrane system (NAS).
- REMOVE: six bare protein-binding rows (Vps17 and Vps35, high-throughput screens).
- No NEW rows. Same reasoning as PEP8 for not proposing GO:0140572 vacuole fission.

## Review follow-up (2026-11-21, PR 6587)

The automated PR review found that the batch argued both sides of some cross-gene questions. These are the calls it now makes:

- Endosome rows: endosome is a series organelle, which the organelle policy does not yet cover, so the ordinary refinement rule applies. A row whose own evidence puts the protein on the endosomal membrane (a peripheral membrane-associated complex, immunogold at the endosome rims, PI3P-dependent puncta) is MODIFY to GO:0010008 endosome membrane. IBA and ARBA rows, whose evidence stops at the organelle, stay ACCEPT at endosome. The resulting inconsistent_review_actions warning for GO:0005768 is the same per-row pattern as the VPS1 GTPase activity rows.
- GO:0032456 (now labelled 'endosome to plasma membrane transport'; 'endocytic recycling' is a narrow synonym): MARK_AS_OVER_ANNOTATED on all five retromer subunits. Retromer is needed for Ftr1 and Chs3 to stay at the surface, but those cargoes return through the Golgi (PMID:17420293), so retromer's carriers go to the Golgi. Each subunit's row carries the same SUSPECTED WRONG_TERM query to ComplexPortal (CPX-1653).
- CROP complex (GO:0170071): ACCEPT, with a CROP core function, on Vps35, Pep8 and Vps29. SGD's rows use is_active_in, but GORULE:0000061 allows only part_of for protein-containing complex terms; a CONFIRMED WRONG_QUALIFIER defect is filed on each.
- The core function location moves from endosome to endosome membrane.
