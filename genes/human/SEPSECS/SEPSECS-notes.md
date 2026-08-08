# SEPSECS (Q9HD40) — Gene Review Notes

## Identity and nomenclature

- HGNC symbol: **SEPSECS**; synonym TRNP48. UniProt Q9HD40, `SPCS_HUMAN`, 501 aa, chromosome 4.
- RecName: **O-phosphoseryl-tRNA(Sec) selenium transferase**; EC **2.9.1.2** [file:human/SEPSECS/SEPSECS-uniprot.txt "RecName: Full=O-phosphoseryl-tRNA(Sec) selenium transferase; ... EC=2.9.1.2"].
- Many AltNames reflect its history as an autoantigen: **Liver-pancreas antigen (LP)**, **SLA-p35**, **SLA/LP autoantigen**, **Soluble liver antigen (SLA)**, **Selenocysteine synthase / Sec synthase**, **Sep-tRNA:Sec-tRNA synthase (SepSecS)**, **UGA suppressor tRNA-associated protein**, **tRNA(Ser/Sec)-associated antigenic protein** [file:human/SEPSECS/SEPSECS-uniprot.txt "AltName: Full=Selenocysteine synthase; Short=Sec synthase"].

## Molecular function (catalysis)

- Final (terminal) step of selenocysteine (Sec) biosynthesis, which uniquely occurs **on the cognate tRNA** in archaea/eukaryotes.
- CATALYTIC ACTIVITY (RHEA:25041): **O-phospho-L-seryl-tRNA(Sec) + selenophosphate + H2O = L-selenocysteinyl-tRNA(Sec) + 2 phosphate**, EC 2.9.1.2 [file:human/SEPSECS/SEPSECS-uniprot.txt "Reaction=O-phospho-L-seryl-tRNA(Sec) + selenophosphate + H2O = L- selenocysteinyl-tRNA(Sec) + 2 phosphate"].
- FUNCTION: "Converts O-phosphoseryl-tRNA(Sec) to selenocysteinyl- tRNA(Sec) required for selenoprotein biosynthesis." [file:human/SEPSECS/SEPSECS-uniprot.txt] (ECO:0000269|PubMed:17142313).
- **PLP (pyridoxal 5'-phosphate)-dependent enzyme**: COFACTOR = pyridoxal 5'-phosphate (ECO:0000269|PubMed:17142313, PubMed:19608919). PLP is covalently bound via Schiff base to Lys284 (MOD_RES 284 = N6-(pyridoxal phosphate)lysine) [file:human/SEPSECS/SEPSECS-uniprot.txt].
- Belongs to the **SepSecS family**, a distinct branch of **fold-type I PLP enzymes** [PMID:19608919 "SepSecS forms its own branch in the family of fold-type I pyridoxal phosphate (PLP) enzymes that goes back to the last universal common ancestor"].

### Mechanism (PMID:17142313, PMID:19608919)

- Two-step eukaryal/archaeal Sec route: Ser is charged onto tRNA(Sec) by SerRS → PSTK phosphorylates it to Sep-tRNA(Sec) → **SepSecS converts Sep-tRNA(Sec) to Sec-tRNA(Sec)** using selenophosphate (from SEPHS2/SelD) as the Se donor [PMID:17142313 "O-phosphoseryl-tRNA(Sec) kinase (PSTK) converts Ser-tRNA(Sec) to Sep-tRNA(Sec). This misacylated tRNA is the obligatory precursor for a Sep-tRNA:Sec-tRNA synthase (SepSecS)"].
- SepSecS acts on **phosphoserine linked to tRNA(Sec), not free phosphoserine or Ser-tRNA(Sec)** [PMID:19608919 "SepSecS acts on phosphoserine that is linked to tRNASec and not on free phosphoserine or Ser-tRNASec"].
- PLP-based mechanism: amino group of Sep attacks the Lys284–PLP Schiff base → external aldimine → β-elimination of phosphate → dehydroalanyl-tRNA(Sec) intermediate → nucleophilic attack of selenium from selenophosphate → Sec-tRNA(Sec) [PMID:19608919 "The reaction begins by the covalently attached Sep being brought into the proximity of the Schiff base ... rapid β-elimination of the phosphate group, which produces an intermediate dehydroalanyl-tRNASec"].
- Reduction of the Schiff base (NaBH4 cross-linking PLP to Lys284) or removal of PLP (hydroxylamine) renders SepSecS **completely inactive** — confirms PLP dependence [PMID:19608919 "the reduction of the Schiff base by sodium borohydride ... renders SepSecS completely inactive in vitro. The catalytic activity of SepSecS is also quenched on removal of PLP"].
- Human and archaeal SepSecS complement an *E. coli* SelA (Sec synthase) deletion in vivo; purified recombinant SepSecS converts Sep-tRNA(Sec) to Sec-tRNA(Sec) in vitro with Na-selenite + SelD (in vitro validation) [PMID:17142313 "purified recombinant SepSecS converts Sep-tRNA(Sec) into Sec-tRNA(Sec) in vitro"].
- Lys284→Ala abolishes activity (MUTAGEN); active-site/tRNA-binding residues Arg75, Gln105, Arg313 (substrate/PLP phosphate) and Arg398 (discriminator base G73), Arg271 (variable arm) are catalytically/recognition critical [file:human/SEPSECS/SEPSECS-uniprot.txt; PMID:19608919].

## tRNA binding / substrate

- SepSecS binds the **acceptor-, TΨC-, and variable arms of tRNA(Sec)** [PMID:19608919 "SepSecS binds only to the acceptor-, TΨC-, and variable arms of tRNASec"].
- Recognition via discriminator base G73 (↔ Arg398) and the unusual 13-bp acceptor-TΨC arm / long variable arm of the 90-nt tRNA(Sec); tRNA(Ser) cannot bind (shorter acceptor-TΨC arm) [PMID:19608919].
- tRNA binding induces conformational changes that organize the catalytic protomer's active site — tRNA-dependent activation [PMID:36929010 "tRNASec binding organizes the active sites of the catalytic protomer, while stabilizing the N- and C-termini of the non-catalytic protomer"].
- Historically identified as the antigen of the **tRNP(Ser)Sec** ribonucleoprotein (SLA/LP), i.e. the tRNA(Sec)-associated antigenic protein [PMID:10801173].

## Quaternary structure / complex

- **Homotetramer** = catalytic dimer + non-catalytic dimer; the non-catalytic dimer is a binding platform orienting tRNA(Sec) for catalysis; each tetramer binds two tRNA(Sec) via their CCA ends pointing to the catalytic dimer's active sites [file:human/SEPSECS/SEPSECS-uniprot.txt "Homotetramer formed by a catalytic dimer and a non-catalytic dimer serving as a binding platform"; PMID:19608919 "Two SepSecS monomers form a homodimer ... The two homodimers associate into a tetramer"].
- Also reported as component of a wider complex with **SEPHS1, SEPHS2, SEPSECS and TRNAU1AP (SECp43)** (supramolecular Sec machinery) [file:human/SEPSECS/SEPSECS-uniprot.txt "Component of a complex composed of SEPHS1, SEPHS2, SEPSECS and TRNAU1AP"; PMID:28414460 "selenocysteine synthase (SEPSECS), SECp43, and selenophosphate synthetases SEPHS1 and SEPHS2 form oligomers in eukaryotic cells"].
- ComplexPortal CPX-26538 "SepSecS-tRNASec complex" (referenced by GOA ComplexPortal annotations to GO:0005829 cytosol and GO:1990234 transferase complex, PMID:36929010).

## Subcellular location

- **Cytoplasm / cytosol** [file:human/SEPSECS/SEPSECS-uniprot.txt "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:28414460}"]. No credible evidence for a nuclear function; the nucleus annotations are ISS/IEA transfers from mouse ortholog Q6P6M7 and are treated as over-annotations.

## Biological process

- **Selenocysteinyl-tRNA(Sec) biosynthesis** (UniPathway UPA00906, UER00898): "Aminoacyl-tRNA biosynthesis; selenocysteinyl-tRNA(Sec) biosynthesis; selenocysteinyl-tRNA(Sec) from L-seryl-tRNA(Sec) (archaeal/eukaryal route): step 2/2." [file:human/SEPSECS/SEPSECS-uniprot.txt].
- Feeds selenoprotein synthesis: charged Sec-tRNA(Sec) is delivered by EEFSEC to recode UGA codons during translation [PMID:19608919 "UGA is recoded by the interaction of a specialized elongation factor ... EFsec in humans"].
- GO:0001514 "selenocysteine incorporation" is the downstream translational process the whole Sec pathway serves; SEPSECS is upstream (tRNA charging) rather than itself the ribosomal incorporation step, but is legitimately annotated `involved_in` this process.

## Disease

- **Pontocerebellar hypoplasia type 2D (PCH2D) [MIM:613811]** / progressive cerebello-cerebral atrophy — autosomal recessive; postnatal progressive cerebral+cerebellar atrophy, microcephaly, profound intellectual disability, spasticity, seizures [file:human/SEPSECS/SEPSECS-uniprot.txt "Pontocerebellar hypoplasia 2D (PCH2D)"; PMID:20920667].
- Pathogenic missense variants: **A239T** and **Y334C** both abrogate enzyme activity (VARIANT, characterized) [file:human/SEPSECS/SEPSECS-uniprot.txt "A -> T (in PCH2D; abrogates enzyme activity)"]; also T325S [PMID:26115735]. Establishes that loss of SepSecS catalytic activity (loss of selenoprotein biosynthesis) is the disease mechanism.

## Term-by-term reasoning (see YAML)

Core molecular function = **GO:0098621** O-phosphoseryl-tRNA(Sec) selenium transferase activity (IDA, PMID:17142313) + **GO:0030170** pyridoxal phosphate binding (cofactor). Core BP = **GO:0001717** conversion of seryl-tRNAsec to selenocys-tRNAsec (IDA) and the broader **GO:0016260** L-selenocysteine biosynthetic process. tRNA binding (GO:0000049) is a genuine, well-supported MF (structural + TAS). Cytoplasm/cytosol (GO:0005737/GO:0005829) accepted. Nucleus (GO:0005634, ISS/IEA from mouse) = over-annotation. Generic GO:0016740 transferase activity (IEA) is a redundant parent of GO:0098621. GO:0005515 protein binding (IPI, HIV gag) kept as non-core (uninformative; not a native functional partner). GO:1990234 transferase complex (part_of, ComplexPortal) accepted as non-core CC (the SepSecS tetramer / Sec machinery complex).

Note: GO:0097056 "selenocysteinyl-tRNA(Sec) biosynthetic process" is now **obsolete**, replaced by GO:0001717 — do not introduce it.
