# VCP review notes

## NE reformation annotation (GO:0007084) — primary reference selection

The `GO:0007084` (mitotic nuclear membrane reassembly) NEW annotation in
`VCP-ai-review.yaml` cites three references in `supported_by`:

- **PMID:18097415** — Ramadan et al. 2007, *Nature* — primary IMP reference;
  direct p97 manipulation showing p97 binds ubiquitylated Aurora-B and
  extracts it from chromatin during exit from mitosis.
- **PMID:11781570** — Hetzer et al. 2001, *Nat Cell Biol* — direct in vitro
  dissection of two discrete p97 functions in NE assembly: p97-Ufd1-Npl4 for
  closed NE formation, p97-p47 for NE growth.
- **PMID:26040713** — Olmos et al. 2015, *Nature* — retained as supporting
  evidence for the downstream UFD1-dependent CHMP2A recruitment step.

PMIDs 11781570 and 18097415 were identified via the structured bibliography
of PMID:26040713 (PMC4471131 NCBI eutils XML, refs 6 and 20) — verified
primary sources, not guessed.

### PMID:21486945 — cached but intentionally excluded

`publications/PMID_21486945.md` (Dobrynin et al. 2011, *J Cell Sci*,
"Cdc48/p97-Ufd1-Npl4 antagonizes Aurora B during chromosome segregation in
HeLa cells") was cached during the same pass that added the direct-VCP
primary references, but is **not** cited in `supported_by` for GO:0007084.

Reasons for exclusion:

1. **Wrong process focus.** The paper's experimental data and conclusions
   concern Aurora-B antagonism on prometaphase/metaphase chromosomes during
   chromosome alignment and segregation, not post-mitotic NE reformation.
   The relevant GO terms would be in the chromosome-segregation /
   spindle-checkpoint area, not `GO:0007084`.
2. **Indirect for VCP.** The siRNA experiments deplete Ufd1-Npl4 (the
   adaptor complex), not VCP itself — the same indirect-evidence concern
   that motivated switching the original Olmos-only annotation to TAS in
   commit `3d7c271c`.
3. **Already covered.** The Aurora-B / chromatin extraction mechanism that
   *is* relevant to NE reformation is more directly established by
   PMID:18097415 (Ramadan 2007), which manipulates p97 directly.

The file was retained in `publications/` rather than removed because (a) it
is a real, correctly-identified primary reference (ref 21 of Olmos 2015) and
may be useful for future annotations in the chromosome-segregation context,
and (b) caching reflects evaluation work that future reviewers should not
have to repeat.

### Experimental systems supporting the IMP evidence code

The IMP evidence code on GO:0007084 annotates *human* VCP (P55072), but the
two direct-p97 manipulation primary references use heterologous /
reconstitution systems rather than direct loss-of-function in human cells:

- **PMID:11781570 (Hetzer 2001)** — in vitro NE assembly reconstitution.
  The abstract describes two discrete p97 functions dissected by direct
  manipulation of the AAA-ATPase in a reconstituted assembly system, not
  by p97 depletion in cultured cells.
- **PMID:18097415 (Ramadan 2007)** — explicitly states "In vitro, nucleus
  formation requires p97" in the abstract. The Aurora-B chromatin-extraction
  mechanism is established by direct p97 manipulation in this in vitro
  nucleus-formation system, with corroborating in-cell data on p97-Aurora-B
  binding after ubiquitylation.
- **PMID:26040713 (Olmos 2015)** — the only primary reference in the
  `supported_by` set with direct loss-of-function data in human cells (HeLa,
  diploid fibroblasts). Olmos depletes UFD1 (a VCP adaptor), not VCP itself,
  which is the indirect-evidence concern that motivated the IMP→TAS interim
  on commit `3d7c271c`.

Annotating human VCP with IMP via direct p97 manipulation in in vitro / in
egg-extract systems is standard GO practice (cross-species annotation by
orthology, with the in vitro reconstitution providing the strongest
mechanistic dissection). This note documents the experimental-system
limitation transparently so a future curator does not need to re-derive it.

A direct human-cell VCP loss-of-function experiment in an NE-reformation
assay (e.g., VCP siRNA, NMS-873, or CB-5083 in HeLa/RPE-1 with NE-rim
imaging) would further strengthen the IMP annotation. This was raised as a
non-blocking suggestion by claude-review on commit `2407bdcf` and is left as
a future-pass concern.
