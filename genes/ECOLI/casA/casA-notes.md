# casA (Cse1 / Cas8e), *Escherichia coli* K-12 — UniProt Q46901

Curation journal. All assertions carry inline provenance as
`[PMID:xxxxxxx "verbatim supporting text"]`. Quotes are copied verbatim from the
cached records in `publications/`.

## Session 1 (2026-10-01): initial full review

Reviewed together with casB, casC, casD and casE, because the five proteins are one
ribonucleoprotein machine and their annotations should come out mutually consistent.

### What the complex is

Cascade was defined biochemically by affinity purification of individually tagged Cas
proteins from *E. coli* K-12 lysates
[PMID:18703739 "Affinity purification of the tagged component enabled the identification of a protein complex composed of five Cas proteins: CasA, CasB, CasC, CasD, and CasE"].
Notably, CasA is the one subunit that could not be used as bait
[PMID:18703739 "The complex, denoted Cascade (CRISPR-associated complex for antiviral defense), could be isolated from E. coli lysates using any of the tagged subunits of the complex as bait, except for CasA."],
which is the first hint that CasA is peripheral to assembly rather than part of the
structural core. UniProt records the same: "CasA is not required for formation of
Cascade, but probably enhances binding to and subsequent recognition of both target
dsDNA and ssDNA" (Q46901 FUNCTION).

The crystal structure resolves the stoichiometry and the RNA
[PMID:25103409 "both assemblies consist of 11 protein subunits and a single 61-nt crRNA that traverses the length of the complex"],
so Cascade is a genuine ribonucleoprotein, not merely a protein-containing complex
[PMID:23079036 "The E. coli Cascade complex is a 405 KDa ribonucleoprotein complex assembled from crRNA and five functionally essential Cse proteins"].

### Where CasA sits and what it touches

CasA (called Cse1 in the structural papers) occupies the tail of the seahorse-shaped
complex, where the crRNA 5' handle is clamped
[PMID:25103409 "Cas6e binds the 3′ end of the crRNA at the head of the complex, while the 5′-end of the crRNA is sandwiched between three protein subunits (Cas5, Cas7.6 and Cse1) in the tail"].
Its docking is via a loop (L1) that enters a pore in CasD and reads the crRNA bases
directly
[PMID:25103409 "In the Cascade structure the L1-helix inserts into the Cas5e helix-binding pore and makes base-specific interactions with the AAC triplet"],
and the same subunit also contacts CasD's RRM
[PMID:25103409 "the globular domain of Cse1 also makes contacts with the modified RRM of Cas5e"].
Its C-terminal four-helix bundle reaches the CasB dimer and thereby ties the tail of the
complex to its head
[PMID:25103409 "This interaction completes the structural bridge that connects the four-helix bundle of the Cse1 tail to the Cas6e head."].
These two contacts — to CasB (P76632) and to CasD (Q46898) — are exactly what the two
GOA `protein binding` IPI rows record, so those rows are about CasA's structural
integration into the complex, not about an informative binding activity.

### Nucleic-acid contacts

CasA touches both the guide and the target. The L1 base-specific contacts above are the
RNA side. On the DNA side, the ssDNA-target-bound structure shows CasA gripping the
displaced strand
[PMID:25123481 "Cse1 contacts the first displaced DNA nucleotide (position 6)"],
with the displaced strand threading around the CasA four-helix bundle
[PMID:25123481 "As the PAM is bound at the L1 loop of Cse1 (31), the displaced strand must first loop around the four-helix bundle of Cse1 to gain access to the groove"],
and the target itself lying in a groove that CasA helps form
[PMID:25123481 "The ssDNA target is juxtaposed to the guide region of the crRNA in a groove formed by the Cas7 filament, the four-helix bundle of Cse1, and the Cse2 dimer"].

### Self/non-self discrimination (PAM reading)

CasA is the discriminating subunit. The CasA loop is what scans for the
protospacer-adjacent motif
[PMID:22521690 "Our data suggest a model in which the CasA loop scans DNA for this short motif"],
and PAM dependence of target binding, plus its strand asymmetry, was shown directly
[PMID:22521689 "Furthermore, efficient target binding requires that the target sequence is flanked by a Protospacer Adjacent Motif (PAM), with PAM recognition taking place exclusively in the targeted strand of the DNA."].
UniProt records the supporting mutagenesis on Q46901: F129A gives an "80% increase in
phage sensitivity; 500-fold decrease in affinity for target dsDNA" and N131A a "60-fold
decrease in affinity for target dsDNA" (both ECO:0000269|PubMed:22521690).

