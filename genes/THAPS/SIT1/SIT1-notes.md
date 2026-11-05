# SIT1 (UniProtKB:B8C2V9), Thalassiosira pseudonana — curation notes

No deep-research provider output was available; these notes come from my own reading of the
cached publications, the UniProt entries and a sequence comparison
(`SIT1-bioinformatics/RESULTS.md`). The SIT2 paralog (B5YNJ0) is reviewed alongside in
`genes/THAPS/SIT2/`.

## Identity

- B8C2V9 (464 aa, ORF THAPSDRAFT_268895, EMBL EED92452, reference proteome UP000001449) is TpSIT1.
  It is an exact C-terminal suffix of the cDNA-derived TpSIT1 (GenBank ABB81825, UniProtKB Q0QVM8,
  517 aa) but lacks the first 53 residues, including a probable N-terminal transmembrane/signal
  segment (`SIT1-bioinformatics/RESULTS.md`).
- The TpSIT1 identity is confirmed by the published reagents: the anti-TpEL4 peptide is
  "a 15-residue region corresponding to amino acids 318 to 332 of TpSIT1 (sequence PANERGTSFFGRKTC)"
  [PMID:17172435], which is residues 318-332 of Q0QVM8 and residues 265-279 of B8C2V9, and the
  TpSIT1 cloning primers encode the Q0QVM8 N-terminus (MSTAEIQ) and the shared C-terminus (DALAEDA)
  [PMID:17172435 Methods].
- Shrestha & Hildebrand state "SIT1 and SIT2 have type I signal peptides" [PMID:25380754]; the
  N-terminal hydrophobic stretch that would carry such a signal is the part missing from B8C2V9.
  Literature residue numbers must be shifted by -53 onto B8C2V9.
- TpSIT1 and TpSIT2 are close paralogs: "Pairwise comparison between each SIT revealed 88% amino
  acid identity and 95% similarity between TpSIT1 and TpSIT2" [PMID:17172435].

## Family function (SIT family, Pfam PF03842 / IPR004693)

- SITs were discovered in Cylindrotheca fusiformis [PMID:9034185, abstract-only cache, no quotable
  text; Hildebrand et al. 1997 Nature]. Background statement in PMID:17172435: "Diatom silicon
  transporters (SITs), first identified in the marine pennate diatom Cylindrotheca fusiformis ( 32
  , 34 ), are membrane-associated proteins that directly interact with and transport silicic acid".
- Direct in vitro transport by purified SITs: PtSIT1 (Phaeodactylum) and NaSIT showed
  Michaelis-Menten transport with "KM for silicic acid of 19.1±4.5 μM and 19.6±7.7 μM" in
  proteoliposomes driven by "An inward-directed electrochemical sodium gradient"; ITC indicated
  "1:1:1 Na+:Si(OH)4:SIT stoichiometry" [PMID:27305972]. TpSIT3 (a T. pseudonana paralog, NOT SIT1)
  was reconstituted earlier: "silicon uptake was found to be dependent upon an applied sodium
  gradient" [PMID:22530967; the T. pseudonana SIT in that paper is identified as TpSIT3 in
  PMID:27305972, "similar to previous results with TpSIT3 (ref. 30)"].
- AlphaFold modelling predicts a conserved SIT fold with a central polar binding site "consistent
  with an alternating access mechanism of transport" [PMID:36191629].
- TpSIT1 itself has never been purified or assayed for transport in vitro. Knight et al. found
  "TpSIT1 and ToSIT were expressed at very low levels" in yeast [PMID:27305972]. The molecular
  function is therefore inferred from the family (ISS), not shown directly.

## In vivo evidence specific to SIT1 (and SIT2)

- Location: "Epifluorescence microscopy of transgenic cells expressing SIT1 and SIT2 in Si-depleted
  cultures showed bright eGFP fluorescence in the plasma membrane under Si starvation for 24 h"
  [PMID:25380754]. Weak ER labelling was seen in G1, interpreted as transit to new plasma membrane.
- Regulation: SIT1/SIT2 protein (eGFP) rises under Si starvation and falls on Si addition; "The
  eGFP intensity of SIT1 was higher than that of SIT2 at all time points" [PMID:25380754]. Earlier
  bulk work found transcript and protein uncoupled through the cell cycle [PMID:17172435].
