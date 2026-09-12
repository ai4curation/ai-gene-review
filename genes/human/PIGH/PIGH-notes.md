# PIGH (Q14442) review notes

Human PIGH — Phosphatidylinositol N-acetylglucosaminyltransferase subunit H (PIG-H).
188 aa, ER membrane protein (UniProt: multi-pass; two predicted TM helices 40-60 and
63-83). HGNC:8964. Chromosome 14. Gene MIM 600154; disease MIM 618010 (GPIBD17).

Deep research: falcon provider was OUT OF CREDITS (HTTP 402) at review time, so no
`-deep-research-falcon.md` was generated. This review is grounded in the UniProt record
(`PIGH-uniprot.txt`), the seeded GOA (`PIGH-goa.tsv`), the cached primary publications,
and the Reactome entry.

## Core biology (verified)

PIGH is a **non-catalytic (accessory) subunit of the GPI-GlcNAc transferase (GPI-GnT)
complex**, the multi-subunit ER enzyme that catalyzes the **first committed step of
GPI-anchor biosynthesis**: transfer of GlcNAc from UDP-GlcNAc onto phosphatidylinositol
(PI) to yield GlcNAc-PI, on the cytoplasmic face of the ER.

- The **catalytic subunit is PIGA** (homologous to a bacterial GlcNAc transferase); PIGH
  is one of the required accessory subunits.
- The complex comprises at least PIGA, PIGC, PIGH, PIGP, PIGQ (GPI1), PIGY and DPM2.
  [PMID:16162815 "consisting of at least six proteins ... requires another component, termed PIG-Y"]
  [UniProt SUBUNIT: "composed at least by PIGA, PIGC, PIGH, PIGP, PIGQ, PIGY and DPM2"]

### Provenance of key claims

- **First step / GlcNAc transfer / complex**:
  [PMID:8900170 "The first step is the transfer of N-acetylglucosamine (GlcNAc) to PI from UDP-GlcNAc to generate GlcNAc-PI"]
  [PMID:8900170 "PIG-A and PIG-H are subunits of the GPI GlcNAc transferase that transfers GlcNAc to PI on the cytoplasmic side of the ER"]
  [PMID:9463366 "The protein complex had GPI-GlcNAc transferase (GPI-GnT) activity in vitro"]
- **PIG-H is ER-associated, cytoplasmically oriented; forms complex with PIG-A**:
  [PMID:8900170 "PIG-H is a cytoplasmically oriented, ER-associated protein; and 3) that they form a protein complex"]
  (UniProt models the mature protein as a multi-pass ER membrane protein; GOA carries
  ER membrane EXP/IDA. I defer to GOA/UniProt for the ER-membrane CC.)
- **Interactions**: PIGH interacts with PIGA (P37287) and PIGQ (Q9BRB3) within the complex.
  [UniProt INTERACTION: "Q14442; P37287: PIGA" and "Q14442; Q9BRB3: PIGQ"]
- **PIG-P / DPM2 components**: [PMID:10944123 "GPI-GnT requires another component, termed PIG-P, and that DPM2 ... also regulates GPI-GnT"]

### Molecular function

The GOA carries **no catalytic MF term** for PIGH — only `GO:0005515 protein binding`
(IPI, from complex/interactome studies). This is consistent with PIGH being a
non-catalytic subunit; the GlcNAc-transferase catalytic activity belongs to the complex
(and specifically to PIGA). I therefore do NOT assign a catalytic MF in core_functions;
I record PIGH's contribution via `directly_involved_in` the BP and `in_complex` the
GPI-GnT complex, plus ER-membrane location.

### Disease

Biallelic PIGH variants cause **GPI biosynthesis defect 17 (GPIBD17)** [MIM:618010], an
autosomal-recessive inherited GPI-deficiency disorder (developmental/epileptic
encephalopathy): developmental delay, epilepsy/seizures, microcephaly, autistic features,
skeletal manifestations. Variants: start-codon disruption (PMID:29573052),
p.Ser103Pro (PMID:29603516, PMID:33156547 — reduced GPI-anchored protein surface
expression), p.Arg163Trp (PMID:33156547, PMID:35445667). Disease refs are not in the
GOA and are used only for the top-level `description`/context (no supporting_text quotes
needed since they are not cached).

## GOA annotation inventory (21 lines -> 20 review entries)

MF: GO:0005515 protein binding (IPI) x6 references (7 GOA lines; two PMID:33961781 lines
  with different partners P37287/Q9BRB3 collapse to one review entry).
CC: GO:0000506 GPI-GnT complex (IBA, IEA, IPI, IDA x2) ; GO:0005789 ER membrane
  (IEA, EXP, IDA, TAS) ; GO:0005783 ER (TAS).
BP: GO:0006506 GPI anchor biosynthetic process (IBA, IEA, IDA, TAS).

### Curation decisions summary

- CC GPI-GnT complex (all evidence): ACCEPT — core, well-supported.
- CC ER membrane / ER (all evidence): ACCEPT — core localization.
- BP GPI anchor biosynthetic process (all evidence): ACCEPT — core.
- MF protein binding (all IPI): MARK_AS_OVER_ANNOTATED — uninformative bare
  `protein binding`; the real informative content (subunit of GPI-GnT) is captured by the
  complex CC term. Per policy, do NOT REMOVE bare protein-binding IPIs.
</content>
</invoke>
