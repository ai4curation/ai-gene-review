# VPS5 (YOR069W, Q92331) curation notes

## Session 2026-11-21: provenance of the research

- Hosted deep research (falcon, perplexity) is not configured in this environment, so no
  `VPS5-deep-research-<provider>.md` file was made. Everything below is my own reading of
  the cached publications and the UniProt record.
- `just mod-description-deep-research yeast VPS5` succeeded and wrote
  `VPS5-deep-research-sgd.md` (SGD hand-written description). Its claims are checked in that
  reference's `reference_review`.
- PubMed searches (NCBI E-utilities esearch/esummary):
  - `Vps5[tiab] AND Vps17[tiab] AND (yeast OR cerevisiae)` (12 hits)
  - `(Vps5[tiab] OR Vps5p[tiab]) AND (yeast[tiab] OR cerevisiae[tiab] OR retromer[tiab])` (43 hits)
  - `(Vps17[tiab] OR Vps17p[tiab]) AND (yeast[tiab] OR retromer[tiab])` (29 hits)
  - `Purushothaman[au] AND retromer`, `Suzuki SW[au] AND Emr SD[au]`
- Papers cached for this review in addition to the GOA references: PMID:9285823, PMID:8416961,
  PMID:35506766, PMID:36644906, PMID:41699388, PMID:38598303, PMID:35938928, PMID:12244127,
  PMID:30188774, PMID:34524084, PMID:35574911, PMID:42135947, PMID:11598206, PMID:31337624.
  Already in the repository and read here: PMID:40234461, PMID:30224749, PMID:28100638,
  PMID:22593205, PMID:24567361.
- Abstract only: PMID:9175702, PMID:9285823, PMID:12181349, PMID:11557775, PMID:12244127,
  PMID:8649377 (truncated), PMID:11598206 and the high-throughput interaction papers except
  PMID:37968396. The full text of PMID:11557775 (JBC) was blocked (HTTP 403 from jbc.org).
- PAINT losses (`just paint-losses yeast VPS5`): "No IRD or IKR loss on this gene's lineage."
  No PTHR10555 family review exists.

## Identity and domains

- 675 aa sorting nexin; synonyms GRD2, PEP10, VPT5. N-terminal disordered region (~1-278),
  PX domain 279-394 (PROSITE), Vps5 C-terminal BAR region (Pfam PF09325; CDD BAR_Vps5p).
- Homologue of human SNX1 [PMID:9285823 "The VPS5 gene is predicted to encode a very hydrophilic protein of 675 amino acids that shows significant sequence homology with mammalian sorting nexin-1."].
- Paralog Vin1 (YKR078W) from the whole-genome duplication [PMID:35938928 "Vin1 and Vps5 arose from a single ancestral gene during a whole-genome duplication (WGD) event"]. Vin1 pairs with Vrl1 to form the VINE complex, not retromer.
- The VAM10 ORF lies inside VPS5 [PMID:40234461 "the VAM10 gene is embedded in VPS5 and deleted with it"]. vps5 deletion
  phenotypes on vacuole morphology therefore need a VAM10-complemented control, as Chen et
  al. 2025 used.

## Complex membership

- Vps5 and Vps17 form a heterodimer [PMID:9285823 "Biochemical cross-linking studies demonstrated that Vps5p and Vps17p physically interact."]; the C-terminal halves (BAR) are necessary and sufficient [PMID:12181349 "the C-terminal halves of Vps5p and Vps17p, which contain the coiled-coils domains, are necessary and sufficient for their interaction"].
- Retromer pentamer: Vps35-Vps29-Vps26 plus Vps5-Vps17 [PMID:9700157 "This complex, designated here as the retromer complex, assembles from two distinct subcomplexes comprising (a) Vps35p, Vps29p, and Vps26p; and (b) Vps5p and Vps17p."]. ComplexPortal CPX-1653.
- Vps5 (not Vps17) carries the retromer assembly domain in its N-terminus [PMID:12181349 "We have also mapped the retromer assembly domain to the N-terminal half of Vps5p"]. Mapped later:
  - a PL motif binding Vps29 plus [K/R]Φ and LF motifs contacting Vps29-Vps35 [PMID:40234461 "Here, we show that Vps5 binds both Vps29 and Vps35 subunits through its unstructured N-terminal domain."];
  - S. cerevisiae Vps5 FTDPL (pocket) and PRILFDS (sheet) motifs at aa 155-198 [PMID:38598303 "these data suggest that Vps5 interacts with Vps29 through an N-terminal bipartite pocket- and sheet-binding motif that is critical for both retromer assembly and efficient sorting"].
  - Vps17's N-terminus does not bind retromer [PMID:40234461 "Vps17 also has a long N-terminal unstructured domain but does not have a conserved PL motif"].
