# UPF3B / UPF3X (Regulator of nonsense transcripts 3B) — research notes

UniProt: Q9BZI7 (REN3B_HUMAN), 483 aa. HGNC:20439. X chromosome. Synonyms: UPF3X, hUpf3b, RENT3B.

## Core function
UPF3B is a **core nonsense-mediated mRNA decay (NMD) factor** and a **peripheral component of the
exon-junction complex (EJC)**. It is a **molecular adaptor** that bridges the EJC core to the UPF
surveillance machinery.
- UniProt FUNCTION: "Involved in nonsense-mediated decay (NMD) of mRNAs containing premature stop codons by associating with the nuclear exon junction complex (EJC) and serving as link between the EJC core and NMD machinery. Recruits UPF2 ... formation of an UPF1-UPF2-UPF3 surveillance complex ... is believed to activate NMD. In cooperation with UPF2 stimulates both ATPase and RNA helicase activities of UPF1."
- [PMID:18066079 "NMD factors UPF2 and UPF3 bridge UPF1 to the exon junction complex and stimulate its RNA helicase activity."]
- Binds the EJC core via C-terminal region (424–483; contacts EIF4A3 and the MAGOH–RBM8A dimer).
- Binds spliced mRNA upstream of exon-exon junctions → MF GO:0003729 mRNA binding.
- In vitro also stimulates translation (independent of UPF2/EJC) — secondary/non-core.

## Localization
Nucleus and cytoplasm; shuttles between them. HPA: nucleoplasm, nucleolus, cytosol. Many Reactome TAS
nucleoplasm/cytosol annotations reflect NMD pathway steps.

## Interactions
Functionally central: UPF1, UPF2, RBM8A/Y14, EIF4A3, MAGOH (EJC); DHX34, DDX5/p68, SMG6, SMG-1 complex
(NMD). Most GOA IPI entries are bare "protein binding" from EJC/NMD interactome studies → KEEP_AS_NON_CORE.

## Disease
X-linked; LoF mutations cause X-linked syndromic/non-syndromic intellectual disability incl. Lujan-Fryns
syndrome (MRXS14) [PMID:17704778]. Variant Y160D.

## Core function conclusion
Core MF: **GO:0003729 mRNA binding** plus molecular-adaptor activity bridging UPF2/EJC to UPF1.
Core BP: **GO:0000184 nuclear-transcribed mRNA catabolic process, nonsense-mediated decay**.
Core CC: **GO:0035145 exon-exon junction complex** / GO:0170010 nonsense-mediated decay complex.
GO:0003676 nucleic acid binding is over-general (mark as over-annotated).
