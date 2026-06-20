# uvrA (UvrABC system protein A) — Pseudomonas putida KT2440 (PSEPK)

UniProt: Q88QK7 (UVRA_PSEPK); Gene: uvrA / PP_0483; 944 aa; Reviewed/Swiss-Prot.
Evidence level: PE 3 (Inferred from homology). All GO annotations are IEA derived from
HAMAP-Rule MF_00205, UniRule UR000101266, ARBA, and InterPro. No P. putida-specific
experimental UvrA publication is cached; the only reference is the genome paper
[PMID:12534463], which does not contain UvrA functional assertions. Supporting text is
therefore drawn from the UniProt record and homology-based family knowledge.

## FUNCTION
- UvrA is the DNA-damage-recognition subunit of the bacterial nucleotide excision repair
  (NER) UvrABC system. [UniProt "The UvrABC repair system catalyzes the recognition and processing of DNA lesions."]
- It is an ATP-dependent DNA-binding protein. [UniProt "UvrA is an ATPase and a DNA-binding protein."]
- A UvrA2UvrB2 damage-recognition complex scans duplex DNA for helix-distorting
  abnormalities; once UvrB verifies a lesion, the UvrA subunits dissociate, handing off to
  UvrB/UvrC for incision. [UniProt "A damage recognition complex composed of 2 UvrA and 2 UvrB subunits scans DNA for abnormalities. When the presence of a lesion has been verified by UvrB, the UvrA molecules dissociate."]
- ATP binding and hydrolysis are mechanistically central: UvrA contains two ABC-ATPase
  (P-loop NTPase) nucleotide-binding domains whose ATP binding/hydrolysis cycle drives
  damage recognition and loading of UvrB. The protein contains two tandem ABC transporter
  domains (residues 309-586 and 606-936) and two ATP-binding P-loops (residues 31-38 and
  639-646). [UniProt "DOMAIN          309..586 ... ABC transporter 1"] [UniProt "BINDING         31..38 ... /ligand=\"ATP\""]

## SUBUNIT
- Forms a heterotetramer (UvrA2UvrB2) with UvrB during the search for lesions.
  [UniProt "Forms a heterotetramer with UvrB during the search for lesions."]

## COFACTOR / METAL
- Binds zinc via two C4-type zinc fingers (residues 253-280 and 739-765), structural
  metal sites typical of the UvrA family. [UniProt "ZN_FING         253..280 ... C4-type"]
  Keywords: Zinc, Zinc-finger, Metal-binding. [UniProt "KW   ... Metal-binding; ... Zinc; Zinc-finger."]

## LOCALIZATION
- Cytoplasmic. [UniProt "SUBCELLULAR LOCATION: Cytoplasm"]

## FAMILY
- Belongs to the ABC transporter superfamily, UvrA family (despite the ABC-transporter
  fold, UvrA is not a membrane transporter). [UniProt "Belongs to the ABC transporter superfamily. UvrA family."]
- HAMAP family MF_00205 (UvrA); TIGRFAM TIGR00630 (uvra); PANTHER PTHR43152.

## Curation reasoning
- Core MF: ATP binding (GO:0005524), ATP hydrolysis activity (GO:0016887), damaged-DNA /
  DNA binding, excinuclease ABC activity (GO:0009381).
- Core BP: nucleotide-excision repair (GO:0006289).
- "DNA repair" (GO:0006281) is a broad parent of NER; "DNA damage response" (GO:0006974)
  is broader still — both over-annotated when GO:0006289 is present.
- "catalytic activity" (GO:0003824) is an uninformative root-level MF — over-annotated when
  ATP hydrolysis activity / excinuclease ABC activity are present.
- "zinc ion binding" (GO:0008270) is supported by the C4 zinc fingers but is a structural
  metal-binding role, non-core relative to the repair functions.
- "DNA binding" (GO:0003677) is a valid generic parent of the damaged-DNA-binding activity
  that UvrA enables; kept but generic.
- ATP binding/hydrolysis: although they are "broad" P-loop NTPase terms, ATP binding and
  hydrolysis are the mechanistic engine of UvrA's ABC-ATPase damage-recognition cycle, so
  they are accepted as core rather than marked over-annotated.
