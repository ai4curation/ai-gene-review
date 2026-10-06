# ARMC1 review notes

## Sources
- Affinage: trust gates clear. The two key papers were checked in full text: PMID:31644573 (peripheral MICOS/MIB component, distribution) and PMID:40203102 (MIRO-ARMC1-MTFR assembly; DNAJC11-mediated release).
- PMID:40203102 states the HMA-like domain "lacks cysteines in the positions required for metal coordination", which contradicts the InterPro-based metal ion binding IEA.
- Partner accessions were resolved by UniProt batch query: MTFR1L (Q9H019), RNF24 (Q9Y225), DNAJC11 (Q9NVH1), MTX1 (Q13505), IMMT (Q16891), MICOS10 (Q5TGZ0), SAMM50 (Q9Y512).

## Decisions
- ACCEPT:
  - Cytoplasm, cytosol, mitochondrion and outer mitochondrial membrane (dual localization).
  - Intracellular distribution of mitochondria (IMP).
- REMOVE:
  - Metal ion binding (IEA): the domain lacks the coordinating cysteines.
  - 11 generic protein-binding rows (policy).
- NEW: protein-macromolecule adaptor activity (IDA, PMID:40203102), for MIRO-MTFR assembly.

## Review round 1 (PR #4184)
- Removed the C. elegans "ortholog ARCP-1" sentence. PMID:31757604 defines arcp-1 as an ankyrin-repeat gene (UNC-44/ankyrin homolog), so it is not an ARMC1 ortholog. The reference is marked MISCITED/NONE and the affinage reference_review notes the error.
- NEW protein stabilization (GO:0050821, IMP, PMID:40203102): MTFR is degraded by the ubiquitin-proteasome system without ARMC1, and the D37R mutant fails to restore MTFR levels.
- The adaptor NEW row is now IMP (D37R separation-of-function), not IDA.
- The description mentions the TMEM11/MTCH2 contacts of the CTD.
- Core-function locations are trimmed to outer membrane and cytosol (no ancestors).
- MTFR1L protein-binding rows stay REMOVE: the assembly role is captured by the NEW adaptor and stabilization rows.
- PMID:41153008 (MSC-conditioned media raise ARMC1 in kidney cells; overexpression lowers DRP1) is not used: the effects are indirect and from overexpression.
