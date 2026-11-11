# unc-29 review notes

## Session 1 (create review)

- `just fetch-gene worm unc-29` resolved P48181 (ACH2_CAEEL); 41 GOA rows seeded.
- Cached extra papers: PMID:23577128 (male mating, AVA; full text), PMID:19020092 (Boulin 2008
  L-AChR reconstitution; full text), PMID:21252855 (OIG-4; full text), PMID:30407909 (CRLD-1;
  full text).
- Literature synthesis in `unc-29-deep-research-manual.md` (no deep-research API keys).

### Core picture

UNC-29 is the obligatory non-alpha subunit of the heteropentameric levamisole-sensitive
acetylcholine receptor (L-AChR: UNC-29, LEV-1, UNC-38, UNC-63, LEV-8) [PMID:19020092 "We
demonstrate that 3 alpha- and 2 non-alpha-subunits assemble into the same receptor"]. The
receptor is an excitatory acetylcholine-gated cation channel in the postsynaptic membrane of
body-wall muscle at cholinergic NMJs [PMID:10461217 "we demonstrated that all three receptor
types function at neuromuscular synapses"]. Also expressed in some neurons, notably AVA,
where it contributes to cholinergic input from PVY/PVX during male mating [PMID:23577128].

### Decisions worth flagging

- GO:0006937 regulation of muscle contraction, IMP PMID:19028454 (UniProt): the full text
  cached for this SYN-1/AEX-1 paper never names unc-29 (only unc-13, unc-64, unc-119). This
  looks like a wrong reference. Figures and supplements were not seen, so UNDECIDED with a
  SUSPECTED WRONG_REFERENCE source defect.
- GO:0014057 positive regulation of acetylcholine secretion, IMP PMID:12657671 (UniProt):
  abstract-only (PMC has no text). UNC-29 is a postsynaptic receptor, so the claim is
  surprising. UNDECIDED.
- GO:0090326, IMP PMID:23351035 (UniProt): the abstract covers acr-5/acr-15. UNDECIDED.
- GO:0043051 pharyngeal pumping, IGI PMID:12750328 (x4, WormBase): abstract-only, does not
  name unc-29. UNDECIDED.
- No NEW rows were proposed. "Regulation of locomotion" (AVA reversal) is already covered by the
  ARBA row, which I keep as non-core and support with PMID:23577128. Male mating behaviour is
  supported by mutant phenotypes only, and the strict NEW bar is not met.
- MF: in core_functions, UNC-29 is recorded as contributing to GO:0022848 within GO:0005892,
  because a non-alpha subunit does not form a functional channel alone [PMID:19020092]. The
  GOA rows use `enables` and are accepted as standard practice for channel subunits.
