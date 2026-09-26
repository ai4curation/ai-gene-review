# GSDMB (Q8TAX9) review notes

## Why this gene was selected

GSDMB is the gasdermin whose pore-forming competence is *isoform-dependent*, and the
question put to this review was: which splice isoforms are pore-competent, and is
granzyme-A-triggered pyroptosis a general GSDMB property or restricted to exon-6-containing
isoforms? GOA carries none of this: five family-level IBAs and six localization rows, with
no isoform qualification anywhere. GSDMB is also the only human gasdermin with no rodent
ortholog, which matters for how the mouse literature can be read.

## Isoform nomenclature - the thing that makes this literature confusing

Three numbering systems are in circulation. UniProt Q8TAX9 reconciles them, and I use
UniProt isoform IDs throughout:

| UniProt isoform | UniProt "Name" | literature synonym (PMID:36899106) | exon 6 | pore-competent? |
|---|---|---|---|---|
| Q8TAX9-4 (canonical, 416 aa) | 4 | GSDMB3 | present | yes - fully functional |
| Q8TAX9-6 | 6 | GSDMB4 | aa 234-242 missing, belt retained | yes, but partially resists NK-triggered cleavage |
| Q8TAX9-3 | 3 | GSDMB1 | disrupted (aa 221-234 replaced by K) | no |
| Q8TAX9-2 | 2 | GSDMB2 | disrupted (aa 221-243 replaced by R) | no |
| Q8TAX9-1 | 1 | - | Asn221 -> SAGLD **and** aa 234-242 missing | no host-cell pyroptosis; bactericidal |
| Q8TAX9-5 | 5 | - | N-terminal domain absent (aa 1-253 missing) | n/a |

The UniProt variant-sequence features localize all of the differences to a small window
around residues 221-243, i.e. exon 6. Note one thing the table makes visible that the
papers do not emphasise: Q8TAX9-6 and Q8TAX9-1 **share** the 234-242 deletion
(VSP_061490), yet Q8TAX9-6 is pore-competent on host membranes and Q8TAX9-1 is not. The
extra difference in Q8TAX9-1 is the Asn221 -> SAGLD substitution (VSP_061489). So the
234-242 deletion cannot by itself be what abolishes host-cell pore formation, and the
lipid-preference switch in Q8TAX9-1 is not obviously attributable to the same change that
explains the GSDMB1/GSDMB2 defect. I have not seen this addressed directly and have raised
it in `suggested_questions` rather than asserting an explanation.

**A caution on the mapping.** PMID:36991125 additionally calls *both* Q8TAX9-4 and Q8TAX9-6
"Isoform 4", and PMID:37115914 numbers its isoforms 1-5 in the Sarrio/Moreno-Bueno
GSDMB1-5 scheme, which has no UniProt synonym for GSDMB5. Where a mapping was not
unambiguous I did not assert one.

## Answer to the question: pore competence requires exon 6

Three independent groups converge, which is unusual for this gene:

