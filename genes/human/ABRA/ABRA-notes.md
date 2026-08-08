# ABRA (STARS) — curation notes

Human ABRA, UniProt Q8N0Z2, 381 aa, HGNC:30655. Also called STARS (striated muscle
activator of Rho signaling) and MS1 (myocyte stress 1).

## 1. What the protein does

The mechanism is worked out and consistent across three papers from one group plus
independent confirmation, but almost all of it is rodent.

- **Discovery and actin binding.** [PMID:11983702 "We describe a novel, evolutionarily
  conserved actin-binding protein, called STARS (striated muscle activator of Rho
  signaling), that is expressed specifically in cardiac and skeletal muscle cells"] and
  [PMID:11983702 "STARS binds to the I-band of the sarcomere and to actin filaments in
  transfected cells, where it activates Rho-signaling events"]. The SRF effect requires the
  actin interaction: [PMID:11983702 "STARS stimulates the transcriptional activity of SRF
  through a mechanism that requires actin binding and involves Rho GTPase activation"].
  UniProt records the binding as being to filaments specifically —
  [file:human/ABRA/ABRA-uniprot.txt "Binds F-actin and ABLIM1, ABLIM2 and ABLIM3."] — with
  two C-terminal actin-binding regions of which the first is disordered
  [file:human/ABRA/ABRA-uniprot.txt "The actin-binding domain 1 (ABD1) is intrinsically disordered,"].

- **The step that actually links actin to transcription.** [PMID:15798203 "Here we show
  that STARS activates SRF by inducing the nuclear translocation of MRTFs."] and
  [PMID:15798203 "The STARS-dependent nuclear import of MRTFs requires RhoA and actin
  polymerization, and the actin-binding domain of STARS is necessary and sufficient for
  this activity."]. This is loss-of-function as well as gain-of-function:
  [PMID:15798203 "A knockdown of endogenous STARS expression by using small interfering
  RNA significantly reduced SRF activity in differentiated C2C12 skeletal muscle cells and
  cardiac myocytes."] UniProt's own human FUNCTION line encodes exactly this step:
  [file:human/ABRA/ABRA-uniprot.txt "-!- FUNCTION: Acts as an activator of serum response factor (SRF)-dependent"].

- **Partners.** ABLIM2 and ABLIM3 were found with STARS as bait
  [PMID:17194709 "we performed a yeast two-hybrid screen of a skeletal muscle cDNA library
  using STARS as bait, and we identified two novel members of the ABLIM protein family,
  ABLIM-2 and -3, as STARS-interacting proteins"] and they amplify the output
  [PMID:17194709 "these novel ABLIM proteins strongly bind F-actin, are localized to actin
  stress fibers, and synergistically enhance STARS-dependent activation of SRF"]. Note that
  **none of the ABLIM interactions appear in the human GOA file** — the only IPI row is
  PPP1R18 from HuRI.

- **In vivo requirement.** Zebrafish knockdown [PMID:22815879 "Morpholino-induced knockdown
  of zSTARS alters atrial and ventricular dimensions and decreases ventricular fractional
  shortening"] rescued by SRF [PMID:22815879 "Co-injection of zsrf (serum response factor)
  mRNA rescues the cardiac phenotype of zSTARS knockdown"]. Mouse deletion impairs
  arteriogenesis [PMID:19778941 "targeted deletion of Abra in CL57BL/6 mice led to impaired arteriogenesis"].

- **A second, MRTF-independent activity.** [PMID:26903873 "Exposing C2C12 cells to
  CCG-1423, a pharmacological inhibitor of SRF preventing the nuclear translocation of its
  co-factor MRTF-A, had no effect on myotube differentiation rate, suggesting that STARS
  regulates differentiation via a MRTF-A independent mechanism."] Worth flagging: the
  canonical MRTF/SRF axis does not account for everything STARS does.

## 2. What the human GO record actually contains

See `ABRA-bioinformatics/RESULTS.md` for the reproducible audit. Headline numbers: 16 rows,
**2 experimental** (one Y2H IPI, one LIFEdb IDA), 14 transferred; and of the transfers,
mouse Abra is the WITH/FROM source for 8 rows under four different identifier styles
(`UniProtKB:Q8BUZ1`, `ensembl:ENSMUSP00000051973`, `MGI:MGI:2444891`, `InterPro:IPR026111`),
rat Abra for 3 more. **No human experiment has established any molecular function, biological
process or native localisation for this protein.** The mechanism above is entirely mouse,
rat, zebrafish and C2C12; the human contribution to the literature is expression profiling.

The propagation topology is clean, though: PANTHER PTHR22739 has 4 reviewed members, all
named ABRA, all in subfamily SF20, so the IBA node PTN001100454 and the ISS transfers sit
inside a one-to-one ortholog group with no paralog to confuse them.

## 3. The plasma-membrane annotation

`GO:0005886` IDA under `GO_REF:0000054` (LIFEdb GFP-fusion survey) is the one annotation
that is not a rodent transfer, and it is the one I do not believe:

- UniProt places ABRA at `Cytoplasm, myofibril, sarcomere` and `Cytoplasm, cytoskeleton`,
  not at the plasma membrane
  [file:human/ABRA/ABRA-uniprot.txt "-!- SUBCELLULAR LOCATION: Cytoplasm, myofibril, sarcomere {ECO:0000250}."].
- ABRA carries none of the four membrane-targeting UniProt feature classes (Transmembrane,
  Intramembrane, Signal, Lipidation) — checked explicitly, see RESULTS.md Q2.
- It is a striated-muscle-enriched protein
  [file:human/ABRA/ABRA-uniprot.txt "DR   HPA; ENSG00000174429; Tissue enhanced (heart muscle, skeletal muscle, tongue)."]
  and a GFP fusion overexpressed in a non-muscle line has no sarcomere to go to. Since ABRA
  binds F-actin, the most economical reading of a rim signal is cortical actin.
- **It has already spread.** Mouse Abra now carries `GO:0005886` twice, by Ensembl Compara
  IEA (`GO_REF:0000107`) and by ISO (`GO_REF:0000119`), and both cite `UniProtKB:Q8N0Z2`.
  One GFP image in a cell line is now a plasma-membrane annotation in two species.

Marked `MARK_AS_OVER_ANNOTATED` rather than `REMOVE`: the observation itself may be real for
an overexpressed fusion, and GO_REF:0000054 is a pipeline reference with no full text to
read against.

## 4. The GO gap: the MRTF nuclear-import step is missing from human

The mechanistic heart of what ABRA does — driving MRTF-A/MRTF-B into the nucleus — has no
human GO annotation. Mouse has `GO:0006606 protein import into nucleus` IDA from
PMID:15798203, but that term says STARS *is imported*, which is not what the paper shows;
STARS *causes* MRTFs to be imported. The correctly-directed term is
`GO:0042307 positive regulation of protein import into nucleus`. Because the mouse
annotation used the wrong-direction term, the step was never propagated to human, and the
human record jumps straight from `actin binding` to `positive regulation of transcription by
RNA polymerase II` with the causal middle missing. Added as a `NEW` annotation and flagged
for the mouse record too.

## 5. Caveats on the affinage record

`self_evaluation_pairwise: win` with clear trust gates, all 12 citations are real numeric PMIDs,
and the mechanistic narrative
is accurate. One over-attribution:

> "Its actin-cytoskeleton-regulating activity is conserved through the C-terminal Costars
> domain, whose function in actin organization and motility is preserved across species
> [PMID:20940261]."

PMID:20940261 is about a *different gene*. The Costars protein is 82 residues
[PMID:20940261 "The 82 amino acid Costars protein sequence appears highly conserved among
diverse species, and significantly resembles the C-terminal region of the striated muscle
activator of Rho signaling (STARS)"] and the rescue used
[PMID:20940261 "Expressing cosA or its human counterpart mCostars eliminated abnormalities
of cosA(-) cells."]. The human counterpart of that 82-residue protein is ABRACL (Q9P1F3,
81 aa) — RESULTS.md Q4 confirms ABRACL and ABRA are the only two reviewed human proteins
carrying Pfam PF14705, and ABRACL is essentially the domain alone. Sharing a domain is not
sharing a phenotype; nothing from that paper is used to support an ABRA annotation here.

## 6. Things I deliberately did not annotate

- **`GO:0030838 positive regulation of actin filament polymerization`.** The claim that
  STARS increases actin polymerization is real but I could only source it to review-style
  statements; Kuwahara 2005's abstract says the STARS effect *requires* actin polymerization
  [PMID:15798203 "requires RhoA and actin polymerization"], which is not the same as STARS
  driving it. Left as a suggested experiment.
- **`GO:0031674 I band`.** Tempting, but the reports disagree on the sub-compartment —
  I-band in PMID:11983702, Z-disc in [PMID:17415416 "a muscle-specific actin-binding protein
  localized to the Z disc"], I-band/Z-disc/M-line in the PMID:26903873 introduction. The
  parent term `GO:0030017 sarcomere` is the honest level.
- **Anything from ABRA's UniProt keywords.** The entry carries `Protein transport`,
  `Translocation` and `Transport`, which used to generate `GO:0015031 protein transport`
  through GO_REF:0000043. Those keywords are a mis-reading of "induces nuclear
  translocation of MKL1/MKL2" — ABRA is not a transporter. The keyword-derived rows are no
  longer in GOA (SPKW annotations were withdrawn for cellular organisms), so there is
  nothing to review, but the keywords themselves should go.
- **A biological-process annotation for arteriogenesis or exercise response.** Real
  phenomena, but they are about ABRA's *expression* being regulated, and in the
  arteriogenesis case the loss-of-function is mouse. Left in the description and questions.
