# GNE (Q9Y223) review notes

## Summary of gene function

GNE is the human **bifunctional UDP-N-acetylglucosamine 2-epimerase / N-acetylmannosamine kinase**
(EC 3.2.1.183 + EC 2.7.1.60), the enzyme that catalyzes the first two committed, rate-limiting steps
of the de novo sialic acid (N-acetylneuraminic acid, Neu5Ac) biosynthetic pathway. It is a cytosolic
722-aa protein with two catalytic domains:

- **N-terminal epimerase domain** (UDP-N-acetylglucosamine 2-epimerase family): converts
  UDP-N-acetyl-alpha-D-glucosamine (UDP-GlcNAc) + H2O to N-acetyl-D-mannosamine (ManNAc) + UDP + H+.
  This is a *hydrolyzing* epimerase (EC 3.2.1.183), distinct from the non-hydrolyzing bacterial
  cell-wall enzymes.
- **C-terminal kinase domain** (ROK / NagC-XylR family): phosphorylates ManNAc with ATP to
  ManNAc-6-phosphate (EC 2.7.1.60).

[file:human/GNE/GNE-uniprot.txt "Bifunctional enzyme that possesses both UDP-N- acetylglucosamine 2-epimerase and N-acetylmannosamine kinase activities, and serves as the initiator of the biosynthetic pathway leading to the production of N-acetylneuraminic acid (NeuAc)"]

The two GNE-catalyzed reactions feed ManNAc-6-P into the downstream pathway (Neu5Ac-9-P synthase NANS,
phosphatase NANP, cytidylyltransferase CMAS) that produces CMP-Neu5Ac, the activated sialic acid donor
used by sialyltransferases. GNE thereby governs overall cell-surface sialylation.
[PMID:26980148 "Sialic acid biosynthesis in mammals starts by converting UDP-GluNAc into UDP and ManNAc, followed by phosphorylation of ManNAc at the sixth position"]

## Catalytic activities (UniProt CATALYTIC ACTIVITY block)

- Epimerase: `UDP-N-acetyl-alpha-D-glucosamine + H2O = aldehydo-N-acetyl-D-mannosamine + UDP + H(+)`;
  RHEA:30683; EC=3.2.1.183 (ECO:0000269 PubMed:11326336, 14707127, 16503651, 26980148, 2808337).
- Kinase: `an N-acyl-D-mannosamine + ATP = an N-acyl-D-mannosamine 6-phosphate + ADP + H(+)`;
  RHEA:23832; EC=2.7.1.60 (ECO:0000269 PubMed:14707127, 16503651).

[file:human/GNE/GNE-uniprot.txt "Reaction=UDP-N-acetyl-alpha-D-glucosamine + H2O = aldehydo-N-acetyl-D-"] (line wraps in UniProt file)

## Feedback regulation (rate-limiting, allosteric)

The epimerase activity (but NOT the kinase activity) is allosterically **feedback-inhibited by
CMP-Neu5Ac**, the end product of the pathway. This makes GNE the rate-controlling enzyme of sialic
acid production.
[file:human/GNE/GNE-uniprot.txt "The UDP-N-acetylglucosamine 2-epimerase activity, in contrast to the N-acetylmannosamine kinase activity, exhibits"] ... [file:human/GNE/GNE-uniprot.txt "allosteric regulation by cytidine monophosphate-N-acetylneuraminic acid"]

The crystal structure of the human epimerase domain with UDP + CMP-Neu5Ac (PMID:26980148) shows a
tetramer locked in a closed conformation, with CMP-Neu5Ac bound at the dimer-dimer interface and
Arg263/Arg266 (sialuria mutation sites) contacting the inhibitor.
[PMID:26980148 "it is feed-back inhibited by the downstream product CMP-Neu5Ac"]
[PMID:26980148 "the CMP-Neu5Ac binding mode clearly elucidates why mutations in Arg263 and Arg266 can cause sialuria"]

## Disease associations (loss of function vs superactivity)

- **Sialuria (MIM:269921)** — autosomal *dominant*; caused by loss of CMP-Neu5Ac feedback inhibition
  of the epimerase (R263L, R266Q, R266W in the allosteric site), producing constitutive Neu5Ac
  overproduction and massive urinary sialic acid excretion.
  [PMID:2808337 "the basic defect in sialuria has been identified unequivocally as the loss of feedback control of uridine diphosphate N-acetylglucosamine 2-epimerase by cytidine monophosphate N-acetylneuraminic acid with resultant overproduction of sialic acid"]
  [file:human/GNE/GNE-uniprot.txt "The metabolic defect involves lack of"] ... [file:human/GNE/GNE-uniprot.txt "feedback inhibition of UDP-GlcNAc 2-epimerase by CMP-Neu5Ac, resulting"]

- **GNE myopathy / Nonaka myopathy (NM, MIM:605820) = hereditary inclusion body myopathy (HIBM/IBM2) =
  distal myopathy with rimmed vacuoles (DMRV)** — autosomal *recessive* loss-of-function; hyposialylation
  of muscle glycoproteins. Missense mutations spread across both epimerase and kinase domains reduce one
  or both activities.
  [PMID:14707127 "we identified pathogenic mutations in the gene encoding the bifunctional enzyme UDP-GlcNAc 2-epimerase/ManNAc kinase"]
  [PMID:14707127 "the levels of sialic acid in muscle and primary cultured cells from DMRV patients were reduced to 60-75% of control"]
  [PMID:16503651 "Each of the mutants that was analyzed displayed a reduction in the two known GNE activities"]

