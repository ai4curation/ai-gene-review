# SLC6A9 (GlyT1) research notes

UniProt: P48067 (SC6A9_HUMAN). HGNC: SLC6A9. 706 aa (displayed isoform GlyT-1C, P48067-1).
Gene on chromosome 1p34.1. Batch 10 canonical-surfaceome backfill.

## Identity and family

- Sodium- and chloride-dependent glycine transporter 1 (GlyT-1 / GlyT1). SLC6/neurotransmitter:sodium
  symporter (SNF / NSS) family, TC 2.A.22, "SLC6A9 subfamily"
  [file:human/SLC6A9/SLC6A9-uniprot.txt "Belongs to the sodium:neurotransmitter symporter (SNF) (TC 2.A.22) family. SLC6A9 subfamily"].
- 12-transmembrane topology (TM1–TM12; cytoplasmic N- and C-termini), confirmed by multiple cryo-EM / X-ray
  structures (6ZBV, 8WFI, 8WFJ–L, 9J8B–D). PANTHER PTHR11616:SF263 "SODIUM- AND CHLORIDE-DEPENDENT GLYCINE
  TRANSPORTER 1". Pfam PF00209 (SNF). InterPro IPR003028 (Na/ntran_symport_glycine_GLY1).

## Core molecular function: Na+/Cl--dependent glycine symport

