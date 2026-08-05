# MAGT1 (Q9H0U3) review notes

## Summary of gene function

MAGT1 ("magnesium transporter 1") is now established as an **endoplasmic-reticulum
membrane, thioredoxin-like oxidoreductase accessory subunit of the STT3B-containing
oligosaccharyltransferase complex (OST-B)**. It is one of two mutually exclusive
STT3B-specific accessory subunits (MAGT1 or its paralog TUSC3) that carry a lumenal
thioredoxin fold with a redox-active CXXC (specifically CVVC) motif. The name
"magnesium transporter" is historical; the OST-B oxidoreductase role is the
best-supported molecular function, and the Mg2+-transport role is secondary/contested.

- UniProt RecName is "Dolichyl-diphosphooligosaccharide--protein glycosyltransferase
  subunit MAGT1" [file:human/MAGT1/MAGT1-uniprot.txt, "RecName: Full=Dolichyl-diphosphooligosaccharide--protein glycosyltransferase subunit MAGT1"].
- UniProt FUNCTION: "Accessory component of the STT3B-containing form of the N-
  oligosaccharyl transferase (OST) complex which catalyzes the transfer of a high
  mannose oligosaccharide ..." and "Specifically required for the glycosylation of a
  subset of acceptor sites that are near cysteine residues; in this function seems to
  act redundantly with TUSC3. In its oxidized form proposed to form transient mixed
  disulfides with a glycoprotein substrate to facilitate access of STT3B to the
  unmodified acceptor site." [file:human/MAGT1/MAGT1-uniprot.txt].
- UniProt: "Could indirectly play a role in Mg(2+) transport in epithelial cells
  (Probable)." — i.e. Mg2+ role is downgraded to indirect/probable
  [file:human/MAGT1/MAGT1-uniprot.txt].
- SIMILARITY: "Belongs to the OST3/OST6 family." [file:human/MAGT1/MAGT1-uniprot.txt].
- Domain features: lumenal Thioredoxin domain (47..175) with redox-active DISULFID
  87..90 (CVVC active-site), signal peptide 1..29, four transmembrane spans
  [file:human/MAGT1/MAGT1-uniprot.txt].

## Molecular function / mechanism

