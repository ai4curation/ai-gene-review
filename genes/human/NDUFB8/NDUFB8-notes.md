# NDUFB8 (Complex I-ASHI) — review notes

UniProt: O95169 (NDUB8_HUMAN). HGNC:7703. Gene ID 4714. 186 aa precursor.
All UniProt quotes below are from `file:human/NDUFB8/NDUFB8-uniprot.txt` (do not edit that file).

## Identity / summary

- Names: "NADH dehydrogenase [ubiquinone] 1 beta subcomplex subunit 8, mitochondrial";
  AltName "Complex I-ASHI" (CI-ASHI); "NADH-ubiquinone oxidoreductase ASHI subunit"
  [file:human/NDUFB8/NDUFB8-uniprot.txt lines 6-9].
- Belongs to the complex I NDUFB8 subunit family
  [file:human/NDUFB8/NDUFB8-uniprot.txt "Belongs to the complex I NDUFB8 subunit family."].

## Function / role (the central point for curation)

- **Accessory (supernumerary), non-catalytic subunit of Complex I.** UniProt FUNCTION:
  "Accessory subunit of the mitochondrial membrane respiratory / chain NADH dehydrogenase
  (Complex I), that is believed not to be / involved in catalysis." The catalytic activity
  belongs to the whole complex, not this subunit
  [file:human/NDUFB8/NDUFB8-uniprot.txt lines 187-189; verbatim single-line quote:
  "chain NADH dehydrogenase (Complex I), that is believed not to be"].
  FUNCTION evidence is ECO:0000269|PubMed:27626371.
- Complex I "functions in the transfer of electrons from NADH to the respiratory chain. The
  immediate electron acceptor for the enzyme is believed to be ubiquinone"
  [file:human/NDUFB8/NDUFB8-uniprot.txt line 190 "from NADH to the respiratory chain. The immediate electron acceptor for"].
- **SUBUNIT:** "Complex I is composed of 45 different subunits."
  [file:human/NDUFB8/NDUFB8-uniprot.txt line 192], evidence PubMed:12611891, PubMed:27626371.

Curation consequence: honest MF for this subunit is **GO:0005198 structural molecule activity**,
*contributing to* complex-level **GO:0008137 NADH dehydrogenase (ubiquinone) activity**
(contributes_to, NOT direct enables). The GOA `enables GO:0008137` (NAS, PMID:9878551) is an
over-annotation → MARK_AS_OVER_ANNOTATED. Likewise the derived `proton transmembrane transport`
(GO:1902600, IEA GO_REF:0000108, logically inferred from GO:0008137) → MARK_AS_OVER_ANNOTATED.

## Localization

- SUBCELLULAR LOCATION: "Mitochondrion inner membrane"; "Single-pass membrane protein";
  "Matrix side" [file:human/NDUFB8/NDUFB8-uniprot.txt lines 194-196].
- TRANSMEM 133..153 (Helical) [line 368]; TRANSIT 1..28 Mitochondrion presequence [line 361];
  mature CHAIN 29..186 [line 364].
- So: core location = mitochondrial inner membrane (GO:0005743). Broad `mitochondrion`
  (GO:0005739; HPA IDA, InterPro IEA, HTP PMID:34800366) is correct but non-core.
- `mitochondrial matrix` (GO:0005759, TAS Reactome R-HSA-8986181) comes from the protein-import
  step (PITRM1 presequence proteolysis) — reflects the transient import intermediate, not the
  steady-state location of the mature membrane protein → MARK_AS_OVER_ANNOTATED.

## Complex membership (all point to GO:0045271 respiratory chain complex I — core)

- IDA PMID:12611891 (Murray et al. 2003): immunopurified human Complex I; MS identified
  "homologues of 42 polypeptides detected so far in the more extensively studied" bovine complex,
  including ASHI/NDUFB8 [publications/PMID_12611891.md]. Abstract-only cache.
