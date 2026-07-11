# PIGU (Q9H490) review notes

## Summary of verified biology
PIGU (GPI-anchor transamidase component PIG-U; CDC91L1) is one of five subunits of the
glycosylphosphatidylinositol (GPI) transamidase (GPI-T) complex — PIGK, GPAA1, PIGT, PIGS, PIGU.
GPI-T is an ER-membrane complex that removes the C-terminal GPI-attachment signal peptide of
proprotein substrates and covalently attaches a pre-assembled GPI anchor to the newly exposed
C-terminus (the ω-site) in the ER lumen. PIGK is the catalytic (cysteine-protease/legumain-like)
subunit; GPAA1 is proposed to form the amide bond. PIGU is a **non-catalytic accessory subunit**:
it is a multi-pass ER membrane protein that binds the lipid portion of the GPI substrate and is
thought to help recognise/present the lipid GPI and to organise the transmembrane layer of the
complex (recruiting other subunits). Cells lacking PIGU still assemble the other four subunits but
have no transamidase activity.

## Key provenance
- Five-subunit complex, ER, PIGU = fifth subunit; class-U mutant cells accumulate GPI, lack in-vitro
  transamidase activity, and lose ability to cleave the GPI attachment signal peptide
  [PMID:12802054 "PIG-U and the yeast orthologue Cdc91p are the fifth component of GPI transamidase that may be involved in the recognition of either the GPI attachment signal or the lipid portion of GPI"];
  [PMID:12802054 "The class U cells accumulated mature and immature GPI and did not have in vitro GPI transamidase activity"].
- GPI-T is ER-membrane, replaces C-terminal GPI attachment signal with pre-assembled GPI
  [PMID:11483512 "The GPI transamidase mediates GPI anchoring in the endoplasmic reticulum, by replacing a protein's C-terminal GPI attachment signal peptide with a pre-assembled GPI"].
- Five subunits, PIGK catalytic, PIGU recognises lipid portion of GPI, loss of PIGU abolishes activity
  [PMID:34576938 "PIGU is homologous with other GPI biosynthetic enzymes (such as PIGW and PIGM), suggesting that it recognizes the lipid portion of GPI"];
  [PMID:34576938 "Lacking PIGU, other subunits (PIGK, GPAA1, PIGT and PIGS) still form a complex, but have no activity"].
- Cryo-EM structure of five-subunit human GPI-T; PIGK catalytic; TM cleft = GPI substrate-binding site
  [PMID:35165458 "The GPIT complex is known to be composed of five subunits: PIGK, PIGU, PIGT, PIGS and GPAA1"].
- Equimolar heteropentamer, ER-membrane GPI-T conserved among eukaryotes
  [PMID:35551457 "an endoplasmic reticulum membrane GPI transamidase complex (GPI-T) conserved among all eukaryotes"];
  [PMID:35551457 "revealing an equimolar heteropentameric assembly"].
- Liganded GPI-T structures; GPI binds GPI-T; PIGU is one of the five subunits contacting GPI
  [PMID:37684232 "The glycolipid is then added to the proproteins by the GPI transamidase (GPI-T), a transmembrane complex composed of five subunits"].
- Disease: biallelic PIGU variants cause NEDBSS / inherited GPI-anchor deficiency (GPIBD) with
  developmental delay, intellectual disability, epilepsy, brain anomalies
  [PMID:31353022 "An essential component of the GPI transamidase complex is PIGU, along with PIGK, PIGS, PIGT, and GPAA1, all of which link GPI-anchored proteins (GPI-APs) onto the GPI anchor in the endoplasmic reticulum (ER)"].

## Annotation decisions (high-level)
- Core: BP = GPI anchor biosynthetic process (GO:0006506) / attachment of GPI anchor to protein
  (GO:0016255); CC = ER membrane (GO:0005789) + GPI-anchor transamidase complex (GO:0042765).
- MF: GOA carries NO catalytic MF for PIGU. The only MF terms are `protein binding` (GO:0005515, IPI,
  HuRI high-throughput — mark over-annotated) and `GPI anchor binding` (GO:0034235, IDA/IMP —
  accept as a subunit-level binding activity, PIGU binds the lipid portion of GPI). Note: UniProt DR
  block lists an IBA `GPI-anchor transamidase activity` (GO:0003923) but it is NOT in the GOA TSV, so
  it is not reviewed here and NOT invented as a core function (PIGU is non-catalytic).
- `plasma membrane` (GO:0005886, IDA, PMID:15034568) and `regulation of receptor signaling pathway
  via JAK-STAT` (GO:0046425, IDA, PMID:15034568): from the bladder-cancer oncogene paper. These are
  downstream/indirect consequences of PIGU overexpression (uPAR up, STAT3 phosphorylation), not the
  core ER-lumenal biosynthetic function. PIGU itself is an ER-membrane protein, not a PM protein;
  the paper reports overexpression effects. Mark over-annotated / non-core rather than core.
- `membrane` (GO:0016020) IEA/HDA: correct but non-informative parent of ER membrane; keep as
  non-core.
