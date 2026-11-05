# epmC (P76938, YfcM, b2326, E. coli K-12) notes

## Deep research availability

Provider deep research was **not available** for this gene in this session: no
provider API keys are configured, so `just deep-research` was not attempted, and
`just mod-description-deep-research ECOLI epmC` reports
`epmC skipped: no MOD provider configured for organism 'ECOLI'` (EcoCyc is not
wired up as a MOD provider here). No `*-deep-research-*.md` file was written.
These notes are built from the cached primary publications, the UniProt entry,
PubMed (esearch/esummary), QuickGO and Rhea.

## Pathway position

- E. coli EF-P modification is a three-enzyme pathway: EpmB (YjeK) makes
  (R)-beta-lysine, EpmA (PoxA/YjeA) ligates it to EF-P Lys34, EpmC (YfcM)
  hydroxylates the modified residue
  [PMID:22706199 "lacks a final hydroxylation step mediated by YfcM"];
  [PMID:25274739 "The post-translational modification is performed in a two-step reaction involving the addition of a β-lysine moiety and the subsequent hydroxylation, catalyzed by PoxA and YfcM, respectively."].
- EpmC is distinct from deoxyhypusine hydroxylase (DOHH), which performs the
  analogous maturation step on eukaryotic eIF5A (PMID:22706199 abstract).

## Reaction and position of the hydroxyl

- UniProt curated reaction (RHEA:83439, ECO:0000269 PubMed:22706199):
  [file:ECOLI/epmC/epmC-uniprot.txt "Reaction=N(6)-((3R)-3,6-diaminohexanoyl)-L-lysyl-[protein] + NADPH + O2 + H(+) = N(6)-((3R)-3,6-diaminohexanoyl)-5-hydroxy-L-lysyl-[protein] + NADP(+) + H2O"].
  Rhea gives RHEA:83439 no GO mapping and no EC (checked 2026-11-02); the entry
  carries `EC=1.14.13.-`.
- The oxygen goes onto Lys34 itself, not onto the appended beta-lysine
  [file:ECOLI/epmC/epmC-uniprot.txt "EpmC adds an oxygen atom to the C5 position of 'Lys-34' and does not modify the added beta-lysine."].
  Kobayashi et al. describe the site as C4(gamma) or C5(delta)
  [PMID:25274739 "A recent study revealed that the β-lysylated Lys34 of EF-P is subsequently hydroxylated at C4(γ) or C5(δ) by YfcM"].
  Hence GO:0017185 peptidyl-lysine hydroxylation (peptidyl-lysine ->
  peptidyl-hydroxylysine) is the right process term; the hydroxyl is on the
  peptidyl lysine.
- NADPH dependence
  [file:ECOLI/epmC/epmC-uniprot.txt "Hydroxylation activity is abolished by NADP and increased by NADPH."];
  reproduced independently
  [PMID:25274739 "In the absence of 5 mM NADPH, we observed a 2-fold decrease in the hydroxylation activity"].

## Metal

- The 2014 structure shows a metal bound by His59, His63 and Glu98, a
  2-His-1-carboxylate motif typical of non-heme iron enzymes. The metal in the
  native crystal is unassigned
  [PMID:25274739 "The metal ion is probably derived from the E. coli lysate, but its identity is unclear."],
  but Fe binds the protein
  [PMID:25274739 "Therefore, the Fe ion directly binds to YfcM."],
  chelating iron reduces activity
  [PMID:25274739 "the hydroxylation efficiency of WT YfcM was reduced by adding 200 μM of the iron chelator 2,2′-Bipyridine, instead of 10 μM FeSO4"],
  and motif mutants are inactive
  [PMID:25274739 "The hydroxylation efficiencies of these YfcM mutants were as low as the background level"].
- Decision: MODIFY GO:0046872 metal ion binding to **GO:0005506 iron ion
  binding**, not GO:0008198 ferrous iron binding: Fe(II) is argued by analogy to
  non-heme iron enzymes, and the oxidation state of the bound metal was not
  established (the authors note the Fe may have oxidised during purification).
- Fold is YbeY/UPF0054-like, with the YbeY 3-His motif replaced by
  2-His-1-carboxylate; EpmC is structurally unlike known amino acid
  hydroxylases (PMID:25274739 discussion).

## Significance of the hydroxylation

- Minor contributor to EF-P activity
  [PMID:25274739 "This modification does not affect the activity of β-lysylated EF-P in the synthesis of proteins containing poly-prolines (3), although it stimulates the reactivity with puromycin (18)."].
- In-cell evidence that EpmC acts on EF-P: epmC mutants carry the +128 Da
  (beta-lysyl) rather than the +144 Da (hydroxy-beta-lysyl) form
  [file:ECOLI/epmC/epmC-uniprot.txt "EF-P proteins in the mutant strain displays a modification of +128 Da, whereas a modification of +144 Da is observed in wild-type strains."].
  This is one of the two lines behind the IC cytoplasm row (the other being
  that EpmC is a soluble 182-residue protein with no signal peptide or
  transmembrane feature in the entry).

## Curation decisions

- GO:0004497 monooxygenase activity (IDA): **MODIFY** -> GO:0016709 (the
  descendant the gene already carries from the same paper; the reaction uses
  NADPH as the second donor).
- GO:0016709 (IDA): **ACCEPT** — core catalytic activity, most specific existing
  term.
- GO:0043687 post-translational protein modification (IDA): **MODIFY** ->
  GO:0017185 peptidyl-lysine hydroxylation. EpmC itself does the covalent work,
  so the term is true (contrast EpmB, where the same term was marked
  over-annotated because EpmB only supplies the donor), but it is uninformative
  about what EpmC does.
- GO:0046872 metal ion binding (IDA): **MODIFY** -> GO:0005506 iron ion binding.
- **NEW** GO:0005737 cytoplasm (IC) — no CC row existed.
- No ND rows in this GOA, so the ND policy does not apply.
- Verified PMIDs: 22706199 (Peil et al. 2012 Nat Chem Biol, abstract-only in
  cache), 25274739 (Kobayashi et al. 2014 Nucleic Acids Res, full text cached),
  23239623 (Ude et al. 2013 Science, abstract-only; cited by UniProt for the
  disruption phenotype). PMID:25195899 (crystallisation note, same group) was
  found by PubMed search but adds nothing and is not cited.
