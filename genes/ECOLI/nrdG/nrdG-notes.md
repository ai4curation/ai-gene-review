# nrdG (P0A9N8) notes

Part of the RADICAL_SAM project (projects/RADICAL_SAM.md), Phase 2 E. coli K-12.

## Literature sources

No deep-research file is available for this gene: the falcon provider fails authentication
(403) and asta returned nothing useful in Phase 1, so deep research was not run. These notes are
built from cached publications (`publications/PMID_*.md`, all abstract-only for the NrdG
biochemistry papers), the UniProt record, PubMed and QuickGO.

## Identity and family

- Anaerobic ribonucleoside-triphosphate reductase-activating protein (NrdG, 154 aa), the small
  ("beta", "activase", formerly "dA1") component of the class III anaerobic ribonucleotide
  reductase system. EC 1.97.1.-. Organic radical-activating enzyme family of the radical SAM
  superfamily (IPR034457, IPR012837 NrdG, TIGR02491, PTHR30352:SF2, SFLDF00299).
  [file:ECOLI/nrdG/nrdG-uniprot.txt "Activation of anaerobic ribonucleoside-triphosphate reductase under anaerobic conditions by generation of an organic free radical, using S-adenosylmethionine and reduced flavodoxin as cosubstrates to produce 5'-deoxy-adenosine."]
- Paralogs in E. coli K-12: PflA (PFL-AE, activates PflB), PflC/YbiY/YjjW (activases of
  the other glycyl radical enzymes). These are reviewed separately.

## Activity (the activase reaction)

- Discovery: the ORF downstream of nrdD encodes a protein needed for, and tightly bound to,
  the glycyl radical of the anaerobic reductase.
  [PMID:7852304 "The protein corresponding to this open reading frame is required for the generation of the glycyl radical of the anaerobic reductase and binds tightly to the reductase."]
- Early fractionation: NrdD (dA3) is the reductase, NrdG (dA1) auxiliary.
  [PMID:1460049 "dA3 is the actual ribonucleoside triphosphate reductase; dA1 has an auxiliary function."]
- NrdG binds SAM (Kd 10 uM, 1:1) and its Fe-S centre reductively cleaves it, giving methionine
  and the NrdD glycyl radical.
  [PMID:9305874 "Here, we demonstrate that AdoMet is directly reduced by the Fe-S center of beta2 during the activation of the enzyme, resulting in methionine and glycyl radical formation."]
  [PMID:9305874 "Direct binding experiments showed that AdoMet binds to beta2 with a Kd of 10 microM and a 1:1 stoichiometry."]
- NrdG is catalytic: one NrdG can activate several NrdD.
  [PMID:10531327 "protein beta has the potential to activate several molecules of protein alpha, suggesting that protein beta is an activating enzyme rather than a component of an alpha(2)beta(2) complex as previously claimed."]
- Electron donor is reduced flavodoxin.
  [PMID:10821845 "Its function is to mediate electron transfer from reduced flavodoxin to S-adenosylmethionine, required for the introduction of a glycyl radical in the large component, named protein alpha, which then becomes active for the reduction of ribonucleotides."]
- Radical site on NrdD is Gly681. [PMID:8621608 "with a stable, oxygen-sensitive radical located at Gly-681 of the 80-kDa polypeptide chain"]

## Cofactor

- One [4Fe-4S] per polypeptide, with 2+ and 1+ states; O2-labile, decays to [2Fe-2S].
  [PMID:10531327 "Protein beta can assemble one [4Fe-4S] center per polypeptide"]
- Three cysteines of the CXXXCXXC motif ligate the cluster; the fourth site is SAM.
  [PMID:10821845 "By site-directed mutagenesis we demonstrate that the three cysteines of the conserved CXXXCXXC sequence are involved in iron chelation."]
- The Fe-S signal first attributed to the reductase (PMID:8381402) came from co-purifying NrdG.
  [PMID:8621608 "A degraded form of this cluster may have been responsible for an EPR signal observed earlier in preparations of the large 160-kDa subunit that suggested the presence of a 3Fe-4S cluster in the reductase."]

## Complex

- NrdD and NrdG form a tight 1:1 complex (alpha2beta2).
  [PMID:8621608 "The large and the small proteins form a tight complex."]
- Tamarit 1999 argues NrdG is a catalytic activase rather than an obligate subunit (above).
  ComplexPortal CPX-3821 names the assembly the "nrdDG class III anaerobic ribonucleotide
  reductase activation complex".

## Physiology

- nrdG knockouts cannot grow under strict anaerobiosis.
  [PMID:8954104 "We now show that knock-out mutants of either nrdD or nrdG cannot grow during strict anaerobiosis, achieved by inclusion of sodium sulfide in the medium."]
  This is necessity evidence: NrdD performs the ribonucleotide reduction; NrdG installs the
  glycyl radical cofactor on NrdD and does no step of the NTP to dNTP conversion itself.

## GO term landscape (QuickGO, checked 2026-10-19)

- GO:0043364 glycyl-radical enzyme activating activity has only two children: GO:0043365
  [formate-C-acetyltransferase]-activating enzyme activity (PflA, EC 1.97.1.4) and GO:0140111
  [choline trimethylamine-lyase]-activating enzyme activity. No NrdG-specific term exists.
- GO has no "glycyl radical formation" process term. The modification is captured by
  GO:0018201 peptidyl-glycine modification and GO:0051604 protein maturation, both of which
  PAINT places on the PflA node (PTN002018048) and which PflA carries by IDA.
- GO:0004748 (ribonucleoside-diphosphate reductase, thioredoxin) is the class I/II RNR
  activity; the class III enzyme is a ribonucleoside-triphosphate reductase.
  [PMID:1460049 "an oxygen-sensitive ribonucleoside triphosphate reductase system, different from the aerobic ribonucleoside diphosphate reductase (EC 1.17.4.1)"]
- IPR012837 (NrdG) InterPro2GO maps to GO:0043365 (PFL activase): wrong substrate for NrdG.

## Decisions

- MF core: GO:0043364 (ACCEPT; most specific available) + GO:0051539 + NEW GO:1904047.
- BP: NEW GO:0018201 and GO:0051604 (the activase catalyses the modification; matches PflA).
- Downstream deoxyribonucleotide processes: upstream necessity, not participation;
  MARK_AS_OVER_ANNOTATED. Same pattern to apply to PflA (no fermentation terms) and paralogs.
