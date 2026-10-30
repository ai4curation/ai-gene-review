# IPO13 (human, O94829) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: IPO13 is the closest experimentally characterised relative of DROME/cdm
(Q9VEC5). Both are in PANTHER subfamily PTHR12363:SF33 (IMPORTIN-13) and under PAINT
node PTN000270925. This review covers human IPO13 in its own right. No ProtNLM2 output
was consulted.

### Deep research

`just deep-research-falcon human IPO13 --fallback perplexity-lite` failed. Falcon
returned "Edison API request failed: Failed to authenticate" (HTTP 403), and the
perplexity-lite fallback timed out after 600 s. No deep-research file exists. The review
is based on cached primary literature, found via a Europe PMC title search for
"importin 13"/IPO13 and cached with `just fetch-pmid`, and on the UniProt record.

### Evolutionary grounding

- UniProt DR: `PANTHER; PTHR12363:SF33; IMPORTIN-13` and family PTHR12363 (TRANSPORTIN 3
  AND IMPORTIN 13). IPO13 is in the same subfamily as fly cdm. TNPO3 is in the same
  family but a different subfamily, so transportin-3-specific functions (SR-protein
  import) are not transferred.
- The IBA rows come from PTN000270925. IPO13 (O94829) is itself an experimental donor
  for the import process IBA, which reflects its own experimental grounding and is not
  circular.
- The family review (interpro/panther/PTHR12363) leaves the family-wide scope of GO:0005049
  UNRESOLVED. For IPO13 the export activity is experimentally established in human
  (eIF1A), so the IBA is accepted.

### What is experimentally established in human (usable for transfer within SF33)

- **Import receptor (GO:0061608 / GO:0006606).** UBC9 and Y14 import
  [PMID:11447110 "It accounts for nuclear accumulation of the SUMO-1/sentrin-conjugating
  enzyme hUBC9 and mediates import of the RBM8 (Y14) protein"]. PAX6, PAX3 and CRX
  [PMID:15143176 "Ran-dependent import of Pax6 by Kap13 was shown to occur by using a
  digitonin-permeabilized cells assay"]. NF-YB/NF-YC [PMID:15964792]. CHRAC-15/17
  [PMID:19218565]. Glucocorticoid receptor [PMID:16809634]. Myopodin [PMID:17828378].
  ARX [PMID:20148114].
- **Export receptor (GO:0005049 / GO:0006611).** eIF1A [PMID:11447110] and
  [PMID:23435562 "Finally, we demonstrate that Imp13 is able to bind and export eIF1A in
  vivo and that its function is essential."]. EIF4G2 and HMG20A [PMID:27993670].
- **RanGTP binding (GO:0031267).** Human IPO13-RanGTP structure (PDB 2X19,
  PMID:20122403). IPO13-RanGTP-eIF1A structure (PMID:23435562, K_D < 100 nM).
- The Mago-Y14 cargo complex structure in PMID:20122403 is of *Drosophila* Imp13. The
  Mago-Y14 import function in human rests on PMID:11447110 (Y14) and on human cell data
  in PMID:23435562.
- The siRNA viability loss in HeLa cells (PMID:23435562) is a phenotype and is not
  annotated.

### Not annotated (deliberately)

- Eye morphogenesis and coloboma: [PMID:29700284] reports human genetics plus a
  zebrafish morpholino phenotype. This is a downstream organismal phenotype, plausibly
  from reduced import of PAX6-class cargoes, and not participation. No NEW
  term was added.
- Negative regulation of UBC9 autosumoylation (in vitro, PMID:21139563) is a side effect
  of cargo shielding and is not annotated.
- Lung development, glucocorticoid signalling and neuronal differentiation are cargo-level
  consequences and are not annotated as IPO13 processes.

### Annotation decisions (summary)

- ACCEPT: GO:0005049 IBA, GO:0061608 IBA, GO:0006606 (IBA/IDA/IEA), GO:0031267 IEA,
  nucleus IEA, cytoplasm IEA.
- KEEP_AS_NON_CORE: nuclear envelope IBA. It is mechanistically expected for the whole
  family but not demonstrated for IPO13.
- MODIFY: intracellular protein transport -> protein import into nucleus and protein
  export from nucleus. Nuclear export -> protein export from nucleus. Protein binding
  rows with UBC9/MAGOH -> import receptor activity, with EIF1AX -> export receptor
  activity, and with RAN -> small GTPase binding. "Ran GTPase binding" is not a
  separate active term in current GO (OLS search).
- REMOVE: 11 high-throughput Y2H protein binding rows (ALX1, PITX1, PBX4, PAX3-iso,
  PSMA1, HMBOX1, DUX4L9), per the GO:0005515 policy. Several are homeodomain proteins,
  consistent with IPO13's known cargo class, but none has a transport assay.
