# UBP11 (YKR098C / P36026) research notes

*S. cerevisiae* ubiquitin-specific protease 11. An **understudied ("dark") gene**: the
molecular activity is clear (a cysteine-type deubiquitinase), but its physiological
substrate, biological process, non-redundant role, and localization are essentially
unknown. These notes record what is KNOWN vs NOT-KNOWN with provenance.

## Identity and domain architecture (KNOWN)

- UniProt P36026, `UBP11_YEAST`, systematic name **YKR098C**, chromosome XI; 717 aa,
  ~82.7 kDa. RecName "Ubiquitin carboxyl-terminal hydrolase 11"; EC 3.4.19.12
  (thiol-dependent hydrolysis of ubiquitin C-terminal ester/thioester/amide/peptide/
  isopeptide bonds). (`UBP11-uniprot.txt`)
- Belongs to the **peptidase C19 family** (USP / ubiquitin-specific protease); single
  USP catalytic domain spanning residues 298–707 (~410 aa). Two annotated catalytic
  `ACT_SITE` residues: **Cys307 (nucleophile)** and **His649 (proton acceptor)**.
  PROSITE USP signatures PS00972 (USP_1, Cys box), PS00973 (USP_2, His box) and PS50235
  (USP_3 profile) all match. (`UBP11-uniprot.txt`)
- Bioinformatics check (this repo, `UBP11-bioinformatics/RESULTS.md`): the catalytic dyad
  Cys307/His649 is **present and intact** → catalytically competent DUB by domain, not a
  degenerate pseudo-DUB. The catalytic Cys sits in the canonical Cys box (`NPCNTC…`).

## Molecular function: deubiquitinase (KNOWN)

- Ubp11p was assayed directly for deubiquitinating activity. In the synthetic-substrate
  study, yeast Ubps 1p, 2p, 3p, 6p, **11p**, and 15p and Yuh1p were "expressed in
  Escherichia coli" and their catalytic capacities assessed against ubiquitin fusions
  [PMID:10527495 "yeast \nUbps 1p, 2p, 3p, 6p, 11p, and 15p and Yuh1p"]. This is the basis
  of the SGD **IDA** annotation to GO:0004843 (cysteine-type deubiquitinase activity).
  - Nuance on specificity: in that same study, **isopeptidase** activity
    (cleavage of ubiquitin-(εN)-lysine) was "only associated with Yuh1p, Unp,
    Ubp1p, and Ubp2p" [PMID:10527495 "isopeptidase activity \n[ubiquitin-(epsilonN)-lysine cleavage] was only \nassociated with Yuh1p, Unp, \nUbp1p, and Ubp2p"]. UBP11 was NOT in the
    isopeptidase-positive set — i.e., its in vitro activity profile against these
    particular synthetic substrates was limited. This does not negate the deubiquitinase
    MF (it cleaves ubiquitin fusions / linear extensions) but flags that the physiological
    linkage/substrate specificity is undefined.
- Family-level confirmation: of the 17 potential yeast DUB genes, "14 of the 17 Dubs have
  now been shown to have ubiquitin-cleaving activity" including Ubp11p
  [PMID:11076031 "14 of the 17 Dubs have now been shown to have \nubiquitin-cleaving activity"].

## Biological process / phenotype / localization (NOT KNOWN)

- **No specific biological process is established for UBP11.** SGD lists its biological
  process and cellular component as unknown despite the clear enzymatic function
  (`https://www.yeastgenome.org/locus/S000001806`, accessed 2026-07).
- Amerik, Li & Hochstrasser systematically deleted each of the 17 yeast DUB genes:
  "none of the mutants is lethal or strongly growth defective under standard conditions,
  although a number have detectable abnormalities"
  [PMID:11076031 "none of the \nmutants is lethal or strongly growth defective under standard \nconditions"]. So *ubp11Δ* has no strong single-mutant phenotype — the classic
  signature of a redundant / condition-specific DUB.
- The GOA localization terms (nucleus GO:0005634, cytosol GO:0005829) are **IBA only**
  (phylogenetic propagation from the USP family), not experimentally determined for
  UBP11 itself. SGD marks localization unknown.
- GOA also carries an SGD **ND** (no data) row for both cellular_component and
  biological_process, which correctly reflects the absence of experimental evidence.

