# GLS (human) — review notes

UniProt: O94925 (GLSK_HUMAN), "Glutaminase kidney isoform, mitochondrial"; gene GLS (syn. GLS1, KIAA0838); 669 aa precursor. HGNC:4331. EC 3.5.1.2.

## Identity and core biochemistry

GLS is the kidney-type / phosphate-activated glutaminase. Two catalytically active isoforms exist by alternative splicing: **KGA** (isoform 1, O94925-1) and **GAC / Glutaminase C** (isoform 3, O94925-3); a third splice product **GAM** (isoform 2, O94925-2) lacks catalytic activity.
- Catalytic reaction (UniProt CATALYTIC ACTIVITY): [file:human/GLS/GLS-uniprot.txt "Reaction=L-glutamine + H2O = L-glutamate + NH4(+)"]; EC=3.5.1.2; Rhea:RHEA:15889.
- FUNCTION (UniProt): [file:human/GLS/GLS-uniprot.txt "Catalyzes the first reaction in the primary pathway for the"] renal catabolism of glutamine; plays a role in maintaining acid-base homeostasis; regulates the levels of the neurotransmitter glutamate.
- Isoform 2 (GAM): [file:human/GLS/GLS-uniprot.txt "Lacks catalytic activity."]
- [PMID:22049910 "Glutaminase (GLS1/2) catalyzes the conversion of L-glutamine to L-glutamate and ammonia."]
- [PMID:24451979 "Glutaminase controls the first step in the glutaminolysis pathway by converting glutamine (Gln) to glutamate (Glu), with subsequent enzymatic reactions generating aspartate, malate, pyruvate, citrate, alanine, and lactate"] — feeds glutamate into the TCA cycle (glutaminolysis/anaplerosis).
- [PMID:11015561 "One isoform contains an open reading frame with high homology with the rat kidney-type glutaminase, suggesting that this isoform represents the human kidney-type glutaminase, hKGA."] and the catalytically inactive hGAM is muscle-specific.

## Subcellular location

Mitochondrion; the mature enzyme is generated from a ~74-kDa cytosolic precursor imported and processed by the mitochondrial-processing peptidase (MPP) to 68-/65-kDa matrix chains.
- [file:human/GLS/GLS-uniprot.txt "The 74-kDa cytosolic precursor is"] translocated into the mitochondria and processed... to yield the mature 68- and 65-kDa subunits.
- Matrix chains: [file:human/GLS/GLS-uniprot.txt "Mitochondrion matrix {ECO:0000250|UniProtKB:P13264}."]
- GAC is distinctly mitochondrial: [PMID:22228304 "GAC is distinctly mitochondrial"].
- Brain GA cDNA encodes a protein with an N-terminal mitochondrial targeting signal: [PMID:10719215 "N-terminal mitochondrial targeting signal"].
- KGA can be relocalised from mitochondria to neurite terminals by ATCAY/Caytaxin: [PMID:16899818 "relocalised \nKGA from the mitochondria to neurite terminals"].
- The cytosol annotation (GO:0005829, IEA UniProtKB-SubCell) reflects the cytosolic precursor stage of isoform 1 before mitochondrial import ([file:human/GLS/GLS-uniprot.txt "Cytoplasm, cytosol"]); it is a real but non-core, transient localization.

## Quaternary structure / regulation

- Homotetramer, dimer of dimers (UniProt SUBUNIT, citing PubMed:22538822, 26988803, 28526749, 29317493). Tetramerization is coupled to activation.
- Phosphate-activated; BPTES/CB-839-class allosteric inhibitors bind at the dimer interface and lock a nonproductive tetramer.
  - [PMID:22049910 "Two BPTES molecules bind at an interface region of the GAC \ntetramer in a manner that appears to lock the GAC tetramer into a nonproductive \nconformation."]
  - Phosphate activation / tetramerization: [PMID:22228304 "the \ntetramerization-induced lifting of a \"gating loop\" as essential for the \nphosphate-dependent activation process"].
