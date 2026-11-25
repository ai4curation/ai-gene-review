# Vcp (rat, UniProt P46462) - manual literature synthesis

No deep-research provider was available for this review. This file was written by
hand from the cached publications in `publications/` and the UniProt record
(`Vcp-uniprot.txt`). Every claim carries an inline citation with a verbatim quote.

## Identity and architecture

- Rat Vcp (p97, transitional endoplasmic reticulum ATPase, TER ATPase) is the rat
  ortholog of yeast Cdc48 and human VCP. It was first isolated from rat liver
  transitional ER as a hexameric ATPase [PMID:7806566 "The native TER ATPase has been
  characterized as a hexamer of six 100-kD subunits by gel filtration. The protein
  catalyzes the hydrolysis of [gamma 32-P]ATP and is phosphorylated in the presence of
  Mg2+."].
- Domain organisation: an N domain plus two AAA ATPase domains, D1 and D2
  [PMID:18332143 "p97 consists of three domains: an N domain that interacts with many
  proteins and two homologous AAA domains with ATPase activity, D1 and D2."]. The
  record carries two Pfam AAA domains (PF00004), CDC48_N (PF02359), CDC48_2 (PF02933)
  and the NCBIfam TIGR01243 CDC48 family signature (Vcp-uniprot.txt).

## ATPase and nucleotide binding (rat protein, direct evidence)

- Recombinant rat p97 was used to measure nucleotide binding to D1 and D2
  [PMID:18332143 "We sought to explore nucleotide binding to recombinant rat p97 by
  studying the D1 and D2 domains separately."].
- ATPgammaS binds both domains; ADP binds D1 more tightly [PMID:18332143 "We report that
  adenosine 5'-O-(thiotriphosphate) (ATPgammaS) binds with similar affinity to D1 and
  D2, but ADP binds with higher affinity to D1 than D2, offering an explanation for the
  higher ATPase activity in D2."].
- D2 is the main site of ATP hydrolysis [PMID:18332143 "p97 carrying the Walker A
  mutation to the D1 domain alone (K251A) showed a moderate decrease in ATPase
  activity, whereas p97 carrying mutations in the D2 domain (K524A, K251A,K524A,
  R359A,R635A) showed little ATPase activity when compared with wild type"].
- Cooperativity within the hexamer [PMID:18332143 "ATPgammaS binding triggers a
  downstream cooperative conformational change of at least three monomers, which
  involves conserved arginine fingers and is necessary for ATP hydrolysis."].

## Cofactor complexes (rat liver cytosol, direct evidence)

- p97 forms two mutually exclusive major complexes [PMID:10811609 "Cytosolic p97
  therefore comprises at least two alternative complexes: p97/p47 and
  p97/Ufd1/Npl4."].
- p47 complex: one p47 trimer per p97 hexamer [PMID:9214505 "which forms a tight,
  stoichiometric complex with cytosolic p97 (one trimer of p47 per hexamer of
  p97)"]. Cryo-EM structures of the p97-p47 complex in two nucleotide states
  [PMID:16601695 "Depending on the nucleotide state, we observe the p47 trimer to be in
  two distinct arrangements on top of the p97 hexamer."].
- Ufd1-Npl4 complex [PMID:10811609 "Binding experiments with recombinant proteins
  revealed that Npl4 and Ufd1 form a binary complex on their own that can bind p97 to
  form a ternary complex."]; cryo-EM [PMID:22232657 "Our reconstructions show that
  p97-Ufd1-Npl4 is highly dynamic and that Ufd1-Npl4 assumes distinct positions
  relative to the p97 ring upon addition of nucleotide."].
- A p47 F253S point mutant fails to bind p97 [PMID:20691684 "p47(F253S) could not form a
  complex with p97 and did not caused any cisternal regrowth in an in vitro Golgi
  reassembly assay."].

## Membrane fusion and Golgi reassembly (p97-p47)

- p47 is the cofactor for p97-mediated regrowth of Golgi cisternae [PMID:9214505 "It is
  essential for the p97-mediated regrowth of Golgi cisternae from mitotic Golgi
  fragments, a process restricted to animal cells."].
- Only p97/p47, not p97/Ufd1/Npl4, drives reassembly [PMID:10811609 "Only a combination
  of p97 and p47 could promote reassembly."; "Neither p97/Ufd1/Npl4 nor p97/Ufd1
  promoted cisternal regrowth from mitotic Golgi fragments."].
- Earlier work implicated the TER ATPase in transition-vesicle formation from rat liver
  tER [PMID:7806566 "These antisera reduced the ATP-dependent cell-free formation of
  transition vesicles from isolated TER of rat liver."].

## ERAD and retrotranslocation (p97-Ufd1-Npl4)

- p97 is required to export ER proteins to the cytosol [PMID:11740563 "Here we
  demonstrate that another member of this family, Cdc48 in yeast and p97 in mammals,
  is required for the export of ER proteins into the cytosol."].
- Dual recognition and ATP-driven extraction [PMID:12847084 "Thus, both ubiquitin
  binding and ATP hydrolysis by p97-Ufd1-Npl4 complex are required for the release of
  polyubiquitinated substrates into the cytosol."]; p97 itself binds polyubiquitin
  [PMID:12847084 "Together, these data suggest that both p97 and Ufd1 can bind
  polyubiquitin chains."]; domain roles [PMID:12847084 "ATP hydrolysis by the D2
  domain, and probably also the D1 domain, are needed to move the polypeptide chain
  into the cytosol."].
- Endogenous ERAD substrate in rat cells: IP3 receptors [PMID:16103111 "Our results
  indicate that the p97-Ufd1-Npl4 complex is required for the processing of
  ubiquitinated IP 3 Rs and, thus, that this complex plays a key role in ERAD in
  mammalian cells."]. The effect was specific: bulk UPP degradation was unaffected
  [PMID:16103111 "3 B ), showing that the bulk degradation of ubiquitinated proteins was
  unaffected by p97 knockdown."].
- Membrane recruitment via Derlin-1/VIMP (human cells) [PMID:16186510 "In higher
  eukaryotes, p97 is bound to the ER membrane by a membrane protein complex containing
  Derlin-1 and VCP-interacting membrane protein (VIMP)."].
- Cytosolic localisation in rat beta-cells, interacting with ERAD machinery (SDF2L1
  study, PMID:23444373; abstract only).

## Other ubiquitin-dependent extraction roles (orthologs; By similarity in UniProt)

- Autophagosome maturation (human cells) [PMID:20104022 "We conclude that VCP is
  essential for maturation of ubiquitin-containing autophagosomes"].
- Endolysosomal sorting of ubiquitylated caveolin-1 with UBXD1 [PMID:21822278 "We show
  that VCP-UBXD1 targets mono-ubiquitylated CAV1 in SDS-resistant high-molecular-weight
  complexes on endosomes, which are en route to degradation in endolysosomes."].
- Mitophagy via UBXD1 recruitment [PMID:30120381 "Once translocated, UBXD1 recruits p97 to
  mitochondria via a bipartite binding motif consisting of its N-terminal VIM and PUB
  domains."].
- Stress granule clearance [PMID:29804830 "ZFAND1 interacts with two key factors of
  protein degradation, the 26S proteasome and the ubiquitin-selective segregase p97, and
  recruits them to arsenite-induced SGs."].
- DNA damage: extraction of L3MBTL1 [PMID:22120668 "The ATPase activity of VCP promotes
  the release of the Polycomb protein L3MBTL1 from chromatin"] and trapped PARP1
  [PMID:35013556 "events that promote recruitment of p97 and removal of trapped PARP1
  from chromatin"].
- Lipid droplets via UBXD8 [PMID:23297223 "UBXD8-mediated recruitment of p97/VCP to LDs
  increases LD size by inhibiting the activity of adipose triglyceride lipase
  (ATGL)"].

## Neuronal / synaptic

- Rat hippocampal neurons: VCP with neurofibromin controls dendritic spine density
  [PMID:22105171 "Here, we show that neurofibromin and VCP interact and work together to
  control the density of dendritic spines."] (abstract only).

## Indirect phenotypes (caution)

- Patient fibroblasts with VCP mutations show mitochondrial uncoupling and low ATP
  [PMID:23498975 "we show that VCP deficiency causes profound mitochondrial uncoupling
  leading to decreased mitochondrial membrane potential and increased mitochondrial
  oxygen consumption."]. These are downstream phenotypes, not activities of VCP.
- Poliovirus replication requires VCP [PMID:22379090 "We identified valosin-containing
  protein (VCP/p97) as a host factor of PV replication required after viral protein
  synthesis"]: host-dependency evidence.