- **Thrombocytopenia 12 with or without myopathy (THC12, MIM:620757)** — autosomal recessive; decreased
  platelet sialylation. (UniProt DISEASE block; multiple case reports.)

## Localization

Cytoplasm, cytosol.
[file:human/GNE/GNE-uniprot.txt "SUBCELLULAR LOCATION: Cytoplasm, cytosol"]
IDA cytosol from HPA immunofluorescence (GO_REF:0000052); ISS from mouse ortholog O35826.

## Protein interactions (IPI annotations = bare "protein binding")

- **PMID:18560563** — GNE binds **alpha-actinin 1 (ACTN1)** in skeletal muscle (SPR biosensor + in vitro
  binding + co-IP). This is a specific, biologically-motivated interaction (searching for muscle-specific
  GNE partners relevant to HIBM), but the GO annotation is only the uninformative `protein binding`
  (GO:0005515). Keep, but mark as over-annotated / non-core.
  [PMID:18560563 "revealed alpha-actinin 1 as a potential interactor of GNE"]
- **PMID:25416956** (Rolland et al., human interactome / Y2H HI-II-14) and **PMID:31515488** (Fragoza
  et al., interactome variant disruption) — high-throughput interactome `protein binding` IPI annotations
  to numerous partners (keratins, keratin-associated proteins, SPRY, NOTCH2NL, etc.; see UniProt
  INTERACTION block). These are systematic-screen bindings with no established functional consequence for
  GNE's enzymatic role. Over-annotation of the uninformative `protein binding` term.

## Annotation review decisions (high level)

Core molecular functions:
- **GO:0008761 UDP-N-acetylglucosamine 2-epimerase activity** — CORE (epimerase domain). Strong
  experimental support: IDA PMID:26980148, IDA PMID:2808337, IMP PMID:14707127. (Note: GO:0008761 is
  the standard GO term GOA/UniProt/Reactome assign for this activity; its def/xrefs are the
  epimerization, and it is xreffed to the exact Reactome reactions cited here. GNE's physiological
  reaction is the *hydrolyzing* variant EC 3.2.1.183, but no separate GO term exists — GO:0008761 is
  correct/accepted.)
- **GO:0009384 N-acylmannosamine kinase activity** — CORE (kinase domain). EXP PMID:16503651, IMP
  PMID:14707127. (Current GO label is "N-acylmannosamine", the general acyl form; ManNAc is the
  physiological substrate; xreffed to EC:2.7.1.60.)

Core biological process:
- **GO:0046380 N-acetylneuraminate biosynthetic process** — CORE. IMP PMID:14707127, IMP PMID:31121216.
- **GO:0006055 CMP-N-acetylneuraminate biosynthetic process** — keep (IMP PMID:31121216 KO shows
  CMP-sialic acid dramatically reduced); slightly downstream framing but supported.

Supporting / non-core / over-annotation:
- `GO:0006047 UDP-N-acetylglucosamine metabolic process` (IEA InterPro) — true but general; substrate side.
- `GO:0006045 N-acetylglucosamine biosynthetic process` (IEA UniPathway) — MISLEADING: GNE consumes
  UDP-GlcNAc; it does not *biosynthesize* GlcNAc. The UniPathway mapping (UPA00630) captures the
  amino-sugar pathway container but the specific term is the wrong direction. Recommend MARK_AS_OVER_ANNOTATED.
- `GO:0004553 hydrolase activity, hydrolyzing O-glycosyl compounds` (IEA InterPro) — the epimerase is
  formally hydrolyzing, but this broad glycosidase term does not describe GNE's actual reaction (it is
  not an O-glycosidase); over-annotation from the InterPro 2-epimerase signature.
- `GO:0005515 protein binding` (IPI x3) — keep per policy, mark over-annotated (uninformative).
- cytosol (IEA/IDA/ISS/TAS) — accept location; one representative kept as core-supporting.

## Term id verification (go.db, local)

- GO:0008761 = "UDP-N-acetylglucosamine 2-epimerase activity" (def: UDP-N-acetyl-D-glucosamine =
  UDP-N-acetyl-D-mannosamine; xref EC:5.1.3.14, Reactome R-HSA-4085021, R-HSA-4088338) — not obsolete.
- GO:0009384 = "N-acylmannosamine kinase activity" (def: ATP + N-acyl-D-mannosamine = ADP + N-acyl-D-
  mannosamine 6-phosphate; xref EC:2.7.1.60, Reactome R-HSA-4085028, R-HSA-4088322).
- GO:0046380 = "N-acetylneuraminate biosynthetic process".
- GO:0006055 = "CMP-N-acetylneuraminate biosynthetic process".
- GO:0005524 = "ATP binding"; GO:0005829 = "cytosol"; GO:0006047 = "UDP-N-acetylglucosamine metabolic
  process"; GO:0006045 = "N-acetylglucosamine biosynthetic process"; GO:0004553 = "hydrolase activity,
  hydrolyzing O-glycosyl compounds"; GO:0046872 = "metal ion binding".
</content>
</invoke>
