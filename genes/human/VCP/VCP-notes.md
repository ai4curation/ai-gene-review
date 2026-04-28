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
