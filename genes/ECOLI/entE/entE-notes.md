# entE (E. coli K-12, P10378, b0594) notes

## Provenance of this review

- 2026-10-19: `just deep-research ECOLI entE --provider falcon` failed twice with
  `Exception: Failed to authenticate` (Edison API). No deep-research file exists; the
  review is grounded in the UniProt record (`entE-uniprot.txt`), GOA (`entE-goa.tsv`),
  and the cached primary literature in `publications/`. Most cached papers are
  abstract-only; PMID:19852513, PMID:20359185, PMID:20845982, PMID:18304323 and
  PMID:24561554 have full text.
- Also reviewed: NCBI PGAP output for WP_000026812.1 (`entE-pgap-predictions-review.yaml`).

## Identity and family

- EntE is the stand-alone adenylation (A) enzyme of the enterobactin NRPS; UniProt:
  "Belongs to the ATP-dependent AMP-binding enzyme family" (ANL superfamily; PANTHER
  PTHR43767). Aryl acid adenylating enzyme (AAAE) class
  [PMID:20359185 "Belonging to the family of aryl acid adenylating enzymes (AAAE), EntE is characterized by a two-step adenylation/ligation reaction"].

## Catalytic activity (core)

- Two half-reactions: DHB + ATP -> DHB-AMP + PPi, then DHB transfer onto the
  phosphopantetheine arm of holo-EntB ArCP domain
  [PMID:20359185 "first, the enzyme catalyzes the condensation of DHB and ATP to form an adenylate intermediate, followed by the ligation of DHB onto the phosphopantetheinylated cofactor that is bound to the ArCP of EntB"].
- First purification/characterisation, enzyme-bound DHB-adenylate
  [PMID:2531000 "The enzyme catalyzes the exchange of [32P]pyrophosphate with ATP, dependent upon aromatic substrate with a turnover number of 340 min-1."].
- EntB identified as the ArCP acylated by EntE
  [PMID:9214294 "This holo-EntB is then acylated with 2,3-DHB in a reaction catalyzed by EntE, previously described as the 2,3-DHB-AMP ligase, with a kcat of 100 min-1"].
- Overall reaction GO:0008668 / EC 6.2.1.71 / RHEA:61652 is therefore exactly EntE's activity.
- Kinetics: Km DHB ~2.5-2.9 uM, Km holo-EntB 0.4-2.9 uM, Km ATP 0.43-1.2 mM (UniProt
  BIOPHYSICOCHEMICAL PROPERTIES, from PMID:20359185, PMID:2531000, PMID:9214294).
- Inhibited by bisubstrate analogues Sal-AMS and DHB-AMS (PMID:20359185).
- Side reaction: in absence of holo-EntB, DHB-AMP reacts with ATP giving Ap4A
  [PMID:19852513 "This is most consistent with the DHB-adenylate being tightly bound, and reacting with ATP while bound in the absence of holo-EntB-ArCP."].
  This is an in-vitro side activity; physiological relevance unproven.
- MbtH-like YbdZ copurifies with/affects EntF A-domain; EntE was purified alongside as
  comparison [PMID:20845982 "We overexpressed and purified EntE, an A domain specific for 2,3-dihydroxybenzoate (2,3-Dhb), and EntF"].

## What EntE does NOT do

- The DHB-serine amide bonds (and the ester bonds) are made by EntF, not EntE
  [PMID:9485415 "The holo-EntF monomer acts as the catalyst for the formation of the three amide and three ester bonds in enterobactin using ATP, L-serine, and acyl-holo-EntB, acylated with 2,3-dihydroxybenzoate by EntE, as substrates"].
  Hence GO:0047527 (2,3-dihydroxybenzoate-serine ligase activity; product N-(2,3-dihydroxybenzoyl)-L-serine)
  and EC 6.3.2.14 (whole enterobactin synthase reaction) describe the multi-protein
  synthetase; EntE contributes the first step only. UniProt nonetheless lists EC 6.3.2.14 on EntE.
- No CoA-ligase activity reported; the thiol acceptor is the phosphopantetheine of holo-EntB
  ArCP (or D-pantetheine as a poor surrogate, Km 34.2 mM, UniProt from PMID:20359185).

## Partners

- EntB: DHB binding to EntE promotes EntE-EntB complexation
  [PMID:19699210 "binding of 2,3-DHB to EntE and EntB primes these proteins for efficient complexation, thus facilitating direct channeling of the siderophore precursor 2,3-DHB-AMP"].
- EntA: tetrameric EntA binds EntE and stimulates activity 6-fold
  [PMID:21166461 "Addition of a 4-fold excess of EntA to an EntE assay mixture resulted in a 6-fold stimulation of EntE activity."].
- No stable synthetase complex in vitro [PMID:9485415 "There is no evidence for a stable complex of the enterobactin synthetase components."].

## Location

- Cytosolic proteomics (PMID:18304323). Small fraction membrane-associated
  [PMID:10692387 "a small fraction of each was found in membrane preparations"].

## Genetics / process

- entE mutants cannot convert DHB to enterochelin [PMID:4939766 "No detectable diffusible intermediate in the formation of enterochelin from 2,3-dihydroxybenzoate was formed by cell extracts of mutants carrying mutations in the entD, entE, or entF genes."].
- Iron-starvation induced, Fur-regulated (UniProt INDUCTION).

## PGAP

- WP_000026812.1 named by BlastRule NBR012093 (no GO); EC 2.5.1.-, 6.2.1.71, 6.3.2.14.
  Equivalog HMMs NF008192 and TIGR02275 (same product name) carry GO:0008668 and GO:0019290 but
  are not the naming model, so PGAP emits no GO. See predictions review.
- EC 2.5.1.- (alkyl/aryl transferases) is a misclassification: DHB transfer to the
  phosphopantetheine thiol is an aroyl (acyl) transfer and is the second half of EC 6.2.1.71.
