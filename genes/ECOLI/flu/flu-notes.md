# flu / Antigen 43 (*Escherichia coli* K-12) — curation notes

UniProt: P39180 (AG43_ECOLI), gene *flu*. The protein is made as a precursor
that is cleaved into two chains held in equal stoichiometry, an alpha
(passenger) chain displayed at the surface and a beta (translocator) chain in
the outer membrane. The original characterisation established exactly that
bipartite arrangement
[PMID:3301815 "Immunoprecipitation experiments conducted with specific antiserum revealed that the complex was expressed on the cell surface and that it contained, in equal stoichiometry, two chemically distinct polypeptides termed alpha and beta (Mrs of 60,000 and 53,000, respectively)."]
and placed both chains in the outer membrane by fractionation
[PMID:3301815 "Analysis of fractions obtained following cell disruption, isopycnic centrifugation, and detergent extraction indicated that both alpha and beta polypeptides were components of the outer membrane."].

UniProt's functional statement is short: "Controls colony form variation and
autoaggregation. May function as an adhesin."

## What GOA has, and what it lacks

All six GOA rows are cellular_component. There is no molecular function and no
biological process annotation at all, for the protein that is the textbook
classical autotransporter of *E. coli*. The locations themselves are sound,
and two are experimental, but the gene's actual biology is entirely unrecorded.

The periplasmic-space row deserves a note: UniProt assigns the periplasm to the
uncleaved precursor only, and by similarity (ECO:0000250), so it describes a
transit intermediate rather than a steady-state location. Worth keeping, but
not as a core location.

## Autoaggregation

Ag43 self-associates between cells, and the phenotype is strong enough to
override flagellar motility
[PMID:16804184 "Here, it has been demonstrated for the first time that Ag43-mediated aggregation can inhibit bacterial motility."],
with the relationship dose-dependent in both directions
[PMID:16804184 "Ag43 overexpression produces a dominant aggregation phenotype that overrides motility in the presence of low levels of flagella."].
GO:0098743 cell aggregation fits this precisely: "The clustering together and
adhesion of initially separate cells to form an aggregate." The work used
naturally occurring phase variants expressing and not expressing Ag43, so the
evidence is mutant-phenotype rather than overexpression artefact alone.

## The important finding: Ag43 is inserted by TAM, not BAM

This is the result that bears on `modules/bacterial_type_v_secretion.yaml`,
which currently models barrel installation as BAM-dependent and grounds that
part on BamA alone.

Ag43's barrel insertion depends on the translocation and assembly module, TamA
in the outer membrane with TamB in the inner membrane
[PMID:22466966 "it consists of an Omp85-family protein, TamA, in the outer membrane and TamB in the inner membrane of diverse bacterial species"],
a module discovered precisely because it promotes autotransporter secretion
[PMID:22466966 "We have discovered a new translocation and assembly module (TAM) that promotes efficient secretion of autotransporters in proteobacteria."].
For Ag43 the dependence is stated directly
[PMID:25341963 "In vivo, the efficient assembly of the β-barrel protein Ag43 depends on the TAM"],
and a reconstituted system shows the requirement is specific: Ag43 does not
associate with a membrane lacking the TAM
[PMID:25341963 "QCM-D measurements confirmed there was no significant association of Ag43 with the membrane observed in the absence of the TAM"],
while TamA alone suffices to start the insertion
[PMID:25341963 "We conclude that TamA is necessary and sufficient to initiate the penetration of Ag43 into a membrane layer, and that TamB regulates this activity of TamA."].

TamA is itself an Omp85-family protein, as BamA is, so this is a second,
parallel insertase rather than a contradiction of the BAM model. The module
should offer both routes.

## Why GO:0015474 autotransporter activity is NOT proposed here

Ag43 is the obvious candidate for GO:0015474, whose definition reads
"Transports a passenger protein from the periplasm to the external milieu; the
passenger protein and the porin are the N- and C-terminal regions of the same
protein, respectively." Ag43 has exactly that architecture.

The reason for withholding it is that the definition asserts the protein does
the transporting, and the TAM literature contests precisely that
[PMID:22466966 "Mounting evidence suggests that autotransporters might be substrates to be secreted, not an autonomous transporter system."].
The same papers that establish the architecture call Ag43 a substrate protein
throughout. Asserting autotransporter activity for Ag43 would commit the review
to the autonomous model on a point its own best references dispute.

So: assert the type V secretion process, which is uncontested, and record the
molecular function as an open ontology question rather than resolving it by
picking the older model. The term is left in the module, where it describes the
architecture class, with the dispute recorded as a knowledge gap.