- Vps26 promotes the CSC-SNX-BAR interaction [PMID:11598206 "Vps26p promotes the interactions between the cargo-selective component Vps35p and the structural components Vps5p/Vps17p."]; Vps29's hydrophobic pocket is needed for SNX assembly [PMID:15965486].
- Alternative retromers: the PROPPINs Atg18 and Atg21 bind the CSC competitively with Vps5/Vps17 [PMID:35574911 "The binding of Atg18 to Vps35 is competitive with the sorting nexin dimer Vps5 and Vps17."; PMID:42135947]. Snx3 forms its own retromer coat and hybrid coats with Vps5-Vps17 [PMID:41699388].
- High-throughput interaction rows (Uetz Y2H, Gavin and Michaelis AP-MS, Tarassov PCA,
  Vollert PX-domain Y2H) recover Vps17, Vps35 and Vps26 (Pep8). Vollert & Uetz also found
  Yip1-family partners [PMID:15263065].

## Molecular function

1. **PI3P binding by the PX domain.** Yu & Lemmon found all but one yeast PX domain bind
   PtdIns3P (low affinity for most) [PMID:11557775]; Burda et al. showed it specifically for
   Vps5 and Vps17 [PMID:12244127 "We demonstrate that the PX domains of Vps5p and Vps17p specifically bind to PtdIns3P in vitro and in vivo."]. Vps5/Vps17 redistribute to the cytoplasm when PtdIns3P falls (vps30Δ, vps38Δ) [PMID:12244127].
2. **Membrane bending (SNX-BAR).** Purified full-length Vps5-Vps17 tubulates PI3P-containing
   liposomes and GUVs; without PI3P there is no binding and no tubulation [PMID:28100638 "The SNX-BAR heterodimer thus requires PI-3-P binding for membrane recruitment and tubulation activity."].
   At high concentration the SNX-BARs alone constrict supported tubes to a 19 nm radius [PMID:36644906 "High concentrations of sorting nexins alone constrict membrane tubes to an invariant radius of 19 nm."].
   Cryo-ET of C. thermophilum retromer on Vps5-coated tubules: "a membrane-associated Vps5 array, from which arches of retromer extend away from the membrane surface" [PMID:30224749].
   GO term: GO:0180020 membrane bending activity (checked in OLS). The PomBase GO-CAM
   gomodel:693b3c0900002174 uses exactly this term for the S. pombe retromer tubulation
   complex (vps5 + vps17).
3. **Recruiting the CSC to membranes (protein-membrane adaptor).** The Vps5 PL motif is needed
   for retromer recruitment to tubules and for Vps10 recycling [PMID:40234461 "A Pro-Leu (PL) motif in Vps5 binds Vps29 and is required for association with Retromer on membrane tubules in vitro, and for the proper recycling of the Vps10 cargo in Saccharomyces cerevisiae."].
   In vivo the CSC needs Vps5-Vps17 for endosomal (not vacuolar) localisation [PMID:22593205 "the Vps5 and Vps17 sorting nexins are required for recruitment to endosomes, and the GTP-loaded form of Ypt7 is required for vacuole localization."].
   GO term: GO:0043495 protein-membrane adaptor activity (definition: brings a protein complex
   to a membrane via lipid binding). SGD has this term on VPS17 (contributes_to, IMP
   PMID:12181349); the S. pombe Snx3 activity in gomodel:693b3c0900002174 uses it too.
4. **Cargo adaptor activity (GO:0140312) is the CSC's activity**, not Vps5's: the CSC
   recognises Vps10 and other cargo [PMID:31337624], and the PomBase GO-CAM puts cargo adaptor
   activity on GO:0030906 and membrane bending on GO:0030905. SGD's contributes_to rows on
   VPS5 are therefore marked over-annotated.
