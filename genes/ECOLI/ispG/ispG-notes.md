# ispG (gcpE, b2515; UniProtKB:P62620) notes

## Identity and reaction

- IspG (GcpE) catalyses step 5 of the MEP pathway: reductive ring opening of
  2-C-methyl-D-erythritol 2,4-cyclodiphosphate (MEcPP) to (E)-4-hydroxy-3-methylbut-2-enyl
  diphosphate (HMBPP). [PMID:16268586 "The IspG protein is known to catalyze the transformation
  of 2-C-methyl-d-erythritol 2,4-cyclodiphosphate into
  1-hydroxy-2-methyl-2-(E)-butenyl 4-diphosphate"]
- In vivo genetic placement in the MEP pathway: deletion is lethal unless the cells can use
  mevalonate. [PMID:11274098 "were viable only if the medium was supplemented with mevalonate or the cells
  were complemented with an episomal copy of gcpE"]; [PMID:11163766 "Our data demonstrate that the gcpE gene is
  essential for the MEP pathway in Escherichia coli"]
- Product identified in engineered cells by 13C NMR. [PMID:11752431 "The additional expression of the gcpE gene afforded
  1-hydroxy-2-methyl-2-(E)-butenyl 4-diphosphate as an intermediate"]

## Cofactor and electron donor

- [4Fe-4S] protein (title of PMID:12434382); purified anaerobic enzyme contains
  ~2.4 Fe and 4.4 S2- per subunit; the three conserved Cys are required. [PMID:16268586 "The protein contained 2.4 iron ions and 4.4 sulfide ions
  per subunit."]
- Electron donor: the physiological and best in vitro reductant is flavodoxin (FldA) with
  flavodoxin reductase and NADPH. [PMID:16268586 "With a mixture of flavodoxin, flavodoxin reductase, and NADPH as the
  reducing agent"]; dithionite does not work, deazaflavin is an artefactual donor.
- fldA is essential because of the MEP pathway; fldA disruption lowers HMBPP.
  [PMID:15978585 "Disruption of fldA
  abrogated mevalonate-independent growth and dramatically decreased HMBPP levels."]
- MBP-IspG fusion was inactive without auxiliary proteins from cell extract.
  [PMID:12571359 "This indicates that auxiliary proteins are required, probably as
  shuttles for redox equivalents."]

## GO term issue: ferredoxin vs flavodoxin

- GO:0046429 is defined with ferredoxin as the electron acceptor (RHEA:26119, EC 1.17.7.1),
  GO:0141197 with flavodoxin (RHEA:43604, EC 1.17.7.3). They are siblings under GO:0052592;
  neither is a descendant of the other (QuickGO ancestors checked 2026-11-13).
- Three GOA rows carry GO:0046429 on P62620: EcoCyc IDA (PMID:16268586, 2007, before
  GO:0141197 existed), PAINT IBA from PTN000765215 (Bacteria node, seeds AT5G60600 and
  P62620, 2017), and a UniProt combined IEA from InterPro IPR004588/IPR016425 and HAMAP
  rule UR000001261 (MF_00159). InterPro API (2026-11-13) shows both IPR004588 and
  IPR016425 map to GO:0046429; the UniRule for MF_00159 lists GO:0046429 while the HAMAP
  rule's own reaction is the flavodoxin reaction (EC 1.17.7.3).
- Decision: MODIFY all three GO:0046429 rows to GO:0141197 (lateral correction of the
  electron-carrier specificity; the reaction on the C5 substrate is correct), with source
  defects on EcoCyc, GO_Central (PAINT node placement) and InterPro/UniProt mappings.
  The plant enzyme (AT5G60600, plastid) is ferredoxin dependent, so GO:0046429 belongs on
  the plastid clade (PTN000765210) rather than the Bacteria root node.
- Note that GO lacks a carrier-agnostic grouping term "HMBPP synthase activity"; the
  nearest shared parent GO:0052592 is uninformative.

## Other rows

- Two IPI protein binding rows with EcpB (P77188) from high-throughput screens
  (PMID:16606699, PMID:24561554); no functional inference; removed per policy.
- Cytosol: proteomics of the cytosolic fraction (PMID:15911532, PMID:18304323); soluble
  protein without TM segments.
- Literature search for this review: cached PMIDs above plus 11752431, 12859972, 15978585
  fetched with the repo tool.
