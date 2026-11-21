# VPS17 (YOR132W, P32913) curation notes

## Session 2026-11-21: provenance of the research

- Reviewed in the same session as VPS5; the literature search, cached papers and GO-CAM check
  are recorded in `genes/yeast/VPS5/VPS5-notes.md` and apply here too. Hosted deep research
  (falcon, perplexity) is not configured, so there is no `VPS17-deep-research-<provider>.md`.
- `just mod-description-deep-research yeast VPS17` succeeded (`VPS17-deep-research-sgd.md`).
- PubMed query specific to this gene: `(Vps17[tiab] OR Vps17p[tiab]) AND (yeast[tiab] OR retromer[tiab])`
  (29 hits; fungal-pathogen papers on Vps17 orthologs in Cryptococcus, Magnaporthe and Candida were
  not used). Additional papers cached for VPS17: PMID:8416961 (cloning) and PMID:35506766 (PX
  domain structure), both abstract only.
- PAINT losses (`just paint-losses yeast VPS17`): "No IRD or IKR loss on this gene's lineage."
  PTHR47433 (VPS17 family) has no family review.

## Identity and domains

- 551 aa; synonyms PEP21, VPT3. N-terminal disordered region (1-100), PX domain 108-227, coiled
  coil 359-385 in a C-terminal BAR region (CDD BAR_Vps17p). Ser544 phosphorylated (HTP).
- Hydrophilic, no signal sequence or transmembrane segment; peripheral membrane protein
  [PMID:8416961 "Vps17p can be released from this particulate fraction by treatment with either Triton X-100 or urea, indicating that the Vps17p is peripherally associated with a crude membrane fraction."].
- Human counterparts are SNX5/SNX6/SNX32 [PMID:34524084 "Vps17 (SNX5/6/32 in humans)"]. No yeast paralog.

## Complex membership and partners

- Heterodimer with Vps5 through the C-terminal halves [PMID:12181349; UniProt DOMAIN, ECO:0000269].
  Vps5's peripheral membrane association depends on Vps17 [PMID:9285823 "This association was found to be dependent on the presence of another class B VPS gene product, Vps17p."].
- Retromer pentamer member [PMID:9700157]; ComplexPortal CPX-1653.
- Vps17 does not itself bind the cargo-selective subcomplex: its N-terminus has no PL motif and
  shows no binding by ITC [PMID:40234461 "Under the same conditions and concentrations no interaction is detected with the Vps17 N-terminal domain."].
  But Vps17 binding to Vps5 "synergizes the interaction between Vps5p and other retromer components" [PMID:12181349].
- In vps17Δ cells a retromer with two Vps5 molecules is said to form [PMID:42135947, citing its ref. 43, not cached].
- Two-hybrid partners Yip1 and Yif1 [PMID:15263065]; interaction with Vps26 (Pep8)
  [PMID:15965486 row]; HTP AP-MS and PCA recover the whole retromer.
- Atg18 binds the cargo-selective subcomplex competitively with Vps5/Vps17 [PMID:35574911]; Atg21
  competes with Vps5 but not Vps17 [PMID:42135947].

## Molecular function

- **PI3P binding (disputed).** SGD's IDA comes from Yu & Lemmon [PMID:11557775], where all yeast PX
  domains but one sequence outlier bound PtdIns3P (the abstract does not say which was the
  outlier; SGD annotated Vps17 positively, so presumably not Vps17). Burda et al. state that
  "the PX domains of Vps5p and Vps17p specifically bind to PtdIns3P in vitro and in vivo"
  [PMID:12244127]. Against this, the crystal structure of the Vps17 PX domain shows "no basic
  residues ... around the canonical phosphatidylinositol phosphate (PtdIns-P) binding site,
  suggesting an inability to bind PtdIns-P molecules" [PMID:35506766]. UniProt annotates no
  PI3P-binding residues on Vps17 (it does on Vps5, by similarity). Kept (ACCEPT), because two
  experimental studies outweigh a structural inference, but flagged as a question. Only abstracts
  of PMID:11557775, PMID:12244127 and PMID:35506766 were available.
- **Membrane bending (with Vps5).** The purified Vps5-Vps17 heterodimer tubulates PI3P membranes
  [PMID:28100638; PMID:30188774 "we added either GFP-tagged or untagged complex to PI-3-P containing membranes, which resulted in a dose-dependent increase in observable tubules emanating from the GUV surface"]
  and constricts tubes [PMID:36644906]. No experiment tests Vps17 without Vps5, so Vps17 gets
  contributes_to GO:0180020.
- **Protein-membrane adaptor (contributes_to).** SGD's IMP row (PMID:12181349). The
  heterodimer recruits the cargo-selective subcomplex to endosomes [PMID:22593205, vps5Δ vps17Δ
  double deletion]; the direct contacts are on Vps5 [PMID:40234461].

