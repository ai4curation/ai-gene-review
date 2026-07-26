# BRIP1 (FANCJ / BACH1) review notes

UniProt: Q9BX63 (FANCJ_HUMAN). Gene: BRIP1 (HGNC:20473). Synonyms: BACH1, FANCJ.
1249 aa. EC 5.6.2.3. Family: DEAD/DEAH box helicase, Rad3/XPD (DinG) subfamily.

## Identity / disambiguation (IMPORTANT)
BRIP1's old alias **BACH1** ("BRCA1-associated C-terminal helicase 1") collides with a
completely different gene, **BACH1 = BTB and CNC homology 1** (bZIP/BTB transcription
factor, transcriptional repressor of heme oxygenase-1; UniProt O14867). These are
unrelated proteins.

- **PMID:14504288** ("Cadmium induces nuclear export of Bach1, a transcriptional repressor
  of heme oxygenase-1 gene") is about the **transcription factor BACH1 (O14867)**, NOT
  BRIP1/FANCJ. The abstract concerns Bach1/small Maf heterodimers, ho-1 repression, Nrf2
  competition, Crm1/Exportin-1-dependent nuclear export — zero helicase/DNA-repair content.
  [PMID:14504288 "ho-1 is repressed by Bach1/small Maf heterodimers, it is activated by
  Nrf2/small Maf heterodimers"]. The three GOA annotations sourced from this PMID
  (nucleus IDA, cytoplasm IDA, and **regulation of transcription by RNA polymerase II**
  GO:0006357 IDA, all MGI-assigned) are mis-mapped via the BACH1 alias.
  - GO:0006357 (regulation of transcription by RNA Pol II) is uniquely from this paper and is
    biologically wrong for the FANCJ helicase → **REMOVE**.
  - nucleus/cytoplasm are coincidentally correct for BRIP1 (supported by valid refs), so those
    terms are retained overall, but this particular evidence line is flagged as mis-attributed.

## Core molecular function
5'-3' ATP-dependent DNA helicase; DNA-dependent ATPase; requires a [4Fe-4S] cluster.
- [PMID:14983014 "we show that BACH1 is both a DNA-dependent ATPase and a 5′-to-3′ DNA helicase"]
- [PMID:14983014 "its activity was greatly stimulated by CT DNA and M13 single-stranded DNA ...
  Purified BACH1-K52R lacked ATPase activity"] (DNA-dependent ATPase; K52R catalytic-dead)
- [PMID:14983014 "BACH1 preferentially displaced the 38-mer fragment ... indicating translocation
  in the 5′-to-3′ direction"]
- Catalytic activity (UniProt): EC 5.6.2.3 "Couples ATP hydrolysis with the unwinding of duplex
  DNA at the replication fork by translocating in the 5'-3' direction."
- Cofactor [4Fe-4S] cluster required for helicase activity: [PMID:20639400 "Purified recombinant
  FANCJ-A349P protein had reduced iron and was defective in coupling adenosine triphosphate (ATP)
  hydrolysis and translocase activity to unwinding forked duplex or G-quadruplex DNA substrates"];
  UniProt DOMAIN "4Fe-4S iron-sulfur-binding is required for helicase activity"
  (PMID:16973432 "The DNA repair helicases XPD and FancJ have essential iron-sulfur domains").
- DNA substrate specificity: prefers forked duplex; needs a minimal 5' ssDNA tail of ~15 nt;
  can release D-loop third strand; fails on Holliday junctions.
  [PMID:15878853 "BACH1 helicase requires a minimal 5 ' ssDNA tail of 15 nucleotides for
  unwinding of conventional duplex DNA substrates ... BACH1 completely fails to unwind a
  synthetic Holliday junction structure"]

## G-quadruplex unwinding
- [PMID:18426915 "FANCJ unwound G4 DNA substrates in an ATPase-dependent manner"]
- [PMID:18426915 "Replication protein A stimulated FANCJ G4 unwinding, whereas the mismatch
  repair complex MSH2/MSH6 inhibited this activity"]
- [PMID:18426915 "FANCJ preserves genomic stability by directly unwinding DNA roadblocks such
  as G4 structures that destabilize or impede the replication fork"]

## DNA-protein crosslink (DPC) repair at replication forks
- [PMID:36608669 "we identify a role for the 5'-to-3' helicase FANCJ in DPC repair. In addition
  to supporting CMG bypass, FANCJ is essential for SPRTN activation. FANCJ binds ssDNA
  downstream of the DPC and uses its ATPase activity to unfold the protein adduct, which exposes
  the underlying DNA and enables cleavage of the adduct"]
- Acts at the replication fork (IDA, PMID:36608669).

## Homologous recombination / DSB repair / BRCA1
- [PMID:11301010 "BRCA1 interacts in vivo with a novel protein, BACH1, a member of the DEAH
  helicase family. BACH1 binds directly to the BRCT repeats of BRCA1"]
- [PMID:11301010 "A BACH1 derivative, bearing a mutation in a residue that was essential for
  catalytic function in other helicases, interfered with normal double-strand break repair in a
  manner that was dependent on its BRCA1 binding function"]
- BRCA1 binding requires phospho-Ser990: PMID:14576433 (BRCT is a phospho-peptide binding domain;
  UniProt: "Phosphorylation is necessary for interaction with BRCA1, and is cell-cycle regulated").
- Part of the BRCA1-B complex (ComplexPortal CPX-4426): GO:0070532, PMID:16391231.

## Interstrand crosslink (ICL) repair / MutLalpha (MLH1)
- [PMID:17581638 "FANCJ interacts with the mismatch repair complex MutLalpha, composed of PMS2
  and MLH1. Specifically, FANCJ directly interacts with MLH1 independent of BRCA1, through its
  helicase domain"]
- [PMID:17581638 "FANCJ helicase activity and MLH1 binding, but not BRCA1 binding, are essential
  to correct the FA-J cells' ICL-induced 4N DNA accumulation and sensitivity to ICLs"]
- FANCJ acts late in the FA pathway, after FANCD2 ubiquitination (UniProt, PMID:16153896/14983014).

## Other interactions
- BLM helicase: [PMID:21240188 "FANCJ and BLM were found to interact physically and functionally
  in human cells and co-localize to nuclear foci in response to replication stress"]
- RPA (RPA1/RPA70): [PMID:17596542 "FANCJ and RPA were shown to coimmunoprecipitate most likely
  through a direct interaction of FANCJ and the RPA70 subunit ... RPA stimulates FANCJ helicase
  to better unwind duplex DNA substrates"]
- CIA machinery (CIAO1, CIAO2B/FAM96B, MMS19) — cytosolic Fe-S cluster assembly / maturation of
  the FANCJ Fe-S cluster: PMID:23585563 (interaction with CIAO1, CIAO2B and MMS19; UniProt SUBUNIT).
- Acetylation at K1249 regulates DDR: PMID:22792074 (UniProt PTM "Acetylation at Lys-1249
  facilitates DNA end processing required for repair and checkpoint signaling").

## Protein-binding (GO:0005515) IPI annotations
All IntAct/UniProt IPI protein-binding lines (BRCA1 P38398, MLH1 P40692, BLM P54132,
MMS19 Q96T76, HSD17B14 Q9BPX1) are uninformative MF (GO:0005515). Per curation guidelines,
marked MARK_AS_OVER_ANNOTATED; the biologically meaningful partners (BRCA1, MLH1, BLM, MMS19/CIA)
are captured in core_functions and BP annotations.

## Localization
Nucleus (core; nucleoplasm), functions at replication fork. Also cytoplasm (CIA/Fe-S maturation,
PMID:23585563). Nuclear membrane (HPA IDA GO:0031965) is a single HPA-antibody localization not
corroborated functionally → over-annotated. Testis-high expression (UniProt tissue specificity).

## Disease
Biallelic loss → Fanconi anemia complementation group J (FANCJ, MIM:609054); monoallelic variants
→ breast/ovarian cancer susceptibility (BC MIM:114480). FANCJ variants A349P (Fe-S), K52R
(Walker A, catalytic-dead), P47A/M299I (breast cancer, helicase-defective).

## NER (GO:0006289) IBA
No FANCJ-specific evidence for classical nucleotide-excision repair; the IBA propagates the
Rad3/XPD family function (XPD does NER) onto FANCJ. FANCJ's characterized roles are ICL/HR/DPC/G4,
not NER → MARK_AS_OVER_ANNOTATED.

## NEW annotations added
- GO:0036297 interstrand cross-link repair (BP) — FANCJ's central biological role
  (PMID:17581638, PMID:18426915; UniProt DISEASE/FUNCTION).
- GO:0051539 4 iron, 4 sulfur cluster binding (MF) — experimentally required cofactor
  (PMID:20639400, PMID:16973432; UniProt COFACTOR/BINDING).
</content>
</invoke>
