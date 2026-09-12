# SLC25A3 (Q00325) — Gene Review Notes

## Summary

SLC25A3 is the **mitochondrial phosphate carrier (PiC / PHC / PTP)**, a member of the
SLC25 mitochondrial carrier family (TC 2.A.29). It is a nuclear-encoded, polytopic
integral protein of the mitochondrial inner membrane that imports inorganic phosphate
(Pi) from the intermembrane space into the matrix. The imported Pi is the phosphate
substrate that F1Fo-ATP synthase (Complex V) uses to phosphorylate ADP to ATP, so PiC
is an essential component of oxidative phosphorylation. A secondary, more recently
characterized activity is mitochondrial copper import required for cytochrome c oxidase
(Complex IV) biogenesis.

## Core identity and family

- UniProt name: "Solute carrier family 25 member 3"; AltName "Phosphate carrier protein,
  mitochondrial"; AltName "Phosphate transport protein (PTP)"
  [file:human/SLC25A3/SLC25A3-uniprot.txt, "RecName: Full=Solute carrier family 25 member 3"].
- Belongs to the mitochondrial carrier (TC 2.A.29) family
  [file:human/SLC25A3/SLC25A3-uniprot.txt, "Belongs to the mitochondrial carrier (TC 2.A.29) family"].
- Tripartite Solcar fold: three ~100-aa repeats, six transmembrane helices. UniProt
  feature table annotates 6 TRANSMEM helices and three REPEAT "Solcar" domains, matching
  the canonical SLC25 architecture. InterPro/Pfam: Mito_carr (PF00153, x3), SOLCAR
  (PS50920), MCP_transmembrane (IPR018108), SLC25A3/Pic2/Mir1-like (IPR044677).
- Precursor with an N-terminal mitochondrial transit peptide (residues 1–49), cleaved to
  give the mature carrier (chain 50–362)
  [file:human/SLC25A3/SLC25A3-uniprot.txt, "TRANSIT ... Mitochondrion" and "CHAIN 50..362"].

## Molecular function: phosphate/H+ symport

- UniProt FUNCTION: "Inorganic ion transporter that transports phosphate or copper ions
  across the mitochondrial inner membrane into the matrix compartment ... Mediates
  proton-coupled symport of phosphate ions necessary for mitochondrial oxidative
  phosphorylation of ADP to ATP"
  [file:human/SLC25A3/SLC25A3-uniprot.txt, "Mediates\n     proton-coupled symport of phosphate ions necessary for\n     mitochondrial oxidative phosphorylation of ADP to ATP"].
- UniProt CATALYTIC ACTIVITY: "phosphate(in) + H(+)(in) = phosphate(out) + H(+)(out)"
  (Rhea RHEA:29939; PhysiologicalDirection right-to-left, i.e. Pi + H+ import), evidence
  by similarity to UniProtKB:P12234 (bovine PiC)
  [file:human/SLC25A3/SLC25A3-uniprot.txt, "phosphate(in) + H(+)(in) = phosphate(out) + H(+)(out)"].
- The physiologically relevant activity is therefore a **phosphate:proton symporter**
  (GO:0015317), which is the specific molecular function. The transport is often described
  mechanistically as either H+/Pi symport or OH-/Pi antiport; UniProt/Rhea encode it as
  H+ symport.
- This is a **transporter, not an enzyme** — no catalytic/enzymatic MF (e.g. hydrolase,
  transferase) is warranted. The Rhea "CATALYTIC ACTIVITY" block describes the transport
  reaction, not a chemical transformation.

GO MF term choices:
- GO:0015317 "phosphate:proton symporter activity" — most specific; matches the UniProt
  Rhea reaction (phosphate + H+ symport). Under molecular_function via symporter activity
  → secondary active transmembrane transporter activity → transporter activity. (verified
  via OLS ancestry). This is the CORE MF.
- GO:0005315 "phosphate transmembrane transporter activity" — valid, a more general parent
  (used by the GOA IBA and InterPro IEA annotations). Correct but non-core relative to the
  symporter term.
- **GO:0015114 "phosphate ion transmembrane transporter activity" is OBSOLETE** (confirmed
  via OLS) — deliberately NOT used, despite being suggested as a candidate.

## Biological process

- Core BP: phosphate ion transmembrane transport (GO:0035435) and its more specific child
  mitochondrial phosphate ion transmembrane transport (GO:1990547).
- The transported Pi feeds ATP synthesis / oxidative phosphorylation (GO:0006119). PiC is
  one of the three nuclear-encoded carriers (with ANT and ATP synthase) that catalyze the
  terminal steps of OXPHOS
  [PMID:8168843, "The terminal steps of oxidative \nphosphorylation include transport of phosphate \nand ADP into the mitochondrial matrix, synthesis of ATP in the matrix"].
- Proton transmembrane transport (GO:1902600) is annotated by inter-ontology inference
  (GOC) from the phosphate:proton symporter activity — it reflects the co-transported H+,
  not an independent proton-pumping function. Non-core.

