# hemH assessment notes

## Identity and core reaction

Q88PV4 (PP_0744) is the reviewed KT2440 ferrochelatase assigned EC 4.98.1.1.
UniProt predicts insertion of ferrous iron into protoporphyrin IX to form heme
b, identifies the reaction as the single protoheme-forming step, and assigns a
cytoplasmic location
[file:PSEPK/hemH/hemH-uniprot.txt "Catalyzes the ferrous insertion into protoporphyrin IX."]
[file:PSEPK/hemH/hemH-uniprot.txt "biosynthesis; protoheme from protoporphyrin-IX: step 1/1."].
The record is reviewed, but these functional details are HAMAP-rule based rather
than direct KT2440 biochemistry.

## OpenScientist assessment

The OpenScientist report correctly identifies the target, reaction, endpoint,
and absence of a dedicated KT2440 HemH experiment. It also presents unsaved
sequence, pairwise-alignment, and AlphaFold analyses and uses them to propose an
internal [2Fe-2S] cluster. Ortholog studies do not establish that cofactor,
inner-membrane association, detailed metal specificity, catalytic mechanism, or
essentiality for Q88PV4. Its pathway sketch names HemG/HemY but omits the
KT2440 HemJ protein PP_0431. These extrapolations were not used as target
evidence.

## Curation decisions

GO:0004325 is accepted as the exact predicted molecular function, and the
cytoplasm annotation is accepted from the UniProt/HAMAP assignment. The broad
porphyrin-biosynthesis row is modified to the live endpoint term GO:0006785.
The imported broad heme-biosynthesis annotation remains correct, while the
endpoint term and terminal catalytic activity carry the core interpretation.
