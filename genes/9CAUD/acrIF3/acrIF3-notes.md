# acrIF3 / JBD5_035 (L7P7R7, Pseudomonas phage JBD5) — curation notes

## Identity

Unreviewed TrEMBL entry, 139 aa, named only `RecName: Full=Phage protein
{ECO:0008006|Google:ProtNLM}` — a machine-generated placeholder. `PE 1: Evidence at
protein level`. Seeded taxon was wrong (`NCBITaxon:10663`); UniProt gives
`OX NCBI_TaxID=1223261` for Pseudomonas phage JBD5 and the review is corrected to that.

**Despite the uninformative name, this is the assayed AcrF3.** The entry carries three
PDB cross-references, all with chains spanning residues 1-139 of this accession:

- `PDB; 5B7I; X-ray; 2.60 A; B/C=1-139` → PMID:27455460, "Structural basis of Cas3
  inhibition by the bacteriophage protein AcrF3" (RCSB primary citation confirms)
- `PDB; 5GNF; X-ray; 1.50 A; A/B=1-139` and `PDB; 5GQH; EM; 4.20 A; B/C=1-139` →
  PMID:27585537, the independent Cell Research structure

and the genome reference is the anti-CRISPR discovery paper itself
(`RX PubMed=23242138`). InterPro `IPR049085 AcrF3-like`, Pfam `PF21401 AcrF3`, CDD
`cd22238 AcrIF3` all agree. So two independent groups solved the AcrF3–Cas3 complex using
this sequence, and experimental evidence codes are appropriate.

This is a textbook instance of the second knowledge gap in
`modules/anti_crispr_suppression.yaml`: InterPro has a mechanism-bearing family name
("Cas3 inhibitor AcrF3-like") while UniProt still calls the protein "Phage protein". The
entry should be nominated for Swiss-Prot review.

## Mechanism: the module's Cas3-sequestration assignment holds

The module (annoton `acrif3_cas3_sequestration`) asserts `GO:0140311 protein sequestering
activity`, with the target being host type I-F Cas3. **The assignment holds and is well
supported by two independent structures.**

Wang X et al.
[PMID:27455460 "Here we report the crystal structure of the anti-CRISPR protein AcrF3 in complex with Pseudomonas aeruginosa Cas3 (PaCas3)."],
[PMID:27455460 "AcrF3 forms a homodimer that locks PaCas3 in an ADP-bound form, blocks the entrance of the DNA-binding tunnel in the helicase domain, and masks the linker region and C-terminal domain of PaCas3, thereby preventing recruitment by Cascade and inhibiting the type I-F CRISPR-Cas system."].

Wang J et al. independently
[PMID:27585537 "our structural analysis of the Cas3-AcrF3 complex revealed that the AcrF3 dimer binds to HD, Linker and CTD domains of the Cas3 protein, therefore blocking the replaced non-complementary DNA access of Cas3"],
and add a consequence the first paper did not report — inhibition also blocks primed
spacer acquisition
[PMID:27585537 "DNA degradation via inhibiting recruitment of Cas3 by Csy complex. In addition, inhibition of Cas3-guided DNA degradation also blocks primed spacer acquisition. In summary, the AcrF3 dimer overcomes the CRISPR system at both the crRNA interference and the primed acquisition stages."].
That second point is biologically significant: AcrF3 does not merely spare the current
infection, it prevents the host from updating its CRISPR memory against the phage.

Bondy-Denomy et al. established the mechanism class biochemically before either structure
[PMID:26416740 "The third anti-CRISPR protein operates by binding to the Cas3 helicase-nuclease and preventing its recruitment to the DNA-bound CRISPR-Cas complex."],
and noted the striking downstream effect that the inhibited system is converted into a
DNA-binding-only module
[PMID:26416740 "In vivo, this anti-CRISPR can convert the CRISPR-Cas system into a transcriptional repressor"].

`GO:0140311 protein sequestering activity` is defined as "Binding to a protein to prevent
it from interacting with other partners or to inhibit its localization to the area of the
cell or complex where it is active." Both clauses apply literally: AcrF3 masks the linker
and CTD that Cascade uses to recruit Cas3, so Cas3 cannot interact with its partner and
cannot localise to the R-loop where it is active. **This is the one anti-CRISPR mechanism
in the module for which GO already has a precise molecular-function term**, and no new
term is proposed here.

Note that in type I-F Cas2 and Cas3 are a single fusion protein
[PMID:27585537 "In the type I-F CRISPR system, Cas2 and Cas3 are coded by one gene as a fused protein"],
so the sequestered entity is Cas2/3; the term is unaffected.

## GOA state: one annotation, and it is an over-annotation

GOA holds exactly one row: `enables GO:0046872 metal ion binding`, IEA from
`GO_REF:0000043`, keyword `KW-0479` (Metal-binding). The keyword chain is traceable and
the chain is the problem:

`PDB 5GNF` → UniProt FT BINDING records at residues 2, 2, 3, 65, 66, 70 for three Ca(2+)
ions, all with `ECO:0007829|PDB:5GNF` (i.e. automatic annotation from PDB ligand records)
→ keywords `KW-0106 Calcium` and `KW-0479 Metal-binding`, both with the same PDB-derived
evidence → `GO:0046872`.

Reasons to treat this as an over-annotation rather than a function:

1. **The paper that produced 5GNF never ascribes any role to calcium.** Searching
   PMID:27585537 for "calcium", "Ca2+" or "ion" returns no statement about a metal
   requirement, metal dependence, or a metal site; the mechanism it reports is entirely
   protein-protein (dimerisation plus masking of the Cas3 HD, Linker and CTD domains).
2. **The sites look crystallographic.** Two of the three Ca(2+) are coordinated by
   residues 2 and 3, i.e. the extreme N-terminus, and the third by the surface stretch
   65/66/70. Surface and terminal Ca(2+) at a 1.50 Å resolution are the classic signature
   of ions picked up from the crystallisation liquor.
3. **The independent structure disagrees.** The 2.60 Å complex 5B7I (PMID:27455460)
   contains no calcium, and its abstract describes the nucleotide state of Cas3 (ADP) as
   the functionally relevant ligand, not a metal on AcrF3.
4. **The mechanism needs no metal.** Sequestration by steric masking is not a chemistry
   that requires a cofactor.

Action: `MARK_AS_OVER_ANNOTATED` rather than `REMOVE`. The Ca(2+) density is a real
observation in a real deposited structure, so saying "metal ion binding is false" would
overstate the case; what is unsupported is the inference that metal binding is a function
of this protein. This is an IEA keyword mapping, not an experimental annotation, so
challenging it does not run against the rule about deferring to curators who read full
texts — and the relevant full text is cached and has been read.

## Not asserted

No Aca repressor is assigned to the JBD5 locus in the evidence reviewed here, so the
module's part 4 is not annotated for this gene.