- Lieberman lab, *Sci Immunol* 2023 (PMID:37115914, full text):
  [PMID:37115914 "Cleaved N-terminal (NT) fragments of GSDMB isoforms 3 and 4 caused
  pyroptosis, but isoforms 1, 2, and 5 did not."] with the structural reason
  [PMID:37115914 "The nonfunctional isoforms have a deleted or modified exon 6 and
  therefore lack a stable belt motif."] and the cell-biological consequence under real
  killer-cell attack [PMID:37115914 "Upon natural killer (NK) cell attack,
  GSDMB3-expressing cells died by pyroptosis, whereas GSDMB4-expressing cells died by mixed
  pyroptosis and apoptosis, and GSDMB1/2-expressing cells died only by apoptosis."]. Note
  the additional refinement [PMID:37115914 "GSDMB4 partially resisted NK cell-triggered
  cleavage, suggesting that only GSDMB3 is fully functional."]
- Moreno-Bueno/Sarrio lab, *Cell Death Differ* 2023 (PMID:36899106, full text):
  [PMID:36899106 "we here prove that exon 6 translation is essential for GSDMB mediated
  pyroptosis, and therefore, GSDMB isoforms lacking this exon (GSDMB1-2) cannot provoke
  cancer cell death."]
- Shao/Ding lab, *Nature* 2023 (PMID:36991125): [PMID:36991125 "Presence of exon 6 in the
  isoforms dictates the pore-forming, pyroptotic activity in GSDMB."], with the structure to
  explain it: [PMID:36991125 "We determine the cryo-electron microscopy structure of the
  27-fold-symmetric GSDMB pore and depict conformational changes that drive pore
  formation."] and [PMID:36991125 "The structure uncovers an essential role for
  exon-6-derived elements in pore assembly"]. Ruan lab, *Nature* 2023 (PMID:36991122,
  full text) reaches the same conclusion from an independent cryo-EM structure:
  [PMID:36991122 "GSDMB isoforms with a canonical interdomain linker exhibit normal
  pyroptotic activity whereas other isoforms exhibit attenuated or no pyroptotic activity."]

So the answer is: **granzyme-A-triggered pyroptosis is not a general GSDMB property.**
Crucially, the restriction is *not* at the level of cleavage. GZMA cleaves every isoform;
what differs is what the freed N-terminal fragment can then do:
[PMID:36899106 "Thus, immunocyte-derived Granzyme-A can cleave all GSDMB isoforms, but in
only those containing exon 6, this processing results in pyroptosis induction."]

This also retro-explains a chunk of the "GSDMB is not a pore-former" literature -
[PMID:36991125 "The structure uncovers an essential role for exon-6-derived elements in pore
assembly"] is offered by its authors as the explanation for pyroptosis deficiency in the
non-canonical splicing isoform used in earlier studies. And it makes isoform composition a
real biological variable: [PMID:36991125 "Different cancer cell lines have markedly
different isoform compositions, correlating with the onset and extent of pyroptosis
following GZMA stimulation."]

Protease selectivity adds a second layer: [PMID:36899106 "By contrast, the cleavage of
GSDMB isoforms by Neutrophil Elastase or caspases produces short N-terminal fragments with
no cytotoxic activity, thus suggesting that these proteases act as inhibitory mechanisms of
pyroptosis."]

## How granzyme A recognizes GSDMB (2026)

*Immunity* 2026 (PMID:41592574, abstract only in cache) gives the recognition mechanism:
[PMID:41592574 "This binding requires the dimerization of GZMA, a unique property among
human granzymes."] and [PMID:41592574 "The exosite engages a two-loop-organized site in the
GSDMB-C domain, rendering a functional cleavage at Lys244 in GSDMB."] with a species caveat
that matters for interpreting mouse work: [PMID:41592574 "Mouse GZMA (mGZMA) adopts a
similar dimer structure, but its exosite is less efficient in engaging GSDMB."]

Combined with GSDMB having no rodent ortholog, this means mouse transgenic experiments test
a pairing (mouse GZMA on human GSDMB) that is intrinsically inefficient.

## The Science erratum - what I could and could not establish

PMID:42424476 is a Published Erratum (Science 2026 Jul 9; 393(6807):eaej7549,
doi 10.1126/science.aej7549) to the original granzyme-A/GSDMB paper, Zhou et al.,
*Science* 2020;368(6494):eaaz7548 (PMID:32299851). I verified the erratum/original linkage
in PubMed and in Europe PMC (`commentCorrection` type "Erratum for", pointing at MED:32299851).

**I could not retrieve the erratum's content.** PubMed carries no abstract for it, Europe
PMC records it as `isOpenAccess: N` / `inPMC: N` with "Subscription required", and
science.org returns HTTP 403. I therefore do not know what was corrected - whether a figure,
an author affiliation, a methods detail, or a data panel. I am not going to guess.

Practical consequence for this review: I treat PMID:32299851 with corresponding caution and
mark it `DISPUTED` in `reference_review` with the reason stated plainly, and I do **not**
use it as the sole support for anything. This costs little, because the central claim of
that 2020 paper - that GZMA cleaves GSDMB to unleash pore-forming activity - has since been
independently re-derived by three other laboratories with structures: two 2023 *Nature*
papers (PMID:36991122, PMID:36991125) and the 2026 *Immunity* exosite/crystal-structure study
(PMID:41592574), which also pins the cleavage site at Lys244. Nothing in this review depends
on the uncorrected 2020 figures. **No GOA annotation on GSDMB cites PMID:32299851**, so the
erratum does not put any existing annotation at risk either.

## The second, competing GSDMB story: bactericidal, not cytolytic

Hansen et al., *Cell* 2021 (PMID:34022140, full text) reported the opposite of pyroptosis:
[PMID:34022140 "This virulence strategy protects Shigella from the bacteriocidic activity of
natural killer cells by suppressing granzyme-A-mediated activation of GSDMB."] and, flatly,
[PMID:34022140 "In contrast to the canonical function of most gasdermin family members,
GSDMB does not inhibit Shigella by lysing host cells. Rather, it exhibits direct
microbiocidal activity through recognition of phospholipids found on Gram-negative bacterial
membranes."] with the lipid specificity [PMID:34022140 "Rather, GSDMB binds and forms pores
in membranes enriched in cardiolipin and other bacterial lipids including
phosphatidylglycerol and lipid A"]. They conclude [PMID:34022140 "These findings place GSDMB
as a central executioner of intracellular bacterial killing and reveal a mechanism employed
by pathogens to counteract this host defense system."]

This was read at the time as contradicting the pyroptosis model, and it produced a direct
published dispute. Chao et al., *PNAS* 2017 had found the opposite lipid profile:
[PMID:28154144 "We show that both full-length GSDMB and the N-terminal domain bind to
nitrocellulose membranes immobilized with phosphoinositides or sulfatide, but not with
cardiolipin."] Gong et al., *Genes Dis* 2022 (PMID:36157507, full text) tested the
prediction directly and found the plasma membrane, not mitochondria:
[PMID:36157507 "an obvious GSDMB-NT localization at plasma membrane was observed after 1, 2
and 4 h of transfection with GZMA"]. They also flagged the likely resolution in their own
discussion - that Hansen used a different isoform from the 416-residue one they used.

**The isoform framework resolves this.** UniProt now curates the two profiles as isoform
properties: Q8TAX9-4 binds host inner-leaflet phosphoinositides (PI4P, PI5P, PI(4,5)P2) and
sulfatide and lyses host cells, while Q8TAX9-1 binds lipid A and cardiolipin, kills
Gram-negative bacteria, and explicitly *does not* bind host inner-leaflet
phosphoinositides. Gong et al. used the 416-residue isoform, i.e. Q8TAX9-4; Hansen et al.
used isoform 1. So the two groups were, in an important sense, working on different proteins.
This is the single most consequential fact for curating GSDMB, and GOA currently expresses
none of it.

## Adjudication taken in this review

1. **Pyroptotic pore formation is accepted as a core GSDMB function**, since four
   laboratories agree on it including two independent cryo-EM pore structures, **but** the
   isoform restriction is written into every relevant `reason`, and the pore-competence
   NEW annotation carries `isoform: Q8TAX9-4`.
2. **Antibacterial defence is accepted as core, not demoted.** GSDMB is one of the few
   gasdermins with direct bactericidal evidence on the target gene itself (PMID:34022140),
   and GSDMB appears in its own `WITH/FROM` for GO:0042742 - which, per project guidance,
   marks experimental grounding on the target rather than circularity.
3. **The phosphoinositide-binding IBAs are accepted**, because unlike GSDMC there *is*
   direct GSDMB measurement behind them (PMID:28154144, and UniProt's curation of isoform 4),
   with the isoform conflict recorded in `reason`.
4. **Phosphatidylserine binding is demoted to non-core.** It is the one lipid term with no
   GSDMB-specific measurement in either direction: its WITH/FROM is mouse Gsdmd plus the
   family node only, Chao tested phosphoinositides/sulfatide/cardiolipin, and the word
   phosphatidylserine does not appear anywhere in the Hansen full text. It is a pure
   GSDMD-to-family transfer.
5. **Cardiolipin binding and Gram-negative killing are proposed as NEW**, tagged
   `isoform: Q8TAX9-1`, because they are the distinctive, well-evidenced GSDMB activities
   that GOA is missing entirely.

## Family-level IBA donors (resolved)

All five IBA rows trace to PANTHER node PTN000419132. Donor identifiers resolve as:
MGI:MGI:1916396 = mouse *Gsdmd*; MGI:MGI:2146102 = mouse *Gsdmc2*; MGI:MGI:3044668 = mouse
*Gsdma3*; UniProtKB:P57764 = human GSDMD; UniProtKB:Q96QA5 = human GSDMA;
UniProtKB:Q9BYG8 = human GSDMC; UniProtKB:Q8TAX9 = human GSDMB itself. The PAINT tree was
not inspectable from this repository, so no structured `propagation_review` metadata was
asserted for any row.
