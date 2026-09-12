# NDUFS8 (TYKY) review notes

UniProtKB: O00217. HGNC:7715. Gene 4728. 210 aa precursor (transit peptide 1-34,
mature chain 35-210). AltNames: Complex I-23kD / CI-23kD; NADH-ubiquinone
oxidoreductase 23 kDa subunit; TYKY subunit.

## Function (grounded in UniProt + literature)

NDUFS8 is a **core (catalytic) subunit of mitochondrial respiratory Complex I**
(NADH:ubiquinone oxidoreductase, EC 7.1.1.2). UniProt FUNCTION: "Core subunit of the
mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I) which catalyzes
electron transfer from NADH through the respiratory chain, using ubiquinone as an
electron acceptor (PubMed:22499348). Essential for the catalytic activity and assembly
of complex I (PubMed:22499348)."

**Two [4Fe-4S] clusters.** The mature protein contains two 4Fe-4S ferredoxin-type
domains (residues 102-131 and 141-170), each coordinating a [4Fe-4S] cluster via four
cysteines (BINDING sites 111/114/117/121 for cluster 1; 150/153/156/160 for cluster 2).
UniProt COFACTOR: "Binds 2 [4Fe-4S] cluster." These clusters (N6a and N6b in Complex I
nomenclature) form part of the electron-transfer wire from NADH (via FMN and the other
Fe-S clusters) to ubiquinone. Historically the TYKY subunit's ferredoxin patterns were
thought to bind cluster N-2 [PMID:9837812, "contains two 4Fe4S ferredoxin consensus
patterns, which have long been thought to provide the binding site for the iron-sulfur
cluster N-2"].

InterPro: IPR010226 (NADH_quinone_OxRdtase_chainI); Pfam PF12838 (Fer4_7); belongs to
the complex I 23 kDa subunit family; part of the iron-sulfur (IP) fragment of Complex I.
Prokaryotic ortholog is NuoI (E. coli). Highly conserved across eukaryotes and
prokaryotes.

## Localization

Mitochondrion inner membrane (peripheral membrane protein, matrix side)
[UniProt SUBCELLULAR LOCATION, ECO:0000305|PubMed:12611891, ECO:0000305|PubMed:9666055].
Anatomical location term for the review = GO:0005743 mitochondrial inner membrane.
Complex I membership = GO:0045271 respiratory chain complex I.

## Disease

Mitochondrial complex I deficiency, nuclear type 2 (MC1DN2) [MIM:618222], autosomal
recessive. First nuclear-encoded Complex I mutation linked to Leigh syndrome was in
NDUFS8 [PMID:9837812]. Compound heterozygous mutations cause complex I deficiency /
(late-onset) Leigh syndrome [PMID:15159508, PMID:22499348, PMID:16142472]. Patient
variants (E63Q, R77W, A159D) decrease enzyme activity and impair complex I assembly;
WT cDNA rescue restores complex I activity and assembly [PMID:22499348].

## Key references / supporting quotes used

- PMID:22499348 (Haack 2012): "rare variants in NDUFS8 in two unrelated individuals";
  "Expression of wild-type cDNA in mutant cell lines rescued complex I activity and
  assembly, thus providing a functional validation of their pathogenicity." Basis for
  the FUNCTION/CATALYTIC ACTIVITY (EC 7.1.1.2) and complex I assembly IMP annotations.
- PMID:9666055 (de Sury 1998): genomic structure; "TYKY subunit of the human
  mitochondrial NADH:ubiquinone oxidoreductase (Complex I)"; ubiquitous expression,
  predominant in heart and skeletal muscle; matrix/inner-membrane localization.
- PMID:9837812 (Loeffen 1998): first nuclear complex I mutation -> Leigh; two 4Fe4S
  ferredoxin consensus patterns.
- PMID:9878551 (Loeffen 1998 BBRC): "Its main function is the transport of electrons
  from NADH to ubiquinone, which is accompanied by translocation of protons from the
  mitochondrial matrix to the intermembrane space." Complex I located in inner
  mitochondrial membrane.
- PMID:12611891 (Murray 2003): subunit composition of human complex I by
  immunopurification; NDUFS8 identified in the complex.
- PMID:11112787 (Triepels 2001): monoclonal-antibody resolution of complex I assembly
  defects, including an NDUFS8 patient; assembly/subunit-profile analysis.
- PMID:14749350 (Ugalde 2004): BN-PAGE of complex I assembly/stability in patients.
- PMID:15159508 (Procaccio 2004): "this subunit is essential for either the assembly or
  stability of complex I."
- PMID:28844695 (Guo 2017): cryo-EM megacomplex I2III2IV2; assigns individual CI
  subunits (structural basis for complex I membership, inner-membrane location).
- PMID:30030361 (Signes 2018): OXPHOS assembly review; core proteins perform catalytic
  activities; aerobic respiration / proton-motive-force ATP synthesis context (NAS).
- PMID:31536960 (Moutaoufik 2019): mitochondrial interactome / co-fractionation; basis
  for the RAB5IF (Q9BUV8) interaction IPI and a complex I membership IDA.
- PMID:34800366 (Morgenstern 2021): high-confidence human mitochondrial proteome (HTP);
  supports mitochondrion localization.

## Curation decisions summary

Core MF present in GOA: GO:0051539 (4 iron, 4 sulfur cluster binding, IEA/InterPro) and
GO:0008137 (NADH dehydrogenase (ubiquinone) activity). Both accepted; used in
core_functions. GO:0008137 IMP (PMID:22499348) accepted; the enzymatic reaction is a
property of the whole complex, so contributes_to on GO:0003954 kept.

CC: complex I = GO:0045271 (many redundant lines, all ACCEPT). Inner membrane =
GO:0005743 (ACCEPT). Reactome GO:0005759 mitochondrial matrix (TAS x11) — mitochondrion
inner membrane, matrix-facing peripheral protein; matrix is a defensible coarse
localization but less precise than inner membrane; MARK_AS_OVER_ANNOTATED (the more
informative inner-membrane term is already present, and UniProt/structure place it as an
inner-membrane peripheral protein, matrix side, not a soluble matrix protein). GO:0016020
membrane (IEA) — MODIFY to GO:0005743 (too general, more specific term available and
already annotated). GO:0005739 mitochondrion (IDA/HTP) — ACCEPT (coarse but correct).

BP: GO:0006120 (electron transport NADH->ubiquinone) ACCEPT (core); GO:0032981 (complex
I assembly) ACCEPT; GO:0009060 aerobic respiration and GO:0042776 proton-motive-force
ATP synthesis (NAS, ComplexPortal) KEEP_AS_NON_CORE (whole-complex/pathway-level, not
this subunit's direct MF); GO:1902600 proton transmembrane transport (IEA from
GO:0008137) MARK_AS_OVER_ANNOTATED (proton pumping is done by the membrane arm ND
subunits, not the IP-fragment TYKY subunit).

MF over-generalizations: GO:0016651 (oxidoreductase acting on NAD(P)H, IEA) MODIFY ->
GO:0008137. GO:0003954 NADH dehydrogenase activity (contributes_to) ACCEPT (correct
whole-complex contribution).

GO:0005515 protein binding IPI (RAB5IF) — MARK_AS_OVER_ANNOTATED per policy (bare
protein binding, uninformative; do not REMOVE an IPI).
</content>
</invoke>