### Cas3 recruitment — the distinctive CasA function

This is the function GOA currently does not express at all. Cas3 is not recruited to
apo-Cascade
[PMID:22521689 "The BiFC analysis reveals that Cascade does not interact with Cas3 in the absence of invading DNA"],
but after target recognition Cas3 and CasA are brought into contact in vivo
[PMID:22521689 "This shows that Cascade and Cas3 specifically interact during infection upon protospacer recognition and that Cse1 and Cas3 are in close proximity of each other in the Cascade-Cas3 binary effector complex."].
The CasA subunit is read as the docking site
[PMID:22521689 "The existence of these fusion proteins suggests that stand-alone Cas3 also directly interacts with Cascade in vivo, and that the Cse1 subunit may provide a docking site for such an association."],
[PMID:22521689 "The conformational changes of Cascade and the target DNA may expose an interaction surface for Cas3 at or near the Cse1 subunit."],
and the independent ssDNA-bound crystal structure maps the same interface
[PMID:25123481 "Negative stain reconstruction of a complex between dsDNA-bound Cascade and Cas3 revealed Cas3 binds Cascade between the four-helix bundle and the base of Cse1"],
downstream of R-loop formation
[PMID:25123481 "Following R-loop formation, Cascade recruits the Cas3 helicase-nuclease"].

CasA therefore performs a step itself — it brings the trans-acting nuclease into
productive contact with the licensed R-loop — which is what GO:0030674
protein-macromolecule adaptor activity describes ("An adaptor activity that brings
together two or more macromolecules in contact, permitting those molecules to function
in a coordinated way"). I propose it as a `NEW` row with IPI evidence from
PMID:22521689 and UniProtKB:P38036 (Cas3) in `supporting_entities`.

Comparator check (as required before any `NEW`): I queried QuickGO for every GO
annotation on the type I-F large subunit Cas8f/Csy1 (UniProtKB:Q02ML9) and found only
two rows, both GO:0005515 protein binding (PMID:21536913, PMID:26416740). No Cas8-family
protein anywhere carries an adaptor or recruitment term. Unlike the AGT/angiotensinogen
case in CLAUDE.md, this is not a well-populated term from which my gene is
systematically absent — GO:0030674 is used in *E. coli* for exactly this kind of
protein (bamE, nlpI, mipA, acrA, all IDA/IPI) and Cas8f is simply uncurated beyond
protein binding. So the absence reads as an uncurated gap, not a convention. I record
the comparator result in the `reason` so a human can overrule me cheaply.

### The zinc question

GOA holds GO:0008270 zinc ion binding for Q46901 as IDA from PMID:25103409. The cited
structure paper identifies the ligand but does not assign its element
[PMID:25103409 "Cse1 is a large two-domain protein that adopts a unique globular fold that contains a metal-ion coordinated by four cysteines (C140, C143, C250, and C253), and a C-terminal four-helix bundle"].
UniProt Q46901 carries no `BINDING` feature for a metal at all, and no keyword for zinc.
A Cys4 site is of course a classic Zn site, but the cited evidence supports only metal
ion binding, so I MODIFY to GO:0046872 metal ion binding (a generalisation, which
CLAUDE.md explicitly sanctions) rather than REMOVE. If anomalous scattering or
metal analysis elsewhere establishes Zn, the specific term should come back.

### Ontology gaps recorded

1. **No cellular-component term for Cascade.** A QuickGO ontology search for "CRISPR"
   returns exactly five terms, all biological_process: GO:0099048, GO:0043571,
   GO:0098672 and two obsolete regulation terms (GO:0110132, GO:0110133). There is no CC
   term for Cascade or any CRISPR surveillance complex, which is why all eleven subunits
   sit on the bare GO:0032991 root. ComplexPortal does have the complex (CPX-1005,
   "Cascade complex"; cross-referenced from Q46899). The best existing GO term is
   GO:1990904 ribonucleoprotein complex, which is a real improvement over the root and
   is directly supported by the structure and the composition papers; I MODIFY to it and
   additionally propose the missing specific CC term.
2. **No molecular-function term for crRNA-guided target recognition.** Noted in
   `modules/crispr_cas_adaptive_immunity.yaml` knowledge_gaps; I do not invent an id for
   it and raise it in `suggested_questions`. CasA's own PAM-scanning contribution is
   recorded with GO:0003677 DNA binding, which is what GOA already has.