## Subcellular location

- Mitochondrion inner membrane; multi-pass membrane protein
  [file:human/SLC25A3/SLC25A3-uniprot.txt, "SUBCELLULAR LOCATION: Mitochondrion inner membrane"].
- EXP annotation for inner-membrane location comes from PMID:40652815 (HCMV UL13 study),
  which describes SLC25A3 as "the inner mitochondrial membrane copper transporter SLC25A3"
  [PMID:40652815, "the inner mitochondrial membrane copper transporter SLC25A3"].
- IDA (HPA), HTP (MitoCoP, PMID:34800366), and several TAS annotations corroborate
  mitochondrial / inner-membrane localization.
- Plasma membrane (TAS, PMID:8144629): the cited paper is a gene-sequencing / alternative-
  splicing study of the mitochondrial phosphate carrier; its abstract describes the
  carrier of the "inner membranes of mitochondria," not the plasma membrane. Plasma-
  membrane localization is inconsistent with the established inner-membrane topology and
  is treated as over-annotation (TAS, not removed).
- Extracellular exosome (HDA, PMID:19056867, urinary exosome proteome) and membrane (HDA,
  PMID:19946888, NK-cell membrane proteome) are generic high-throughput detections;
  mitochondrial inner-membrane proteins are common contaminants of such preparations.
  Non-core / over-annotation.

## Copper transport (secondary function, from UniProt)

- SLC25A3 also transports copper ions into the matrix to supply the mitochondrial matrix
  copper pool for cytochrome c oxidase (Complex IV) assembly
  [file:human/SLC25A3/SLC25A3-uniprot.txt, "Transports copper ions probably in the form of\n     anionic copper(I) complexes to maintain mitochondrial matrix copper\n     pool and to supply copper for cytochrome C oxidase complex assembly"].
- Kinetic parameters for copper are given for both isoforms (KM 15 uM / Vmax 25 for
  isoform A; KM 11 uM / Vmax 30 for isoform B) from PMID:29237729 (not cached; Boulet et
  al. 2018, J Biol Chem).
- PMID:40652815 (HCMV UL13): UL13 associates with SLC25A3 at the inner membrane and drives
  excessive mitochondrial copper accumulation → cuproptosis; SLC25A3 knockout abrogates
  UL13-induced DLAT oligomerization
  [PMID:40652815, "it \nassociates with the inner mitochondrial membrane copper transporter SLC25A3, \nleading to an excessive accumulation of mitochondrial copper. Knockout of \nSLC25A3 abrogates UL13-induced DLAT oligomerization"].
- The copper-transport function is not currently reflected in the GOA existing_annotations
  (all MF/BP annotations concern phosphate/proton). It is documented here for completeness
  and could support future copper-transport annotations, but no such GOA term exists to
  review.

## Disease

- Mitochondrial phosphate carrier deficiency (MPCD; MIM:610773): autosomal recessive
  disorder of oxidative phosphorylation with lactic acidosis, hypertrophic cardiomyopathy
  and muscular hypotonia, death within the first year of life; caused by the Gly72Glu
  variant [file:human/SLC25A3/SLC25A3-uniprot.txt, "Mitochondrial phosphate carrier deficiency (MPCD)"; PMID:17273968 (not cached), "Mitochondrial phosphate-carrier deficiency: a novel disorder of oxidative phosphorylation"].

## Isoforms

- Two alternative-splicing isoforms differ in the mutually-exclusive exon IIIA/IIIB
  encoding part of the first transmembrane region (aa 54–83; VSP_003269). Isoform A
  (Q00325-1) and isoform B (Q00325-2) are tissue-differentially expressed (A high in
  heart/liver/muscle; B high in lung); both transport phosphate and copper
  [PMID:8144629, "two exons, named \nIIIA and IIIB, are closely related, and they appear to the alternatively \nspliced"; file:human/SLC25A3/SLC25A3-uniprot.txt kinetic parameters for both isoforms].

## Annotation-specific notes

- **GO:0044877 protein-containing complex binding (IDA, PMID:23209302, assigned by MGI)**:
  The cached publication is the KIF14/Radil breast-cancer signaling paper; its full text
  (checked by grep) does not mention SLC25A3, the phosphate carrier, or Q00325. The
  IDA was made by MGI (mouse), so the supporting evidence is presumably in a mouse Slc25a3
  context not visible in this human-titled cache. Per policy, an experimental IDA is not
  removed; because bare "complex binding" is uninformative and the cached reference does
  not visibly support it for SLC25A3, it is marked as over-annotated / undecided rather
  than accepted as a core function.

## Core function synthesis

1. **Phosphate:proton symporter (GO:0015317)** of the mitochondrial inner membrane
   (GO:0005743), importing inorganic phosphate into the matrix (GO:0035435 /
   GO:1990547) coupled to H+, supplying the phosphate substrate for ATP synthase in
   oxidative phosphorylation (GO:0006119). This is the defining core function.
</content>
</invoke>