- Knockdown: one construct targeted both genes — "Separate knockdowns of SIT1 and SIT2 could not
  be pursued with the vector construction design used in this study" [PMID:25380754]. At 20 μM
  Si, "the wild type depleted the medium of silicon by 2 h, whereas the transgenic clones lagged
  and took 1 h longer"; at 200 μM, uptake was "more or less equal to those in the wild type,
  consistent with diffusion being predominant" [PMID:25380754].
- Kinetics model: "active transport by Si transporters at low Si(OH)(4) and diffusional transport
  ... at high Si(OH)(4)" [PMID:18162598, abstract].
- Sensing: the authors propose that "Their primary role is to sense silicic acid levels"
  [PMID:25380754]; this is a hypothesis, with an upstream sensor kept as the alternative. I do not
  annotate a sensing/regulatory process.

## GO decisions

- GO:0015708 silicic acid import across plasma membrane (IEA, InterPro2GO): ACCEPT. Supported for
  this gene by plasma-membrane localization plus the joint SIT1/SIT2 knockdown phenotype at low Si,
  and by family-level Na+-coupled transport.
- NEW GO:0005886 plasma membrane (IDA, PMID:25380754): direct eGFP-fusion localization of SIT1.
- NEW GO:0015115 silicate transmembrane transporter activity (ISS, PMID:27305972): inferred from
  directly assayed family members; no GO term exists for silicic-acid-specific transporter activity
  or for sodium-coupled silicic acid symport (GO:0015708 is the process, not the activity).

## ISS With/From donors (verified)

Both donor accessions were checked against the UniProt REST API on 2026-10-28, so a later reader
need not re-check them:
- **B7T1F4** = B7T1F4_PHATR, *Phaeodactylum tricornutum*, 512 aa, gene `SIT1`, protein name "SIT1".
- **B8C4N0** = B8C4N0_THAPS, *Thalassiosira pseudonana*, 437 aa, gene `SIT3`, protein name
  "SIT3, silicic acid transporter-like protein".

The two donors are not equal. The paralog identity of the TpSIT3 donor is stated in
[PMID:27305972 "TpSIT3, NaSIT and PtSIT1 were reconstituted into proteoliposomes preloaded with 6 mM Zn acetate"],
and the same paper qualifies it:
[PMID:27305972 "PtSIT1 and NaSIT showed similar activity, but TpSIT3 gave a modest signal change that was only just discernible above background."]
and [PMID:27305972 "Given the lower activity of TpSIT3 we chose to focus on characterizing the transport kinetics of PtSIT1 and NaSIT."].
So B7T1F4 carries the inference and B8C4N0 is a supporting conspecific donor. (The earlier
PMID:22530967 citation for the paralog claim was wrong: that abstract names no paralog. It is
retained only for the family-level sodium-dependence statement it does make.)

Carry forward to a future THAPS SIT3 review: B8C4N0 is itself a third instance of the
gene-model truncation reported here as a source defect - a 437-residue model that is an exact
*internal* substring of the 565-residue TpSIT3 cDNA protein (GenBank ABB81827), i.e. shortened at
both ends. Reporting it would make the UniProt report cover all three T. pseudonana SITs rather
than two.
- Not added: biomineral tissue/cell-wall biogenesis processes. SIT1 supplies substrate to
  silica-deposition vesicles but does not perform silica polymerization; knockdown lowering PDMPO
  incorporation is a necessity argument, not participation.

## CMMMech claims (data/records/silicon.yaml)

- functional_role for B8C2V9: "High-affinity sodium/silicic acid symporter SIT1 ... mediating
  active uptake ... across the diatom plasma membrane under silicon-limiting conditions". Plasma
  membrane location and a low-Si uptake contribution are supported for SIT1 (the latter only jointly
  with SIT2). "Sodium/silicic acid symporter" and "high-affinity" are family-level inferences
  (PtSIT1, NaSIT, TpSIT3, CfSIT1); TpSIT1 sodium coupling and affinity have not been measured.
  The record's own evidence wording ("supports: partial") is appropriately cautious.
- The CMMMech protein example points to the N-terminally truncated gene-model entry B8C2V9 rather
  than the full-length cDNA entry Q0QVM8; worth noting if CMMMech wants the experimentally
  characterized sequence.
