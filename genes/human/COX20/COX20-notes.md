# COX20 (FAM36A) review notes

UniProtKB:Q5RI15 · HGNC:26970 · gene 116228 · human chromosome 1.
118 aa, mitochondrial inner-membrane multi-pass protein (2 TM helices, aa 34-51 and 61-77;
N- and C-termini in intermembrane space, short matrix loop aa 52-60). Belongs to the COX20 family
(Pfam PF12597, InterPro IPR022533, TCDB 8.A.182). Isoforms 1 (canonical) and 2 (VSP_014855).

## Core biology (verified)

COX20 = mitochondrial inner-membrane assembly chaperone/scaffold for Complex IV (cytochrome c oxidase),
specific to the core catalytic subunit MT-CO2 (COX2). It is **non-catalytic**.

- Binds and stabilises newly synthesised MT-CO2 during insertion of its N-proximal TM domain, and
  chaperones it through membrane insertion and CuA copper metallation by SCO1/SCO2 (with COA6/COX18/TMEM177),
  delivering mature MT-CO2 into the assembling CIV holoenzyme.
  [PMID:24403053 abstract: "We propose that COX20 acts as a chaperone in the early steps of COX2 maturation,
  stabilizing the newly synthesized protein and presenting COX2 to its metallochaperone module, which in turn
  facilitates the incorporation of mature COX2 into the CIV assembly line."]
  [PMID:28330871 abstract: "We demonstrate that COX20 stabilizes COX2 during insertion of its N-proximal
  transmembrane domain ... The release of COX18 from this complex coincides with the binding of the
  SCO1-SCO2-COA6 copper metallation module to COX2-COX20 to finalize COX2 biogenesis."]
  [PMID:29154948 abstract: "Upon synthesis, COX2 engages with COX20 in the inner mitochondrial membrane,
  a scaffold protein that recruits metallochaperones for copper delivery to the CuA-Site of COX2."]

- Loss of COX20 → severe isolated CIV deficiency; cells accumulate COX1/COX4-containing CIV subassemblies
  almost devoid of COX2. [PMID:24403053; PMID:23125284]
  [PMID:23125284 abstract: "These results establish the function of the human gene FAM36A/COX20 in complex IV
  assembly and support a causal role of the gene in complex IV deficiency."]

- Disease: Mitochondrial complex IV deficiency, nuclear type 11 (MC4DN11; MIM:619054), autosomal recessive,
  childhood/adolescent onset — cerebellar ataxia, dystonia, choreoathetosis, dysarthria, muscle hypotonia,
  increased serum lactate. Recurrent variant T52P. [PMID:23125284; PMID:24202787; PMID:29154948]

## Localization

Mitochondrial inner membrane (GO:0005743): experimental (IDA/EXP) in PMID:23125284, PMID:24403053, PMID:29154948;
also broad "mitochondrion" (GO:0005739) IDA (HPA) and HTP (MitoCoP proteome, PMID:34800366).
[PMID:29154948 full text: COX20 described as "COX20-associated protein, residing in the inner membrane" and
"COX20 in the inner mitochondrial membrane".]

## Annotation assessment summary

- Complex IV assembly BP (GO:0033617): strongly supported experimentally (IMP PMID:23125284, PMID:24403053) +
  IBA + IEA → ACCEPT (core). This is the core biological process.
- Inner membrane CC (GO:0005743): experimental (IDA/EXP) + IEA + Reactome TAS → ACCEPT (core location).
- Mitochondrion CC (GO:0005739): broader parent of inner membrane; IBA/IDA/HTP → ACCEPT as non-core (redundant
  with the more precise inner-membrane term).
- protein binding (GO:0005515) IPI, many entries:
  - The mitochondrial physiological interactors (MT-CO2/COX2=P00403, SCO1=O43819, SCO2=O75880, COA6=Q5JTJ3,
    COX18=Q8N8Q8, TMEM177=Q53S58) from PMID:23125284/24403053/28330871/29154948 are meaningful (they underpin
    the assembly-chaperone role) but the GO term itself (bare "protein binding") is uninformative → MARK_AS_OVER_ANNOTATED
    (defer to curator; the biology is captured by the BP term). Not REMOVE (experimental IPI).
  - The HuRI large-scale binary Y2H interactome (PMID:32296183): AQP6, CHIA, CREB3L1, DYNC1H1, ERGIC3, FUNDC2,
    GET1, GJA8, GOLT1A, JAGN1, MAOB, MENT, NCBP2AS2, PGRMC2, SLC10A1, SLC10A6, TCEA2, TEX44, TMEM35A, TMX2 —
    almost all non-mitochondrial secretory/plasma-membrane proteins; high-throughput, no functional relevance to
    CIV assembly → MARK_AS_OVER_ANNOTATED (bare protein binding, HTP, biologically noise).

## Core MF decision

GOA carries NO catalytic or chaperone molecular-function term for COX20 (only bare GO:0005515 protein binding).
COX20 is a non-catalytic assembly chaperone. Per project policy, OMIT `molecular_function` from core_functions;
represent the core via directly_involved_in (GO:0033617) + locations (GO:0005743).

## Files / references
- file:human/COX20/COX20-uniprot.txt — UniProt Q5RI15 (FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, DISEASE, topology).
- Reactome R-HSA-9865630 (metallochaperone inserts 2Cu2+ into MT-CO2), R-HSA-9902096 (COX18 inserts nascent
  MT-CO2 in COX20:TMEM177) — inner-membrane TAS localization.