- Active-site catalytic residues (KGA numbering): catalytic nucleophile Ser286, Lys289 general base, Tyr466; substrate/active-site residues Tyr249, Asn335, Glu381, Asn388, Tyr414, Val484 ([PMID:24451979]). DON covalently modifies Ser286.
- KGA activity is stimulated by EGF/Raf-Mek-Erk phosphorylation and the enzyme associates with RAF1/MAP2K2 ([PMID:22538822]); interacts with ATCAY (Caytaxin), which relocalises it and reduces its activity ([PMID:16899818]).
- C-terminal ANK repeats: [PMID:28526749] — glutaminase ANK repeats fold via intramolecular contacts that occlude the usual ANK protein-protein-interaction surface and limit assembly into supra-tetrameric filaments.

## Biological roles

- Glutaminolysis / anaplerosis: first, committed step feeding glutamate to TCA (via GLUD1/transaminases -> alpha-ketoglutarate). Central to cancer "glutamine addiction"; drug target (CB-839/telaglenastat, BPTES).
  - [PMID:29317493 "This requirement is met by the overexpression of glutaminase C \n(GAC), which catalyzes the first step in glutamine metabolism and therefore \nrepresents a potential therapeutic target."]
- Renal ammoniagenesis / acid-base homeostasis (UniProt FUNCTION).
- Brain glutamate-glutamine cycle: supplies neurotransmitter glutamate.
  - [PMID:16899818 "KGA converts glutamine to glutamate, which could serve as an important \nsource of neurotransmitter."]
- Intracellular glutamate homeostasis: gain-of-function Ser482Cys causes hyperactivity, increased glutamate/decreased glutamine.
  - [PMID:30239721 "increased glutamate and decreased glutamine \nconcentrations were measured in urine and fibroblasts"]; "we describe an inborn error of glutamate metabolism caused by a GLS hyperactivity variant".

## Disease

- **DEE71** (developmental & epileptic encephalopathy 71; MIM 618328): autosomal recessive, loss-of-function (UniProt DISEASE; PubMed:30575854).
- **CASGID** (cataract, subcutaneous nodules, glutamate excess, developmental delay; MIM 618339): autosomal dominant, gain-of-function Ser482Cys ([PMID:30239721]).
- **GDPAG** (global developmental delay, progressive ataxia, elevated glutamine; MIM 618412): autosomal recessive, GAG/short-tandem-repeat expansion loss-of-function (UniProt DISEASE; PubMed:30970188).

## Annotation review judgments (summary)

- Core MF: **glutaminase activity (GO:0004359)** — strongly supported by multiple EXP/IDA structural-enzymology papers and UniProt catalytic activity. ACCEPT.
- Core BP: **L-glutamine catabolic process (GO:0006543)** and **L-glutamate biosynthetic process (GO:0097054)** — the two faces of the same reaction; both directly supported (IDA PMID:22049910). ACCEPT.
- Location: **mitochondrion (GO:0005739)** core; **mitochondrial matrix (GO:0005759)** the specific matrix location of the mature chains. ACCEPT.
- **protein homotetramerization (GO:0051289)** — real quaternary-structure property (dimer of dimers); KEEP_AS_NON_CORE (structural, not the pathway function).
- **intracellular glutamate homeostasis (GO:0090461)** IMP PMID:30239721 — supported by the gain-of-function disease study; ACCEPT (organism-level consequence of the MF).
- **negative regulation of L-glutamine biosynthetic process (GO:0062133)** IDA PMID:16899818 — the paper shows ATCAY/Caytaxin *inhibits* KGA and reduces glutamate; it is not evidence that GLS negatively regulates glutamine *biosynthesis*. This BP term is a poor fit for GLS's own activity (glutamine catabolism, not regulation of glutamine synthesis). MARK_AS_OVER_ANNOTATED (experimental IDA — do not REMOVE).
- **protein binding (GO:0005515)** IPI PMID:16899818 with ATCAY (Q86WG3) — bare protein binding; keep as evidence of the direct ATCAY interaction but MARK_AS_OVER_ANNOTATED (uninformative MF); the biology is captured in notes/core.
- IEA/IBA/ISS/NAS/TAS/HTP duplicates of the above accepted terms: ACCEPT or KEEP_AS_NON_CORE per redundancy.
- **amino acid metabolic process (GO:0006520)** IEA (ARBA) and **L-glutamine metabolic process (GO:0006541)** IEA (InterPro) — correct but general parents of the specific catabolic term; KEEP_AS_NON_CORE / MODIFY toward the specific GO:0006543.
</content>
</invoke>