- Secondary-active symporter: couples glycine uptake to Na+ and Cl- co-transport. UniProt catalytic activity
  (Rhea RHEA:70691) gives the stoichiometry explicitly:
  [file:human/SLC6A9/SLC6A9-uniprot.txt "glycine(out) + chloride(out) + 2 Na(+)(out) = glycine(in) + chloride(in) + 2 Na(+)(in)"].
  => **2 Na+ : 1 Cl- : 1 glycine**. This lower Na+ coupling (vs GlyT2/SLC6A5's 3:1:1) makes GlyT1 less
  concentrative and bidirectional, so GlyT1 can both clear and release glycine depending on the Na+/membrane-potential
  gradient — relevant to whether its role is framed as "reuptake" vs "uptake/import".
- Km ~90 uM for glycine (isoform GlyT-1C)
  [file:human/SLC6A9/SLC6A9-uniprot.txt "KM=90 uM for glycine"].
- **Sarcosine-SENSITIVE** (inhibited by sarcosine), distinguishing GlyT1 from the sarcosine-insensitive GlyT2
  [file:human/SLC6A9/SLC6A9-uniprot.txt "Inhibited by sarcosine"]. The enterocyte study independently confirms a
  sarcosine-sensitive, Na+/Cl--dependent "system GLY" = GlyT1
  [PMID:11159884 "The dominant Na(+)- and Cl(-)-dependent mechanism was characterized by a restricted inhibition profile, selectively sensitive to sarcosine"].
- GO MF handling: there is **no** glycine:Na+:Cl- symporter term in GO (search returns only GO:0140814
  glycine BETAINE:Na:Cl symporter activity). The most specific EXISTING term is **GO:0015375 glycine:sodium
  symporter activity** (def "glycine(out)+Na+(out)=glycine(in)+Na+(in)"), used as core MF. OLS ancestor check:
  GO:0015375 is_a descendant of GO:0005283 (amino acid:sodium symporter) and GO:0015370 (solute:sodium symporter)
  => both are TOO_GENERAL. A proposed_new_term "glycine:sodium:chloride symporter activity" (parent GO:0015375,
  analogous to GO:0140814) is filed for the Cl- co-substrate, mirroring the batch-9 SLC6A5/GlyT2 review precedent
  (genes/human/SLC6A5/SLC6A5-ai-review.yaml).
- Note GO:0015187 (glycine transmembrane transporter activity) is a PARALLEL glycine-specific MF branch, NOT an
  is_a ancestor of GO:0015375 (OLS-verified: GO:0015375 ancestors do not include GO:0015187). It is a true,
  substance-specific MF => ACCEPT, not TOO_GENERAL.

## Localization and cell types

- Plasma-membrane (cell membrane), multi-pass
  [file:human/SLC6A9/SLC6A9-uniprot.txt "Cell membrane"]. Directly shown: WT GlyT1 at the cell surface
  [PMID:37962965 "WT GLYT1 was predominantly located on the cell surface"].
- Predominantly **glial/astrocytic** in CNS: "GLYT1 is primarily expressed by astrocytes adjacent to glycinergic
  neurons to facilitate the rapid clearance of glycine from the synaptic cleft"
  [PMID:37962965 "GLYT1 is primarily expressed by astrocytes adjacent to glycinergic neurons to facilitate the rapid clearance of glycine from the synaptic cleft"].
  Controls extracellular/synaptic glycine, including the NMDA-receptor co-agonist pool (basis of GlyT1 inhibitors
  bitopertin/iclepertin as pro-cognitive/schizophrenia drugs; DrugBank xrefs).
- In polarized epithelia (enterocytes), expressed basolaterally, mediating high-affinity glycine acquisition
  [PMID:11159884 "Enterocytes express GLYT1 along the length of the crypt-villus axis, where it mediates high-affinity basolateral glycine uptake"].
- Reuptake vs glial uptake: GlyT1 is largely glial (not presynaptic-neuronal like GlyT2). GO:0098810/GO:0051936
  "reuptake" terms are presynaptic-cytosol by definition and would overstate GlyT1's role, so NO reuptake NEW term
  is proposed (contrast the GlyT2 precedent). GO:0001504 "neurotransmitter uptake" is appropriate because its
  definition explicitly covers "into neurons or glial cells" (OLS-verified) => ACCEPT for glial glycine clearance.

## Biological processes

- Core: glycine import/transport across the plasma membrane (GO:1903804 ACCEPT; GO:0015816 glycine transport
  TOO_GENERAL since GO:1903804 is_a descendant, OLS-verified). Neurotransmitter transport (GO:0006836) ACCEPT
  (glycine is a neurotransmitter; the term adds the neurotransmitter dimension and is not entailed by the
  amino-acid-transport branch).
- Regulation of glycinergic synaptic transmission (GO:0060092) — GlyT1 performs transport and thereby shapes the
  glycinergic signal; KEEP_AS_NON_CORE (downstream regulatory/participation role, not the molecular activity).
- Positive regulation of heme / hemoglobin biosynthesis (GO:0070455 / GO:0046985) — glycine is a precursor of
  heme (via ALA synthase); GlyT1 supplies glycine in erythroid cells. This is an indirect substrate-supply /
  metabolic role, documented via the mouse ortholog => KEEP_AS_NON_CORE (peripheral, not the core CNS transport).

## Disease

- Glycine encephalopathy with normal serum glycine (GCENSG, MIM:617301), autosomal recessive, NKH-like; loss of
  GlyT1 causes raised CSF glycine (PMID:27773429, PMID:27481395; variant S407G)
  [file:human/SLC6A9/SLC6A9-uniprot.txt "Loss of Glycine Transporter 1 Causes a Subtype of Glycine Encephalopathy"].
- Isolated scoliosis 6 (IS6, MIM:621428), autosomal dominant; heterozygous variants reduce surface GlyT1 and
  glycine uptake [PMID:37962965 "Impaired glycine neurotransmission causes adolescent idiopathic scoliosis"].
- Disease LOF is consistent with the participation test: loss of GlyT1 establishes necessity for glycine
  homeostasis, which is what substrate-supply/transport means — it does not make GlyT1 a performer of downstream
  synaptic or developmental processes.

## Annotation review decisions (summary)

- Core MF: GO:0015375 glycine:sodium symporter activity (ACCEPT; IEA/TAS rows). GO:0015187 ACCEPT (glycine-specific
  MF). GO:0005283, GO:0015370 TOO_GENERAL (is_a ancestors of GO:0015375).
- Core BP: GO:1903804 glycine import across plasma membrane (ACCEPT, all rows). GO:0015816 glycine transport
  TOO_GENERAL. GO:0001504 neurotransmitter uptake ACCEPT (glial). GO:0006836 neurotransmitter transport ACCEPT.
- Locations: GO:0005886 plasma membrane ACCEPT (incl. IDA PMID:37962965). GO:0016020 membrane MODIFY -> GO:0005886.
  Polarized-epithelium PM subdomains (GO:0009925 basal, GO:0016323 basolateral, GO:0016324 apical, GO:0016328
  lateral; all IDA PMID:11159884) KEEP_AS_NON_CORE (enterocyte context, peripheral; defer to curator who read full
  text). Endosome (GO:0005768) KEEP_AS_NON_CORE (recycling pool; rat-ortholog transfer).
- Rat-ortholog (P28572) Ensembl-Compara block: synaptic-membrane localizations (GO:0042734 presynaptic membrane,
  GO:0045211 postsynaptic membrane, GO:0098686 mossy-fiber-CA3, GO:0098688 parallel-fiber-Purkinje) KEEP_AS_NON_CORE
  (GlyT1 active peri-synaptically). GO:0014069 postsynaptic density and GO:0030672 synaptic vesicle membrane
  MARK_AS_OVER_ANNOTATED (intracellular/structural compartments inconsistent with a surface transporter).
  GO:0031045 dense core granule (IEA+ISS) UNDECIDED (surprising claim; rat-ortholog primary evidence inaccessible;
  matches SLC6A5 precedent). GO:0009612 response to mechanical stimulus MARK_AS_OVER_ANNOTATED (single rat-ortholog
  electronic transfer; no mechanism for a glycine transporter).
- GO:0035725 sodium ion transmembrane transport KEEP_AS_NON_CORE (obligate co-transported Na+).
- GO:0150104 transport across blood-brain barrier (NAS x2) UNDECIDED: the cited references (PMID:30280653,
  PMID:26590417) are general BBB-physiology reviews that do NOT mention glycine, GlyT1 or SLC6A9 (grep-verified),
  so they do not substantiate a GlyT1-specific vectorial BBB-transport claim, and no primary evidence establishes it.

## Cross-paralog (GlyT1 vs GlyT2 / SLC6A5, Q9Y345)

Several IBA rows carry Q9Y345 (GlyT2) in WITH/FROM (GO:0005283, GO:0005886, GO:1903804). The glycine-transporter
clade nodes (PTN000907238, PTN000177662) legitimately include GlyT1: both paralogs import glycine across the
plasma membrane. The paralog distinction is mechanistic/pharmacological — GlyT1 is 2 Na+ : 1 Cl- : 1 glycine and
sarcosine-SENSITIVE; GlyT2 is 3:1:1 and sarcosine-INsensitive — not a difference in whether glycine is transported.
So the IBA node placements are sound for GlyT1; the stoichiometry/pharmacology difference is recorded in
propagation_review rather than used to challenge the node.