5. Self-assembly of cytosolic and recombinant Vps5 into large particles [PMID:9700157]. No
   separate GO term proposed.

## Location

- Cytosolic pool plus peripheral membrane pool [PMID:9175702 "Fractionation studies indicate that Vps5p is distributed between a free cytosolic pool and a particulate fraction containing Golgi, transport vesicles, and possibly endosomes, but lacking vacuolar membranes."]; ~40-60% soluble [PMID:9700157].
- Endosome: IF of the membrane-associated pool on the class E compartment [PMID:9175702];
  immunogold at the rims of the prevacuolar endosome [PMID:9700157]; Vps5-GFP and Vps17-GFP
  endosomal puncta [PMID:22593205]; Vps17-coated tubules bud from endosomes and carry Vps10
  [PMID:24567361].
- Golgi membrane: only UniProt's ECO:0000305 inference. Horazdovsky et al. found the dense
  membrane fraction "distinct from Golgi, endosomal, and vacuolar membranes" [PMID:9285823],
  and imaging puts Vps17 on endosomes distinct from Sec7 Golgi [PMID:24567361]. Marked
  over-annotated.
- Liu et al. note that Vps5/Vps17 "do not detectably localize to the vacuole membrane"
  [PMID:22593205], whereas Arlt et al. 2015 (cited in PMID:28100638) saw SNX-BAR/CSC tubules
  leaving the vacuole. Not resolved here.

## Biological role

- Endosome-to-Golgi retrieval of Vps10 and late-Golgi membrane proteins (A-ALP, Kex2)
  [PMID:9175702; PMID:9285823; PMID:9700157]. In vps5Δ Vps10-mNeonGreen accumulates on
  fragmented vacuoles; a PX-BAR-only Vps5 (Δ1-280) does not rescue [PMID:40234461].
- Snx3 cargo (Ear1, Ste13) also mislocalise in vps5Δ or vps17Δ [PMID:41699388 "showed significant mislocalization to vacuoles not only in snx3Δ, but also in vps5Δ or vps17Δ cells, suggesting that the Snx3 recycling pathway requires SNX-BARs for its function."].
  Strubel et al. 2026 [PMID:42135947] instead state that Ear1 sorting is normal in vps17Δ
  (citing their ref. 43, reference list not cached). Conflict noted, not resolved.
- Vacuole morphology: vps5Δ/vps17Δ give fragmented vacuoles [PMID:9285823] and
  hyper-fragmentation under hyperosmotic stress, while Vps5 overexpression blocks
  fragmentation [PMID:35574911]. Interpreted as competition of Vps5-Vps17 with Atg18 (and
  Atg21, Hsv2) for the CSC, and free CSC binding Ypt7 [PMID:22593205; PMID:35574911]. This is
  an indirect role, so no vacuole-fission term is proposed.
- Endocytic recycling (GO:0032456, endosome to plasma membrane): no evidence for Vps5 or the
  yeast SNX-BAR retromer. PMID:9700157 (the ComplexPortal NAS source) describes only
  endosome-to-Golgi retrieval. Marked over-annotated.
- Golgi retention (GRD2): the grd screen [PMID:8649377] and PMID:9175702. Kept as non-core,
  as in the VPS1 review: it is the outcome of retrieval.

## NEW rows and the participation/comparator tests

- GO:0180020 membrane bending activity: Vps5-Vps17 does the bending itself (in vitro tubulation
  and constriction). Comparators: no SNX-BAR protein yet carries the term in QuickGO; its
  non-IEA annotations (29) are on Mgm1, OPA1, CHMP2A/3, Yop1/hva22, Rtn1, i.e. membrane-shaping
  proteins. The query returns positives, so the absence on SNX-BARs reflects the term's
  recency. PomBase uses it for the S. pombe tubulation complex in a production GO-CAM.
- GO:0097750 endosome membrane tubulation: human SNX1 and SNX5 carry it by IDA
  (ComplexPortal, PMID:37322239) in QuickGO; same GO-CAM as above. Vps17-coated tubules bud
  from endosomes in vivo [PMID:24567361].
