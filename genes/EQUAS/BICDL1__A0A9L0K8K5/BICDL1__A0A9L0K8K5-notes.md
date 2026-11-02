# BICDL1 (donkey, A0A9L0K8K5) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Scope: full review of the Ensembl canonical product (ENSEAST00005058854, ENSEASP00005061163, 626 aa) of donkey
BICDL1 (ENSEASG00005007623). This is a separate UniProt entry from the benchmark product A0A9L0JLY3, which has
its own folder (`genes/EQUAS/BICDL1/`), so this one uses `BICDL1__A0A9L0K8K5`. No ProtNLM2 files were opened.

Deep research: `just deep-research-falcon EQUAS BICDL1__A0A9L0K8K5 --fallback perplexity-lite` failed
(falcon "Failed to authenticate"; perplexity HTTP 401 insufficient quota). The review uses the cached primary
literature instead.

Evolutionary grounding:
- PANTHER PTHR32123:SF12 (BICD FAMILY-LIKE CARGO ADAPTER 1), shared with mouse Bicdl1 A0JNT9, human Q6ZP65,
  Xenopus and zebrafish bicdl1.
- PAINT IBDs at PTN001281025 (Deuterostomia): GO:0047496 (seed zebrafish ZDB-GENE-091204-439) and GO:0055107
  (seed mouse MGI:1922915). PAINT did not propagate the mouse binding, centrosome or neuron projection terms;
  I treated the neuron-projection omission as deliberate (downstream phenotype) and kept the binding/location
  terms only as one-to-one mammalian ortholog transfers with conserved residues.
- Sequence (`BICDL1__A0A9L0K8K5-bioinformatics/RESULTS.md`): 95% identity to mouse over aligned residues,
  CC1 box at 114, mouse Rab6-binding Lys512 = donkey Lys562, one 48-residue isoform-2-type insertion (442-489).

Evidence (all from other species; nothing experimental in donkey):
- Rab6 effector; Lys512 needed for Rab6 binding [PMID:20360680 "showed that lysine 512 is required for binding to Rab6"].
- Recruits dynein/dynactin and Kif1C to Rab6/NPY vesicles [PMID:20360680 "BICDR-1 is a Rab6 effector, recruits dynein/dynactin and Kif1C to Rab6/NPY-positive secretory vesicles"].
- Pericentrosomal localization, dynein/dynactin dependent [PMID:20360680].
- Recruits two dyneins, faster motor [PMID:29420470 "both BICDR1 and HOOK3 preferentially recruit two"].
- Accelerates minus-end vesicle movement [PMID:25176647].
- Neurite phenotype is from overexpression; BICDR-1 restricts neuritogenesis indirectly [PMID:20360680].
- Mouse Bicdl1 knock-in retinal phenotype [PMID:42774019] noted, not used (organismal phenotype).

Decisions: centrosome ACCEPT; neuron projection development MARK_AS_OVER_ANNOTATED; small GTPase binding ACCEPT;
dynactin binding ACCEPT; vesicle transport along microtubule ACCEPT; Golgi to secretory granule transport
KEEP_AS_NON_CORE; NEW cytoskeletal motor activator activity (ISS, PMID:29420470).
