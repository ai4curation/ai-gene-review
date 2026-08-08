# PSTK (Q8IV42) — review notes

Human gene **PSTK** (formerly C10orf89), HGNC:28578, chromosome 10; UniProt Q8IV42.

## Identity and enzymatic function

PSTK is **O-phosphoseryl-tRNA(Sec) kinase**, also named **L-seryl-tRNA(Sec) kinase** /
**phosphoseryl-tRNA[Ser]Sec kinase**; EC 2.7.1.164.

UniProt RecName is "L-seryl-tRNA(Sec) kinase" with AltName "O-phosphoseryl-tRNA(Sec)
kinase" [file:human/PSTK/PSTK-uniprot.txt "RecName: Full=L-seryl-tRNA(Sec) kinase"].

It catalyzes an ATP-dependent phosphorylation of the seryl moiety of Ser-tRNA(Sec):
[file:human/PSTK/PSTK-uniprot.txt "Reaction=L-seryl-tRNA(Sec) + ATP = O-phospho-L-seryl-tRNA(Sec) + ADP;"].
The product O-phosphoseryl-tRNA(Sec) is the activated intermediate that SEPSECS then
converts, using selenophosphate, to selenocysteyl-tRNA(Sec)
[file:human/PSTK/PSTK-uniprot.txt "phosphoseryl-tRNA(Sec), an activated intermediate for selenocysteine"].
The enzyme is substrate-specific: [file:human/PSTK/PSTK-uniprot.txt "biosynthesis. No activity with other tRNAs has been detected."].
Cofactor Mg(2+) [file:human/PSTK/PSTK-uniprot.txt "Name=Mg(2+); Xref=ChEBI:CHEBI:18420;"].

Pathway assignment: aminoacyl-tRNA biosynthesis; selenocysteinyl-tRNA(Sec) biosynthesis;
step 1/2 of the archaeal/eukaryal route
[file:human/PSTK/PSTK-uniprot.txt "selenocysteinyl-tRNA(Sec) from L-seryl-tRNA(Sec)"].
Family: [file:human/PSTK/PSTK-uniprot.txt "Belongs to the L-seryl-tRNA(Sec) kinase family."].

Structurally PSTK has a P-loop / atypical protein-kinase-related fold; UniProt annotates
an ATP-binding P-loop at residues 25–32 [file:human/PSTK/PSTK-uniprot.txt "BINDING         25..32"],
consistent with the KTI12/PSTK InterPro family (IPR013641) and the P-loop NTPase superfamily.

## Selenocysteine tRNA maturation pathway (eukaryotic route)

1. SerRS (SARS) serylates tRNA(Sec) → Ser-tRNA(Sec)
2. **PSTK** phosphorylates Ser-tRNA(Sec) → O-phosphoseryl-tRNA(Sec) (this gene)
3. SEPSECS converts O-phosphoseryl-tRNA(Sec) + selenophosphate → Sec-tRNA(Sec)
4. Sec-tRNA(Sec) is delivered by EEFSEC to UGA (with SECISBP2/SECIS) for co-translational
   selenocysteine incorporation.

Reactome places PSTK in "Selenocysteine synthesis" (R-HSA-2408557); go.db carries the
GO-CAM reaction node "Ser-tRNA(Sec) is phosphorylated to Sep-tRNA(Sec) by PSTK".

## GO term id verification (via ~/.data/oaklib/go.db)

- GO:0043915 "L-seryl-tRNA(Sec) kinase activity" — CURRENT; is_a GO:0016301 kinase activity;
  def "Catalysis of the reaction: ATP + L-seryl-tRNA(Sec) = ADP + O-phospho-L-seryl-tRNA(Sec)."
  This is the specific MF for PSTK.
- GO:0016301 "kinase activity" — CURRENT but general parent of GO:0043915.
- GO:0000049 "tRNA binding" — CURRENT (MF).
- GO:0005524 "ATP binding" — CURRENT (MF).
- GO:0001717 "conversion of seryl-tRNAsec to selenocys-tRNAsec" — CURRENT; is_a GO:0008033
  tRNA processing / under biosynthetic process; def "The modification process that results
  in the conversion of serine, carried by a specialized tRNA(ser)…to selenocysteine." This is
  the precise BP for the pathway PSTK participates in.
- GO:0097056 "selenocysteinyl-tRNA(Sec) biosynthetic process" — **OBSOLETE** (do not use).
- GO:0016259 "selenocysteine metabolic process" — **OBSOLETE** (do not use).
- GO:0005829 "cytosol" — CURRENT (CC).

## Evidence status of the existing GOA annotations

All 4 seeded GOA annotations are **computational**, not experimental:
- GO:0000049 tRNA binding — IBA (GO_REF:0000033, PANTHER PTN000466790)
- GO:0016301 kinase activity — IBA (GO_REF:0000033) — general; a specific child (GO:0043915) exists
- GO:0043915 L-seryl-tRNA(Sec) kinase activity — IEA (GO_REF:0000120, RHEA:25037 / EC:2.7.1.164)
- GO:0043915 L-seryl-tRNA(Sec) kinase activity — ISS (GO_REF:0000024, from mouse ortholog Q8BP74)

The ISS/EC/IBA calls converge on the same, well-supported enzymology, so the specific MF is
robustly supported despite the absence of a direct experimental GOA annotation for the human
protein.

## Foundational literature (not cached; provenance only, NOT used for verbatim supporting_text)

- Carlson BA, Xu X-M, Kryukov GV, Rao M, Berry MJ, Gladyshev VN, Hatfield DL. "Identification
  and characterization of phosphoseryl-tRNA[Ser]Sec kinase." PNAS 2004;101(35):12848–53.
  PMID:15317934 — discovery/characterization of PSTK; identified by comparative genomics
  (present in Sec-utilizing organisms, absent otherwise) and shown to phosphorylate
  Ser-tRNA(Sec). (verified title/authors via PubMed listing; full text not in local cache.)
- Yuan J, et al. "RNA-dependent conversion of phosphoserine forms selenocysteine in eukaryotes
  and archaea." PNAS 2006/2007. PMID:17142313 — establishes the Sep-tRNA(Sec)→Sec-tRNA(Sec)
  step downstream of PSTK. (not cached)
- Chiba S, et al. / "Structure of a tRNA-dependent kinase essential for selenocysteine
  decoding." PNAS 2009 (PMC2752577). — PSTK structure. (not cached)
- Sherrer RL, et al. "Structural basis for the major role of O-phosphoseryl-tRNA kinase in the
  UGA-specific encoding of selenocysteine." PMID:20705242. (not cached)

Because none of these are present in `publications/`, no verbatim `supporting_text` is drawn
from them; the Carlson 2004 paper is listed in `references` (full_text_unavailable) for
provenance but carries no verbatim quote. All verbatim supporting_text in the review comes
from the authoritative UniProt record.

Note: two files initially suspected to be PSTK papers in the cache — PMID_15769744 (LAT1/LAT2
S-nitrosocysteine transporters) and PMID_18093978 (nuclear TRAF6 / c-Myb) — are UNRELATED to
PSTK and were not used.

## Other observations

- Two isoforms (Q8IV42-1 displayed; Q8IV42-2 via VSP_014989, alt C-terminus from PMID:14702039).
- Coding variant G206R (rs3736582) reported from an MGC clone (PMID:15489334); no functional
  consequence established.
- No experimental subcellular-location line in UniProt; localization to cytosol is inferred
  from pathway/Reactome context, so cytosol is discussed here but not asserted as a
  verbatim-supported core-function location.