- GO:0043495 protein-membrane adaptor activity: Vps5 itself binds the CSC (N-terminus) and
  PI3P membranes (PX); VPS17 already carries the term (contributes_to). S. pombe Snx3 carries
  it in the GO-CAM.

## GO-CAMs (gocams/index.tsv)

- No production GO-CAM contains S. cerevisiae Vps5 (SGD:S000005595, Q92331) or Vps17.
- S. pombe model gomodel:693b3c0900002174 "retrograde transport endosome to Golgi (GO:0042147)
  (partial)": activity 693b3c0900002185 is enabled by GO:0030905 retromer, tubulation complex
  (has_part PomBase:SPCPJ732.01 vps5 and PomBase:SPAPJ696.01c vps17), MF GO:0180020 membrane
  bending activity, occurs_in GO:0005768 endosome, part_of GO:0097750 endosome membrane
  tubulation, causally upstream (RO:0002304) of grp1 (SPAC27D7.02c) vesicle membrane tethering.
  The CSC (GO:0030906; SPCC777.13, SPAC15E1.06, SPAC4G9.13c) enables GO:0140312 cargo adaptor
  activity and is constitutively upstream (RO:0012009) of the tubulation complex. Snx3
  (SPBC887.06c) enables GO:0043495 protein-membrane adaptor activity upstream of the CSC.
  Evidence on these edges is ECO:0000305 / GO_REF:0000111 (curator inference).

## Relation to the VPS1 review

- VPS1 says Vps1 cuts retromer/Mvp1 SNX-BAR tubules [PMID:24567361]. Consistent: that paper
  shows Vps17-GFP coated tubules budding from endosomes, half of them also Mvp1-coated. No
  disagreement found.

## Review follow-up (2026-11-21, PR 6587)

The automated PR review found that the batch argued both sides of some cross-gene questions. These are the calls it now makes:

- Endosome rows: endosome is a series organelle, which the organelle policy does not yet cover, so the ordinary refinement rule applies. A row whose own evidence puts the protein on the endosomal membrane (a peripheral membrane-associated complex, immunogold at the endosome rims, PI3P-dependent puncta) is MODIFY to GO:0010008 endosome membrane. IBA and ARBA rows, whose evidence stops at the organelle, stay ACCEPT at endosome. The resulting inconsistent_review_actions warning for GO:0005768 is the same per-row pattern as the VPS1 GTPase activity rows.
- GO:0032456 (now labelled 'endosome to plasma membrane transport'; 'endocytic recycling' is a narrow synonym): MARK_AS_OVER_ANNOTATED on all five retromer subunits. Retromer is needed for Ftr1 and Chs3 to stay at the surface, but those cargoes return through the Golgi (PMID:17420293), so retromer's carriers go to the Golgi. Each subunit's row carries the same SUSPECTED WRONG_TERM query to ComplexPortal (CPX-1653).
- Cytosol stays KEEP_AS_NON_CORE on direct fractionation of a 40-60% soluble Vps5 pool. The description no longer says the heterodimer comes from that pool, which has not been shown for Vps17.

## GO-CAMs are not support (2026-11-21)

The S. pombe GO-CAMs referred to above are not independent evidence and are no longer cited as support or as comparators in the review. In gomodel:693b3c0900002174, the function nodes carry no evidence, and the retromer complexes' edges are curator inferences from complex membership (ECO:0000305). The Snx3 edge is an IBA seeded by S. cerevisiae Snx3, and in gomodel:6918f23700004102 the mvp1 edge rests on an InterPro mapping and an IBA seeded by S. cerevisiae MVP1. Claims rest on the cited papers. Comparators now come from experimental annotations only (QuickGO, experimental evidence codes, 2026-11-21):

- endosome membrane tubulation (GO:0097750): human SNX1 and SNX5, IDA, ComplexPortal, PMID:37322239.
- protein-membrane adaptor activity (GO:0043495): yeast VPS17 (IMP, PMID:12181349) and Drosophila Snx3 (IPI, FlyBase, PMID:22041890).
- membrane bending activity (GO:0180020): no SNX-BAR protein yet; the 12 experimental annotations are on Mgm1, OPA1, CHMP2A/CHMP3 and the reticulon/Yop1 family.