- MAGT1 is a subunit of the STT3B (post-translocational) OST isoform, not STT3A
  [PMID:25135935 "MagT1, an ER-localized thioredoxin homologue, is a subunit of the STT3B
  isoform of the oligosaccharyltransferase (OST)"].
- The lumenal active-site CVVC (a thioredoxin CXXC-type) motif is required for
  glycosylation of STT3B-dependent acceptor sites, including sequons bracketed by
  disulfides or containing an internal Cys (NCT/S) [PMID:25135935 "Mutants that lacked
  both active site cysteine residues (e.g., MagT1 m1) were not able to fully restore
  glycosylation"; "the CXXC motif is necessary for MagT1 and TUSC3 activity"]. UniProt
  MUTAGEN C87S / C90S: "Reduces N-glycosylation of cysteine-proximal acceptor sites"
  [file:human/MAGT1/MAGT1-uniprot.txt].
- The predominant in-vivo form is oxidized; MAGT1 forms transient mixed disulfides with
  substrate glycoproteins to delay disulfide bond formation until STT3B glycosylates the
  acceptor site [PMID:25135935 "The predominant form of MagT1 in vivo is oxidized";
  "MagT1 can form a transient mixed disulfide with a free thiol in a glycoprotein
  substrate, thereby delaying disulfide bond formation until STT3B glycosylates the
  acceptor site"].
- MAGT1 also has oxidoreductase-independent functions (substrate recognition) within
  OST-B [PMID:26864433 "the oxidoreductase subunits are also required for glycosylation
  of the extreme C-terminal sequons in a SHBG derivative that lacks the C-terminal
  disulfide5, suggesting that MagT1 or TUSC3 are needed for substrate recognition"].
- Cryo-EM: MAGT1 is a distinct subunit of OST-B; STT3B makes contacts to MAGT1
  [PMID:31831667 "structural differences in the catalytic subunits STT3A and STT3B
  facilitate contacts to distinct OST subunits, DC2 in OST-A and MAGT1 in OST-B"].
- OST-B / STT3B redundancy: MAGT1 and TUSC3 are functionally interchangeable; loss of
  MAGT1 up-regulates TUSC3 as a compensatory mechanism [PMID:26864433; PMID:31036665
  "MAGT1 deficiency is associated with an enhanced expression of TUSC3"].

## Localization

- ER resident: MAGT1 colocalizes with calreticulin (ER lumenal lectin), NOT with the
  plasma-membrane Na+K+-ATPase [PMID:25135935 "MagT1 colocalizes with calreticulin, a
  lumenal lectin in the RER"; "Colocalization of MagT1-V5 and calreticulin confirmed
  that MagT1 is an ER resident protein"]. UniProt SUBCELLULAR LOCATION lists both
  Endoplasmic reticulum membrane and Cell membrane (the latter from the older Mg2+
  studies) [file:human/MAGT1/MAGT1-uniprot.txt].
- Plasma-membrane localization (GO:0005886) comes from the earlier Mg2+-transport work
  (Zhou & Clapham 2009; Goytain & Quamme 2005). Gilmore lab surface-biotinylation shows
  very low cell-surface reactivity, consistent with an intracellular (ER) pool
  [PMID:25135935 full text, Fig 1A]. Treat plasma-membrane annotations as non-core.

## Magnesium transport (secondary / contested)

- Original description as a Mg2+ transporter/channel: Goytain & Quamme 2005
  (PMID:15804357, not cached; cited in UniProt). Zhou & Clapham 2009 (PMID:19717468)
  showed MagT1/TUSC3 knockdown lowers intracellular Mg2+ and morpholino knockdown arrests
  zebrafish development [PMID:19717468 "Knockdown of either MagT1 or TUSC3 protein
  significantly lowers the" ...]. UniProt now frames this as an indirect/probable role
  and RecName no longer uses "magnesium transporter" as the primary name.
- The prevailing interpretation (Gilmore lab; Matsuda-Lennikov 2019, PMID:31337704) is
  that the Mg2+ phenotype is downstream of a glycosylation defect (e.g. hypoglycosylation
  of Mg2+-handling and immune glycoproteins such as NKG2D/CD28), not a direct
  channel/transporter activity. Keep Mg2+-transport experimental annotations as
  KEEP_AS_NON_CORE (do not remove experimental IMP/IDA); mark IEA MF Mg2+-transporter
  and IBA Mg2+-transport as over-annotation of the core function.

## Disease

- XMEN (X-linked immunodeficiency with Mg defect, EBV infection, neoplasia)
  [MIM:300853]; loss-of-function truncating variants [file:human/MAGT1/MAGT1-uniprot.txt].
- MAGT1-CDG / CDG1CC [MIM:301031]: congenital disorder of glycosylation with
  hypoglycosylated serum transferrin; STT3B-dependent post-translational glycosylation is
  dysfunctional in patients [PMID:31036665 "different substrates, such as GLUT1 and SHBG,
  demonstrating that the posttranslational glycosylation carried out by the STT3B complex
  is dysfunctional in all three patients"].
- X-linked intellectual disability (V311G): originally proposed (PMID:18455129) but role
  is now questioned; UniProt CAUTION: "its pathological role is questionable
  (PubMed:23871722)" [file:human/MAGT1/MAGT1-uniprot.txt]. The `cognition` (GO:0050890)
  IMP annotation rests on this contested variant.

## Curation decisions (high level)

Core: disulfide oxidoreductase activity (GO:0015036) via the CVVC motif;
contributes_to dolichyl-diphosphooligosaccharide-protein glycotransferase activity
(GO:0004579) as an OST-B subunit; in_complex oligosaccharyltransferase complex B
(GO:0160227); protein N-linked glycosylation (GO:0006487); at the ER membrane
(GO:0005789).

- OST complex membership (GO:0008250 / GO:0160227) and protein N-linked glycosylation
  (GO:0006487): ACCEPT the experimental/IBA/IDA/IPI annotations; these are the core.
- ER / ER membrane (GO:0005783, GO:0005789): ACCEPT (experimental IDA + redundant IEA/TAS).
- plasma membrane (GO:0005886), membrane (GO:0016020), azurophil granule membrane
  (GO:0035577): KEEP_AS_NON_CORE / over-annotation — from Mg2+ studies, NK/neutrophil
  proteomics, and Reactome neutrophil-degranulation propagation; not the ER core.
- Mg2+ MF/BP terms (GO:0015095 IEA & TAS, GO:1903830 IBA, GO:0015693 IMP): the IMP
  (PMID:19717468) is experimental -> KEEP_AS_NON_CORE; the IEA MF and IBA/TAS -> MARK_AS_OVER_ANNOTATED
  (secondary/indirect, likely downstream of glycosylation).
- transmembrane transport (GO:0055085 TAS Reactome): MARK_AS_OVER_ANNOTATED (generic,
  from the contested transporter model).
- cognition (GO:0050890 IMP PMID:18455129): UNDECIDED/KEEP_AS_NON_CORE — rests on the
  V311G variant whose pathogenicity UniProt flags as questionable; keep but non-core.
- protein N-linked glycosylation NAS (PMID:18455129): the paper is about OTase-subunit
  role in NSMR; the general glycosylation involvement is sound -> ACCEPT as non-core / accept.
</content>
</invoke>
