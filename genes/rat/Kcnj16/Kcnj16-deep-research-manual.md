# Kcnj16 (rat, Kir5.1) - manual literature summary

No deep-research API was available; this summary was compiled manually from cached
publications in `publications/` and the UniProt record (P52191, Swiss-Prot).

## Identity

- Rat Kcnj16 encodes Kir5.1 (BIR9), an inward rectifier K+ channel subunit of 419 aa
  with the Kir topology (M1, pore helix H5 with selectivity filter, M2, large
  cytoplasmic C-terminal domain) [file:rat/Kcnj16/Kcnj16-uniprot.txt].
- Cloned from rat brain; Kir5.1 does not produce macroscopic current alone but modifies
  currents when coexpressed with specific Kir partners
  [PMID:8973378 "Two other members of this family (Kir5.1 and Kir3.4) did not produce macroscopic currents, when expressed by themselves, yet both subunits modified the currents when coexpressed with other specific members of the Kir family."].

## Obligate heteromer with Kir4.1 / Kir4.2

- Kir5.1 forms functional channels only with Kir4.1 (Kcnj10) or Kir4.2 (Kcnj15)
  [PMID:11306656 "The inwardly rectifying potassium channel Kir5.1 appears to form functional channels only by coexpression with either Kir4.1 or Kir4.2."].
- Heteromeric Kir4.1/Kir5.1 channels are highly pH-sensitive, an effect conferred mainly
  by Kir5.1 [PMID:10764726 "Kir5.1/Kir4.1 heteromeric channel activity is extremely sensitive to inhibition by intracellular acidification and that this novel property is conferred predominantly by the Kir5.1 subunit"].
- Kir5.1 within the heteromer determines single-channel subconductance behaviour; rat
  Kir5.1 linked to Kir4.1 gives the ~45 pS channel with short-lived sublevels
  [PMID:19665991 "XtKir4.1/ratKir5.1 channels behaved like rat Kir4.1/Kir5.1 channels"].
  The same paper confirms Kir5.1 alone is non-functional
  [PMID:19665991 "The Kir5.1 subunit does not form functional channels by itself and has no related homologs in the mammalian genome"].
- PIP2 and pH gating of the heteromer depend on H-bonding at the helix-bundle crossing;
  Kir5.1 lacks the TM1 lysine [PMID:18690035 "Kir5.1 subunits do not possess a TM1 lysine."].
- Heteromeric Kir4.1/Kir5.1 channels were used to study EAST/SeSAME mutations in Kir4.1
  (PMID:20807765; abstract only).

## Localization

- Kir5.1 is expressed in renal tubular epithelia together with Kir4.1 (PMID:10764726).
- Kir4.1/Kir5.1 are basolateral in distal tubules and set transepithelial voltage
  [PMID:28931751 "Inwardly rectifying K+ channels Kir4.1 (Kcnj10) and Kir5.1 (Kcnj16) are highly expressed in the basolateral membrane of distal renal tubules"].
- Kir5.1 is also found in tissues lacking Kir4.1 (pancreas, with Kir4.2) (PMID:11306656),
  and in brainstem chemosensitive neurons (PMID:30605394, introduction).

## Physiology (Dahl SS Kcnj16-/- rats)

- Knockout rats: hypokalemia, reduced BP, 100% mortality on high salt from salt wasting;
  collecting-duct basolateral K+ channel activity shows only homomeric Kir4.1
  [PMID:28931751 "Electrophysiological recordings of basolateral K+ channels in the collecting ducts isolated from SSKcnj16-/- rats revealed activity of only homomeric Kir4.1 channels."].
- Knockout rats: chronic metabolic acidosis, hyperventilation at rest, blunted hypercapnic
  and hypoxic ventilatory responses [PMID:30605394 "SS Kcnj16−/− rats hyperventilated at rest, likely compensating for a chronic metabolic acidosis."].

## Interpretation

Kir5.1 is a regulatory/pore-contributing subunit that requires Kir4.x partners, so its
channel activity is best captured as `contributes_to` inward rectifier potassium channel
activity. Its major physiological role is in the basolateral K+ conductance of distal
nephron epithelia (K+ recycling supporting Na+ reabsorption) and in pH-sensitive K+
conductances. pH regulation and CO2 response phenotypes are organism-level consequences
of knockout.
