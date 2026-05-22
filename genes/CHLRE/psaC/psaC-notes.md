# psaC (Chlamydomonas reinhardtii) — research notes

UniProt: Q00914 (PSAC_CHLRE). Chloroplast (plastid)-encoded gene `psaC`.
NCBI taxon: 3055. Protein: 81 aa, ~9 kDa (mature ~8.86 kDa).

## Summary of gene function

PsaC is the small stromal (extrinsic) subunit of Photosystem I (PSI). It is the
apoprotein that binds the two terminal [4Fe-4S] iron-sulfur clusters of PSI,
named FA and FB. Together with PsaA/PsaB (which carry P700, A0, A1 and the [4Fe-4S]
cluster FX) PsaC completes the linear electron transfer chain of PSI. FA receives
electrons from FX (in the PsaA/PsaB core); FB is the most distal cluster and is the
immediate electron donor to soluble ferredoxin on the stromal side. PsaC, together
with PsaD and PsaE, forms the docking/ferredoxin-reduction site on the stromal face
of PSI.

## Structural facts

- PsaC structurally resembles 2[4Fe-4S] bacterial dicluster ferredoxins, but has
  two extra elements: an internal loop and a C-terminal extension that mediate
  binding into the PSI complex [PMID:9463363 "This subunit resembles 2[4Fe-4S]
  bacterial ferredoxins but contains two additional sequences: an internal loop and
  a C-terminal extension."].
- The 81-aa protein has two 4Fe-4S ferredoxin-type domains (residues ~2-31 and
  ~39-68). Eight cysteine residues coordinate the two clusters: cluster 1 (FB)
  ligated by Cys11, Cys14, Cys17, Cys58; cluster 2 (FA) ligated by Cys21, Cys48,
  Cys51, Cys54 (UniProt Q00914 BINDING features; UniProt COFACTOR note: "Binds 2
  [4Fe-4S] clusters. Cluster 2 is most probably ... FA and cluster 1 is most
  probably FB.").
- Numerous Chlamydomonas PSI cryo-EM structures resolve PsaC as chain C (e.g. PDB
  7R3K at 2.52 A, 7ZQC at 2.31 A, 6IJJ, 6JO5; UniProt cross-references).

## PsaC is essential for PSI: insertional inactivation

- The chloroplast `psaC` gene of C. reinhardtii was cloned; its deduced sequence is
  highly conserved relative to higher plants and cyanobacteria [PMID:1712288 "The
  deduced amino acid sequence is highly related to that of higher plants and
  cyanobacteria."].
- Directed chloroplast transformation disrupting `psaC` with an aadA cassette gave
  transformants that "are unable to grow on minimal medium lacking acetate and are
  deficient in PSI activity" [PMID:1712288].
- In `psaC` knockout cells, neither the PSI reaction center subunits nor the seven
  small PSI subunits accumulate stably; the reaction center subunits are made but
  turn over rapidly [PMID:1712288 "neither PSI reaction center subunits nor the
  seven small subunits belonging to PSI accumulate stably in the thylakoid
  membranes of the transformants. Pulse-chase labeling ... shows that the PSI
  reaction center subunits are synthesized normally but turn over rapidly"].
- Conclusion: "the iron sulfur binding protein encoded by the psaC gene is an
  essential component, both for photochemical activity and for stable assembly of
  PSI" [PMID:1712288].

## Electron transfer: FB is the terminal cluster donating to ferredoxin

- PsaC binds "the two terminal electron acceptors FA and FB" of PSI [PMID:9463363].
- FB is the cluster that interacts with soluble ferredoxin. Site-directed mutants in
  C. reinhardtii placing positive charges next to FB (I12V/T15K/Q16R, "FB1" mutant)
  gave a 60-fold increase in ferredoxin affinity and faster, near-monophasic Fd
  reduction; mutations next to FA (V49I/K52T/R53Q, "FA2") only modestly decreased Fd
  affinity. "These data indicate that F(B) is the cluster interacting with Fd and
  therefore the outermost iron-sulfur cluster of PSI." [PMID:10438510 "The
  introduction of positively charged residues close to the F(B) cluster in the
  FB(1) triple mutant ... results in a 60-fold increase of Fd affinity ... These
  data indicate that F(B) is the cluster interacting with Fd and therefore the
  outermost iron-sulfur cluster of PSI."].
- Lysine 35 in the PsaC internal loop is a key electrostatic interaction site with
  ferredoxin: K35T/K35D/K35E mutations "drastically affect electron transfer from
  PSI to Fd", and abolish chemical cross-linking of Fd to PsaC; the conservative
  K35R change has no effect [PMID:9463363 "K35 is a main interaction site between
  PsaC and ferredoxin (Fd) and ... it plays a key role in the electrostatic
  interaction between Fd and PSI ... the mutations K35T, K35D and K35E drastically
  affect electron transfer from PSI to Fd ... whereas the K35R change has no
  effect"].
- Cross-linking shows ferredoxin contacts not only PsaD and PsaE but also PsaC
  [PMID:9463363 "Chemical cross-linking experiments show that Fd interacts not only
  with PsaD and PsaE, but also with the PsaC subunit of PSI."].
- Mutations of K52/R53 near FA (K52S/R53A) can make FB preferentially photoreduced
  at low temperature (as in green sulfur bacterium Chlorobium), but room-temperature
  measurements show "electron transfer from PSI to ferredoxin proceeds at normal
  rates in the mutant" — i.e. the FA-region change did not block the FX->FA->FB->Fd
  flow [PMID:8993322 "in contrast to wild type, FB is preferentially photoreduced in
  this mutant ... room temperature optical measurements show that stable charge
  separation still occurs and, surprisingly, that electron transfer from PSI to
  ferredoxin proceeds at normal rates in the mutant."].

## PSI overall reaction (UniProt / HAMAP MF_01303)

PSI is a plastocyanin/cytochrome c6-ferredoxin oxidoreductase (EC 1.97.1.12):
light-driven charge separation transfers an electron from P700 through A0, A1, FX,
FA and FB in turn, ending in reduction of soluble ferredoxin
(reduced plastocyanin + hnu + oxidized ferredoxin -> oxidized plastocyanin +
reduced ferredoxin; Rhea:RHEA:30407). PsaC carries the FA/FB part of this chain.
The EC number and the whole-PSI reaction describe the holocomplex; PsaC's own
contribution is electron carriage via its two clusters, not catalysis of the
overall photochemical reaction.

## Localization

PsaC is a peripheral membrane protein on the stromal side of the chloroplast
thylakoid membrane (UniProt SUBCELLULAR LOCATION; HAMAP-Rule MF_01303). It is an
extrinsic subunit, not an integral membrane protein, but is part of the
membrane-embedded PSI complex.

## GO term closure observations (OLS, checked 2026-05-21)

Relevant to the retired SPKW annotations:

- GO:0051539 "4 iron, 4 sulfur cluster binding" ancestry:
  binding -> small molecule binding -> metal cluster binding (GO:0051540) ->
  iron-sulfur cluster binding (GO:0051536) -> 4Fe-4S cluster binding.
  It does NOT pass through GO:0046872 "metal ion binding". Metal ion binding sits on
  the ion binding / cation binding branch (binding -> small molecule binding ->
  ion binding -> cation binding -> metal ion binding). So "4Fe-4S cluster binding"
  and "metal ion binding" are NOT in a parent/child relationship in GO; they share
  only the broad ancestor "small molecule binding". A [4Fe-4S] cluster is bound as a
  cluster cofactor, not as free metal ions; "metal ion binding" is a related but
  imprecise generalization for this protein. The precise, biologically meaningful
  term is the still-current GO:0051539.

- GO:0009055 "electron transfer activity" ancestry: it is a direct child of
  molecular_function (GO:0003674). It is NOT under GO:0016491 "oxidoreductase
  activity". In current GO, electron transfer activity (electron carrier) was
  deliberately separated from oxidoreductase activity (catalysis of a redox
  reaction). PsaC carries electrons through FA/FB; it is not itself a catalytic
  oxidoreductase enzyme. So "oxidoreductase activity" is an imprecise/borderline
  description, and "electron transfer activity" is the precise current term.
  (The EC 1.97.1.12 oxidoreductase designation belongs to the whole PSI complex,
  not to PsaC as a standalone catalyst.)

## Bottom line for the SPKW retrospective

Both retired SPKW annotations (metal ion binding, oxidoreductase activity) were
broad/imprecise descriptions of well-characterized PsaC functions that are better
captured by still-current, more specific annotations: GO:0051539 (4Fe-4S cluster
binding) and GO:0009055 (electron transfer activity). No correct information is lost
by their removal; GOA's retirement of these SPKW terms is justified.
</content>
</invoke>
