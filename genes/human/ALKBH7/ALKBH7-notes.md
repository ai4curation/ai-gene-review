# ALKBH7 (Q9BT30) review notes

## 2026-10-04: PAINT/affinage review

ALKBH7 is a mitochondrial matrix RNA demethylase.
- **Activity:** [PMID:34253897 "discovered that human ALKBH7 demethylates m22G and m1A within mitochondrial Ile and Leu1 pre-tRNA regions, respectively, in nascent polycistronic mitochondrial RNA"]
- **Location:** matrix in mouse [PMID:23572141 "We show that the Alkbh7 protein is located in the mitochondrial matrix and that an Alkbh7 deletion dramatically increases body weight and body fat."]

IBA donor check for the nucleus and chromatin IBAs (node PTN000471721), via QuickGO on 2026-10-04:
- Fission yeast ortholog Q9UT12 (SPAP8A3.02c) carries nucleus IDA (PMID:21949882) and chromatin IDA (PMID:22235339).
- The trypanosome member Q383D9 listed in with/from has only IBA for nucleus and chromatin, and is itself annotated to mitochondrion (HTP, RCA).
- So the nuclear placement rests on the yeast data. The human lineage is mitochondrial, so both IBAs are REMOVEd as COMPARTMENT_OR_COMPLEX_MISMATCH.

Other decisions:
- **Accepted:** dioxygenase (IBA, IEA), RNA and tRNA demethylase, RNA demethylation, mitochondrion and matrix rows.
- **Kept as non-core:** DNA damage response, necrosis-associated membrane permeability, and the mouse lipid/fatty-acid rows.
- **Five generic protein-binding rows** (HuRI, CFTR screen): REMOVE.
