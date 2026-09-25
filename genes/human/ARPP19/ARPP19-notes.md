# ARPP19 (P56211) curation notes

## 2026-09-25 - initial review

### Identity and inputs

- Human ARPP19, cAMP-regulated phosphoprotein 19, 112 aa, endosulfine family (PF04667),
  two isoforms: ARPP-19 (P56211-1) and the 16-residue-shorter, striatum-enriched ARPP-16
  (P56211-2). Paralog: ENSA (O43768).
- Inputs: UniProt record (entry v197), GOA tsv (23 rows), falcon deep research, cached
  publications for all six PMIDs and the Reactome reaction. Exemplar: `genes/human/MASTL`
  (COMPLETE). ENSA review was still INITIALIZED when this was written.
- Relevant repository objects: `modules/g2_m_transition.yaml` (endosulfine annoton, cites
  PMID:21164014) and GO-CAM `gocams/69729a3800000481` (MAST3 regulates ARPP19; ARPP19
  activity typed GO:0004864, part_of GO:0010923, has_input PPP2R2A, negatively regulates
  the PP2A activity node).

### Synthesized biology

- Core: MASTL/Greatwall phosphorylates Ser62 at mitotic entry; pSer62-ARPP19 binds and
  inhibits PP2A-B55 so CDK1 substrate phosphorylation persists; it is later slowly
  dephosphorylated by PP2A-B55, which times mitotic exit.
  [PMID:21164014 "We identified cyclic adenosine monophosphate-regulated phosphoprotein 19
  (Arpp19) and α-Endosulfine as two substrates of Gwl that, when phosphorylated by this
  kinase, associate with and inhibit PP2A, thus promoting mitotic entry."]
  [PMID:38123684 "ARPP19 strictly requires phosphorylation by MASTL kinase to inhibit
  PP2A:B55"] [PMID:38123684 "pS62-ARPP19 functions first as an inhibitor of PP2A:B55 but
  later becomes a substrate"]
- Structure: cryo-EM 8TTB of PP2A:B55 with thiophosphorylated ARPP19; tripartite binding
  to the top of B55 (res 25-61), PP2Ac (pS62 + helix alpha4) and a distal B55 pocket
  (res 86-112). C-terminal deletion abolishes inhibition of the unphosphorylated protein
  and weakens the phosphorylated one >50-fold. [PMID:38123684 "tpARPP19 binds PP2A:B55
  using a tripartite mechanism"]
- Endogenous relevance: in Xenopus egg extracts Arpp19, not ENSA, is the mitotic-entry
  inhibitor [PMID:21164014 "endogenous Arpp19, but not α-Endosulfine, is responsible for
  PP2A inhibition at mitotic entry in Xenopus egg extracts"]. Deep research: mouse Arpp19
  KO is embryonic lethal; Arpp19-null MEFs prematurely dephosphorylate CDK1 substrates in
  mitosis and ENSA does not compensate (Hached et al. 2019, not cached).
- Neuronal arm: ARPP-16 in striatal MSNs is phosphorylated on Ser46 (= Ser62 of ARPP-19)
  by MAST3, giving basal inhibition of B55alpha/B56delta PP2A; PKA phosphorylation of
  Ser88 (= Ser104) is accompanied by Ser46 dephosphorylation, i.e. dopamine/cAMP relieves
  the inhibition. Conditional KO increases dephosphorylation of DARPP-32 Thr75, Akt
  Thr308, ERK. [PMID:28167675 "phosphorylation of ARPP-16 at Ser46 by MAST3 kinase
  converts the protein into a selective inhibitor of B55α- and B56δ-containing
  heterotrimeric forms of PP2A"]
- PKA site Ser104 confirmed on human protein [PMID:38123684 "Ser104, a serine that was
  previously identified as a protein kinase A (PKA) substrate"]. Xenopus oocyte
  prophase-I arrest via the PKA site is model-organism evidence (deep research).
- Localization: UniProt cytoplasm (by similarity); IBA cytoplasm; Reactome models the
  MASTL reaction in nucleoplasm. Deep research: ectopic Arpp19 in MEFs is both cytoplasmic
  and nuclear. No direct localization study of endogenous human ARPP19 through the cell
  cycle.
- The family authors themselves conclude the function is limited to PP2A control and
  that older ENSA "extracellular ligand" ideas are unsupported. [PMID:28167675 "suggest
  that the function of the ARPP-16/19/ENSA family of proteins is limited to control of
  PP2A activity."] [PMID:28167675 "However, there is no evidence that ENSA is found
  extracellularly."]

### Key curation decision: PMID:9653196 rows

Four GOA rows on ARPP19 cite Heron et al. 1998 (GO:0005102 IDA, GO:0015459 IDA,
GO:0045722 IDA, GO:0046326 NAS). The full text is cached. The paper clones and expresses
human alpha-endosulfine (ENSA) and performs every functional assay with that recombinant
protein; ARPP-19 appears only as a partial cDNA cloned for sequence comparison, explicitly
described as a different gene.
[PMID:9653196 "We therefore cloned part of the human ARPP-19 cDNA (EMBL accession no.
AJ223091 ), and compared its sequence to that of human α-endosulfine (Fig. 1 A )."]
[PMID:9653196 "although the two proteins appeared to be encoded by different genes ( 14 )."]
[PMID:9653196 "The recombinant protein displaces binding of the sulfonylurea
[ 3 H]glibenclamide to β cell membranes, inhibits cloned K ATP channel currents, and
stimulates insulin secretion."]

The paper never mentions gluconeogenesis or glucose import at all (grep of full text).
The same paper is correctly annotated to ENSA in GOA (GO:0005102, GO:0019870, GO:0050796,
GO:0007584). The likely origin of the ARPP19 rows is that this paper is UniProt reference
[1] for the ARPP-19 mRNA (AJ223091). All four rows -> REMOVE. This is not a case of
overruling a curator from an abstract: the full text is available and explicit.
Raised as a suggested question for GOA curators.

### Other decisions

- GO:0000086 IMP and GO:0000278 IMP (PMID:21164014): ACCEPT both. Abstract-only in
  cache, but the function is established and reconstituted with human proteins.
  `mitotic cell cycle` is general but not redundant, because ARPP19 also acts as the
  PP2A-B55 "timer" for mitotic exit.
- GO:0004864 IBA/IDA/IDA/IMP: ACCEPT. IBA node PTN001309504 spans fly/yeast/pombe/human;
  human ARPP19 in its own WITH/FROM is the expected marker of direct evidence.
- GO:0010923 IDA: ACCEPT; obsolete children (GO:0032515, GO:0035308) verified on QuickGO,
  so this is the right level; matches the GO-CAM.
- GO:0051721 EXP/IDA/IMP/ISS: ACCEPT; informative binding term, structurally resolved.
- GO:0005515 IPI x3: PPP2R2A (PMID:38123684) -> MODIFY to GO:0051721; SPDYC (HuRI Y2H)
  and APP (ND interactome Y2H) -> REMOVE as uninformative, without asserting the
  interactions are false.
- GO:0019212 / GO:0019888 ISS from Xenopus Arpp19-A (Q6DEB4): ACCEPT (parents of 0004864).
- GO:0005654 TAS Reactome: KEEP_AS_NON_CORE (pathway placement, not localization data);
  MASTL review ACCEPTed the same row for the kinase, which is nuclear in interphase.
- GO:0005737 IBA/IEA: ACCEPT.
- No NEW terms. Considered `regulation of mitotic cell cycle` and meiosis terms; the
  meiotic arrest role is Xenopus-only and the existing G2/M + mitotic cell cycle terms
  cover the human evidence.

### Validation

`just validate human ARPP19` -> Valid, no warnings (after fixing a folded-scalar hyphen
and adding a deep-research citation). All supporting_text checked as verbatim substrings
(three quotes contain U+2009 thin spaces copied from the source).
