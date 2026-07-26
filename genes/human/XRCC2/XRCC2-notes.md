# XRCC2 review notes

UniProt: O43543 (XRCC2_HUMAN), 280 aa. HGNC:12829. Gene on chr7.
RecName: DNA repair protein XRCC2 (X-ray repair cross-complementing protein 2).
Also known as FANCU (Fanconi anemia complementation group U).
SIMILARITY: RecA family, RAD51 subfamily. P-loop NTPase fold; Rad51_C domain (Pfam PF08423 Rad51; InterPro IPR030547 XRCC2, IPR020588 RecA_ATP-bd).

## Core biology (verified)

XRCC2 is one of five human RAD51 paralogs (RAD51B, RAD51C, RAD51D, XRCC2, XRCC3).
It is an obligate structural subunit of the **BCDX2 complex** (RAD51B-RAD51C-RAD51D-XRCC2),
one of the two RAD51-paralog complexes (the other being CX3 = RAD51C-XRCC3).

[PMID:11751635 "the five paralogs exist in two distinct complexes in human cells: one contains RAD51B, RAD51C, RAD51D, and XRCC2 (defined as BCDX2)"]
[PMID:11751635 "BCDX2 binds single-stranded DNA and single-stranded gaps in duplex DNA"]

BCDX2 acts as an HR **mediator**: it promotes the nucleation and extension of the RAD51
nucleoprotein filament on ssDNA. The 2023 cryo-EM structure/function paper is definitive:

[PMID:37344587 "BCDX2 stimulates the nucleation and extension of RAD51 filaments-which are essential for recombinational DNA repair-in reactions that depend on the coupled ATPase activities of RAD51B and RAD51C"]
[PMID:37344587 "we found that BCDX2 increases both the quantity (nucleation) and length (growth) of RAD51 filaments"]
[PMID:37344587 "BCDX2 promotes RAD51 filament nucleation and growth in an ATP hydrolysis dependent manner"]
[PMID:37344587 "BCDX2 binds specifically to ssDNA"]

RAD51C-RAD51D-XRCC2 within BCDX2 structurally mimic three RAD51 protomers aligned within a
nucleoprotein filament; RAD51B is dynamic. The ATP hydrolysis that drives the high-affinity
ssDNA-binding state is contributed by **RAD51B and RAD51C**, NOT by XRCC2. XRCC2 does bind
ATP (near-identical Walker A/B arrangement) but XRCC2's own catalytic function (and its
lysine finger K261) is not established as catalytic:

[PMID:37344587 "XRCC2 binds ATP in a near-identical arrangement via Walker A K54/T55 and Walker B D149"]

=> XRCC2's core role is HR **mediator / RAD51 filament assembly factor**, NOT a classic
recombinase/strand-exchange enzyme in its own right. This is why "ATP-dependent DNA damage
sensor activity" (InterPro IEA) is an over-annotation for XRCC2.

### Pathway position
[PMID:23149936 "the BCDX2 complex acts downstream of BRCA2 recruitment but upstream of Rad51 recruitment"]
BCDX2 and CX3 act at different HR stages; both epistatic with BRCA2.

### DNA-binding specificity of BCDX2
[PMID:20207730 "both complexes bind with exceptionally high specificity to the DNA junctions"] (Holliday junctions and replication forks; ring-shaped complexes). Supports four-way junction DNA binding (contributes_to) and replication-fork localization.

### Homologous pairing / strand invasion activity of subcomplex
[PMID:11834724 "pairing between single-stranded and double-stranded DNA"] — purified Xrcc2*Rad51D subcomplex catalyzes homologous pairing; forms multimeric rings without DNA and filaments with ssDNA. Supports DNA strand invasion (involved_in).

### Replication fork
[PMID:32669601 "the BCDX2 subcomplex restrains fork progression upon stress, promoting fork reversal"] — sequential role of RAD51 paralog complexes in fork remodeling/restart. Supports replication fork localization/function.

### Chromosome stability / DNA repair
[PMID:10422536 "play essential roles in"] maintaining chromosome stability (XRCC2/XRCC3); irs1 (XRCC2-mutant) hamster cells hypersensitive to cross-linkers (MMC), genomic instability. Supports DNA repair (IGI).
[PMID:9628903 "elevated in mouse testis, suggesting an additional role"] in meiosis — supports meiotic cell cycle (non-core) and DNA repair (TAS).

### Centrosome / mitotic role (secondary)
[PMID:21276791 "XRCC2 and other HR proteins, including the key"] recombinase RAD51, co-localize with the centrosome; XRCC2-deficient cells show centrosome disruption and mitotic catastrophe.
[PMID:21276791 "centrosome disruption is dynamic"] — supports centrosome localization, centrosome cycle, mitotic cell cycle (all non-core/secondary; likely indirect consequence of genome-instability, not a distinct molecular function).

## Disease
- FANCU: Fanconi anemia complementation group U [PMID:22232082] (biallelic loss).
- SPGF50 (spermatogenic failure, meiotic arrest/azoospermia) [PMID:30042186 L14P].
- POF17 (premature ovarian failure) [PMID:30489636 L14P].
- Rare missense variants -> breast cancer susceptibility (uncertain); most tested missense
  variants do NOT impair HR in rescue assays [PMID:27233470].

## Interactions (IPI protein binding annotations)
Direct partner: RAD51D (O75771, NbExp=42), RAD51C (O43502). Many GO:0005515 "protein binding"
IPI annotations point to RAD51D/RAD51C (the biologically meaningful ones) plus high-throughput
interactome partners (MEOX2 P50222, etc.). "protein binding" is uninformative as a core MF ->
mark over-annotated; the meaningful content (BCDX2 assembly, RAD51D interaction) is captured by
the GO:0033063 complex annotations.

## Curation summary
Core = BCDX2 subunit acting as RAD51-filament-assembly mediator in HR / ICL repair / replication
fork protection. Non-core/secondary = centrosome, mitotic cell cycle, meiotic cell cycle.
Over-annotations = protein binding (GO:0005515), ATP-dependent DNA damage sensor activity (GO:0140664).