## Location

- Endosomes: Vps17-GFP endosomal puncta [PMID:22593205]; Vps17-GFP decorates endosomes and the
  tubules budding from them, half of which carry Vps10 [PMID:24567361]; Vps17-mCherry is used as
  an endosome marker distinct from Sec7 Golgi [PMID:42135947, PMID:24567361].
- UniProt SUBCELLULAR LOCATION 'Endomembrane system' with the note "Membrane-associated on the
  cytoplasmic side of either the Golgi complex or an intermediate in Golgi to vacuole transport"
  restates the 1993 proposal of PMID:8416961; later imaging resolves it to endosomes. Not filed as
  a source defect (the term is imprecise, not wrong).
- Cytosol (IEA from GO_REF:0000108, inferred from the process term): wild-type Vps17 fractionates
  as particulate [PMID:8416961]; Vps17 becomes cytoplasmic only when PtdIns3P is lowered
  [PMID:12244127]. Marked over-annotated.

## Biological role

- Endosome-to-Golgi retrieval of Vps10: vps17 mutants secrete 95% of CPY [PMID:8416961];
  Vps10-mNeonGreen colocalises with the vacuole in vps17Δ [PMID:41699388].
- vps17Δ vacuoles hyper-fragment under hyperosmotic stress; this depends on Atg18 and Atg21
  [PMID:35574911; PMID:42135947]. Indirect (competition for the cargo-selective subcomplex), so no
  vacuole-fission term is proposed. UniProt's FUNCTION sentence "Involved in vacuolar
  fragmentation during hyperosmotic stress" is a loose reading of a loss-of-function phenotype
  (loss of Vps17 increases fragmentation).
- Endocytic recycling (GO:0032456, NAS): no evidence for Vps17; marked over-annotated, as for VPS5.

## NEW rows

- GO:0180020 membrane bending activity (contributes_to), GO:0097750 endosome membrane tubulation
  and GO:0010008 endosome membrane. Comparator and participation reasoning as in the VPS5 notes;
  the PomBase GO-CAM gomodel:693b3c0900002174 has S. pombe vps17 (SPAPJ696.01c) as part of the
  tubulation complex that enables GO:0180020 and is part_of GO:0097750.

## Review follow-up (2026-11-21, PR 6587)

The automated PR review found that the batch argued both sides of some cross-gene questions. These are the calls it now makes:

- Endosome rows: endosome is a series organelle, which the organelle policy does not yet cover, so the ordinary refinement rule applies. A row whose own evidence puts the protein on the endosomal membrane (a peripheral membrane-associated complex, immunogold at the endosome rims, PI3P-dependent puncta) is MODIFY to GO:0010008 endosome membrane. IBA and ARBA rows, whose evidence stops at the organelle, stay ACCEPT at endosome. The resulting inconsistent_review_actions warning for GO:0005768 is the same per-row pattern as the VPS1 GTPase activity rows.
- GO:0032456 (now labelled 'endosome to plasma membrane transport'; 'endocytic recycling' is a narrow synonym): MARK_AS_OVER_ANNOTATED on all five retromer subunits. Retromer is needed for Ftr1 and Chs3 to stay at the surface, but those cargoes return through the Golgi (PMID:17420293), so retromer's carriers go to the Golgi. Each subunit's row carries the same SUSPECTED WRONG_TERM query to ComplexPortal (CPX-1653).
- Cytosol stays MARK_AS_OVER_ANNOTATED. The large soluble Vps5 pool assembles the same way in vps17 deletion cells (PMID:9700157), so it is not evidence of a cytosolic Vps17 pool.

## GO-CAMs are not support (2026-11-21)

The S. pombe GO-CAMs referred to above are not independent evidence and are no longer cited as support or as comparators in the review. In gomodel:693b3c0900002174, the function nodes carry no evidence, and the retromer complexes' edges are curator inferences from complex membership (ECO:0000305). The Snx3 edge is an IBA seeded by S. cerevisiae Snx3, and in gomodel:6918f23700004102 the mvp1 edge rests on an InterPro mapping and an IBA seeded by S. cerevisiae MVP1. Claims rest on the cited papers. Comparators now come from experimental annotations only (QuickGO, experimental evidence codes, 2026-11-21):

- endosome membrane tubulation (GO:0097750): human SNX1 and SNX5, IDA, ComplexPortal, PMID:37322239.
- protein-membrane adaptor activity (GO:0043495): yeast VPS17 (IMP, PMID:12181349) and Drosophila Snx3 (IPI, FlyBase, PMID:22041890).
- membrane bending activity (GO:0180020): no SNX-BAR protein yet; the 12 experimental annotations are on Mgm1, OPA1, CHMP2A/CHMP3 and the reticulon/Yop1 family.
