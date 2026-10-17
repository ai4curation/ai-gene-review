# sox10 (Xenopus laevis, Q8AXX8) — review notes

## Identity

- SoxE-group HMG-box transcription factor (Sox8/Sox9/Sox10 group). UniProt domains: HMG box, Sox_N; PANTHER PTHR45803:SF6 "TRANSCRIPTION FACTOR SOX-10".
- Frog clone: 446 aa, HMG box 98-166, C-terminal transactivation region 358-446 [file:XENLA/sox10/sox10-deep-research-falcon.md "predicted an HMG DNA-binding box at residues 98–166 and a C-terminal transactivation region at residues 358–446"].
- Homeologs: Q8AXX8 is the reviewed Swiss-Prot entry; L/S homeolog splitting not relevant to GOA rows here (all rows on Q8AXX8).

## Expression (network layer evidence)

- Lateral neural plate edge at gastrulation, neural-crest-forming region [PMID:12812785 "Sox10 mRNA accumulates during gastrulation at the lateral edges of the neural plate, in the neural crest-forming region"].
- Expressed after the SoxB1->SoxE switch: Sox9 and Sox10 not detected until late gastrula/early neurula, "when they mark the neural crest populations at the neural plate border" [PMID:30144418]. Unlike most NC potency factors (Snail1, Myc, Foxd3, Ets1, Ap2, Vent2), Sox10 is NOT first expressed in blastula pluripotent cells [PMID:30144418 "Sox9 and Sox10 are not first expressed in pluripotent naïve blastula cells"].
- Later: migrating cranial and trunk NC, otic placode/vesicle, pigment cells, cranial ganglia [PMID:12885557 "It is expressed in prospective neural crest and otic placode regions from the earliest stages of neural crest specification and in migrating cranial and trunk neural crest cells"].
- Upstream: Wnt, FGF, Snail [PMID:12885557 "We show that Sox10 expression is dependent on FGF and Wnt activity"; "Snail is able to control Sox10 expression"]. Sox10 placed between Snail and Slug [PMID:12885557 "Sox10 may lie between Snail and Slug in the genetic cascade"].

## Loss of function

- MO: loss of NC precursors, expanded neural plate/epidermis; loss of Slug and FoxD3 [PMID:12885557 "This effect of Sox10 depletion is produced during some of the earliest steps of neural crest specification"]. Rescued by MO-resistant RNA (deep research summary of full text).
- Apoptosis up / proliferation down in neural folds [PMID:12885557 "Sox10 could work as a survival as well as a specification factor"].
- Late: melanocytes and ganglia blocked in explants [PMID:12885557 "we were able to block their development by inhibiting Sox10 activity"].
- In Wnt8/Chordin-induced NC explants Sox10 MO prevents Sox9, Sox10, FoxD3 [PMID:30144418 "morpholino-mediated depletion of Sox10 prevents expression of the neural crest markers Sox9, Sox10 and Foxd3 in these explants"].

## Gain of function

- Sox10 expands the Slug domain; C-terminal portion sufficient; massive increase in pigment cells; competence lost during gastrulation [PMID:12812785 "Overexpression of Sox10 causes a dramatic expansion of the Slug expression domain"; "These results suggest that Sox10 is involved in the specification of neural crest progenitors fated to form the pigment cell lineage"].
- Sox9 and Sox10 are functionally equivalent in NC and inner ear; activity regulated by SUMOylation [PMID:16256735].
- Premature Sox10 in blastula represses pluripotency genes (Oct25, Vent2, Id3, TF-AP2) in an HMG (DNA-binding)-dependent, activation-domain-independent way [PMID:30144418 "suggesting that the observed down-regulation of pluripotency genes by SoxE factors is dependent upon DNA binding"].
- Sox10 can replace SoxB1 (Sox2/3) for blastula pluripotency in a molecular replacement assay [PMID:30144418 "Sox9 and Sox10 do have the ability to maintain pluripotency, although they may do so less robustly than SoxB1 factors do"]; SoxB1 cannot replace SoxE for NC [PMID:30144418 "SoxB1 factors have only a limited ability to replace SoxE function in promoting formation and maintenance of neural crest cells"].

## Molecular activity

- Sequence-specific HMG-box DNA-binding TF; activator via TAM/TAC (by similarity to human SOX10, P48436). SUMOylated SoxE recruit repressors (Lee 2012, cited in PMID:30144418 "SoxE proteins can functions as activators or repressors depending upon whether they have been modified by Sumoylation").
- Interacts with Ubc9 and SUMO1 [UniProt, PMID:16256735] — this is Sox10 as a SUMOylation substrate.
- Direct targets in frog not mapped by ChIP in cached literature; MITF/DCT/MPZ/GJB1 targets established in mammals/zebrafish [file:XENLA/sox10/sox10-deep-research-falcon.md].

## Network layer judgement

Sox10 is a **neural crest specifier**, not a neural plate border specifier and not a competence/pluripotency factor:
- expression begins after border specifiers, within the NC domain, downstream of Wnt/FGF and Snail;
- required for early NC specifier genes (slug/snai2, foxd3, sox9);
- sufficient to expand the NC (Slug) domain;
- later re-deployed in melanocyte (and, by orthology, glial/ENS) lineages, and in otic development.
The 2018 LaBonne study adds a twist: SoxE takes over (part of) the potency-maintaining Sox role from SoxB1 in NC — SoxE co-option is argued to be a true vertebrate novelty. This is a hypothesis about NC stemness, not grounds for a stem-cell maintenance annotation on frog Sox10 (evidence is replacement/overexpression only).

GO term choice: GO:0014036 neural crest cell fate specification (part_of GO:0014029 neural crest formation) best fits the Honoré MO data; GO:0014029 retained for the other IMPs (also covers survival/maintenance of precursors).

## Evolution

- Lamprey has three SoxE genes (SoxE1-3) with independent duplication history relative to gnathostome Sox8/9/10 [PMID:21889937 "our results also have implications for understanding the independent evolution of duplicated SoxE genes among agnathan and gnathostome vertebrates"]. So 1:1 orthology of Sox10 outside gnathostomes cannot be assumed; the NC-specifier role is a SoxE-group property.
- Amphioxus single SoxE is not expressed at the neural plate border (literature; not cached here) — consistent with SoxE recruitment into the border/NC GRN at the vertebrate base [PMID:30144418 "the co-option of SoxE factors into the GRN represents one of the true novelties"].
