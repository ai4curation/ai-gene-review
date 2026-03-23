# glk Gene Research Notes

## Identity

- `glk` in *Pseudomonas putida* KT2440 corresponds to UniProt `Q88P42` and locus `PP_1011`, and UniProt annotates the protein as glucokinase (EC 2.7.1.2) in the bacterial glucokinase family with cytoplasmic localization. [file:PSEPK/glk/glk-uniprot.txt "RecName: Full=Glucokinase"; "EC=2.7.1.2"; "SUBCELLULAR LOCATION: Cytoplasm"; "Belongs to the bacterial glucokinase family."]

## Core Biochemistry

- In KT2440, glucose imported into the cytoplasm is phosphorylated by glucokinase to glucose-6-phosphate before conversion to 6-phosphogluconate. [PMID:17483213 Convergent peripheral pathways catalyze initial glucose catabolism in *Pseudomonas putida*: genomic and flux analysis, "Glucose is transported to the cytoplasm in a process mediated by an ABC uptake system encoded by open reading frames PP1015 to PP1018 and is then phosphorylated by glucokinase (encoded by the glk gene) and converted by glucose-6-phosphate dehydrogenase (encoded by the zwf genes) to 6-phosphogluconate."]

- *P. putida* catabolizes glucose through three simultaneous routes that converge at 6-phosphogluconate, and the glucokinase branch is quantitatively important within that network. [PMID:17483213 Convergent peripheral pathways catalyze initial glucose catabolism in *Pseudomonas putida*: genomic and flux analysis, "glucose catabolism in Pseudomonas putida occurs through the simultaneous operation of three pathways that converge at the level of 6-phosphogluconate"; "although all three functioned simultaneously, the glucokinase pathway and the 2-ketogluconate loop were quantitatively more important than the direct phosphorylation of gluconate."]

- The 2007 mutant and flux study concluded that the glucokinase pathway is required for growth on glucose in KT2440. [PMID:17483213 Convergent peripheral pathways catalyze initial glucose catabolism in *Pseudomonas putida*: genomic and flux analysis, "It can therefore be concluded that the glucokinase pathway is a sine qua non condition for P. putida to grow with glucose."]

## Pathway Context And Regulation

- `glk` is physically linked to the Entner-Doudoroff pathway because `edd` and `glk` form one operon in KT2440. [PMID:19506074 Regulation of Glucose Metabolism in *Pseudomonas*: The Phosphorylative Branch and Entner-Doudoroff Enzymes Are Regulated by a Repressor Containing a Sugar Isomerase Domain, "The edd and glk genes form another operon that encodes, respectively, 6-phosphogluconate dehydratase (the first enzyme of the Entner-Doudoroff pathway) and glucokinase (an enzyme of the glucose phosphorylative pathway)."]

- Because of this genomic organization, the glucokinase pathway is co-induced with Entner-Doudoroff genes and is expressed even during growth on gluconate or 2-ketogluconate. [PMID:19506074 Regulation of Glucose Metabolism in *Pseudomonas*: The Phosphorylative Branch and Entner-Doudoroff Enzymes Are Regulated by a Repressor Containing a Sugar Isomerase Domain, "the glucokinase pathway genes are co-transcribed with Entner-Doudoroff pathway enzymes"; "the glucokinase pathway is induced when bacteria are exposed to gluconate and 2-ketogluconate."]

- HexR controls the relevant promoters through sensing KDPG rather than glucose or glucose-6-phosphate, placing `glk` in a broader glucose-responsive Entner-Doudoroff regulatory module. [PMID:19506074 Regulation of Glucose Metabolism in *Pseudomonas*: The Phosphorylative Branch and Entner-Doudoroff Enzymes Are Regulated by a Repressor Containing a Sugar Isomerase Domain, "Binding of the Entner-Doudoroff pathway intermediate 2-keto-3-deoxy-6-phosphogluconate to HexR released the repressor from its target operators, whereas other chemicals such as glucose, glucose 6-phosphate, and 6-phosphogluconate did not induce complex dissociation."]

## Annotation Implications

- The strongest core annotation for `glk` is glucokinase activity coupled to glucose catabolism through the Entner-Doudoroff-centered network.

- `ATP binding` and `D-glucose binding` are mechanistically true but substantially less informative than the specific catalytic term `glucokinase activity`.

- For cellular component, `cytosol` is the more specific GO term for a soluble bacterial cytoplasmic enzyme, while `cytoplasm` is acceptable but broader.