- IDA PMID:27626371 (Stroud et al. 2016, Nature): systematic KO of the 45 subunits;
  "required for assembly of a functional complex and 1 subunit is essential for" cell viability;
  "of each subunit affects the stability of other subunits residing in the same" structural module
  [publications/PMID_27626371.md]. This is the UniProt FUNCTION reference. Abstract-only cache.
- IDA + IPI PMID:28844695 (Guo et al. 2017, Cell): cryo-EM megacomplex I2III2IV2;
  "reveals the precise assignment of individual subunits of" human CI and CIII
  [publications/PMID_28844695.md]. Abstract-only cache. Supports ComplexPortal membership +
  inner-membrane localization.
- NAS PMID:9878551 (Loeffen et al. 1998): cDNA characterization of nuclear-encoded CI subunits;
  Complex I "located in the inner mitochondrial membrane"; main function "transport of electrons
  from NADH to ubiquinone, which is" "accompanied by translocation of protons from the
  mitochondrial matrix to the" intermembrane space [publications/PMID_9878551.md].
- IBA GO_REF:0000033 and IEA GO_REF:0000107 (Ensembl Compara from mouse ortholog) — consistent.
- **IMP PMID:19393246** (Oswald et al. 2009, "Knockdown of human COX17 affects assembly ... of
  cytochrome c oxidase"): the cached abstract is about COX17 / Complex IV supercomplexes, NOT
  Complex I subunit composition [publications/PMID_19393246.md]. This looks like a possibly
  mis-sourced citation for NDUFB8 CI membership, BUT it is an experimental (IMP) annotation whose
  full text I have not read, and the term (complex I) is correct biology independently established
  above. Per project policy → ACCEPT (do not REMOVE an experimental annotation on an abstract-only
  cache); flagged in reference_review as UNVERIFIED / LOW relevance.

## Process annotations

- GO:0006120 mitochondrial electron transport, NADH to ubiquinone (IEA GO_REF:0000002; NAS
  PMID:9878551) — subunit-appropriate core BP → ACCEPT.
- GO:0032981 mitochondrial respiratory chain complex I assembly — added to core_functions
  directly_involved_in (NDUFB8 is required for assembly; Stroud 2016). Not in GOA (warning only).
- GO:0009060 aerobic respiration (NAS PMID:30030361) and GO:0042776 PMF-driven mitochondrial ATP
  synthesis (NAS PMID:30030361) — true at whole-OXPHOS/complex level, downstream/broad → KEEP_AS_NON_CORE.
  PMID:30030361 (Signes & Fernandez-Vizarra 2018 review): human complexes = "core proteins,
  performing the catalytic activities" + "of 'supernumerary' subunits that play essential roles in
  assembly, regulation" and stability [publications/PMID_30030361.md]. Abstract-only cache.

## Disease

- MC1DN32 (Mitochondrial complex I deficiency, nuclear type 32; MIM:618252), autosomal recessive,
  Leigh-like encephalomyopathy [file:human/NDUFB8/NDUFB8-uniprot.txt lines 205-216;
  ECO:0000269|PubMed:29429571 (Piekutowska-Abramczuk et al. 2018 AJHG; not cached locally)].
  Variants: His-62, Gln-76, exon-4-skip del 105-156, Trp-144 [lines 383-406].

## Core function decision

- molecular_function: GO:0005198 structural molecule activity
- contributes_to_molecular_function: GO:0008137 NADH dehydrogenase (ubiquinone) activity
- directly_involved_in: GO:0006120, GO:0032981
- locations: GO:0005743 (mitochondrial inner membrane)
- in_complex: GO:0045271 (respiratory chain complex I)

## Publications cache status
Present locally: PMID_12611891, 27626371, 19393246, 28844695, 30030361, 34800366, 9878551.
Missing: PMID_21269460 (proteome, not cited in GOA rows reviewed), PMID_29429571 (disease; MC1DN32).
Most cached abstracts are abstract-only (full_text_available: false) except PMID_34800366.
