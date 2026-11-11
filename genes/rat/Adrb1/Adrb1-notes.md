# Adrb1 (rat) review notes

## Setup
- `just fetch-gene rat Adrb1` resolved P18090 (Swiss-Prot, RGD:2059, GeneID 24925). 77 GOA rows.
- No deep-research API keys; literature synthesis is in `Adrb1-deep-research-manual.md`.
- Extra papers cached for donor checks: PMID:1695899 (rat cloning), 8693001, 10358009, 12161655,
  15066288, 11171998, 12529373, 11526121, 21540189, 10595521, 21321602, 25083013, 31473062.

## Key decisions
- Core: Gs-coupled beta1-adrenergic receptor activity (GO:0004940) at the plasma membrane, acting in
  GO:0071880 adenylate cyclase-activating adrenergic receptor signaling; physiological core output is
  sympathetic positive chronotropy/inotropy (GO:0001996, GO:0001997) [PMID:8693001; PMID:10358009;
  PMID:19133992].
- PDZ-ligand interactions (MAGI3, RAPGEF2, DLG4, GOPC) are well supported; GO:0005515 IPI with
  Magi3 MODIFIED to GO:0030165 PDZ domain binding [PMID:16316992].
- General parents (GPCR activity, adrenergic receptor activity, beta-adrenergic receptor activity,
  GPCR signaling, AC-activating GPCR signaling, membrane, positive regulation of heart contraction,
  positive regulation of apoptotic process, regulation of calcium ion transport, positive regulation of
  developmental growth) MODIFIED to the specific descendants the gene already carries.
- `regulation of cardiac muscle cell contraction` rows MODIFIED to `positive regulation of cardiac
  muscle cell contraction` (GO:0106134): beta1 stimulation increases shortening [PMID:19525381;
  PMID:22216755].
- `positive regulation of AC-activating GPCR signaling` (IMP, PMID:18202135) MODIFIED to GO:0071880:
  the paper shows the receptor itself is coupled to adenylyl cyclase (constitutively active), it does
  not regulate another receptor's pathway.
- `glycogen catabolic process` IDA MODIFIED to `positive regulation of glycogen catabolic process`.

## Over-annotations / expert flags
- GO:0007266 Rho signal transduction and GO:0045986 negative regulation of smooth muscle contraction
  (PMID:18306009): effect of 700 microM landiolol; nothing in abstract ties it to beta1 (tracheal
  relaxation is classically beta2). MARK_AS_OVER_ANNOTATED.
- GO:0035811 negative regulation of urine volume (IDA PMID:7912752 + ARBA IEA): abstract attributes
  antidiuresis predominantly to beta2. MARK_AS_OVER_ANNOTATED.
- GO:0060080 inhibitory postsynaptic potential (PMID:18262504): beta1 acts presynaptically to restrain
  GABA release; it is not a component of the IPSP. MARK_AS_OVER_ANNOTATED. The derived postsynapse
  IEA was kept non-core because postsynaptic beta1 (PSD-95/MAGI-2 scaffolding) is independently
  plausible [PMID:11526121].
- GO:0040015 / GO:0050873 from triple-KO mice (PMID:12387862): cannot be apportioned to beta1.
- GO:1905665 IDA PMID:11408541: abstract is a beta2 study; beta1 antagonist did not modify zinterol
  effect. Function is true for beta1 from PMID:12514203 and PMID:19133992, so kept as non-core and
  flagged.

## Source defect
- GO:0045187 regulation of circadian sleep/wake cycle, sleep: the human (P08588) and mouse (P34971)
  IMP rows assigned by UniProt (2019-09-19) cite PMID:25083013, a BHLHE41 short-sleep paper that
  never mentions adrenergic receptors. The ADRB1 short-sleep paper is PMID:31473062 (Shi et al. 2019
  Neuron), which UniProt P08588 itself cites in CC FUNCTION. Recorded as WRONG_REFERENCE (PROBABLE)
  on the rat ISS row derived from P08588.

## Key paper PMID:21177871
- Christian et al. 2011, AKAP-PKA disruptor FMP-API-1 in rat cardiomyocytes. Uses isoproterenol
  (non-selective beta agonist) to drive Gs/AC/PKA and shows AKAP-PKA anchoring shapes
  beta-adrenergic cAMP compartmentation and contractility. Does not assay Adrb1 specifically; it
  informs downstream compartmentalized cAMP/PKA signaling. Relevance MEDIUM.

## 2026-10-28 review-fix pass

- Removed supported_by self-citations of the gene's own -deep-research-manual.md where a primary citation in the same block already supports the row (the reviewer's own conclusion is not independent evidence). The validator now warns that no annotation cites the deep-research file; that warning is accepted deliberately, which sets the status to DRAFT.