## Paralogy and redundancy (KNOWN structure, UNKNOWN functional division)

- UBP11 has a paralog, **UBP7 (YIL156W)**, that arose from the whole-genome duplication
  (WGD); both single nulls are viable (SGD). This is the most likely explanation for the
  lack of a *ubp11Δ* phenotype, but the functional division of labour between UBP11 and
  UBP7 (and vs the broader 16-17 member yeast UBP family) has **not** been dissected.
- Family context: the yeast genome encodes ~16-17 UBPs; they are "largely divergent in
  primary sequence except in two short motifs, the Cys and His boxes"; and "the cellular
  functions of most of the UBPs have not yet been discovered" (family reviews /
  Amerik et al. 2000, PMID:11076031).

## Candidate pathway lead (WEAK / genetic, not in GOA) — Rsp5 endosomal network

- The falcon deep research surfaces a candidate-pathway lead worth recording but NOT
  strong enough to annotate: Tardiff et al. 2013 (Science, doi:10.1126/science.1245321,
  "Yeast reveal a druggable Rsp5/Nedd4 network that ameliorates α-synuclein toxicity")
  place **UBP7 and UBP11** in an **Rsp5-centered ubiquitin-dependent endosomal transport
  network** as "two proteins that can deubiquitinate Rsp5 substrates," where
  **overexpression** of UBP7/UBP11 partially compromised NAB2-mediated rescue of
  α-synuclein toxicity.
- Why this stays a *lead*, not an annotation: the same study found that **deletion of
  UBP7 and UBP11, singly or as the ubp7Δ ubp11Δ double, had no effect** on NAB2 rescue,
  i.e. UBP11 is not the central target and any role is redundant/context-dependent. This
  is genetic/chemical-genetic association, no direct in vivo UBP11 substrate, and the
  paper is not in our publications cache (would need fetching + verbatim-quote checking
  before any YAML citation). So the review keeps the conservative "BP-dark, substrate
  unknown" stance; Rsp5/endosomal trafficking is the leading *hypothesis* to test, and is
  reflected in the knowledge_gaps resolution (paralog-aware ubiquitylome of the double
  mutant). Paralog UBP7 has been shown directly to deubiquitinate the endocytic factor
  Ede1 (Weinberg & Drubin 2014), which is consistent with, but does not itself
  demonstrate, an equivalent UBP11 role.

## Zinc ion binding annotation (weak / computational)

- GOA has GO:0008270 (zinc ion binding), evidence **RCA**, from PMID:30358795 (Wang et al.,
  yeast zinc proteome). This is a proteome-wide bioinformatic prediction of zinc-binding
  proteins (domain + motif search), NOT a direct measurement of zinc binding by UBP11.
  Many USP-family DUBs contain a zinc-finger/Zn-ribbon subdomain, so the prediction is
  plausible, but it is a computational reconstruction (RCA), not experimental. The UniProt
  record does NOT annotate a zinc-binding site in UBP11.

## Summary: what is the gap?

- **MF known** (competent cysteine-type deubiquitinase, by domain + in vitro assay).
- **BP dark**: no physiological process; no in vivo substrate; no non-redundant role
  distinguished from paralog UBP7 or the wider UBP family.
- **CC uncertain**: nucleus/cytosol are IBA propagations, not UBP11-specific data.
- This is a **BIOLOGY gap (primary) + CURATION note**: the deubiquitinase MF is real but
  the "for what?" is genuinely undetermined, and a single-gene deletion has no strong
  phenotype because of paralog redundancy.

## References used

- PMID:10527495 — Layfield et al. 1999, Anal Biochem. Synthetic ubiquitin substrates;
  Ubp11p among yeast DUBs assayed. (abstract only in cache)
- PMID:11076031 — Amerik, Li & Hochstrasser 2000, Biol Chem. Systematic deletion of all
  17 yeast DUB genes; none lethal/strongly growth-defective; 14/17 have Ub-cleaving
  activity. (abstract only in cache)
- PMID:30358795 — Wang et al. 2018, Metallomics. Yeast zinc proteome; source of the RCA
  zinc-ion-binding annotation. (abstract only in cache)
- SGD locus page S000001806 (UBP11) — paralog UBP7/WGD; BP & CC unknown.
- `file:yeast/UBP11/UBP11-bioinformatics/RESULTS.md` — catalytic-dyad integrity check.
