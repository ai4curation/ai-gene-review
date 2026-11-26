# ARPC4 (p20-Arc) review notes

## Sources
- The affinage record tripped the BLOCKING symbol-collision gate on "bacterial". I inspected it (`--out`): the word refers to bacterial actin tails as an Arp2/3 context, so this is a false positive. Written with `--force`. The synthesis is accurate.
- Key papers:
  - PMID:11741539: reconstitution; the p34-p20 heterodimer is the structural core.
  - PMID:11721045: crystal structure.
  - PMID:20404198 (full text): the ARPC2/ARPC4 mother-filament interface.
  - PMID:11162547: p20 is the subunit hub.
  - PMID:29925947 (full text): nuclear Arp2/3 at DNA breaks.
- Sibling review ARPC1B was followed for consistency on structural constituent, cytosol, actin cytoskeleton and actin filament binding.
- IBA seeds (PTN000505000): budding and fission yeast, Arabidopsis, Dictyostelium and Xenopus ARPC4, and human ARPC4 itself.
- 18 Reactome cytosol rows: each summary names its own reaction (from the cached reactome/R-HSA-*.md display_name). Most cached summaries do not name ARPC4, which participates within ARP2/3-containing entities.

## Decisions
- ACCEPT:
  - Arp2/3 protein complex (6 rows) and Arp2/3-mediated actin nucleation (4 rows).
  - Actin filament binding (contributes_to), structural constituent of cytoskeleton.
  - Actin cytoskeleton and cytosol.
- MODIFY: actin nucleation (NAS) → GO:0034314.
- KEEP_AS_NON_CORE:
  - Actin filament polymerization, cytoskeleton (broad).
  - Adaptor activity (intra-complex hub), METTL21A enzyme binding.
  - Nucleus and site of DSB (nuclear Arp2/3), exosome.
- REMOVE: 18 generic protein-binding rows (subunits ARPC2/3/5/5L; WASL, PNMA5).
