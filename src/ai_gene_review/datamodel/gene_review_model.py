from __future__ import annotations 

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal 
from enum import Enum 
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    field_validator
)


metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )
    pass




class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'gene_review',
     'default_range': 'string',
     'description': 'Schema for gene curation Top level entity is a GeneReview, '
                    'which is about a single gene (and its equivalent swiss-prot '
                    'entry). It contains a high level summary of the gene, plus a '
                    'review of all existing annotations. It also contains a list '
                    'of core functions, which are GO-CAM-like annotons describing '
                    'the core evolved functions of the gene.',
     'id': 'https://ai4curation.io/ai-gene-review',
     'imports': ['linkml:types'],
     'name': 'gene_review',
     'prefixes': {'ECO': {'prefix_prefix': 'ECO',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/ECO_'},
                  'IAO': {'prefix_prefix': 'IAO',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/IAO_'},
                  'SO': {'prefix_prefix': 'SO',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/SO_'},
                  'dcat': {'prefix_prefix': 'dcat',
                           'prefix_reference': 'http://www.w3.org/ns/dcat#'},
                  'dcterms': {'prefix_prefix': 'dcterms',
                              'prefix_reference': 'http://purl.org/dc/terms/'},
                  'gene_review': {'prefix_prefix': 'gene_review',
                                  'prefix_reference': 'https://w3id.org/ai4curation/gene_review/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'oa': {'prefix_prefix': 'oa',
                         'prefix_reference': 'http://www.w3.org/ns/oa#'},
                  'owl': {'prefix_prefix': 'owl',
                          'prefix_reference': 'http://www.w3.org/2002/07/owl#'},
                  'rdf': {'prefix_prefix': 'rdf',
                          'prefix_reference': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'},
                  'rdfs': {'prefix_prefix': 'rdfs',
                           'prefix_reference': 'http://www.w3.org/2000/01/rdf-schema#'},
                  'skos': {'prefix_prefix': 'skos',
                           'prefix_reference': 'http://www.w3.org/2004/02/skos/core#'},
                  'xsd': {'prefix_prefix': 'xsd',
                          'prefix_reference': 'http://www.w3.org/2001/XMLSchema#'}},
     'source_file': 'src/ai_gene_review/schema/gene_review.yaml'} )

class ModuleTypeEnum(str, Enum):
    """
    Broad type of biological module node.
    """
    MODULE = "MODULE"
    """
    Generic or unspecified module.
    """
    BIOLOGICAL_PROCESS = "BIOLOGICAL_PROCESS"
    """
    Biological-process-like module.
    """
    MOLECULAR_FUNCTION = "MOLECULAR_FUNCTION"
    """
    Molecular-function-like module.
    """
    METABOLIC_PATHWAY = "METABOLIC_PATHWAY"
    """
    Metabolic pathway or pathway segment.
    """
    SIGNALING_PATHWAY = "SIGNALING_PATHWAY"
    """
    Signaling pathway or pathway segment.
    """
    DEVELOPMENTAL_PROCESS = "DEVELOPMENTAL_PROCESS"
    """
    Developmental process, stage, or program.
    """
    CELLULAR_COMPONENT = "CELLULAR_COMPONENT"
    """
    Cellular component or structure viewed as a module.
    """
    ORGANELLE_LIFECYCLE = "ORGANELLE_LIFECYCLE"
    """
    Assembly, maintenance, operation, and turnover of an organelle.
    """
    PROTEIN_COMPLEX = "PROTEIN_COMPLEX"
    """
    Protein complex or complex lifecycle.
    """
    REACTION = "REACTION"
    """
    Reaction-like module step.
    """
    TRANSPORT_STEP = "TRANSPORT_STEP"
    """
    Transport or translocation step.
    """
    REGULATORY_STEP = "REGULATORY_STEP"
    """
    Regulatory or control step.
    """


class VariantSelectionEnum(str, Enum):
    """
    How variants in a variant set may be selected in a realization.
    """
    EXACTLY_ONE = "EXACTLY_ONE"
    """
    Exactly one variant applies.
    """
    ONE_OR_MORE = "ONE_OR_MORE"
    """
    One or more variants may apply.
    """
    ZERO_OR_MORE = "ZERO_OR_MORE"
    """
    Variants are optional and any number may apply.
    """


class ParticipantSelectorTypeEnum(str, Enum):
    """
    How a module annoton participant is selected.
    """
    GENE = "GENE"
    """
    A concrete gene.
    """
    GENE_PRODUCT = "GENE_PRODUCT"
    """
    A concrete gene product, protein, isoform, or form.
    """
    PROTEIN_COMPLEX = "PROTEIN_COMPLEX"
    """
    A concrete protein-containing complex or subcomplex.
    """
    FAMILY = "FAMILY"
    """
    Any member of a specified family or orthogroup.
    """
    DOMAIN = "DOMAIN"
    """
    Any entity with a specified domain, motif, or site.
    """
    ORTHOLOG_OF = "ORTHOLOG_OF"
    """
    Any ortholog of a specified gene.
    """
    HOMOLOG_OF = "HOMOLOG_OF"
    """
    Any homolog of a specified gene.
    """
    ANY_WITH_FUNCTION = "ANY_WITH_FUNCTION"
    """
    Any participant satisfying the specified molecular function descriptor.
    """
    ANY_WITH_DOMAIN = "ANY_WITH_DOMAIN"
    """
    Any participant satisfying the specified domain descriptor.
    """
    ANY_PARTICIPANT = "ANY_PARTICIPANT"
    """
    An unspecified participant.
    """


class ModuleConnectionTypeEnum(str, Enum):
    """
    Common connection types between module elements.
    """
    PRECEDES = "PRECEDES"
    """
    The source occurs before the target.
    """
    CAUSES = "CAUSES"
    """
    The source causally promotes or produces the target.
    """
    POSITIVELY_REGULATES = "POSITIVELY_REGULATES"
    """
    The source positively regulates the target.
    """
    NEGATIVELY_REGULATES = "NEGATIVELY_REGULATES"
    """
    The source negatively regulates the target.
    """
    PROVIDES_INPUT_FOR = "PROVIDES_INPUT_FOR"
    """
    The source provides material, signal, or context used by the target.
    """
    HAS_INPUT = "HAS_INPUT"
    """
    The target has the source as input.
    """
    HAS_OUTPUT = "HAS_OUTPUT"
    """
    The source has the target as output.
    """
    PART_OF = "PART_OF"
    """
    The source is part of the target.
    """


class EvidenceType(str, Enum):
    """
    Gene Ontology evidence codes mapped to Evidence and Conclusion Ontology (ECO) terms
    """
    EXP = "EXP"
    """
    Inferred from Experiment
    """
    IDA = "IDA"
    """
    Inferred from Direct Assay
    """
    IPI = "IPI"
    """
    Inferred from Physical Interaction
    """
    IMP = "IMP"
    """
    Inferred from Mutant Phenotype
    """
    IGI = "IGI"
    """
    Inferred from Genetic Interaction
    """
    IEP = "IEP"
    """
    Inferred from Expression Pattern
    """
    HTP = "HTP"
    """
    Inferred from High Throughput Experiment
    """
    HDA = "HDA"
    """
    Inferred from High Throughput Direct Assay
    """
    HMP = "HMP"
    """
    Inferred from High Throughput Mutant Phenotype
    """
    HGI = "HGI"
    """
    Inferred from High Throughput Genetic Interaction
    """
    HEP = "HEP"
    """
    Inferred from High Throughput Expression Pattern
    """
    IBA = "IBA"
    """
    Inferred from Biological aspect of Ancestor
    """
    IBD = "IBD"
    """
    Inferred from Biological aspect of Descendant
    """
    IKR = "IKR"
    """
    Inferred from Key Residues
    """
    IRD = "IRD"
    """
    Inferred from Rapid Divergence
    """
    ISS = "ISS"
    """
    Inferred from Sequence or structural Similarity
    """
    ISO = "ISO"
    """
    Inferred from Sequence Orthology
    """
    ISA = "ISA"
    """
    Inferred from Sequence Alignment
    """
    ISM = "ISM"
    """
    Inferred from Sequence Model
    """
    IGC = "IGC"
    """
    Inferred from Genomic Context
    """
    RCA = "RCA"
    """
    Inferred from Reviewed Computational Analysis
    """
    TAS = "TAS"
    """
    Traceable Author Statement
    """
    NAS = "NAS"
    """
    Non-traceable Author Statement
    """
    IC = "IC"
    """
    Inferred by Curator
    """
    ND = "ND"
    """
    No biological Data available
    """
    IEA = "IEA"
    """
    Inferred from Electronic Annotation
    """


class ActionEnum(str, Enum):
    ACCEPT = "ACCEPT"
    """
    Accept the existing annotation as-is, no modifications, and retain as representing the core function of the gene
    """
    KEEP_AS_NON_CORE = "KEEP_AS_NON_CORE"
    """
    Keep the existing annotation as-is, but mark it as non-core. For pleiotropic genes, this may be the developmental processes, or other processes that are not the core function of the gene.
    """
    REMOVE = "REMOVE"
    """
    Remove the existing annotation, as it is unlikely to be correct based on combined evidence
    """
    MODIFY = "MODIFY"
    """
    The essence of the annotation is sound, but there are better terms to use (use in combination with proposed_replacement_terms). if the term is too general, then MODIFY should be used, with a proposed replacement term for the correct specific function. sometimes terms can also be overly specific and contorted, so in some cases you might want to generalize
    """
    MARK_AS_OVER_ANNOTATED = "MARK_AS_OVER_ANNOTATED"
    """
    The term is not entirely wrong, but likely represents an over-annotation of the gene
    """
    UNDECIDED = "UNDECIDED"
    """
    The annotation is not clear, and the reviewer is not sure what to do with it. ALWAYS USE THIS IF YOU ARE UNABLE TO ACCESS RELEVANT PUBLICATIONS
    """
    PENDING = "PENDING"
    """
    The review entry is a stub, and the review has not been completed yet.
    """
    NEW = "NEW"
    """
    This is a proposed annotation, not one that exists in the existing GO annotations. Use this to propose a new annotation not covered by the existing GO annotations. Use this conservatively, do not over-annotate, especially for biological process. Do not use for indirect or pleiotropic effects. Be sure you have good evidence, this can be from multiple sources.
    """


class AnnotationQualifierEnum(str, Enum):
    """
    GO annotation qualifiers specifying the relationship between a gene product and a GO term. These correspond to the QUALIFIER column in GAF/GPAD files and the QuickGO API.
    """
    enables = "enables"
    """
    The gene product has the molecular function activity (MF qualifier). The gene product independently possesses this catalytic or binding activity.
    """
    contributes_to = "contributes_to"
    """
    The gene product contributes to a molecular function as part of a complex (MF qualifier). The gene product does not independently have this activity but is required for the complex to have it. Typical for accessory/structural subunits of multi-protein complexes (e.g., accessory subunit of NADH dehydrogenase).
    """
    involved_in = "involved_in"
    """
    The gene product is involved in a biological process (BP qualifier).
    """
    acts_upstream_of = "acts_upstream_of"
    """
    The gene product acts upstream of or within a biological process (BP qualifier).
    """
    acts_upstream_of_positive_effect = "acts_upstream_of_positive_effect"
    """
    Acts upstream of or within, positive effect (BP qualifier).
    """
    acts_upstream_of_negative_effect = "acts_upstream_of_negative_effect"
    """
    Acts upstream of or within, negative effect (BP qualifier).
    """
    acts_upstream_of_or_within = "acts_upstream_of_or_within"
    """
    Acts upstream of or within a biological process (BP qualifier).
    """
    acts_upstream_of_or_within_positive_effect = "acts_upstream_of_or_within_positive_effect"
    """
    Acts upstream of or within, positive effect (BP qualifier).
    """
    acts_upstream_of_or_within_negative_effect = "acts_upstream_of_or_within_negative_effect"
    """
    Acts upstream of or within, negative effect (BP qualifier).
    """
    located_in = "located_in"
    """
    The gene product is located in a cellular component (CC qualifier).
    """
    is_active_in = "is_active_in"
    """
    The gene product is active in a cellular component (CC qualifier). Stronger than located_in -- implies the gene product carries out its molecular function in this location.
    """
    part_of = "part_of"
    """
    The gene product is part of a cellular component, typically a complex (CC qualifier).
    """
    colocalizes_with = "colocalizes_with"
    """
    The gene product colocalizes with a cellular component (CC qualifier). Weaker than located_in or part_of.
    """


class GOTermEnum(str):
    """
    A term in the GO ontology (including roots, to allow ND annotations)
    """
    pass


class GOMolecularActivityEnum(str):
    """
    A molecular activity term in the GO ontology
    """
    pass


class GOBiologicalProcessEnum(str):
    """
    A biological process term in the GO ontology
    """
    pass


class GOCellularLocationEnum(str):
    """
    A cellular location term in the GO ontology (excludes protein-containing complexes)
    """
    pass


class GOProteinContainingComplexEnum(str):
    """
    A protein-containing complex term in the GO ontology
    """
    pass


class ROTermEnum(str):
    """
    A term in the relation ontology
    """
    pass


class ProductTypeEnum(str, Enum):
    """
    Type of gene product
    """
    PROTEIN = "PROTEIN"
    """
    Protein-coding gene
    """
    MIRNA = "MIRNA"
    """
    microRNA
    """
    LNCRNA = "LNCRNA"
    """
    Long non-coding RNA
    """
    SNORNA = "SNORNA"
    """
    Small nucleolar RNA
    """
    SNRNA = "SNRNA"
    """
    Small nuclear RNA
    """
    TRNA = "TRNA"
    """
    Transfer RNA
    """
    RRNA = "RRNA"
    """
    Ribosomal RNA
    """
    PIRNA = "PIRNA"
    """
    PIWI-interacting RNA
    """
    ANTISENSE_RNA = "ANTISENSE_RNA"
    """
    Antisense RNA
    """
    PSEUDOGENE = "PSEUDOGENE"
    """
    Pseudogene
    """
    OTHER_NCRNA = "OTHER_NCRNA"
    """
    Other non-coding RNA
    """


class GeneReviewStatusEnum(str, Enum):
    """
    Status of the gene review process
    """
    INITIALIZED = "INITIALIZED"
    """
    All annotations have action PENDING - review has been initialized but not started
    """
    IN_PROGRESS = "IN_PROGRESS"
    """
    At least one annotation is PENDING and at least one annotation is not PENDING - review is underway
    """
    DRAFT = "DRAFT"
    """
    No PENDING annotations, but may have validation warnings - review is complete but needs refinement
    """
    COMPLETE = "COMPLETE"
    """
    No PENDING annotations and no validation warnings - review is fully complete and validated
    """


class ManuscriptSection(str, Enum):
    """
    Sections of a scientific manuscript or publication
    """
    TITLE = "TITLE"
    """
    Title section
    """
    ABSTRACT = "ABSTRACT"
    """
    Abstract
    """
    KEYWORDS = "KEYWORDS"
    """
    Keywords
    """
    INTRODUCTION = "INTRODUCTION"
    """
    Introduction/Background
    """
    LITERATURE_REVIEW = "LITERATURE_REVIEW"
    """
    Literature review
    """
    METHODS = "METHODS"
    """
    Methods/Materials and Methods
    """
    RESULTS = "RESULTS"
    """
    Results
    """
    DISCUSSION = "DISCUSSION"
    """
    Discussion
    """
    CONCLUSIONS = "CONCLUSIONS"
    """
    Conclusions
    """
    APPENDICES = "APPENDICES"
    """
    Appendices
    """
    SUPPLEMENTARY_MATERIAL = "SUPPLEMENTARY_MATERIAL"
    """
    Supplementary material
    """
    DATABASE_ENTRY = "DATABASE_ENTRY"
    """
    Database entry
    """
    OTHER = "OTHER"
    """
    Other main text section
    """


class RuleTypeEnum(str, Enum):
    """
    Type of UniProt annotation rule
    """
    ARBA = "ARBA"
    """
    Association-Rule-Based Annotator rule (automatically mined)
    """
    UNIRULE = "UNIRULE"
    """
    Expert-curated UniRule
    """


class RuleReviewStatusEnum(str, Enum):
    """
    Status of the rule review
    """
    PENDING = "PENDING"
    """
    Review has not been started
    """
    IN_PROGRESS = "IN_PROGRESS"
    """
    Review is underway
    """
    COMPLETE = "COMPLETE"
    """
    Review is complete
    """


class RuleActionEnum(str, Enum):
    """
    Recommended action for the rule
    """
    ACCEPT = "ACCEPT"
    """
    Rule is correct and should be kept as-is
    """
    MODIFY = "MODIFY"
    """
    Rule needs modification (see suggested_modifications)
    """
    DEPRECATE = "DEPRECATE"
    """
    Rule should be removed or retired
    """
    SPLIT = "SPLIT"
    """
    Rule should be split into multiple more specific rules
    """
    MERGE = "MERGE"
    """
    Rule should be merged with another related rule
    """
    UNDECIDED = "UNDECIDED"
    """
    Unable to determine appropriate action
    """


class ParsimonyEnum(str, Enum):
    """
    Assessment of rule parsimony (simplicity vs complexity)
    """
    PARSIMONIOUS = "PARSIMONIOUS"
    """
    Rule is appropriately simple - conditions are necessary and sufficient
    """
    ACCEPTABLE = "ACCEPTABLE"
    """
    Rule complexity is reasonable given the biological context
    """
    REDUNDANT = "REDUNDANT"
    """
    Some conditions are redundant and could be removed
    """
    OVERLY_COMPLEX = "OVERLY_COMPLEX"
    """
    Rule has unnecessary complexity that should be simplified
    """


class LiteratureSupportEnum(str, Enum):
    """
    Level of literature support for the rule
    """
    STRONG = "STRONG"
    """
    Multiple high-quality papers directly support the domain-function relationship
    """
    MODERATE = "MODERATE"
    """
    Some supporting evidence exists but not comprehensive
    """
    WEAK = "WEAK"
    """
    Limited evidence, mostly indirect or from computational studies
    """
    NONE = "NONE"
    """
    No literature support found
    """
    CONTRADICTED = "CONTRADICTED"
    """
    Literature contradicts the rule's predicted function
    """


class OverlapEnum(str, Enum):
    """
    Assessment of condition overlap/redundancy
    """
    NONE = "NONE"
    """
    Conditions are independent and non-overlapping
    """
    MINOR = "MINOR"
    """
    Slight overlap but conditions add meaningful specificity
    """
    SIGNIFICANT = "SIGNIFICANT"
    """
    Substantial overlap - conditions may be capturing the same thing
    """
    COMPLETE = "COMPLETE"
    """
    Conditions are essentially equivalent/redundant
    """


class SpecificityEnum(str, Enum):
    """
    Assessment of GO term specificity
    """
    TOO_BROAD = "TOO_BROAD"
    """
    GO term is too general - a more specific term should be used
    """
    APPROPRIATE = "APPROPRIATE"
    """
    GO term specificity matches the evidence
    """
    TOO_NARROW = "TOO_NARROW"
    """
    GO term is overly specific for what the domains predict
    """
    MISMATCHED = "MISMATCHED"
    """
    GO term is in wrong branch or aspect
    """


class TaxonomicScopeEnum(str, Enum):
    """
    Assessment of taxonomic restriction appropriateness
    """
    TOO_BROAD = "TOO_BROAD"
    """
    Taxon is too inclusive - should be restricted further
    """
    APPROPRIATE = "APPROPRIATE"
    """
    Taxonomic scope matches the domain's evolutionary distribution
    """
    TOO_NARROW = "TOO_NARROW"
    """
    Taxon is overly restrictive - function applies more broadly
    """
    MISSING = "MISSING"
    """
    Rule lacks necessary taxonomic restriction
    """
    UNNECESSARY = "UNNECESSARY"
    """
    Taxonomic restriction is not needed for this domain
    """


class ConditionTypeEnum(str, Enum):
    """
    Types of conditions in rule antecedents
    """
    INTERPRO = "INTERPRO"
    """
    InterPro domain/family
    """
    FUNFAM = "FUNFAM"
    """
    CATH FunFam functional family
    """
    PANTHER = "PANTHER"
    """
    PANTHER family
    """
    PFAM = "PFAM"
    """
    Pfam domain
    """
    TAXON = "TAXON"
    """
    Taxonomic constraint
    """
    SEQUENCE_LENGTH = "SEQUENCE_LENGTH"
    """
    Sequence length constraint
    """
    OTHER = "OTHER"
    """
    Other condition type
    """


class ProteinDatabaseEnum(str, Enum):
    """
    Protein database types for rule analysis
    """
    SWISSPROT = "SWISSPROT"
    """
    Swiss-Prot (reviewed, manually curated proteins)
    """
    TREMBL = "TREMBL"
    """
    TrEMBL (unreviewed, automatically annotated proteins)
    """
    UNIPROT = "UNIPROT"
    """
    Full UniProtKB (Swiss-Prot + TrEMBL)
    """


class InterProTypeEnum(str, Enum):
    """
    InterPro entry types categorizing protein signatures
    """
    FAMILY = "FAMILY"
    """
    Protein family (groups of proteins sharing similar sequence and function)
    """
    DOMAIN = "DOMAIN"
    """
    Protein domain (distinct functional or structural unit)
    """
    ACTIVE_SITE = "ACTIVE_SITE"
    """
    Active site (residues directly involved in catalysis)
    """
    BINDING_SITE = "BINDING_SITE"
    """
    Binding site (residues involved in binding substrates/ligands)
    """
    CONSERVED_SITE = "CONSERVED_SITE"
    """
    Conserved site (conserved residues with functional significance)
    """
    REPEAT = "REPEAT"
    """
    Repeat (short sequence motif that occurs multiple times)
    """
    HOMOLOGOUS_SUPERFAMILY = "HOMOLOGOUS_SUPERFAMILY"
    """
    Homologous superfamily (proteins with distant evolutionary relationships)
    """
    PTM = "PTM"
    """
    Post-translational modification site
    """


class OverlapInterpretationEnum(str, Enum):
    """
    Automated interpretation of domain overlap patterns
    """
    REDUNDANT = "REDUNDANT"
    """
    Very high overlap (Jaccard > 0.9), conditions are nearly identical
    """
    SUBSET = "SUBSET"
    """
    One condition is a subset of the other (containment > 0.95)
    """
    HIGH_OVERLAP = "HIGH_OVERLAP"
    """
    High overlap (Jaccard > 0.5), conditions are similar
    """
    MODERATE = "MODERATE"
    """
    Moderate overlap (0.2 < Jaccard <= 0.5)
    """
    LOW = "LOW"
    """
    Low overlap (Jaccard <= 0.2), conditions are mostly distinct
    """
    DISJOINT = "DISJOINT"
    """
    No overlap (intersection = 0), conditions are completely distinct
    """


class EntryTypeEnum(str, Enum):
    """
    Type of entry in a rule review (domain/family condition or GO term target)
    """
    INTERPRO = "INTERPRO"
    """
    InterPro entry (domain, family, repeat, etc.)
    """
    FUNFAM = "FUNFAM"
    """
    CATH FunFam (functional family from CATH database)
    """
    PANTHER = "PANTHER"
    """
    PANTHER family or subfamily
    """
    GO_TERM = "GO_TERM"
    """
    Gene Ontology term (annotation target)
    """


class EntryRelationshipEnum(str, Enum):
    """
    Type of relationship between entries in a rule
    """
    PREDICTS = "PREDICTS"
    """
    This entry predicts the target (this ⊆ target). Selected when containment_a_in_b is highest among {jaccard+0.05, containment_a_in_b, containment_b_in_a}.
    """
    PREDICTED_BY = "PREDICTED_BY"
    """
    This entry is predicted by the target (target ⊆ this). Selected when containment_b_in_a is highest among {jaccard+0.05, containment_a_in_b, containment_b_in_a}.
    """
    EQUIV = "EQUIV"
    """
    This entry is equivalent to the target (bidirectional high similarity). Selected when jaccard_boosted (jaccard + 0.05) is highest among {jaccard+0.05, containment_a_in_b, containment_b_in_a}.
    """


class FunctionalIsoformTypeEnum(str, Enum):
    """
    Type of functional isoform or product. Distinguishes between different mechanisms that produce functionally distinct forms of a gene product.
    """
    SPLICE_VARIANT = "SPLICE_VARIANT"
    """
    Alternative splicing produces functionally distinct isoforms. Maps to one or more UniProt isoform IDs (e.g., P19544-1, P19544-2).
    """
    SPLICE_CLASS = "SPLICE_CLASS"
    """
    A class of splice variants that share functional properties. Groups multiple UniProt isoform IDs that have similar functions. Example: WT1 +KTS isoforms (multiple UniProt IDs) vs -KTS isoforms.
    """
    CLEAVAGE_PRODUCT = "CLEAVAGE_PRODUCT"
    """
    Post-translational proteolytic cleavage produces distinct peptides. Maps to UniProt chain IDs (PRO_NNNNNNN from FT PEPTIDE lines). Example: POMC cleavage into ACTH, alpha-MSH, beta-endorphin.
    """
    MODIFICATION_STATE = "MODIFICATION_STATE"
    """
    Post-translational modification creates functionally distinct forms. Example: Phosphorylated vs unphosphorylated forms with different activities.
    """
    CONFORMATIONAL_STATE = "CONFORMATIONAL_STATE"
    """
    Different conformational states with distinct functions. Example: GTP-bound vs GDP-bound forms of GTPases.
    """


class FunctionalIsoformMappingTypeEnum(str, Enum):
    """
    Type of identifier that a functional isoform maps to
    """
    UNIPROT_ISOFORM = "UNIPROT_ISOFORM"
    """
    UniProt isoform ID (e.g., P19544-1, Q07817-2)
    """
    UNIPROT_CHAIN = "UNIPROT_CHAIN"
    """
    UniProt chain/peptide ID from FT PEPTIDE (e.g., PRO_0000024969)
    """


class PredictedTermTypeEnum(str, Enum):
    """
    Type of predicted annotation term
    """
    EC = "EC"
    """
    Enzyme Commission number (e.g., EC:2.7.7.87)
    """
    GO_MF = "GO_MF"
    """
    GO Molecular Function term
    """
    GO_BP = "GO_BP"
    """
    GO Biological Process term
    """
    GO_CC = "GO_CC"
    """
    GO Cellular Component term
    """


class PredictionAssessmentEnum(str, Enum):
    """
    Assessment categories for computational predictions, based on de Crécy-Lagard et al. 2025 (PMID:40703034) Fig. 4.
    """
    COR = "COR"
    """
    Correct prediction - validated by literature/bioinformatic evidence as a genuinely novel correct prediction (CS=2)
    """
    CNN = "CNN"
    """
    Correct but Not Novel - the prediction matches an annotation already present in UniProt or in the training data. Not a novel discovery (CS=2)
    """
    LSP = "LSP"
    """
    Less Precise - the prediction is more generic than the existing annotation. Correct at a higher level but not informative (CS=2)
    """
    UNC = "UNC"
    """
    Uncertain - the prediction cannot be validated or refuted with available evidence. Requires additional experiments or data (CS=1)
    """
    PLI = "PLI"
    """
    Paralog Incorrect - wrong prediction due to failure to distinguish nonisofunctional paralogs within a protein superfamily (CS=0)
    """
    NPI = "NPI"
    """
    Nonparalog Incorrect - wrong prediction refuted by evidence: pathway absent in organism, activity belongs to a different gene, or published data contradict the prediction (CS=0)
    """
    REP = "REP"
    """
    Repetition - frequency-biased duplication of a common EC/GO term. The model assigns a high-frequency term (e.g., histidine kinase) to proteins with no sequence similarity to that family (CS=0)
    """


class PredictionErrorTypeEnum(str, Enum):
    """
    Types of errors that lead to incorrect functional predictions, based on Table 1 of de Crécy-Lagard et al. 2025 (PMID:40703034).
    """
    FAILURE_TO_CAPTURE_LITERATURE = "FAILURE_TO_CAPTURE_LITERATURE"
    """
    Type 1: Function is known and published but not captured in the database used for training. The protein is falsely labeled as unknown.
    """
    NAMING_INCONSISTENCY = "NAMING_INCONSISTENCY"
    """
    Type 2: Inconsistent naming of the same entity across databases leads to missed or incorrect propagation.
    """
    MULTIPLE_FUNCTIONS = "MULTIPLE_FUNCTIONS"
    """
    Type 3: Protein has multiple functions (fusion, moonlighting, promiscuity) and only one function is captured or a non-primary function is predicted.
    """
    CURATION_MISTAKE = "CURATION_MISTAKE"
    """
    Type 4: The training data contain an incorrect annotation from a biocuration error or an outdated annotation that has since been corrected.
    """
    EXPERIMENTAL_MISTAKE = "EXPERIMENTAL_MISTAKE"
    """
    Type 5: The training data are based on experimental findings that have been refuted or are inconclusive.
    """
    PARALOG_OVERANNOTATION = "PARALOG_OVERANNOTATION"
    """
    Type 6: Annotation wrongly propagated to a nonisofunctional paralog. The model fails to distinguish between paralogs with different substrate specificities or functions within the same superfamily.
    """
    FREQUENCY_BIAS = "FREQUENCY_BIAS"
    """
    The model makes predictions biased toward high-frequency labels in the training data, regardless of sequence features. Common with EC numbers like histidine kinase (2.7.13.3) or PTS transporter (2.7.1.69).
    """
    TRAINING_DATA_CONTAMINATION = "TRAINING_DATA_CONTAMINATION"
    """
    The prediction appears novel but the annotation was already present in the version of the database used to build the training set.
    """
    PATHWAY_CONTEXT_IGNORED = "PATHWAY_CONTEXT_IGNORED"
    """
    The model ignores metabolic/pathway context. The predicted activity requires a pathway that is absent from the organism's genome.
    """
    IN_VITRO_NOT_IN_VIVO = "IN_VITRO_NOT_IN_VIVO"
    """
    The predicted activity can be demonstrated in vitro but does not represent the in vivo biological function (e.g., promiscuous activity at orders of magnitude lower rate than the dedicated enzyme).
    """


class ReferenceRelevanceEnum(str, Enum):
    """
    Reviewer's assessment of how relevant a reference is to the gene's function and review.
    """
    HIGH = "HIGH"
    """
    Directly establishes or strongly informs the gene's function, mechanism, process, or localization
    """
    MEDIUM = "MEDIUM"
    """
    Provides supporting or corroborating evidence for a function or annotation
    """
    LOW = "LOW"
    """
    Background or contextual only (e.g. family/pathway reviews, methods, or a passing mention)
    """
    NONE = "NONE"
    """
    Not relevant to this gene's function (a candidate for removal from the references)
    """


class ReferenceCorrectnessEnum(str, Enum):
    """
    Reviewer's overall manual assessment of a reference's trustworthiness, spanning both citation correctness (does the identifier point to the intended paper that supports its use) and scientific soundness (is that paper's claim reliable). Single-valued: record the most salient issue and elaborate in review_notes. Complements is_invalid (retracted/replaced) and full_text_unavailable.
    """
    VERIFIED = "VERIFIED"
    """
    Identifier resolves to the intended paper, which supports how it is used, with no soundness concerns
    """
    UNVERIFIED = "UNVERIFIED"
    """
    Not yet manually checked (the default state)
    """
    WRONG_IDENTIFIER = "WRONG_IDENTIFIER"
    """
    Identifier resolves to a DIFFERENT paper than intended (e.g. a PMID pointing to an unrelated article)
    """
    MISCITED = "MISCITED"
    """
    Paper is correctly identified but does not actually support the claim it is cited for
    """
    DISPUTED = "DISPUTED"
    """
    Correctly cited, but the paper's central claim is contradicted or contested by other evidence
    """
    LOW_QUALITY = "LOW_QUALITY"
    """
    Correctly cited, but methodologically weak or preliminary; treat its conclusions with caution
    """


class FindingReviewStatusEnum(str, Enum):
    """
    Reviewer's assessment of the empirical standing of a specific finding (a statement extracted from a reference) in light of other evidence. Unlike ReferenceCorrectnessEnum, which judges a whole reference, this applies per finding: a paper may have some findings that stand and others that have been overturned. Use superseded_by to point to the reference(s) responsible.
    """
    CURRENT = "CURRENT"
    """
    The finding is consistent with the body of evidence and can be curated from
    """
    CORROBORATED = "CORROBORATED"
    """
    The finding is independently supported by additional evidence
    """
    DISPUTED = "DISPUTED"
    """
    The finding is contested or contradicted by other evidence, but not definitively refuted; curate with caution
    """
    OVERTURNED = "OVERTURNED"
    """
    The finding has been refuted or superseded by later, stronger evidence and should NOT be curated from; record the overturning reference(s) in superseded_by
    """
    UNVERIFIED = "UNVERIFIED"
    """
    The finding has not yet been manually assessed (default)
    """


class KnowledgeGapKindEnum(str, Enum):
    """
    The kind of ignorance a knowledge gap represents, which determines who can resolve it. A single gap may carry several values when it is a blend.
    """
    BIOLOGY = "BIOLOGY"
    """
    Nobody knows; resolvable only by new experiments. This is the unknome and the primary target of the Function Knowledge Gaps project.
    """
    CURATION = "CURATION"
    """
    The knowledge exists in the literature but is not yet annotated, or is annotated too generically. Resolvable by curation.
    """
    ONTOLOGY = "ONTOLOGY"
    """
    The knowledge exists but no GO/ontology term can express it (e.g. "structural subunit of complex X", or a novel activity). Resolvable by ontology development; usually paired with proposed_new_terms.
    """


class KnowledgeGapAspectEnum(str, Enum):
    """
    Which GO aspect (or pattern) is dark for a knowledge gap. Most "dark" genes are not uniformly dark.
    """
    MF_DARK = "MF_DARK"
    """
    Process/location known, molecular mechanism unknown. The most common and most insidious case — rich BP/CC make the gene look known. The "protein binding" smell lives here.
    """
    BP_DARK = "BP_DARK"
    """
    An activity is known but not what it is for (common in microbial/plant metabolism).
    """
    CC_DARK = "CC_DARK"
    """
    Function known, but where/when unknown.
    """
    WHOLLY_DARK = "WHOLLY_DARK"
    """
    Only root terms / IEA / "protein binding" survive review (the deep unknome).
    """
    RESIDUAL_SUBGAP = "RESIDUAL_SUBGAP"
    """
    The core function is textbook-solid, but one sharp, load-bearing mechanistic hole remains (e.g. an unidentified GEF/GAP, a catalysis-independent scaffolding mechanism, an unidentified recruit). Easy to miss because the gene looks finished.
    """


class KnowledgeGapStatusEnum(str, Enum):
    """
    Lifecycle status of a knowledge gap, tracking progress toward resolution.
    """
    OPEN = "OPEN"
    """
    Unresolved and not under active, evidence-producing investigation.
    """
    NARROWING = "NARROWING"
    """
    Under active investigation with emerging but still incomplete evidence.
    """
    CLOSING = "CLOSING"
    """
    Function-defining evidence exists (e.g. recent preprints) but has not yet propagated to peer-reviewed, GO-curated form.
    """
    RESOLVED = "RESOLVED"
    """
    The gap has been closed; retained for provenance/history.
    """


class PublicationTypeEnum(str, Enum):
    """
    The kind of publication or source a reference is. For PMIDs this is inferred from the PubMed publication-type ('PT') metadata; for non-literature references it is inferred from the identifier scheme. Used to test hypotheses about which evidence sources (primary papers, reviews, abstracts, deep research) suffice for GO annotation review.
    """
    PRIMARY_RESEARCH = "PRIMARY_RESEARCH"
    """
    An original/primary research article reporting new experimental or observational results (PubMed 'Journal Article' without a more specific review/secondary type).
    """
    REVIEW = "REVIEW"
    """
    A narrative review article that synthesizes prior literature (PubMed PT 'Review'). Reviews often carry phylogenetic/comparative reasoning and broad functional context.
    """
    SYSTEMATIC_REVIEW = "SYSTEMATIC_REVIEW"
    """
    A systematic review (PubMed PT 'Systematic Review').
    """
    META_ANALYSIS = "META_ANALYSIS"
    """
    A meta-analysis combining results across studies (PubMed PT 'Meta-Analysis').
    """
    COMMENT_EDITORIAL = "COMMENT_EDITORIAL"
    """
    A comment, editorial, letter, or news item (PubMed PT 'Comment', 'Editorial', 'Letter', 'News').
    """
    CASE_REPORT = "CASE_REPORT"
    """
    A clinical case report (PubMed PT 'Case Reports').
    """
    PREPRINT = "PREPRINT"
    """
    A preprint or other not-yet-peer-reviewed manuscript (PubMed PT 'Preprint').
    """
    DATABASE = "DATABASE"
    """
    A database record or curated method reference rather than a narrative publication (e.g. a GO_REF, Reactome pathway, or UniProt entry).
    """
    BIOINFORMATICS = "BIOINFORMATICS"
    """
    A local ad-hoc bioinformatics analysis carried out for this review, referenced via a 'file:' identifier (e.g. a bioinformatics RESULTS.md).
    """
    DEEP_RESEARCH = "DEEP_RESEARCH"
    """
    An AI/LLM deep-research report generated for this review, referenced via a 'file:' identifier (e.g. GENE-deep-research-PROVIDER.md).
    """
    OTHER = "OTHER"
    """
    A publication or source that does not fit the other categories.
    """
    UNKNOWN = "UNKNOWN"
    """
    The publication type could not be determined (e.g. PubMed metadata unavailable).
    """



class GeneReview(ConfiguredBaseModel):
    """
    Complete review for a gene
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review',
         'slot_usage': {'description': {'name': 'description', 'recommended': True}},
         'tree_root': True})

    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['GeneReview',
                       'AlternativeProduct',
                       'FunctionalIsoform',
                       'Term',
                       'Reference',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'RuleReview',
                       'RuleReviewEntry',
                       'PredictionReview']} })
    gene_symbol: str = Field(default=..., description="""Symbol of the gene""", json_schema_extra = { "linkml_meta": {'alias': 'gene_symbol', 'domain_of': ['GeneReview', 'PredictionReview']} })
    product_type: Optional[ProductTypeEnum] = Field(default=None, description="""Type of gene product (protein, ncRNA, etc.)""", json_schema_extra = { "linkml_meta": {'alias': 'product_type',
         'comments': ['currently not required, assumed PROTEIN by default, but this '
                      'may be explicit in future'],
         'domain_of': ['GeneReview']} })
    aliases: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'aliases', 'domain_of': ['GeneReview']} })
    tags: Optional[list[str]] = Field(default=None, description="""Tags associated with the gene for categorization and organization""", json_schema_extra = { "linkml_meta": {'alias': 'tags', 'domain_of': ['GeneReview']} })
    status: Optional[GeneReviewStatusEnum] = Field(default=None, description="""Overall status of the gene review""", json_schema_extra = { "linkml_meta": {'alias': 'status',
         'domain_of': ['GeneReview',
                       'ModuleReview',
                       'KnowledgeGap',
                       'RuleReview',
                       'PredictionReview'],
         'recommended': True} })
    description: Optional[str] = Field(default=None, description="""Description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['GeneReview',
                       'AlternativeProduct',
                       'FunctionalIsoform',
                       'Term',
                       'Descriptor',
                       'ModuleReview',
                       'ModuleNode',
                       'ParticipantSelector',
                       'ModuleConnection',
                       'CoreFunction',
                       'Experiment',
                       'RuleReview',
                       'PredictionReview'],
         'recommended': True,
         'slot_uri': 'dcterms:description'} })
    taxon: Term = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'taxon',
         'domain_of': ['GeneReview', 'ParticipantSelector', 'PredictionReview']} })
    alternative_products: Optional[list[AlternativeProduct]] = Field(default=None, description="""Alternative splicing products (isoforms) of the gene. Seeded from UniProt ALTERNATIVE PRODUCTS section. Only populated if there are multiple isoforms. Use this to document isoform-specific functions and biology. DEPRECATED: Use functional_isoforms instead for curated functional classes.""", json_schema_extra = { "linkml_meta": {'alias': 'alternative_products', 'domain_of': ['GeneReview']} })
    functional_isoforms: Optional[list[FunctionalIsoform]] = Field(default=None, description="""Curated functional isoform classes for the gene. Unlike alternative_products (which is seeded from UniProt), this field is purely curator/agent-defined to capture FUNCTIONALLY RELEVANT distinctions. Examples: - Splice classes that group multiple UniProt isoforms (e.g., WT1 +KTS vs -KTS) - Cleavage products from polyproteins (e.g., POMC peptides) - Modification states with distinct functions Only populate when there ARE functionally distinct forms worth documenting.""", json_schema_extra = { "linkml_meta": {'alias': 'functional_isoforms', 'domain_of': ['GeneReview']} })
    references: Optional[list[Reference]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'references',
         'domain_of': ['GeneReview', 'ModuleReview', 'RuleReview', 'PredictionReview']} })
    existing_annotations: Optional[list[ExistingAnnotation]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'existing_annotations', 'domain_of': ['GeneReview']} })
    core_functions: Optional[list[CoreFunction]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'core_functions', 'domain_of': ['GeneReview']} })
    proposed_new_terms: Optional[list[ProposedOntologyTerm]] = Field(default=None, description="""Proposed new ontology terms that should exist but don't""", json_schema_extra = { "linkml_meta": {'alias': 'proposed_new_terms', 'domain_of': ['GeneReview']} })
    suggested_questions: Optional[list[Question]] = Field(default=None, description="""Suggested questions to ask experts about the gene. Only include if not obvious from the literature.""", json_schema_extra = { "linkml_meta": {'alias': 'suggested_questions',
         'domain_of': ['GeneReview'],
         'recommended': True} })
    suggested_experiments: Optional[list[Experiment]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'suggested_experiments',
         'domain_of': ['GeneReview'],
         'recommended': True} })
    knowledge_gaps: Optional[list[KnowledgeGap]] = Field(default=None, description="""Curated, literature-grounded statements of what is NOT known — applicable at the level of the whole gene, a single existing annotation, a core function, a whole module, or a single module step/node. The inverse of core_functions: everywhere else the schema records what IS known; here it records, with the same evidentiary discipline, what is not. See the Function Knowledge Gaps project (projects/FUNCTION_KNOWLEDGE_GAPS.md).""", json_schema_extra = { "linkml_meta": {'alias': 'knowledge_gaps',
         'domain_of': ['GeneReview',
                       'ModuleReview',
                       'ModuleNode',
                       'Review',
                       'CoreFunction']} })


class AlternativeProduct(ConfiguredBaseModel):
    """
    An alternative splicing product (isoform) of the gene. Corresponds to UniProt isoform entries. Use this to document isoform-specific functions where different isoforms have distinct or even antagonistic biological activities. DEPRECATED: Use FunctionalIsoform instead for curated functional classes.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review',
         'slot_usage': {'description': {'description': 'Agent-populated description of '
                                                       "the isoform's function. "
                                                       'Document any isoform-specific '
                                                       'functions, expression '
                                                       'patterns, or biological '
                                                       'activities that differ from '
                                                       'other isoforms.',
                                        'name': 'description',
                                        'recommended': True},
                        'id': {'description': 'UniProt isoform ID (e.g., Q07817-1, '
                                              'Q07817-2)',
                               'name': 'id',
                               'required': True},
                        'name': {'description': 'Common name of the isoform (e.g., '
                                                'Bcl-xL, Bcl-xS)',
                                 'name': 'name',
                                 'required': False},
                        'sequence_note': {'description': 'Brief note about sequence '
                                                         'differences (e.g., "lacks '
                                                         'exon 2", "shorter '
                                                         'C-terminus")',
                                          'name': 'sequence_note',
                                          'required': False}}})

    id: str = Field(default=..., description="""UniProt isoform ID (e.g., Q07817-1, Q07817-2)""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['GeneReview',
                       'AlternativeProduct',
                       'FunctionalIsoform',
                       'Term',
                       'Reference',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'RuleReview',
                       'RuleReviewEntry',
                       'PredictionReview']} })
    name: Optional[str] = Field(default=None, description="""Common name of the isoform (e.g., Bcl-xL, Bcl-xS)""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['AlternativeProduct', 'FunctionalIsoform']} })
    sequence_note: Optional[str] = Field(default=None, description="""Brief note about sequence differences (e.g., \"lacks exon 2\", \"shorter C-terminus\")""", json_schema_extra = { "linkml_meta": {'alias': 'sequence_note', 'domain_of': ['AlternativeProduct']} })
    description: Optional[str] = Field(default=None, description="""Agent-populated description of the isoform's function. Document any isoform-specific functions, expression patterns, or biological activities that differ from other isoforms.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['GeneReview',
                       'AlternativeProduct',
                       'FunctionalIsoform',
                       'Term',
                       'Descriptor',
                       'ModuleReview',
                       'ModuleNode',
                       'ParticipantSelector',
                       'ModuleConnection',
                       'CoreFunction',
                       'Experiment',
                       'RuleReview',
                       'PredictionReview'],
         'recommended': True,
         'slot_uri': 'dcterms:description'} })


class FunctionalIsoform(ConfiguredBaseModel):
    """
    A curated functional isoform class. Unlike AlternativeProduct (which maps 1:1 to UniProt isoforms), this captures FUNCTIONALLY RELEVANT distinctions that may: - Group multiple UniProt isoforms into a functional class (e.g., WT1 +KTS isoforms) - Represent cleavage products from polyproteins (e.g., POMC peptides) - Describe modification states or conformational variants Only create entries when there ARE functionally distinct forms worth documenting.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    id: str = Field(default=..., description="""Curator-defined identifier for this functional class. Use a descriptive format like GENE_CLASS (e.g., WT1_PLUS_KTS, POMC_ACTH, BCL2L1_XL).""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['GeneReview',
                       'AlternativeProduct',
                       'FunctionalIsoform',
                       'Term',
                       'Reference',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'RuleReview',
                       'RuleReviewEntry',
                       'PredictionReview']} })
    name: str = Field(default=..., description="""Human-readable name for this functional class (e.g., \"+KTS isoforms\", \"ACTH/Corticotropin\", \"Bcl-xL\").""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['AlternativeProduct', 'FunctionalIsoform']} })
    type: FunctionalIsoformTypeEnum = Field(default=..., description="""Type of functional distinction (SPLICE_VARIANT, SPLICE_CLASS, CLEAVAGE_PRODUCT, MODIFICATION_STATE, CONFORMATIONAL_STATE).""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'domain_of': ['FunctionalIsoform',
                       'FunctionalIsoformMapping',
                       'RuleReviewEntry']} })
    maps_to: Optional[list[FunctionalIsoformMapping]] = Field(default=None, description="""Mappings to underlying UniProt identifiers. Optional - some functional classes may not map cleanly to specific UniProt IDs.""", json_schema_extra = { "linkml_meta": {'alias': 'maps_to', 'domain_of': ['FunctionalIsoform']} })
    description: str = Field(default=..., description="""Detailed description of this functional class. Document the specific functions, how they differ from other classes, tissue specificity, and any antagonistic relationships (e.g., \"OREXIGENIC - opposite to alpha-MSH\").""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['GeneReview',
                       'AlternativeProduct',
                       'FunctionalIsoform',
                       'Term',
                       'Descriptor',
                       'ModuleReview',
                       'ModuleNode',
                       'ParticipantSelector',
                       'ModuleConnection',
                       'CoreFunction',
                       'Experiment',
                       'RuleReview',
                       'PredictionReview']} })
    isoform_specific_terms: Optional[list[Term]] = Field(default=None, description="""GO terms that are specific to this functional class. These are terms that should NOT be annotated to the gene as a whole, only to this specific form. Using Term objects enables linkml-term-validator checking.""", json_schema_extra = { "linkml_meta": {'alias': 'isoform_specific_terms', 'domain_of': ['FunctionalIsoform']} })


class FunctionalIsoformMapping(ConfiguredBaseModel):
    """
    A mapping from a functional isoform class to underlying UniProt identifiers. Allows grouping multiple UniProt isoforms or chains into a single functional class.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    type: FunctionalIsoformMappingTypeEnum = Field(default=..., description="""Type of identifier (UNIPROT_ISOFORM or UNIPROT_CHAIN)""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'domain_of': ['FunctionalIsoform',
                       'FunctionalIsoformMapping',
                       'RuleReviewEntry']} })
    ids: list[str] = Field(default=..., description="""UniProt identifiers belonging to this functional class. For UNIPROT_ISOFORM: P19544-1, P19544-2, etc. For UNIPROT_CHAIN: PRO_0000024969, PRO_0000024970, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'ids', 'domain_of': ['FunctionalIsoformMapping']} })
    residues: Optional[str] = Field(default=None, description="""Residue range for cleavage products (e.g., \"138-176\" for ACTH). Only applicable for UNIPROT_CHAIN type.""", json_schema_extra = { "linkml_meta": {'alias': 'residues', 'domain_of': ['FunctionalIsoformMapping']} })


class Term(ConfiguredBaseModel):
    """
    A term in a specific ontology
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review',
         'slot_usage': {'id': {'description': 'A CURIE for a term or database object '
                                              'in GO, CL, CHEBI, UniProtKB, PANTHER, '
                                              'etc.',
                               'name': 'id'},
                        'label': {'description': 'the term name',
                                  'name': 'label',
                                  'required': True}}})

    id: str = Field(default=..., description="""A CURIE for a term or database object in GO, CL, CHEBI, UniProtKB, PANTHER, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['GeneReview',
                       'AlternativeProduct',
                       'FunctionalIsoform',
                       'Term',
                       'Reference',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'RuleReview',
                       'RuleReviewEntry',
                       'PredictionReview']} })
    label: str = Field(default=..., description="""the term name""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'domain_of': ['Term',
                       'ComplexUnit',
                       'ModuleNode',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'RuleCondition',
                       'RuleReviewEntry'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""Description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['GeneReview',
                       'AlternativeProduct',
                       'FunctionalIsoform',
                       'Term',
                       'Descriptor',
                       'ModuleReview',
                       'ModuleNode',
                       'ParticipantSelector',
                       'ModuleConnection',
                       'CoreFunction',
                       'Experiment',
                       'RuleReview',
                       'PredictionReview'],
         'slot_uri': 'dcterms:description'} })
    ontology: Optional[str] = Field(default=None, description="""Ontology of the term. E.g `go`, `cl`, `hp`""", json_schema_extra = { "linkml_meta": {'alias': 'ontology', 'domain_of': ['Term']} })


class Reference(ConfiguredBaseModel):
    """
    A reference is a published text  that describes a finding or a method. References might be formal publications (where the ID is a PMID), or for methods, a GO_REF. Additionally, a reference to a local ad-hoc analysis or review can be made by using the `file:` prefix.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review',
         'slot_usage': {'id': {'implements': ['dcterms:references'], 'name': 'id'}}})

    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['GeneReview',
                       'AlternativeProduct',
                       'FunctionalIsoform',
                       'Term',
                       'Reference',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'RuleReview',
                       'RuleReviewEntry',
                       'PredictionReview'],
         'implements': ['dcterms:references']} })
    title: str = Field(default=..., description="""Title of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'domain_of': ['Reference', 'EvidenceItem', 'ModuleReview'],
         'slot_uri': 'dcterms:title'} })
    findings: Optional[list[Finding]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'findings', 'domain_of': ['Reference'], 'recommended': True} })
    is_invalid: Optional[bool] = Field(default=None, description="""Whether the reference is invalid (e.g., retracted or replaced)""", json_schema_extra = { "linkml_meta": {'alias': 'is_invalid', 'domain_of': ['Reference']} })
    publication_type: Optional[PublicationTypeEnum] = Field(default=None, description="""The kind of publication or source this reference is (e.g. primary research article, review, meta-analysis, database record, AI deep-research report). For PMIDs this is normally inferred from the PubMed publication-type ('PT') metadata rather than set by hand; for non-PMID references (GO_REF, Reactome, file:) it is inferred from the identifier. Lets analyses ask, e.g., whether review articles or abstracts alone are sufficient to support a given annotation action.""", json_schema_extra = { "linkml_meta": {'alias': 'publication_type', 'domain_of': ['Reference']} })
    full_text_unavailable: Optional[bool] = Field(default=None, description="""Whether the full text is unavailable""", json_schema_extra = { "linkml_meta": {'alias': 'full_text_unavailable',
         'domain_of': ['Reference', 'Finding', 'SupportingTextInReference']} })
    reference_review: Optional[ReferenceReview] = Field(default=None, description="""Manual reviewer assessment of this reference (relevance, and citation correctness / scientific soundness). Reviewer-supplied, distinct from the machine-fetched id/title.""", json_schema_extra = { "linkml_meta": {'alias': 'reference_review', 'domain_of': ['Reference']} })


class ReferenceReview(ConfiguredBaseModel):
    """
    Manual reviewer assessment of a reference - how relevant it is to the gene's function, and whether it is correctly cited and scientifically sound. Distinct from the machine-fetched id/title fields; all fields are optional and reviewer-supplied.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    relevance: Optional[ReferenceRelevanceEnum] = Field(default=None, description="""Reviewer judgment of how relevant the reference is to the gene's function and this review.""", json_schema_extra = { "linkml_meta": {'alias': 'relevance', 'domain_of': ['ReferenceReview']} })
    correctness: Optional[ReferenceCorrectnessEnum] = Field(default=None, description="""Reviewer's overall assessment of a reference's trustworthiness - both citation correctness (the identifier resolves to the intended paper that supports its use) and scientific soundness of that paper's claim.""", json_schema_extra = { "linkml_meta": {'alias': 'correctness', 'domain_of': ['ReferenceReview']} })
    review_notes: Optional[str] = Field(default=None, description="""Free-text note explaining the relevance/correctness judgment (e.g. what was verified, or why a citation is wrong, disputed, or low quality).""", json_schema_extra = { "linkml_meta": {'alias': 'review_notes', 'domain_of': ['ReferenceReview', 'FindingReview']} })


class Finding(ConfiguredBaseModel):
    """
    A finding is a statement about a gene, which is supported by a reference. Similar to \"comments\" in uniprot
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    statement: Optional[str] = Field(default=None, description="""Concise statement describing an aspect of the gene""", json_schema_extra = { "linkml_meta": {'alias': 'statement',
         'domain_of': ['Finding', 'EvidenceItem'],
         'recommended': True} })
    supporting_text: Optional[str] = Field(default=None, description="""Supporting text from the publication. This should be exact substrings. Different substrings can be broken up by '...'s. These substrings will be checked against the actual text of the paper. If editorialization is necessary, put this in square brackets (this is not checked). For example, you can say '...[CFAP300 shows] transport within cilia is IFT dependent...'""", json_schema_extra = { "linkml_meta": {'alias': 'supporting_text',
         'domain_of': ['Finding', 'SupportingTextInReference', 'EvidenceItem'],
         'implements': ['oa:exact'],
         'recommended': True} })
    full_text_unavailable: Optional[bool] = Field(default=None, description="""Whether the full text is unavailable""", json_schema_extra = { "linkml_meta": {'alias': 'full_text_unavailable',
         'domain_of': ['Reference', 'Finding', 'SupportingTextInReference']} })
    reference_section_type: Optional[ManuscriptSection] = Field(default=None, description="""Type of section in the reference (e.g., 'ABSTRACT', 'METHODS', 'RESULTS', 'DISCUSSION')""", json_schema_extra = { "linkml_meta": {'alias': 'reference_section_type',
         'domain_of': ['Finding', 'SupportingTextInReference'],
         'recommended': True} })
    finding_review: Optional[FindingReview] = Field(default=None, description="""Manual reviewer assessment of this specific finding - in particular whether the finding remains current, is disputed, or has been overturned/superseded by later evidence. Reviewer-supplied; distinct from the statement/supporting_text that describe the finding itself.""", json_schema_extra = { "linkml_meta": {'alias': 'finding_review', 'domain_of': ['Finding']} })


class FindingReview(ConfiguredBaseModel):
    """
    Manual reviewer assessment of a specific finding within a reference - in particular whether it remains current, is disputed, or has been overturned/superseded by later evidence. This is finer-grained than reference_review (which assesses the whole reference); a paper may contain some findings that stand and others that are overturned. All fields optional and reviewer-supplied.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    finding_status: Optional[FindingReviewStatusEnum] = Field(default=None, description="""Reviewer's assessment of the empirical standing of a specific finding in light of other evidence (e.g. whether it has been disputed or overturned).""", json_schema_extra = { "linkml_meta": {'alias': 'finding_status', 'domain_of': ['FindingReview']} })
    superseded_by: Optional[list[str]] = Field(default=None, description="""Reference(s) that dispute, correct, or overturn this finding. Used together with finding_status DISPUTED or OVERTURNED.""", json_schema_extra = { "linkml_meta": {'alias': 'superseded_by', 'domain_of': ['FindingReview']} })
    review_notes: Optional[str] = Field(default=None, description="""Free-text note explaining the relevance/correctness judgment (e.g. what was verified, or why a citation is wrong, disputed, or low quality).""", json_schema_extra = { "linkml_meta": {'alias': 'review_notes', 'domain_of': ['ReferenceReview', 'FindingReview']} })


class SupportingTextInReference(ConfiguredBaseModel):
    """
    A supporting text in a reference.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    reference_id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'reference_id',
         'domain_of': ['SupportingTextInReference'],
         'implements': ['dcterms:references']} })
    supporting_text: Optional[str] = Field(default=None, description="""Supporting text from the publication. This should be exact substrings. Different substrings can be broken up by '...'s. These substrings will be checked against the actual text of the paper. If editorialization is necessary, put this in square brackets (this is not checked). For example, you can say '...[CFAP300 shows] transport within cilia is IFT dependent...'""", json_schema_extra = { "linkml_meta": {'alias': 'supporting_text',
         'domain_of': ['Finding', 'SupportingTextInReference', 'EvidenceItem'],
         'implements': ['oa:exact'],
         'recommended': True} })
    supporting_text_fulltext: Optional[str] = Field(default=None, description="""Supporting text from the full-text PDF when the full text cannot be committed to the repository. This is an interim solution for cases where we have access to full text but cannot share it publicly. Unlike supporting_text, this field is not validated against cached publication text.""", json_schema_extra = { "linkml_meta": {'alias': 'supporting_text_fulltext',
         'domain_of': ['SupportingTextInReference']} })
    full_text_unavailable: Optional[bool] = Field(default=None, description="""Whether the full text is unavailable""", json_schema_extra = { "linkml_meta": {'alias': 'full_text_unavailable',
         'domain_of': ['Reference', 'Finding', 'SupportingTextInReference']} })
    reference_section_type: Optional[ManuscriptSection] = Field(default=None, description="""Type of section in the reference (e.g., 'ABSTRACT', 'METHODS', 'RESULTS', 'DISCUSSION')""", json_schema_extra = { "linkml_meta": {'alias': 'reference_section_type',
         'domain_of': ['Finding', 'SupportingTextInReference'],
         'recommended': True} })


class EvidenceItem(ConfiguredBaseModel):
    """
    A lightweight citable source for module-level assertions. The source may be a PMID, DOI, database record, local file, pathway record, issue, or any other citable artifact. This is deliberately less strict than the publication quote validation used in gene reviews.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    source_id: str = Field(default=..., description="""Identifier for the evidence source, e.g. PMID:123456, DOI:..., Reactome:R-HSA-..., MetaCyc:..., file:...""", json_schema_extra = { "linkml_meta": {'alias': 'source_id', 'domain_of': ['EvidenceItem']} })
    title: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['Reference', 'EvidenceItem', 'ModuleReview']} })
    statement: Optional[str] = Field(default=None, description="""The assertion this evidence supports in this module.""", json_schema_extra = { "linkml_meta": {'alias': 'statement', 'domain_of': ['Finding', 'EvidenceItem']} })
    supporting_text: Optional[str] = Field(default=None, description="""Optional quote or excerpt from the evidence source.""", json_schema_extra = { "linkml_meta": {'alias': 'supporting_text',
         'domain_of': ['Finding', 'SupportingTextInReference', 'EvidenceItem']} })
    url: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['EvidenceItem']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['EvidenceItem',
                       'Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection',
                       'RuleConditionSet',
                       'ParsimonyAssessment',
                       'LiteratureSupportAssessment',
                       'ConditionOverlapAssessment',
                       'GOSpecificityAssessment',
                       'TaxonomicScopeAssessment']} })


class Descriptor(ConfiguredBaseModel):
    """
    A human-friendly descriptor with optional ontology/database grounding. The preferred_term may be more nuanced than the term label, and the term may be absent when no good identifier exists yet.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    preferred_term: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'preferred_term', 'domain_of': ['Descriptor']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['GeneReview',
                       'AlternativeProduct',
                       'FunctionalIsoform',
                       'Term',
                       'Descriptor',
                       'ModuleReview',
                       'ModuleNode',
                       'ParticipantSelector',
                       'ModuleConnection',
                       'CoreFunction',
                       'Experiment',
                       'RuleReview',
                       'PredictionReview']} })
    term: Optional[Term] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'term',
         'domain_of': ['Descriptor', 'ExistingAnnotation', 'AnnotationExtension']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['EvidenceItem',
                       'Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection',
                       'RuleConditionSet',
                       'ParsimonyAssessment',
                       'LiteratureSupportAssessment',
                       'ConditionOverlapAssessment',
                       'GOSpecificityAssessment',
                       'TaxonomicScopeAssessment']} })


class ChemicalEntityDescriptor(Descriptor):
    """
    A descriptor for a chemical entity, metabolite, cofactor, ion, or small molecule.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    preferred_term: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'preferred_term', 'domain_of': ['Descriptor']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['GeneReview',
                       'AlternativeProduct',
                       'FunctionalIsoform',
                       'Term',
                       'Descriptor',
                       'ModuleReview',
                       'ModuleNode',
                       'ParticipantSelector',
                       'ModuleConnection',
                       'CoreFunction',
                       'Experiment',
                       'RuleReview',
                       'PredictionReview']} })
    term: Optional[Term] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'term',
         'domain_of': ['Descriptor', 'ExistingAnnotation', 'AnnotationExtension']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['EvidenceItem',
                       'Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection',
                       'RuleConditionSet',
                       'ParsimonyAssessment',
                       'LiteratureSupportAssessment',
                       'ConditionOverlapAssessment',
                       'GOSpecificityAssessment',
                       'TaxonomicScopeAssessment']} })


class GeneDescriptor(Descriptor):
    """
    A descriptor for a gene or locus.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    preferred_term: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'preferred_term', 'domain_of': ['Descriptor']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['GeneReview',
                       'AlternativeProduct',
                       'FunctionalIsoform',
                       'Term',
                       'Descriptor',
                       'ModuleReview',
                       'ModuleNode',
                       'ParticipantSelector',
                       'ModuleConnection',
                       'CoreFunction',
                       'Experiment',
                       'RuleReview',
                       'PredictionReview']} })
    term: Optional[Term] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'term',
         'domain_of': ['Descriptor', 'ExistingAnnotation', 'AnnotationExtension']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['EvidenceItem',
                       'Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection',
                       'RuleConditionSet',
                       'ParsimonyAssessment',
                       'LiteratureSupportAssessment',
                       'ConditionOverlapAssessment',
                       'GOSpecificityAssessment',
                       'TaxonomicScopeAssessment']} })


class GeneProductDescriptor(Descriptor):
    """
    A descriptor for a gene product, protein, isoform, or gene-product form.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    preferred_term: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'preferred_term', 'domain_of': ['Descriptor']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['GeneReview',
                       'AlternativeProduct',
                       'FunctionalIsoform',
                       'Term',
                       'Descriptor',
                       'ModuleReview',
                       'ModuleNode',
                       'ParticipantSelector',
                       'ModuleConnection',
                       'CoreFunction',
                       'Experiment',
                       'RuleReview',
                       'PredictionReview']} })
    term: Optional[Term] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'term',
         'domain_of': ['Descriptor', 'ExistingAnnotation', 'AnnotationExtension']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['EvidenceItem',
                       'Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection',
                       'RuleConditionSet',
                       'ParsimonyAssessment',
                       'LiteratureSupportAssessment',
                       'ConditionOverlapAssessment',
                       'GOSpecificityAssessment',
                       'TaxonomicScopeAssessment']} })


class FamilyDescriptor(Descriptor):
    """
    A descriptor for a protein family, orthogroup, or other evolutionary grouping.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    representative_members: Optional[list[GeneProductDescriptor]] = Field(default=None, description="""Representative concrete members used to orient the family. These are examples, not an exhaustive member list and not a claim that the module is limited to these proteins.""", json_schema_extra = { "linkml_meta": {'alias': 'representative_members', 'domain_of': ['FamilyDescriptor']} })
    preferred_term: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'preferred_term', 'domain_of': ['Descriptor']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['GeneReview',
                       'AlternativeProduct',
                       'FunctionalIsoform',
                       'Term',
                       'Descriptor',
                       'ModuleReview',
                       'ModuleNode',
                       'ParticipantSelector',
                       'ModuleConnection',
                       'CoreFunction',
                       'Experiment',
                       'RuleReview',
                       'PredictionReview']} })
    term: Optional[Term] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'term',
         'domain_of': ['Descriptor', 'ExistingAnnotation', 'AnnotationExtension']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['EvidenceItem',
                       'Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection',
                       'RuleConditionSet',
                       'ParsimonyAssessment',
                       'LiteratureSupportAssessment',
                       'ConditionOverlapAssessment',
                       'GOSpecificityAssessment',
                       'TaxonomicScopeAssessment']} })


class DomainDescriptor(Descriptor):
    """
    A descriptor for a protein domain, motif, site, or architectural feature.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    preferred_term: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'preferred_term', 'domain_of': ['Descriptor']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['GeneReview',
                       'AlternativeProduct',
                       'FunctionalIsoform',
                       'Term',
                       'Descriptor',
                       'ModuleReview',
                       'ModuleNode',
                       'ParticipantSelector',
                       'ModuleConnection',
                       'CoreFunction',
                       'Experiment',
                       'RuleReview',
                       'PredictionReview']} })
    term: Optional[Term] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'term',
         'domain_of': ['Descriptor', 'ExistingAnnotation', 'AnnotationExtension']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['EvidenceItem',
                       'Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection',
                       'RuleConditionSet',
                       'ParsimonyAssessment',
                       'LiteratureSupportAssessment',
                       'ConditionOverlapAssessment',
                       'GOSpecificityAssessment',
                       'TaxonomicScopeAssessment']} })


class CellularComponentDescriptor(Descriptor):
    """
    A descriptor for a cellular component, organelle, compartment, or complex location.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    preferred_term: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'preferred_term', 'domain_of': ['Descriptor']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['GeneReview',
                       'AlternativeProduct',
                       'FunctionalIsoform',
                       'Term',
                       'Descriptor',
                       'ModuleReview',
                       'ModuleNode',
                       'ParticipantSelector',
                       'ModuleConnection',
                       'CoreFunction',
                       'Experiment',
                       'RuleReview',
                       'PredictionReview']} })
    term: Optional[Term] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'term',
         'domain_of': ['Descriptor', 'ExistingAnnotation', 'AnnotationExtension']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['EvidenceItem',
                       'Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection',
                       'RuleConditionSet',
                       'ParsimonyAssessment',
                       'LiteratureSupportAssessment',
                       'ConditionOverlapAssessment',
                       'GOSpecificityAssessment',
                       'TaxonomicScopeAssessment']} })


class ProteinComplexDescriptor(CellularComponentDescriptor):
    """
    A descriptor for a protein-containing complex or subcomplex.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    active_units: Optional[list[ComplexUnit]] = Field(default=None, description="""Active units or role-bearing components of the complex. This is used to avoid leaving functionally important complex structure as prose.""", json_schema_extra = { "linkml_meta": {'alias': 'active_units', 'domain_of': ['ProteinComplexDescriptor']} })
    preferred_term: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'preferred_term', 'domain_of': ['Descriptor']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['GeneReview',
                       'AlternativeProduct',
                       'FunctionalIsoform',
                       'Term',
                       'Descriptor',
                       'ModuleReview',
                       'ModuleNode',
                       'ParticipantSelector',
                       'ModuleConnection',
                       'CoreFunction',
                       'Experiment',
                       'RuleReview',
                       'PredictionReview']} })
    term: Optional[Term] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'term',
         'domain_of': ['Descriptor', 'ExistingAnnotation', 'AnnotationExtension']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['EvidenceItem',
                       'Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection',
                       'RuleConditionSet',
                       'ParsimonyAssessment',
                       'LiteratureSupportAssessment',
                       'ConditionOverlapAssessment',
                       'GOSpecificityAssessment',
                       'TaxonomicScopeAssessment']} })


class ComplexUnit(ConfiguredBaseModel):
    """
    A role-bearing unit within a protein complex descriptor.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['GeneReview',
                       'AlternativeProduct',
                       'FunctionalIsoform',
                       'Term',
                       'Reference',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'RuleReview',
                       'RuleReviewEntry',
                       'PredictionReview']} })
    label: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'label',
         'domain_of': ['Term',
                       'ComplexUnit',
                       'ModuleNode',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'RuleCondition',
                       'RuleReviewEntry']} })
    participant: Optional[ParticipantSelector] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'participant', 'domain_of': ['ComplexUnit', 'ModuleAnnoton']} })
    role: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'role', 'domain_of': ['ComplexUnit', 'ModulePart']} })
    stoichiometry: Optional[str] = Field(default=None, description="""Optional stoichiometry or copy-number statement when known.""", json_schema_extra = { "linkml_meta": {'alias': 'stoichiometry', 'domain_of': ['ComplexUnit']} })
    function: Optional[MolecularFunctionDescriptor] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'function', 'domain_of': ['ComplexUnit', 'ModuleAnnoton']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['EvidenceItem',
                       'Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection',
                       'RuleConditionSet',
                       'ParsimonyAssessment',
                       'LiteratureSupportAssessment',
                       'ConditionOverlapAssessment',
                       'GOSpecificityAssessment',
                       'TaxonomicScopeAssessment']} })


class CellTypeDescriptor(Descriptor):
    """
    A descriptor for a cell type or cell state.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    preferred_term: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'preferred_term', 'domain_of': ['Descriptor']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['GeneReview',
                       'AlternativeProduct',
                       'FunctionalIsoform',
                       'Term',
                       'Descriptor',
                       'ModuleReview',
                       'ModuleNode',
                       'ParticipantSelector',
                       'ModuleConnection',
                       'CoreFunction',
                       'Experiment',
                       'RuleReview',
                       'PredictionReview']} })
    term: Optional[Term] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'term',
         'domain_of': ['Descriptor', 'ExistingAnnotation', 'AnnotationExtension']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['EvidenceItem',
                       'Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection',
                       'RuleConditionSet',
                       'ParsimonyAssessment',
                       'LiteratureSupportAssessment',
                       'ConditionOverlapAssessment',
                       'GOSpecificityAssessment',
                       'TaxonomicScopeAssessment']} })


class AnatomicalEntityDescriptor(Descriptor):
    """
    A descriptor for an anatomical entity, tissue, organismal region, or structure.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    preferred_term: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'preferred_term', 'domain_of': ['Descriptor']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['GeneReview',
                       'AlternativeProduct',
                       'FunctionalIsoform',
                       'Term',
                       'Descriptor',
                       'ModuleReview',
                       'ModuleNode',
                       'ParticipantSelector',
                       'ModuleConnection',
                       'CoreFunction',
                       'Experiment',
                       'RuleReview',
                       'PredictionReview']} })
    term: Optional[Term] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'term',
         'domain_of': ['Descriptor', 'ExistingAnnotation', 'AnnotationExtension']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['EvidenceItem',
                       'Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection',
                       'RuleConditionSet',
                       'ParsimonyAssessment',
                       'LiteratureSupportAssessment',
                       'ConditionOverlapAssessment',
                       'GOSpecificityAssessment',
                       'TaxonomicScopeAssessment']} })


class DevelopmentalStageDescriptor(Descriptor):
    """
    A descriptor for a developmental stage, life-cycle stage, or temporal window.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    preferred_term: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'preferred_term', 'domain_of': ['Descriptor']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['GeneReview',
                       'AlternativeProduct',
                       'FunctionalIsoform',
                       'Term',
                       'Descriptor',
                       'ModuleReview',
                       'ModuleNode',
                       'ParticipantSelector',
                       'ModuleConnection',
                       'CoreFunction',
                       'Experiment',
                       'RuleReview',
                       'PredictionReview']} })
    term: Optional[Term] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'term',
         'domain_of': ['Descriptor', 'ExistingAnnotation', 'AnnotationExtension']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['EvidenceItem',
                       'Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection',
                       'RuleConditionSet',
                       'ParsimonyAssessment',
                       'LiteratureSupportAssessment',
                       'ConditionOverlapAssessment',
                       'GOSpecificityAssessment',
                       'TaxonomicScopeAssessment']} })


class TaxonDescriptor(Descriptor):
    """
    A descriptor for a taxon or taxonomic scope.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    preferred_term: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'preferred_term', 'domain_of': ['Descriptor']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['GeneReview',
                       'AlternativeProduct',
                       'FunctionalIsoform',
                       'Term',
                       'Descriptor',
                       'ModuleReview',
                       'ModuleNode',
                       'ParticipantSelector',
                       'ModuleConnection',
                       'CoreFunction',
                       'Experiment',
                       'RuleReview',
                       'PredictionReview']} })
    term: Optional[Term] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'term',
         'domain_of': ['Descriptor', 'ExistingAnnotation', 'AnnotationExtension']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['EvidenceItem',
                       'Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection',
                       'RuleConditionSet',
                       'ParsimonyAssessment',
                       'LiteratureSupportAssessment',
                       'ConditionOverlapAssessment',
                       'GOSpecificityAssessment',
                       'TaxonomicScopeAssessment']} })


class MolecularFunctionDescriptor(Descriptor):
    """
    A descriptor for a molecular function. Extra slots capture common functional nuance without requiring formal post-composition.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    substrates: Optional[list[Descriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'substrates',
         'domain_of': ['MolecularFunctionDescriptor', 'CoreFunction']} })
    products: Optional[list[Descriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'products', 'domain_of': ['MolecularFunctionDescriptor']} })
    cofactors: Optional[list[Descriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'cofactors', 'domain_of': ['MolecularFunctionDescriptor']} })
    targets: Optional[list[Descriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'targets', 'domain_of': ['MolecularFunctionDescriptor']} })
    cargo: Optional[list[Descriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'cargo', 'domain_of': ['MolecularFunctionDescriptor']} })
    source_location: Optional[CellularComponentDescriptor] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'source_location', 'domain_of': ['MolecularFunctionDescriptor']} })
    destination_location: Optional[CellularComponentDescriptor] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'destination_location', 'domain_of': ['MolecularFunctionDescriptor']} })
    preferred_term: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'preferred_term', 'domain_of': ['Descriptor']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['GeneReview',
                       'AlternativeProduct',
                       'FunctionalIsoform',
                       'Term',
                       'Descriptor',
                       'ModuleReview',
                       'ModuleNode',
                       'ParticipantSelector',
                       'ModuleConnection',
                       'CoreFunction',
                       'Experiment',
                       'RuleReview',
                       'PredictionReview']} })
    term: Optional[Term] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'term',
         'domain_of': ['Descriptor', 'ExistingAnnotation', 'AnnotationExtension']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['EvidenceItem',
                       'Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection',
                       'RuleConditionSet',
                       'ParsimonyAssessment',
                       'LiteratureSupportAssessment',
                       'ConditionOverlapAssessment',
                       'GOSpecificityAssessment',
                       'TaxonomicScopeAssessment']} })


class BiologicalProcessDescriptor(Descriptor):
    """
    A descriptor for a biological process, pathway, reaction, or process-like module grounding.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    inputs: Optional[list[Descriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'inputs', 'domain_of': ['BiologicalProcessDescriptor']} })
    outputs: Optional[list[Descriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'outputs', 'domain_of': ['BiologicalProcessDescriptor']} })
    occurs_in: Optional[list[Descriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'occurs_in', 'domain_of': ['BiologicalProcessDescriptor']} })
    starts_with: Optional[Descriptor] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'starts_with', 'domain_of': ['BiologicalProcessDescriptor']} })
    ends_with: Optional[Descriptor] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'ends_with', 'domain_of': ['BiologicalProcessDescriptor']} })
    preferred_term: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'preferred_term', 'domain_of': ['Descriptor']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['GeneReview',
                       'AlternativeProduct',
                       'FunctionalIsoform',
                       'Term',
                       'Descriptor',
                       'ModuleReview',
                       'ModuleNode',
                       'ParticipantSelector',
                       'ModuleConnection',
                       'CoreFunction',
                       'Experiment',
                       'RuleReview',
                       'PredictionReview']} })
    term: Optional[Term] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'term',
         'domain_of': ['Descriptor', 'ExistingAnnotation', 'AnnotationExtension']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['EvidenceItem',
                       'Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection',
                       'RuleConditionSet',
                       'ParsimonyAssessment',
                       'LiteratureSupportAssessment',
                       'ConditionOverlapAssessment',
                       'GOSpecificityAssessment',
                       'TaxonomicScopeAssessment']} })


class RelationDescriptor(Descriptor):
    """
    A descriptor for a relation or connection predicate.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    preferred_term: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'preferred_term', 'domain_of': ['Descriptor']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['GeneReview',
                       'AlternativeProduct',
                       'FunctionalIsoform',
                       'Term',
                       'Descriptor',
                       'ModuleReview',
                       'ModuleNode',
                       'ParticipantSelector',
                       'ModuleConnection',
                       'CoreFunction',
                       'Experiment',
                       'RuleReview',
                       'PredictionReview']} })
    term: Optional[Term] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'term',
         'domain_of': ['Descriptor', 'ExistingAnnotation', 'AnnotationExtension']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['EvidenceItem',
                       'Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection',
                       'RuleConditionSet',
                       'ParsimonyAssessment',
                       'LiteratureSupportAssessment',
                       'ConditionOverlapAssessment',
                       'GOSpecificityAssessment',
                       'TaxonomicScopeAssessment']} })


class ModuleReview(ConfiguredBaseModel):
    """
    Review or curation record for a recursively decomposable biological module. This can describe a pathway, organelle lifecycle, protein complex, molecular function, developmental process, or abstract/evolutionary functional plan.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review', 'tree_root': True})

    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['GeneReview',
                       'AlternativeProduct',
                       'FunctionalIsoform',
                       'Term',
                       'Reference',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'RuleReview',
                       'RuleReviewEntry',
                       'PredictionReview']} })
    title: str = Field(default=..., description="""Title of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'domain_of': ['Reference', 'EvidenceItem', 'ModuleReview'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""Description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['GeneReview',
                       'AlternativeProduct',
                       'FunctionalIsoform',
                       'Term',
                       'Descriptor',
                       'ModuleReview',
                       'ModuleNode',
                       'ParticipantSelector',
                       'ModuleConnection',
                       'CoreFunction',
                       'Experiment',
                       'RuleReview',
                       'PredictionReview'],
         'slot_uri': 'dcterms:description'} })
    references: Optional[list[Reference]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'references',
         'domain_of': ['GeneReview', 'ModuleReview', 'RuleReview', 'PredictionReview']} })
    knowledge_gaps: Optional[list[KnowledgeGap]] = Field(default=None, description="""Curated, literature-grounded statements of what is NOT known — applicable at the level of the whole gene, a single existing annotation, a core function, a whole module, or a single module step/node. The inverse of core_functions: everywhere else the schema records what IS known; here it records, with the same evidentiary discipline, what is not. See the Function Knowledge Gaps project (projects/FUNCTION_KNOWLEDGE_GAPS.md).""", json_schema_extra = { "linkml_meta": {'alias': 'knowledge_gaps',
         'domain_of': ['GeneReview',
                       'ModuleReview',
                       'ModuleNode',
                       'Review',
                       'CoreFunction']} })
    status: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'status',
         'domain_of': ['GeneReview',
                       'ModuleReview',
                       'KnowledgeGap',
                       'RuleReview',
                       'PredictionReview']} })
    module: ModuleNode = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'module', 'domain_of': ['ModuleReview']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['EvidenceItem',
                       'Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection',
                       'RuleConditionSet',
                       'ParsimonyAssessment',
                       'LiteratureSupportAssessment',
                       'ConditionOverlapAssessment',
                       'GOSpecificityAssessment',
                       'TaxonomicScopeAssessment']} })


class ModuleNode(ConfiguredBaseModel):
    """
    A node in a module. Nodes can be recursively decomposed using parts and variant_sets, and may also carry leaf annotons and connections.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    knowledge_gaps: Optional[list[KnowledgeGap]] = Field(default=None, description="""Curated, literature-grounded statements of what is NOT known — applicable at the level of the whole gene, a single existing annotation, a core function, a whole module, or a single module step/node. The inverse of core_functions: everywhere else the schema records what IS known; here it records, with the same evidentiary discipline, what is not. See the Function Knowledge Gaps project (projects/FUNCTION_KNOWLEDGE_GAPS.md).""", json_schema_extra = { "linkml_meta": {'alias': 'knowledge_gaps',
         'domain_of': ['GeneReview',
                       'ModuleReview',
                       'ModuleNode',
                       'Review',
                       'CoreFunction']} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['GeneReview',
                       'AlternativeProduct',
                       'FunctionalIsoform',
                       'Term',
                       'Reference',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'RuleReview',
                       'RuleReviewEntry',
                       'PredictionReview']} })
    label: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'label',
         'domain_of': ['Term',
                       'ComplexUnit',
                       'ModuleNode',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'RuleCondition',
                       'RuleReviewEntry']} })
    module_type: Optional[ModuleTypeEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'module_type', 'domain_of': ['ModuleNode']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['GeneReview',
                       'AlternativeProduct',
                       'FunctionalIsoform',
                       'Term',
                       'Descriptor',
                       'ModuleReview',
                       'ModuleNode',
                       'ParticipantSelector',
                       'ModuleConnection',
                       'CoreFunction',
                       'Experiment',
                       'RuleReview',
                       'PredictionReview']} })
    concepts: Optional[list[Descriptor]] = Field(default=None, description="""Optional ontology/database grounding for this module node.""", json_schema_extra = { "linkml_meta": {'alias': 'concepts', 'domain_of': ['ModuleNode']} })
    context: Optional[ModuleContext] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'context', 'domain_of': ['ModuleNode', 'ModuleConnection']} })
    annotons: Optional[list[ModuleAnnoton]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'annotons', 'domain_of': ['ModuleNode']} })
    parts: Optional[list[ModulePart]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'parts', 'domain_of': ['ModuleNode']} })
    variant_sets: Optional[list[ModuleVariantSet]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'variant_sets', 'domain_of': ['ModuleNode']} })
    connections: Optional[list[ModuleConnection]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'connections', 'domain_of': ['ModuleNode']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['EvidenceItem',
                       'Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection',
                       'RuleConditionSet',
                       'ParsimonyAssessment',
                       'LiteratureSupportAssessment',
                       'ConditionOverlapAssessment',
                       'GOSpecificityAssessment',
                       'TaxonomicScopeAssessment']} })


class ModulePart(ConfiguredBaseModel):
    """
    A conjunctive part or step of a module node.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    order: Optional[int] = Field(default=None, description="""Optional display or temporal order. Equal or absent values imply partial ordering only.""", json_schema_extra = { "linkml_meta": {'alias': 'order', 'domain_of': ['ModulePart']} })
    role: Optional[str] = Field(default=None, description="""Curator-supplied role of this part within the parent module.""", json_schema_extra = { "linkml_meta": {'alias': 'role', 'domain_of': ['ComplexUnit', 'ModulePart']} })
    optional: Optional[bool] = Field(default=None, description="""Whether this part is optional in the parent module.""", json_schema_extra = { "linkml_meta": {'alias': 'optional', 'domain_of': ['ModulePart']} })
    node: ModuleNode = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'node', 'domain_of': ['ModulePart']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['EvidenceItem',
                       'Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection',
                       'RuleConditionSet',
                       'ParsimonyAssessment',
                       'LiteratureSupportAssessment',
                       'ConditionOverlapAssessment',
                       'GOSpecificityAssessment',
                       'TaxonomicScopeAssessment']} })


class ModuleVariantSet(ConfiguredBaseModel):
    """
    A set of alternative implementations for a module node or part. Variants may themselves contain parts, annotons, connections, and nested variant sets.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['GeneReview',
                       'AlternativeProduct',
                       'FunctionalIsoform',
                       'Term',
                       'Reference',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'RuleReview',
                       'RuleReviewEntry',
                       'PredictionReview']} })
    label: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'label',
         'domain_of': ['Term',
                       'ComplexUnit',
                       'ModuleNode',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'RuleCondition',
                       'RuleReviewEntry']} })
    axis: Optional[str] = Field(default=None, description="""The dimension along which these variants differ, e.g. taxon, cell type, compartment, route, enzyme family.""", json_schema_extra = { "linkml_meta": {'alias': 'axis', 'domain_of': ['ModuleVariantSet']} })
    selection: Optional[VariantSelectionEnum] = Field(default=None, description="""How many variants may be selected in a concrete realization.""", json_schema_extra = { "linkml_meta": {'alias': 'selection', 'domain_of': ['ModuleVariantSet']} })
    variants: list[ModuleNode] = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'variants', 'domain_of': ['ModuleVariantSet']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['EvidenceItem',
                       'Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection',
                       'RuleConditionSet',
                       'ParsimonyAssessment',
                       'LiteratureSupportAssessment',
                       'ConditionOverlapAssessment',
                       'GOSpecificityAssessment',
                       'TaxonomicScopeAssessment']} })


class ModuleAnnoton(ConfiguredBaseModel):
    """
    A leaf role assertion in a module. The participant may be a concrete gene or an abstract selector, and the function/process/location fields are descriptor holders rather than direct GO annotation exports.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['GeneReview',
                       'AlternativeProduct',
                       'FunctionalIsoform',
                       'Term',
                       'Reference',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'RuleReview',
                       'RuleReviewEntry',
                       'PredictionReview']} })
    label: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'label',
         'domain_of': ['Term',
                       'ComplexUnit',
                       'ModuleNode',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'RuleCondition',
                       'RuleReviewEntry']} })
    participant: Optional[ParticipantSelector] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'participant', 'domain_of': ['ComplexUnit', 'ModuleAnnoton']} })
    function: Optional[MolecularFunctionDescriptor] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'function', 'domain_of': ['ComplexUnit', 'ModuleAnnoton']} })
    processes: Optional[list[BiologicalProcessDescriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'processes', 'domain_of': ['ModuleAnnoton']} })
    locations: Optional[list[CellularComponentDescriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'locations', 'domain_of': ['ModuleAnnoton', 'CoreFunction']} })
    role_description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'role_description', 'domain_of': ['ModuleAnnoton']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['EvidenceItem',
                       'Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection',
                       'RuleConditionSet',
                       'ParsimonyAssessment',
                       'LiteratureSupportAssessment',
                       'ConditionOverlapAssessment',
                       'GOSpecificityAssessment',
                       'TaxonomicScopeAssessment']} })


class ParticipantSelector(ConfiguredBaseModel):
    """
    A selector for a concrete or abstract participant in a module annoton. This can ground to a gene, gene product, complex, family, domain, ortholog, homolog, or any entity satisfying a functional/domain constraint.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    selector_type: ParticipantSelectorTypeEnum = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'selector_type', 'domain_of': ['ParticipantSelector']} })
    gene: Optional[GeneDescriptor] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'gene', 'domain_of': ['ParticipantSelector']} })
    gene_product: Optional[GeneProductDescriptor] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'gene_product', 'domain_of': ['ParticipantSelector']} })
    protein_complex: Optional[ProteinComplexDescriptor] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'protein_complex', 'domain_of': ['ParticipantSelector']} })
    family: Optional[FamilyDescriptor] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'family', 'domain_of': ['ParticipantSelector']} })
    domain: Optional[DomainDescriptor] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'domain', 'domain_of': ['ParticipantSelector']} })
    homolog_of: Optional[GeneDescriptor] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'homolog_of', 'domain_of': ['ParticipantSelector']} })
    ortholog_of: Optional[GeneDescriptor] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'ortholog_of', 'domain_of': ['ParticipantSelector']} })
    required_function: Optional[MolecularFunctionDescriptor] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'required_function', 'domain_of': ['ParticipantSelector']} })
    required_domain: Optional[DomainDescriptor] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'required_domain', 'domain_of': ['ParticipantSelector']} })
    taxon: Optional[TaxonDescriptor] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'taxon',
         'domain_of': ['GeneReview', 'ParticipantSelector', 'PredictionReview']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['GeneReview',
                       'AlternativeProduct',
                       'FunctionalIsoform',
                       'Term',
                       'Descriptor',
                       'ModuleReview',
                       'ModuleNode',
                       'ParticipantSelector',
                       'ModuleConnection',
                       'CoreFunction',
                       'Experiment',
                       'RuleReview',
                       'PredictionReview']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['EvidenceItem',
                       'Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection',
                       'RuleConditionSet',
                       'ParsimonyAssessment',
                       'LiteratureSupportAssessment',
                       'ConditionOverlapAssessment',
                       'GOSpecificityAssessment',
                       'TaxonomicScopeAssessment']} })


class ModuleContext(ConfiguredBaseModel):
    """
    Context that applies to a module node, variant, annoton, or connection.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    taxa: Optional[list[TaxonDescriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'taxa', 'domain_of': ['ModuleContext']} })
    cell_types: Optional[list[CellTypeDescriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'cell_types', 'domain_of': ['ModuleContext']} })
    anatomical_locations: Optional[list[AnatomicalEntityDescriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'anatomical_locations',
         'domain_of': ['ModuleContext', 'CoreFunction']} })
    developmental_stages: Optional[list[DevelopmentalStageDescriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'developmental_stages', 'domain_of': ['ModuleContext']} })
    cellular_components: Optional[list[CellularComponentDescriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'cellular_components', 'domain_of': ['ModuleContext']} })
    conditions: Optional[list[Descriptor]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'conditions', 'domain_of': ['ModuleContext', 'RuleConditionSet']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['EvidenceItem',
                       'Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection',
                       'RuleConditionSet',
                       'ParsimonyAssessment',
                       'LiteratureSupportAssessment',
                       'ConditionOverlapAssessment',
                       'GOSpecificityAssessment',
                       'TaxonomicScopeAssessment']} })


class ModuleConnection(ConfiguredBaseModel):
    """
    A connection between module nodes, annotons, or other named elements. Source and target are IDs scoped to the module document.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    source: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'source', 'domain_of': ['ModuleConnection', 'RuleReviewEntry']} })
    target: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'target', 'domain_of': ['ModuleConnection']} })
    connection_type: Optional[ModuleConnectionTypeEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'connection_type', 'domain_of': ['ModuleConnection']} })
    predicate: Optional[RelationDescriptor] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'predicate',
         'domain_of': ['ModuleConnection', 'AnnotationExtension', 'TermMapping']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['GeneReview',
                       'AlternativeProduct',
                       'FunctionalIsoform',
                       'Term',
                       'Descriptor',
                       'ModuleReview',
                       'ModuleNode',
                       'ParticipantSelector',
                       'ModuleConnection',
                       'CoreFunction',
                       'Experiment',
                       'RuleReview',
                       'PredictionReview']} })
    context: Optional[ModuleContext] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'context', 'domain_of': ['ModuleNode', 'ModuleConnection']} })
    evidence: Optional[list[EvidenceItem]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'evidence',
         'domain_of': ['Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['EvidenceItem',
                       'Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection',
                       'RuleConditionSet',
                       'ParsimonyAssessment',
                       'LiteratureSupportAssessment',
                       'ConditionOverlapAssessment',
                       'GOSpecificityAssessment',
                       'TaxonomicScopeAssessment']} })


class ExistingAnnotation(ConfiguredBaseModel):
    """
    An existing annotation from the GO database, plus a review of the annotation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    term: Optional[Term] = Field(default=None, description="""Term to be annotated""", json_schema_extra = { "linkml_meta": {'alias': 'term',
         'domain_of': ['Descriptor', 'ExistingAnnotation', 'AnnotationExtension']} })
    qualifier: Optional[AnnotationQualifierEnum] = Field(default=None, description="""The GO annotation qualifier specifying the relationship between the gene product and the term. For MF annotations, distinguishes 'enables' (gene product has the activity independently) from 'contributes_to' (gene product contributes to a complex's activity but does not have the activity alone). For BP, distinguishes 'involved_in', 'acts_upstream_of', etc. For CC, distinguishes 'located_in', 'part_of', 'is_active_in', 'colocalizes_with'.""", json_schema_extra = { "linkml_meta": {'alias': 'qualifier', 'domain_of': ['ExistingAnnotation']} })
    extensions: Optional[list[AnnotationExtension]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'extensions', 'domain_of': ['ExistingAnnotation']} })
    negated: Optional[bool] = Field(default=None, description="""Whether the term is negated""", json_schema_extra = { "linkml_meta": {'alias': 'negated', 'domain_of': ['ExistingAnnotation', 'RuleCondition']} })
    evidence_type: EvidenceType = Field(default=..., description="""Evidence code (e.g., IDA, IBA, ISS, TAS)""", json_schema_extra = { "linkml_meta": {'alias': 'evidence_type', 'domain_of': ['ExistingAnnotation']} })
    original_reference_id: Optional[str] = Field(default=None, description="""ID of the original reference""", json_schema_extra = { "linkml_meta": {'alias': 'original_reference_id', 'domain_of': ['ExistingAnnotation']} })
    retired: Optional[bool] = Field(default=None, description="""Whether the annotation is retired or replaced""", json_schema_extra = { "linkml_meta": {'alias': 'retired', 'domain_of': ['ExistingAnnotation']} })
    isoform: Optional[str] = Field(default=None, description="""UniProt isoform identifier (e.g., \"P19544-1\" for WT1 isoform 1). Only populated when the annotation is specific to a particular isoform rather than the canonical protein sequence. Note that just because an experiment used a particular isoform doesn't mean the annotation is isoform-specific - it may apply to all isoforms. Use this field only when there is clear evidence the annotation is isoform-specific.""", json_schema_extra = { "linkml_meta": {'alias': 'isoform', 'domain_of': ['ExistingAnnotation']} })
    supporting_entities: Optional[list[str]] = Field(default=None, description="""IDs of the supporting entities""", json_schema_extra = { "linkml_meta": {'alias': 'supporting_entities', 'domain_of': ['ExistingAnnotation']} })
    review: Optional[Review] = Field(default=None, description="""Review of the gene""", json_schema_extra = { "linkml_meta": {'alias': 'review',
         'domain_of': ['ExistingAnnotation', 'PredictedAnnotation'],
         'recommended': True} })


class Review(ConfiguredBaseModel):
    """
    A review of an existing annotation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review',
         'rules': [{'postconditions': {'slot_conditions': {'proposed_replacement_terms': {'name': 'proposed_replacement_terms',
                                                                                          'required': True}}},
                    'preconditions': {'slot_conditions': {'action': {'equals_string': 'MODIFY',
                                                                     'name': 'action'}}}}]})

    summary: Optional[str] = Field(default=None, description="""Summary of the review""", json_schema_extra = { "linkml_meta": {'alias': 'summary',
         'domain_of': ['Review', 'InterPro2GORedundancy', 'PredictionAssessment'],
         'recommended': True} })
    action: ActionEnum = Field(default=..., description="""Action to be taken""", json_schema_extra = { "linkml_meta": {'alias': 'action', 'domain_of': ['Review', 'RuleReview']} })
    reason: Optional[str] = Field(default=None, description="""Reason for the action""", json_schema_extra = { "linkml_meta": {'alias': 'reason', 'domain_of': ['Review'], 'recommended': True} })
    proposed_replacement_terms: Optional[list[Term]] = Field(default=None, description="""If the action is MODIFY, then this is a list of proposed replacement terms""", json_schema_extra = { "linkml_meta": {'alias': 'proposed_replacement_terms',
         'comments': ['note there is a separate rule that this is required IF the '
                      'action is MODIFY'],
         'domain_of': ['Review']} })
    additional_reference_ids: Optional[list[str]] = Field(default=None, description="""IDs of the references""", json_schema_extra = { "linkml_meta": {'alias': 'additional_reference_ids', 'domain_of': ['Review']} })
    supported_by: Optional[list[SupportingTextInReference]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'supported_by',
         'domain_of': ['Review',
                       'CoreFunction',
                       'ProposedOntologyTerm',
                       'RuleReview',
                       'ParsimonyAssessment',
                       'LiteratureSupportAssessment',
                       'ConditionOverlapAssessment',
                       'GOSpecificityAssessment',
                       'TaxonomicScopeAssessment',
                       'PredictionAssessment'],
         'recommended': True} })
    knowledge_gaps: Optional[list[KnowledgeGap]] = Field(default=None, description="""Curated, literature-grounded statements of what is NOT known — applicable at the level of the whole gene, a single existing annotation, a core function, a whole module, or a single module step/node. The inverse of core_functions: everywhere else the schema records what IS known; here it records, with the same evidentiary discipline, what is not. See the Function Knowledge Gaps project (projects/FUNCTION_KNOWLEDGE_GAPS.md).""", json_schema_extra = { "linkml_meta": {'alias': 'knowledge_gaps',
         'domain_of': ['GeneReview',
                       'ModuleReview',
                       'ModuleNode',
                       'Review',
                       'CoreFunction']} })


class CoreFunction(ConfiguredBaseModel):
    """
    A core function is a GO-CAM-like annotation of the core evolved functions of a gene. This is a synthesis of the reviewed core annotations, brought together into a unified GO-CAM-like representation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review',
         'slot_usage': {'description': {'name': 'description', 'recommended': True}}})

    knowledge_gaps: Optional[list[KnowledgeGap]] = Field(default=None, description="""Curated, literature-grounded statements of what is NOT known — applicable at the level of the whole gene, a single existing annotation, a core function, a whole module, or a single module step/node. The inverse of core_functions: everywhere else the schema records what IS known; here it records, with the same evidentiary discipline, what is not. See the Function Knowledge Gaps project (projects/FUNCTION_KNOWLEDGE_GAPS.md).""", json_schema_extra = { "linkml_meta": {'alias': 'knowledge_gaps',
         'domain_of': ['GeneReview',
                       'ModuleReview',
                       'ModuleNode',
                       'Review',
                       'CoreFunction']} })
    description: Optional[str] = Field(default=None, description="""Description of the core function""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['GeneReview',
                       'AlternativeProduct',
                       'FunctionalIsoform',
                       'Term',
                       'Descriptor',
                       'ModuleReview',
                       'ModuleNode',
                       'ParticipantSelector',
                       'ModuleConnection',
                       'CoreFunction',
                       'Experiment',
                       'RuleReview',
                       'PredictionReview'],
         'recommended': True} })
    supported_by: Optional[list[SupportingTextInReference]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'supported_by',
         'domain_of': ['Review',
                       'CoreFunction',
                       'ProposedOntologyTerm',
                       'RuleReview',
                       'ParsimonyAssessment',
                       'LiteratureSupportAssessment',
                       'ConditionOverlapAssessment',
                       'GOSpecificityAssessment',
                       'TaxonomicScopeAssessment',
                       'PredictionAssessment']} })
    molecular_function: Optional[Term] = Field(default=None, description="""The molecular function this gene product enables (i.e., has the activity independently). For complex subunits that contribute to but don't independently have a complex-level activity, use contributes_to_molecular_function instead and put a subunit-specific MF here (e.g., structural constituent of ribosome, electron transfer activity).""", json_schema_extra = { "linkml_meta": {'alias': 'molecular_function',
         'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'GOMolecularActivityEnum'}],
         'domain_of': ['CoreFunction']} })
    contributes_to_molecular_function: Optional[Term] = Field(default=None, description="""A molecular function that this gene product contributes to as part of a complex, but does not independently enable. Used for accessory/structural subunits of multi-protein complexes (e.g., an accessory subunit of Complex I contributes_to NADH dehydrogenase activity but does not have that activity on its own). The molecular_function slot should then contain the subunit-specific activity (e.g., structural molecule activity).""", json_schema_extra = { "linkml_meta": {'alias': 'contributes_to_molecular_function',
         'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'GOMolecularActivityEnum'}],
         'domain_of': ['CoreFunction']} })
    directly_involved_in: Optional[list[Term]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'directly_involved_in',
         'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'GOBiologicalProcessEnum'}],
         'domain_of': ['CoreFunction']} })
    locations: Optional[list[Term]] = Field(default=None, description="""Cellular anatomical entities (e.g. membranes, nucleus, cytosol, organelle parts) where the gene product functions. Do NOT use this for protein-containing complexes (GO:0032991 and its descendants) — record complex membership in in_complex instead.""", json_schema_extra = { "linkml_meta": {'alias': 'locations',
         'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'GOCellularLocationEnum'}],
         'domain_of': ['ModuleAnnoton', 'CoreFunction']} })
    anatomical_locations: Optional[list[Term]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'anatomical_locations',
         'domain_of': ['ModuleContext', 'CoreFunction']} })
    substrates: Optional[list[Term]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'substrates',
         'domain_of': ['MolecularFunctionDescriptor', 'CoreFunction']} })
    in_complex: Optional[Term] = Field(default=None, description="""The protein-containing complex (GO:0032991 descendant) that this gene product is an active unit of. Use this — not locations — for complex membership (e.g. ribosome, spliceosome, EMC, signal peptidase complex).""", json_schema_extra = { "linkml_meta": {'alias': 'in_complex',
         'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'GOProteinContainingComplexEnum'}],
         'domain_of': ['CoreFunction']} })


class AnnotationExtension(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review',
         'slot_usage': {'predicate': {'bindings': [{'binds_value_of': 'id',
                                                    'obligation_level': 'REQUIRED',
                                                    'range': 'ROTermEnum'}],
                                      'name': 'predicate'}}})

    predicate: str = Field(default=..., description="""Predicate of the extension""", json_schema_extra = { "linkml_meta": {'alias': 'predicate',
         'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'ROTermEnum'}],
         'domain_of': ['ModuleConnection', 'AnnotationExtension', 'TermMapping'],
         'slot_uri': 'rdf:predicate'} })
    term: Optional[Term] = Field(default=None, description="""Term to be annotated""", json_schema_extra = { "linkml_meta": {'alias': 'term',
         'domain_of': ['Descriptor', 'ExistingAnnotation', 'AnnotationExtension']} })


class TermMapping(ConfiguredBaseModel):
    """
    A mapping between the proposed term and an equivalent term in another ontology
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    predicate: str = Field(default=..., description="""Mapping predicate (e.g., 'skos:exactMatch', 'skos:closeMatch', 'skos:broadMatch', 'skos:narrowMatch')""", json_schema_extra = { "linkml_meta": {'alias': 'predicate',
         'domain_of': ['ModuleConnection', 'AnnotationExtension', 'TermMapping']} })
    target_term: Term = Field(default=..., description="""The target term in another ontology""", json_schema_extra = { "linkml_meta": {'alias': 'target_term', 'domain_of': ['TermMapping']} })


class ProposedOntologyTerm(ConfiguredBaseModel):
    """
    A proposed new ontology term that should exist but doesn't currently
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    proposed_name: str = Field(default=..., description="""Proposed name for the new term""", json_schema_extra = { "linkml_meta": {'alias': 'proposed_name', 'domain_of': ['ProposedOntologyTerm']} })
    proposed_definition: str = Field(default=..., description="""Proposed definition for the new term""", json_schema_extra = { "linkml_meta": {'alias': 'proposed_definition', 'domain_of': ['ProposedOntologyTerm']} })
    justification: Optional[str] = Field(default=None, description="""Justification for why this term is needed""", json_schema_extra = { "linkml_meta": {'alias': 'justification', 'domain_of': ['ProposedOntologyTerm']} })
    proposed_parent: Optional[Term] = Field(default=None, description="""Proposed parent term in the ontology hierarchy""", json_schema_extra = { "linkml_meta": {'alias': 'proposed_parent', 'domain_of': ['ProposedOntologyTerm']} })
    proposed_mappings: Optional[list[TermMapping]] = Field(default=None, description="""Proposed mappings to equivalent terms in other ontologies""", json_schema_extra = { "linkml_meta": {'alias': 'proposed_mappings', 'domain_of': ['ProposedOntologyTerm']} })
    supported_by: Optional[list[SupportingTextInReference]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'supported_by',
         'domain_of': ['Review',
                       'CoreFunction',
                       'ProposedOntologyTerm',
                       'RuleReview',
                       'ParsimonyAssessment',
                       'LiteratureSupportAssessment',
                       'ConditionOverlapAssessment',
                       'GOSpecificityAssessment',
                       'TaxonomicScopeAssessment',
                       'PredictionAssessment']} })


class KnowledgeGap(ConfiguredBaseModel):
    """
    A curated, literature-grounded statement of what is NOT known about a gene product, core function, module, or step — its molecular activity, mechanism, partner(s), localization, or biological role. A knowledge gap is a reviewer judgment reached by reading the primary literature, NOT a pattern in the annotations: a heavily annotated gene can hide a gaping mechanistic hole, and a sparsely annotated one can be perfectly understood and merely under-curated. Each gap is a small, defensible scholarly object with the same evidentiary discipline used for positive claims. See projects/FUNCTION_KNOWLEDGE_GAPS.md for the methodology and worked exemplars.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    gap_statement: str = Field(default=..., description="""The specific unknown, stated precisely. Not \"role unclear\" but e.g. \"the direct substrate / the catalytic activity / the essential partner is undetermined\".""", json_schema_extra = { "linkml_meta": {'alias': 'gap_statement', 'domain_of': ['KnowledgeGap']} })
    boundary: Optional[str] = Field(default=None, description="""What IS firmly established, so the gap is sharply delimited. The edge of current knowledge against which the gap is defined.""", json_schema_extra = { "linkml_meta": {'alias': 'boundary', 'domain_of': ['KnowledgeGap'], 'recommended': True} })
    gap_kind: Optional[list[KnowledgeGapKindEnum]] = Field(default=None, description="""The kind(s) of ignorance — biology, curation, and/or ontology — which determines who can resolve it. Multiple values denote a blend (e.g. a biology gap with an ontology shadow).""", json_schema_extra = { "linkml_meta": {'alias': 'gap_kind', 'domain_of': ['KnowledgeGap'], 'recommended': True} })
    dark_aspect: Optional[KnowledgeGapAspectEnum] = Field(default=None, description="""Which GO aspect (or pattern) is dark for this gap. Most \"dark\" genes are not uniformly dark.""", json_schema_extra = { "linkml_meta": {'alias': 'dark_aspect', 'domain_of': ['KnowledgeGap']} })
    status: Optional[KnowledgeGapStatusEnum] = Field(default=None, description="""Lifecycle status of the gap, tracking progress toward resolution.""", json_schema_extra = { "linkml_meta": {'alias': 'status',
         'domain_of': ['GeneReview',
                       'ModuleReview',
                       'KnowledgeGap',
                       'RuleReview',
                       'PredictionReview']} })
    significance: Optional[str] = Field(default=None, description="""Why closing this gap matters.""", json_schema_extra = { "linkml_meta": {'alias': 'significance', 'domain_of': ['KnowledgeGap']} })
    resolution: Optional[str] = Field(default=None, description="""What would resolve the gap — the experiment, ontology term, or curation action. For ONTOLOGY gaps, pair with proposed_terms (or the gene's top-level proposed_new_terms).""", json_schema_extra = { "linkml_meta": {'alias': 'resolution', 'domain_of': ['KnowledgeGap']} })
    provenance: Optional[list[SupportingTextInReference]] = Field(default=None, description="""Evidence that the unknown is REAL and not merely uncurated — ideally the field's own admissions of ignorance (\"remains to be determined\", \"the precise role is unknown\"). The supporting_text is a verbatim substring of the cited reference and is checked by the reference validator exactly like supported_by. When the only available source is a DOI-only paper or a local analysis, anchor provenance to that reference_id (e.g. a file: path).""", json_schema_extra = { "linkml_meta": {'alias': 'provenance', 'domain_of': ['KnowledgeGap'], 'recommended': True} })
    proposed_terms: Optional[list[ProposedOntologyTerm]] = Field(default=None, description="""For ONTOLOGY gaps, the new ontology term(s) that would let the knowledge be expressed (e.g. \"structural constituent of complex X\"). May elaborate the gene's top-level proposed_new_terms.""", json_schema_extra = { "linkml_meta": {'alias': 'proposed_terms', 'domain_of': ['KnowledgeGap']} })


class Experiment(ConfiguredBaseModel):
    """
    A suggested experiment to answer a question about the gene
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    hypothesis: Optional[str] = Field(default=None, description="""Hypothesis to be investigated""", json_schema_extra = { "linkml_meta": {'alias': 'hypothesis', 'domain_of': ['Experiment'], 'recommended': True} })
    description: str = Field(default=..., description="""Detailed description of the experiment to be performed""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['GeneReview',
                       'AlternativeProduct',
                       'FunctionalIsoform',
                       'Term',
                       'Descriptor',
                       'ModuleReview',
                       'ModuleNode',
                       'ParticipantSelector',
                       'ModuleConnection',
                       'CoreFunction',
                       'Experiment',
                       'RuleReview',
                       'PredictionReview']} })
    experiment_type: Optional[str] = Field(default=None, description="""Type of experiment or assay to answer the question""", json_schema_extra = { "linkml_meta": {'alias': 'experiment_type', 'domain_of': ['Experiment']} })


class Question(ConfiguredBaseModel):
    """
    A question to be answered about the gene
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    question: str = Field(default=..., description="""Question to be answered""", json_schema_extra = { "linkml_meta": {'alias': 'question', 'domain_of': ['Question']} })
    experts: Optional[list[str]] = Field(default=None, description="""Experts to answer the question. These should be drawn from the authors of relevant publications already referenced. If no suitable experts are available, it's OK to leave this as an empty list!""", json_schema_extra = { "linkml_meta": {'alias': 'experts', 'domain_of': ['Question']} })


class RuleReview(ConfiguredBaseModel):
    """
    A review of a UniProt annotation rule (ARBA or UniRule). Each review covers ONE rule and assesses its quality, literature support, and biological appropriateness.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review',
         'slot_usage': {'id': {'description': 'The rule ID (e.g., ARBA00026249, '
                                              'UR000000070)',
                               'name': 'id'}}})

    id: str = Field(default=..., description="""The rule ID (e.g., ARBA00026249, UR000000070)""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['GeneReview',
                       'AlternativeProduct',
                       'FunctionalIsoform',
                       'Term',
                       'Reference',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'RuleReview',
                       'RuleReviewEntry',
                       'PredictionReview']} })
    description: Optional[str] = Field(default=None, description="""Description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['GeneReview',
                       'AlternativeProduct',
                       'FunctionalIsoform',
                       'Term',
                       'Descriptor',
                       'ModuleReview',
                       'ModuleNode',
                       'ParticipantSelector',
                       'ModuleConnection',
                       'CoreFunction',
                       'Experiment',
                       'RuleReview',
                       'PredictionReview'],
         'slot_uri': 'dcterms:description'} })
    references: Optional[list[Reference]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'references',
         'domain_of': ['GeneReview', 'ModuleReview', 'RuleReview', 'PredictionReview']} })
    status: Optional[RuleReviewStatusEnum] = Field(default=None, description="""Status of the rule review""", json_schema_extra = { "linkml_meta": {'alias': 'status',
         'domain_of': ['GeneReview',
                       'ModuleReview',
                       'KnowledgeGap',
                       'RuleReview',
                       'PredictionReview']} })
    rule_type: RuleTypeEnum = Field(default=..., description="""Type of rule (ARBA or UniRule)""", json_schema_extra = { "linkml_meta": {'alias': 'rule_type', 'domain_of': ['RuleReview']} })
    rule: EmbeddedRule = Field(default=..., description="""The embedded rule being reviewed""", json_schema_extra = { "linkml_meta": {'alias': 'rule', 'domain_of': ['RuleReview']} })
    review_summary: Optional[str] = Field(default=None, description="""Overall summary of the review findings""", json_schema_extra = { "linkml_meta": {'alias': 'review_summary', 'domain_of': ['RuleReview']} })
    action: RuleActionEnum = Field(default=..., description="""Recommended action for this rule""", json_schema_extra = { "linkml_meta": {'alias': 'action', 'domain_of': ['Review', 'RuleReview']} })
    action_rationale: Optional[str] = Field(default=None, description="""Rationale for the recommended action""", json_schema_extra = { "linkml_meta": {'alias': 'action_rationale', 'domain_of': ['RuleReview']} })
    suggested_modifications: Optional[list[str]] = Field(default=None, description="""Specific modifications suggested if action is MODIFY""", json_schema_extra = { "linkml_meta": {'alias': 'suggested_modifications', 'domain_of': ['RuleReview']} })
    parsimony: Optional[ParsimonyAssessment] = Field(default=None, description="""Assessment of rule parsimony (simplicity vs complexity)""", json_schema_extra = { "linkml_meta": {'alias': 'parsimony', 'domain_of': ['RuleReview']} })
    literature_support: Optional[LiteratureSupportAssessment] = Field(default=None, description="""Assessment of literature support for the rule""", json_schema_extra = { "linkml_meta": {'alias': 'literature_support', 'domain_of': ['RuleReview']} })
    condition_overlap: Optional[ConditionOverlapAssessment] = Field(default=None, description="""Assessment of overlap between rule conditions""", json_schema_extra = { "linkml_meta": {'alias': 'condition_overlap', 'domain_of': ['RuleReview']} })
    go_specificity: Optional[GOSpecificityAssessment] = Field(default=None, description="""Assessment of GO term specificity""", json_schema_extra = { "linkml_meta": {'alias': 'go_specificity', 'domain_of': ['RuleReview']} })
    taxonomic_scope: Optional[TaxonomicScopeAssessment] = Field(default=None, description="""Assessment of taxonomic restriction appropriateness""", json_schema_extra = { "linkml_meta": {'alias': 'taxonomic_scope', 'domain_of': ['RuleReview']} })
    confidence: Optional[float] = Field(default=None, description="""Overall confidence in the rule (0.0 to 1.0)""", ge=0.0, le=1.0, json_schema_extra = { "linkml_meta": {'alias': 'confidence', 'domain_of': ['RuleReview']} })
    supported_by: Optional[list[SupportingTextInReference]] = Field(default=None, description="""Supporting text from literature for this review""", json_schema_extra = { "linkml_meta": {'alias': 'supported_by',
         'domain_of': ['Review',
                       'CoreFunction',
                       'ProposedOntologyTerm',
                       'RuleReview',
                       'ParsimonyAssessment',
                       'LiteratureSupportAssessment',
                       'ConditionOverlapAssessment',
                       'GOSpecificityAssessment',
                       'TaxonomicScopeAssessment',
                       'PredictionAssessment']} })


class EmbeddedRule(ConfiguredBaseModel):
    """
    An embedded representation of an ARBA or UniRule for storage in YAML. Captures the essential structure: conditions (antecedent) and GO annotations (consequent).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    rule_id: str = Field(default=..., description="""Original rule ID (e.g., ARBA00026249, UR000000070)""", json_schema_extra = { "linkml_meta": {'alias': 'rule_id', 'domain_of': ['EmbeddedRule']} })
    condition_sets: list[RuleConditionSet] = Field(default=..., description="""List of condition sets (OR-ed together). Each condition set is a conjunction (AND) of conditions. The rule fires if ANY condition set matches.""", json_schema_extra = { "linkml_meta": {'alias': 'condition_sets', 'domain_of': ['EmbeddedRule']} })
    go_annotations: Optional[list[RuleGOAnnotation]] = Field(default=None, description="""GO terms assigned by this rule""", json_schema_extra = { "linkml_meta": {'alias': 'go_annotations', 'domain_of': ['EmbeddedRule']} })
    ipr2go_redundancy: Optional[InterPro2GORedundancy] = Field(default=None, description="""Analysis of redundancy with InterPro2GO mappings""", json_schema_extra = { "linkml_meta": {'alias': 'ipr2go_redundancy', 'domain_of': ['EmbeddedRule']} })
    entries: list[RuleReviewEntry] = Field(default=..., description="""Entry-centric view of all entities in the rule (domain conditions and GO terms). Each entry tracks its relationships (PREDICTS, PREDICTED_BY, EQUIV) to other entries.""", json_schema_extra = { "linkml_meta": {'alias': 'entries', 'domain_of': ['EmbeddedRule']} })
    reviewed_protein_count: Optional[int] = Field(default=None, description="""Number of reviewed (Swiss-Prot) proteins annotated by this rule""", json_schema_extra = { "linkml_meta": {'alias': 'reviewed_protein_count', 'domain_of': ['EmbeddedRule']} })
    unreviewed_protein_count: Optional[int] = Field(default=None, description="""Number of unreviewed (TrEMBL) proteins annotated by this rule""", json_schema_extra = { "linkml_meta": {'alias': 'unreviewed_protein_count', 'domain_of': ['EmbeddedRule']} })
    created_date: Optional[str] = Field(default=None, description="""Date the rule was created""", json_schema_extra = { "linkml_meta": {'alias': 'created_date', 'domain_of': ['EmbeddedRule']} })
    modified_date: Optional[str] = Field(default=None, description="""Date the rule was last modified""", json_schema_extra = { "linkml_meta": {'alias': 'modified_date', 'domain_of': ['EmbeddedRule']} })


class RuleConditionSet(ConfiguredBaseModel):
    """
    A set of conditions that must ALL be true (conjunction/AND). Multiple condition sets in a rule are OR-ed together (disjunction).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    number: int = Field(default=..., description="""1-based condition set number (CS1, CS2, CS3, etc.)""", ge=1, json_schema_extra = { "linkml_meta": {'alias': 'number', 'domain_of': ['RuleConditionSet']} })
    conditions: list[RuleCondition] = Field(default=..., description="""Conditions in this set (all must match)""", json_schema_extra = { "linkml_meta": {'alias': 'conditions', 'domain_of': ['ModuleContext', 'RuleConditionSet']} })
    notes: Optional[str] = Field(default=None, description="""Reviewer notes on this specific condition set""", json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['EvidenceItem',
                       'Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection',
                       'RuleConditionSet',
                       'ParsimonyAssessment',
                       'LiteratureSupportAssessment',
                       'ConditionOverlapAssessment',
                       'GOSpecificityAssessment',
                       'TaxonomicScopeAssessment']} })
    pairwise_overlap: Optional[list[PairwiseOverlap]] = Field(default=None, description="""Pairwise overlap statistics for domain conditions in this set. Only computed for InterPro, FunFam, PANTHER conditions. Provides set difference metrics (uniqueness) and Jaccard similarity.""", json_schema_extra = { "linkml_meta": {'alias': 'pairwise_overlap', 'domain_of': ['RuleConditionSet']} })


class RuleCondition(ConfiguredBaseModel):
    """
    A single condition in a rule antecedent
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    condition_type: ConditionTypeEnum = Field(default=..., description="""Type of condition""", json_schema_extra = { "linkml_meta": {'alias': 'condition_type', 'domain_of': ['RuleCondition']} })
    value: str = Field(default=..., description="""The condition value (e.g., IPR000001, NCBITaxon:4751)""", json_schema_extra = { "linkml_meta": {'alias': 'value', 'domain_of': ['RuleCondition']} })
    curie: Optional[str] = Field(default=None, description="""Normalized CURIE form (e.g., InterPro:IPR000001, NCBITaxon:4751)""", json_schema_extra = { "linkml_meta": {'alias': 'curie', 'domain_of': ['RuleCondition']} })
    label: Optional[str] = Field(default=None, description="""Human-readable label""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'domain_of': ['Term',
                       'ComplexUnit',
                       'ModuleNode',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'RuleCondition',
                       'RuleReviewEntry']} })
    interpro_type: Optional[InterProTypeEnum] = Field(default=None, description="""InterPro entry type (family, domain, active_site, etc.). Only populated for InterPro conditions (condition_type = INTERPRO). Extracted from InterPro metadata or API.""", json_schema_extra = { "linkml_meta": {'alias': 'interpro_type', 'domain_of': ['RuleCondition']} })
    negated: Optional[bool] = Field(default=None, description="""Whether this is a negative condition (NOT)""", json_schema_extra = { "linkml_meta": {'alias': 'negated', 'domain_of': ['ExistingAnnotation', 'RuleCondition']} })
    protein_count: Optional[int] = Field(default=None, description="""Number of proteins matching this condition in specified database. Only populated for domain/family conditions (InterPro, FunFam, PANTHER). Null for taxon and other condition types.""", ge=0, json_schema_extra = { "linkml_meta": {'alias': 'protein_count', 'domain_of': ['RuleCondition', 'RuleReviewEntry']} })
    protein_database: Optional[ProteinDatabaseEnum] = Field(default=None, description="""Which protein database was queried (e.g., SWISSPROT, TREMBL). Defaults to SWISSPROT (reviewed proteins only). Important to specify since counts differ dramatically between databases.""", json_schema_extra = { "linkml_meta": {'alias': 'protein_database', 'domain_of': ['RuleCondition', 'PairwiseOverlap']} })
    uniqueness_score: Optional[float] = Field(default=None, description="""Measure of domain uniqueness (0.0 to 1.0). Calculated as 1.0 - mean(containment in other domains in same condition set). High score = more unique/specific domain. Low score = broad domain that commonly co-occurs.""", ge=0.0, le=1.0, json_schema_extra = { "linkml_meta": {'alias': 'uniqueness_score', 'domain_of': ['RuleCondition']} })
    sample_proteins: Optional[list[str]] = Field(default=None, description="""Sample UniProt IDs matching this condition. Only included when protein_count < 20 to avoid bloating files. Limited to max 10 examples.""", json_schema_extra = { "linkml_meta": {'alias': 'sample_proteins', 'domain_of': ['RuleCondition']} })


class RuleGOAnnotation(ConfiguredBaseModel):
    """
    A GO annotation produced by the rule
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    go_id: str = Field(default=..., description="""GO term ID (e.g., GO:0004791)""", json_schema_extra = { "linkml_meta": {'alias': 'go_id', 'domain_of': ['RuleGOAnnotation', 'RedundantAnnotation']} })
    go_label: Optional[str] = Field(default=None, description="""GO term name""", json_schema_extra = { "linkml_meta": {'alias': 'go_label', 'domain_of': ['RuleGOAnnotation', 'RedundantAnnotation']} })
    aspect: Optional[str] = Field(default=None, description="""GO aspect (F, P, or C)""", json_schema_extra = { "linkml_meta": {'alias': 'aspect', 'domain_of': ['RuleGOAnnotation']} })


class PairwiseOverlap(ConfiguredBaseModel):
    """
    Overlap statistics between two domain conditions (InterPro, FunFam, etc.) in the same condition set. Provides set difference metrics to measure uniqueness and redundancy.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    condition_a: str = Field(default=..., description="""First condition value (e.g., IPR005982)""", json_schema_extra = { "linkml_meta": {'alias': 'condition_a', 'domain_of': ['PairwiseOverlap']} })
    condition_b: str = Field(default=..., description="""Second condition value (e.g., IPR008255)""", json_schema_extra = { "linkml_meta": {'alias': 'condition_b', 'domain_of': ['PairwiseOverlap']} })
    condition_a_label: Optional[str] = Field(default=None, description="""Human-readable label for condition A""", json_schema_extra = { "linkml_meta": {'alias': 'condition_a_label', 'domain_of': ['PairwiseOverlap']} })
    condition_b_label: Optional[str] = Field(default=None, description="""Human-readable label for condition B""", json_schema_extra = { "linkml_meta": {'alias': 'condition_b_label', 'domain_of': ['PairwiseOverlap']} })
    protein_database: ProteinDatabaseEnum = Field(default=..., description="""Which protein database was queried (SWISSPROT or TREMBL)""", json_schema_extra = { "linkml_meta": {'alias': 'protein_database', 'domain_of': ['RuleCondition', 'PairwiseOverlap']} })
    count_a: int = Field(default=..., description="""Number of proteins matching condition A in specified database""", ge=0, json_schema_extra = { "linkml_meta": {'alias': 'count_a', 'domain_of': ['PairwiseOverlap']} })
    count_b: int = Field(default=..., description="""Number of proteins matching condition B in specified database""", ge=0, json_schema_extra = { "linkml_meta": {'alias': 'count_b', 'domain_of': ['PairwiseOverlap']} })
    intersection_count: int = Field(default=..., description="""Number of proteins matching BOTH A AND B (|A ∩ B|) in specified database""", ge=0, json_schema_extra = { "linkml_meta": {'alias': 'intersection_count',
         'domain_of': ['PairwiseOverlap', 'RelatedEntry']} })
    a_minus_b_count: int = Field(default=..., description="""Number of proteins in A but not in B (|A - B|). Represents the uniqueness of A with respect to B. High value = A adds unique coverage beyond B. Zero value = A is completely contained in B (A ⊆ B).""", ge=0, json_schema_extra = { "linkml_meta": {'alias': 'a_minus_b_count', 'domain_of': ['PairwiseOverlap']} })
    b_minus_a_count: int = Field(default=..., description="""Number of proteins in B but not in A (|B - A|). Represents the uniqueness of B with respect to A. High value = B adds unique coverage beyond A. Zero value = B is completely contained in A (B ⊆ A).""", ge=0, json_schema_extra = { "linkml_meta": {'alias': 'b_minus_a_count', 'domain_of': ['PairwiseOverlap']} })
    jaccard_similarity: float = Field(default=..., description="""Jaccard similarity coefficient: |A ∩ B| / |A ∪ B| = intersection / (count_a + count_b - intersection). 0.0 = no overlap, 1.0 = complete overlap.""", ge=0.0, le=1.0, json_schema_extra = { "linkml_meta": {'alias': 'jaccard_similarity',
         'domain_of': ['PairwiseOverlap', 'RelatedEntry']} })
    containment_a_in_b: float = Field(default=..., description="""Proportion of A contained in B: |A ∩ B| / |A|. 1.0 means A is completely contained in B (A ⊆ B).""", ge=0.0, le=1.0, json_schema_extra = { "linkml_meta": {'alias': 'containment_a_in_b', 'domain_of': ['PairwiseOverlap']} })
    containment_b_in_a: float = Field(default=..., description="""Proportion of B contained in A: |A ∩ B| / |B|. 1.0 means B is completely contained in A (B ⊆ A).""", ge=0.0, le=1.0, json_schema_extra = { "linkml_meta": {'alias': 'containment_b_in_a', 'domain_of': ['PairwiseOverlap']} })
    interpretation: Optional[OverlapInterpretationEnum] = Field(default=None, description="""Automated interpretation of overlap pattern""", json_schema_extra = { "linkml_meta": {'alias': 'interpretation', 'domain_of': ['PairwiseOverlap']} })
    condition_a_in_sets: Optional[list[int]] = Field(default=None, description="""List of 1-based condition set indices where condition A appears""", ge=1, json_schema_extra = { "linkml_meta": {'alias': 'condition_a_in_sets', 'domain_of': ['PairwiseOverlap']} })
    condition_b_in_sets: Optional[list[int]] = Field(default=None, description="""List of 1-based condition set indices where condition B appears""", ge=1, json_schema_extra = { "linkml_meta": {'alias': 'condition_b_in_sets', 'domain_of': ['PairwiseOverlap']} })


class RuleReviewEntry(ConfiguredBaseModel):
    """
    An entity in the rule - either a domain/family condition or a GO term target. Each entry tracks its relationships (predictions, predicted-by, equivalence) to other entries.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    id: str = Field(default=..., description="""Identifier (IPR005982, GO:0004791, 3.50.50.60:FF:000064, etc.)""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['GeneReview',
                       'AlternativeProduct',
                       'FunctionalIsoform',
                       'Term',
                       'Reference',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'RuleReview',
                       'RuleReviewEntry',
                       'PredictionReview']} })
    label: Optional[str] = Field(default=None, description="""Human-readable name""", json_schema_extra = { "linkml_meta": {'alias': 'label',
         'domain_of': ['Term',
                       'ComplexUnit',
                       'ModuleNode',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'RuleCondition',
                       'RuleReviewEntry']} })
    type: EntryTypeEnum = Field(default=..., description="""Type of entry (INTERPRO, FUNFAM, PANTHER, GO_TERM, etc.)""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'domain_of': ['FunctionalIsoform',
                       'FunctionalIsoformMapping',
                       'RuleReviewEntry']} })
    appears_in_condition_sets: Optional[list[int]] = Field(default=None, description="""Which condition sets (1-based) contain this entry (for domain conditions only)""", ge=1, json_schema_extra = { "linkml_meta": {'alias': 'appears_in_condition_sets', 'domain_of': ['RuleReviewEntry']} })
    protein_count: Optional[int] = Field(default=None, description="""Number of proteins matching this condition (from SwissProt)""", json_schema_extra = { "linkml_meta": {'alias': 'protein_count', 'domain_of': ['RuleCondition', 'RuleReviewEntry']} })
    source: Optional[str] = Field(default=None, description="""Source of this entry if external to the rule (e.g., 'ipr2go' for InterPro entries that map to the same GO term via InterPro2GO but are not part of any condition set)""", json_schema_extra = { "linkml_meta": {'alias': 'source', 'domain_of': ['ModuleConnection', 'RuleReviewEntry']} })
    asserted_predicted_go_terms: Optional[list[str]] = Field(default=None, description="""GO terms that this entry maps to via external mappings (e.g., ipr2go). Only populated for external entries not in the rule's condition sets.""", json_schema_extra = { "linkml_meta": {'alias': 'asserted_predicted_go_terms', 'domain_of': ['RuleReviewEntry']} })
    related_entries: Optional[list[RelatedEntry]] = Field(default=None, description="""Relationships to other entries in the rule""", json_schema_extra = { "linkml_meta": {'alias': 'related_entries', 'domain_of': ['RuleReviewEntry']} })


class RelatedEntry(ConfiguredBaseModel):
    """
    A relationship from this entry to another entry in the rule. Categorized as PREDICTS (this → other), PREDICTED_BY (other → this), or EQUIV (bidirectional).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    relationship: EntryRelationshipEnum = Field(default=..., description="""Type of relationship""", json_schema_extra = { "linkml_meta": {'alias': 'relationship', 'domain_of': ['RelatedEntry']} })
    target_id: str = Field(default=..., description="""ID of the related entry""", json_schema_extra = { "linkml_meta": {'alias': 'target_id', 'domain_of': ['RelatedEntry']} })
    containment: Optional[float] = Field(default=None, description="""Containment score (0-1) for the directional relationship. For PREDICTS: this_in_target (how much of this is contained in target). For PREDICTED_BY: target_in_this (how much of target is contained in this). For EQUIV: max of both directions.""", ge=0.0, le=1.0, json_schema_extra = { "linkml_meta": {'alias': 'containment', 'domain_of': ['RelatedEntry']} })
    jaccard_similarity: Optional[float] = Field(default=None, description="""Jaccard similarity coefficient (0-1)""", ge=0.0, le=1.0, json_schema_extra = { "linkml_meta": {'alias': 'jaccard_similarity',
         'domain_of': ['PairwiseOverlap', 'RelatedEntry']} })
    intersection_count: Optional[int] = Field(default=None, description="""Number of proteins in both this and target""", json_schema_extra = { "linkml_meta": {'alias': 'intersection_count',
         'domain_of': ['PairwiseOverlap', 'RelatedEntry']} })
    exclusive_count: Optional[int] = Field(default=None, description="""Number of proteins exclusive to the \"source\" of the relationship. For PREDICTS: proteins in this but not target. For PREDICTED_BY: proteins in target but not this. For EQUIV: proteins in this but not target (A - B).""", json_schema_extra = { "linkml_meta": {'alias': 'exclusive_count', 'domain_of': ['RelatedEntry']} })


class InterPro2GORedundancy(ConfiguredBaseModel):
    """
    Analysis of whether rule GO annotations are redundant with existing InterPro2GO mappings from the GO Consortium.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    redundant_annotations: Optional[list[RedundantAnnotation]] = Field(default=None, description="""GO annotations that already exist in InterPro2GO""", json_schema_extra = { "linkml_meta": {'alias': 'redundant_annotations', 'domain_of': ['InterPro2GORedundancy']} })
    novel_annotations: Optional[list[str]] = Field(default=None, description="""GO IDs not found in InterPro2GO for any rule condition""", json_schema_extra = { "linkml_meta": {'alias': 'novel_annotations', 'domain_of': ['InterPro2GORedundancy']} })
    summary: Optional[str] = Field(default=None, description="""Human-readable summary of redundancy analysis""", json_schema_extra = { "linkml_meta": {'alias': 'summary',
         'domain_of': ['Review', 'InterPro2GORedundancy', 'PredictionAssessment']} })


class RedundantAnnotation(ConfiguredBaseModel):
    """
    A GO annotation that is redundant with an existing InterPro2GO mapping
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    go_id: str = Field(default=..., description="""GO term ID (e.g., GO:0004791)""", json_schema_extra = { "linkml_meta": {'alias': 'go_id', 'domain_of': ['RuleGOAnnotation', 'RedundantAnnotation']} })
    go_label: Optional[str] = Field(default=None, description="""GO term label""", json_schema_extra = { "linkml_meta": {'alias': 'go_label', 'domain_of': ['RuleGOAnnotation', 'RedundantAnnotation']} })
    interpro_source: str = Field(default=..., description="""InterPro ID that already maps to this GO term in ipr2go""", json_schema_extra = { "linkml_meta": {'alias': 'interpro_source', 'domain_of': ['RedundantAnnotation']} })
    interpro_label: Optional[str] = Field(default=None, description="""InterPro domain label""", json_schema_extra = { "linkml_meta": {'alias': 'interpro_label', 'domain_of': ['RedundantAnnotation']} })


class ParsimonyAssessment(ConfiguredBaseModel):
    """
    Assessment of rule parsimony (simplicity vs complexity)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    assessment: ParsimonyEnum = Field(default=..., description="""Parsimony assessment value""", json_schema_extra = { "linkml_meta": {'alias': 'assessment',
         'domain_of': ['ParsimonyAssessment',
                       'LiteratureSupportAssessment',
                       'ConditionOverlapAssessment',
                       'GOSpecificityAssessment',
                       'TaxonomicScopeAssessment',
                       'PredictionAssessment']} })
    notes: Optional[str] = Field(default=None, description="""Notes on parsimony - e.g., which conditions are redundant""", json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['EvidenceItem',
                       'Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection',
                       'RuleConditionSet',
                       'ParsimonyAssessment',
                       'LiteratureSupportAssessment',
                       'ConditionOverlapAssessment',
                       'GOSpecificityAssessment',
                       'TaxonomicScopeAssessment']} })
    supported_by: Optional[list[SupportingTextInReference]] = Field(default=None, description="""Supporting text from literature for this assessment""", json_schema_extra = { "linkml_meta": {'alias': 'supported_by',
         'domain_of': ['Review',
                       'CoreFunction',
                       'ProposedOntologyTerm',
                       'RuleReview',
                       'ParsimonyAssessment',
                       'LiteratureSupportAssessment',
                       'ConditionOverlapAssessment',
                       'GOSpecificityAssessment',
                       'TaxonomicScopeAssessment',
                       'PredictionAssessment']} })


class LiteratureSupportAssessment(ConfiguredBaseModel):
    """
    Assessment of literature support for the rule
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    assessment: LiteratureSupportEnum = Field(default=..., description="""Level of literature support""", json_schema_extra = { "linkml_meta": {'alias': 'assessment',
         'domain_of': ['ParsimonyAssessment',
                       'LiteratureSupportAssessment',
                       'ConditionOverlapAssessment',
                       'GOSpecificityAssessment',
                       'TaxonomicScopeAssessment',
                       'PredictionAssessment']} })
    notes: Optional[str] = Field(default=None, description="""Notes on literature support - key papers, gaps in evidence""", json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['EvidenceItem',
                       'Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection',
                       'RuleConditionSet',
                       'ParsimonyAssessment',
                       'LiteratureSupportAssessment',
                       'ConditionOverlapAssessment',
                       'GOSpecificityAssessment',
                       'TaxonomicScopeAssessment']} })
    supported_by: Optional[list[SupportingTextInReference]] = Field(default=None, description="""Supporting text from literature for this assessment""", json_schema_extra = { "linkml_meta": {'alias': 'supported_by',
         'domain_of': ['Review',
                       'CoreFunction',
                       'ProposedOntologyTerm',
                       'RuleReview',
                       'ParsimonyAssessment',
                       'LiteratureSupportAssessment',
                       'ConditionOverlapAssessment',
                       'GOSpecificityAssessment',
                       'TaxonomicScopeAssessment',
                       'PredictionAssessment']} })


class ConditionOverlapAssessment(ConfiguredBaseModel):
    """
    Assessment of overlap between rule conditions
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    assessment: OverlapEnum = Field(default=..., description="""Overlap assessment value""", json_schema_extra = { "linkml_meta": {'alias': 'assessment',
         'domain_of': ['ParsimonyAssessment',
                       'LiteratureSupportAssessment',
                       'ConditionOverlapAssessment',
                       'GOSpecificityAssessment',
                       'TaxonomicScopeAssessment',
                       'PredictionAssessment']} })
    notes: Optional[str] = Field(default=None, description="""Notes on condition overlap - e.g., \"IPR000001 and IPR000002 both represent the same structural domain\" or \"FunFam subsumes the InterPro entry\"""", json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['EvidenceItem',
                       'Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection',
                       'RuleConditionSet',
                       'ParsimonyAssessment',
                       'LiteratureSupportAssessment',
                       'ConditionOverlapAssessment',
                       'GOSpecificityAssessment',
                       'TaxonomicScopeAssessment']} })
    supported_by: Optional[list[SupportingTextInReference]] = Field(default=None, description="""Supporting text from literature for this assessment""", json_schema_extra = { "linkml_meta": {'alias': 'supported_by',
         'domain_of': ['Review',
                       'CoreFunction',
                       'ProposedOntologyTerm',
                       'RuleReview',
                       'ParsimonyAssessment',
                       'LiteratureSupportAssessment',
                       'ConditionOverlapAssessment',
                       'GOSpecificityAssessment',
                       'TaxonomicScopeAssessment',
                       'PredictionAssessment']} })


class GOSpecificityAssessment(ConfiguredBaseModel):
    """
    Assessment of GO term specificity
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    assessment: SpecificityEnum = Field(default=..., description="""Specificity assessment value""", json_schema_extra = { "linkml_meta": {'alias': 'assessment',
         'domain_of': ['ParsimonyAssessment',
                       'LiteratureSupportAssessment',
                       'ConditionOverlapAssessment',
                       'GOSpecificityAssessment',
                       'TaxonomicScopeAssessment',
                       'PredictionAssessment']} })
    notes: Optional[str] = Field(default=None, description="""Notes on specificity - suggested alternative terms if too broad/narrow""", json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['EvidenceItem',
                       'Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection',
                       'RuleConditionSet',
                       'ParsimonyAssessment',
                       'LiteratureSupportAssessment',
                       'ConditionOverlapAssessment',
                       'GOSpecificityAssessment',
                       'TaxonomicScopeAssessment']} })
    supported_by: Optional[list[SupportingTextInReference]] = Field(default=None, description="""Supporting text from literature for this assessment""", json_schema_extra = { "linkml_meta": {'alias': 'supported_by',
         'domain_of': ['Review',
                       'CoreFunction',
                       'ProposedOntologyTerm',
                       'RuleReview',
                       'ParsimonyAssessment',
                       'LiteratureSupportAssessment',
                       'ConditionOverlapAssessment',
                       'GOSpecificityAssessment',
                       'TaxonomicScopeAssessment',
                       'PredictionAssessment']} })


class TaxonomicScopeAssessment(ConfiguredBaseModel):
    """
    Assessment of taxonomic restriction appropriateness
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    assessment: TaxonomicScopeEnum = Field(default=..., description="""Taxonomic scope assessment value""", json_schema_extra = { "linkml_meta": {'alias': 'assessment',
         'domain_of': ['ParsimonyAssessment',
                       'LiteratureSupportAssessment',
                       'ConditionOverlapAssessment',
                       'GOSpecificityAssessment',
                       'TaxonomicScopeAssessment',
                       'PredictionAssessment']} })
    notes: Optional[str] = Field(default=None, description="""Notes on taxonomic scope - suggested changes to taxon constraints""", json_schema_extra = { "linkml_meta": {'alias': 'notes',
         'domain_of': ['EvidenceItem',
                       'Descriptor',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModulePart',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'ParticipantSelector',
                       'ModuleContext',
                       'ModuleConnection',
                       'RuleConditionSet',
                       'ParsimonyAssessment',
                       'LiteratureSupportAssessment',
                       'ConditionOverlapAssessment',
                       'GOSpecificityAssessment',
                       'TaxonomicScopeAssessment']} })
    supported_by: Optional[list[SupportingTextInReference]] = Field(default=None, description="""Supporting text from literature for this assessment""", json_schema_extra = { "linkml_meta": {'alias': 'supported_by',
         'domain_of': ['Review',
                       'CoreFunction',
                       'ProposedOntologyTerm',
                       'RuleReview',
                       'ParsimonyAssessment',
                       'LiteratureSupportAssessment',
                       'ConditionOverlapAssessment',
                       'GOSpecificityAssessment',
                       'TaxonomicScopeAssessment',
                       'PredictionAssessment']} })


class PredictionReview(ConfiguredBaseModel):
    """
    Review of computational/ML predictions for a gene that are NOT in the curated GOA/UniProt annotations. This captures predictions from methods like DeepECTF, PANTHER/IBA, InterPro2GO, CLEAN, GloEC, MAPred, etc. and evaluates them against literature and bioinformatic evidence. Inspired by the systematic evaluation in de Crécy-Lagard et al. 2025 (PMID:40703034).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review',
         'slot_usage': {'description': {'description': 'Summary of the prediction '
                                                       'review findings',
                                        'name': 'description',
                                        'recommended': True},
                        'id': {'description': 'UniProt accession for the gene product',
                               'name': 'id'}}})

    id: str = Field(default=..., description="""UniProt accession for the gene product""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['GeneReview',
                       'AlternativeProduct',
                       'FunctionalIsoform',
                       'Term',
                       'Reference',
                       'ComplexUnit',
                       'ModuleReview',
                       'ModuleNode',
                       'ModuleVariantSet',
                       'ModuleAnnoton',
                       'RuleReview',
                       'RuleReviewEntry',
                       'PredictionReview']} })
    gene_symbol: str = Field(default=..., description="""Symbol of the gene""", json_schema_extra = { "linkml_meta": {'alias': 'gene_symbol', 'domain_of': ['GeneReview', 'PredictionReview']} })
    taxon: Term = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'taxon',
         'domain_of': ['GeneReview', 'ParticipantSelector', 'PredictionReview']} })
    description: Optional[str] = Field(default=None, description="""Summary of the prediction review findings""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['GeneReview',
                       'AlternativeProduct',
                       'FunctionalIsoform',
                       'Term',
                       'Descriptor',
                       'ModuleReview',
                       'ModuleNode',
                       'ParticipantSelector',
                       'ModuleConnection',
                       'CoreFunction',
                       'Experiment',
                       'RuleReview',
                       'PredictionReview'],
         'recommended': True,
         'slot_uri': 'dcterms:description'} })
    references: Optional[list[Reference]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'references',
         'domain_of': ['GeneReview', 'ModuleReview', 'RuleReview', 'PredictionReview']} })
    status: Optional[GeneReviewStatusEnum] = Field(default=None, description="""Overall status of the gene review""", json_schema_extra = { "linkml_meta": {'alias': 'status',
         'domain_of': ['GeneReview',
                       'ModuleReview',
                       'KnowledgeGap',
                       'RuleReview',
                       'PredictionReview'],
         'recommended': True} })
    locus_tag: Optional[str] = Field(default=None, description="""Locus tag for the gene (e.g., b1267 for E. coli)""", json_schema_extra = { "linkml_meta": {'alias': 'locus_tag', 'domain_of': ['PredictionReview']} })
    source_documents: Optional[list[str]] = Field(default=None, description="""Paths to supporting source documents (e.g., reasoning traces, raw model outputs) for provenance""", json_schema_extra = { "linkml_meta": {'alias': 'source_documents', 'domain_of': ['PredictionReview']} })
    predictions: Optional[list[PredictedAnnotation]] = Field(default=None, description="""List of predictions to review""", json_schema_extra = { "linkml_meta": {'alias': 'predictions', 'domain_of': ['PredictionReview']} })


class PredictedAnnotation(ConfiguredBaseModel):
    """
    A single computational prediction and its review. Each prediction comes from a specific method and predicts a term (EC number, GO term, etc.) for the gene.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    source_method: str = Field(default=..., description="""Name of the prediction method (e.g., DeepECTF, PANTHER_IBA, InterPro2GO, CLEAN, GloEC, MAPred, ProteinInfer)""", json_schema_extra = { "linkml_meta": {'alias': 'source_method', 'domain_of': ['PredictedAnnotation']} })
    source_version: Optional[str] = Field(default=None, description="""Version or date of the prediction method""", json_schema_extra = { "linkml_meta": {'alias': 'source_version', 'domain_of': ['PredictedAnnotation']} })
    source_reference_id: Optional[str] = Field(default=None, description="""Reference for the prediction method or study (e.g., PMID:37820725 for the Kim et al. 2023 DeepECTF study)""", json_schema_extra = { "linkml_meta": {'alias': 'source_reference_id', 'domain_of': ['PredictedAnnotation']} })
    predicted_term: Term = Field(default=..., description="""The predicted term (GO term, EC number, etc.)""", json_schema_extra = { "linkml_meta": {'alias': 'predicted_term', 'domain_of': ['PredictedAnnotation']} })
    predicted_term_type: PredictedTermTypeEnum = Field(default=..., description="""Type of predicted term (EC, GO_MF, GO_BP, GO_CC)""", json_schema_extra = { "linkml_meta": {'alias': 'predicted_term_type', 'domain_of': ['PredictedAnnotation']} })
    review: PredictionAssessment = Field(default=..., description="""Assessment of this prediction""", json_schema_extra = { "linkml_meta": {'alias': 'review', 'domain_of': ['ExistingAnnotation', 'PredictedAnnotation']} })


class PredictionAssessment(ConfiguredBaseModel):
    """
    Assessment of a single computational prediction. Uses categories from de Crécy-Lagard et al. 2025 (PMID:40703034) plus extensions for GO predictions.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ai4curation.io/ai-gene-review'})

    assessment: PredictionAssessmentEnum = Field(default=..., description="""Assessment category for this prediction""", json_schema_extra = { "linkml_meta": {'alias': 'assessment',
         'domain_of': ['ParsimonyAssessment',
                       'LiteratureSupportAssessment',
                       'ConditionOverlapAssessment',
                       'GOSpecificityAssessment',
                       'TaxonomicScopeAssessment',
                       'PredictionAssessment']} })
    confidence_score: int = Field(default=..., description="""Confidence score following de Crécy-Lagard et al. 2025: 2 = concordant with evidence, 1 = uncertain, 0 = discordant with evidence""", ge=0, le=2, json_schema_extra = { "linkml_meta": {'alias': 'confidence_score', 'domain_of': ['PredictionAssessment']} })
    error_type: Optional[PredictionErrorTypeEnum] = Field(default=None, description="""Type of error that led to the incorrect prediction, following Table 1 of de Crécy-Lagard et al. 2025""", json_schema_extra = { "linkml_meta": {'alias': 'error_type', 'domain_of': ['PredictionAssessment']} })
    summary: str = Field(default=..., description="""Summary of the assessment rationale""", json_schema_extra = { "linkml_meta": {'alias': 'summary',
         'domain_of': ['Review', 'InterPro2GORedundancy', 'PredictionAssessment']} })
    supported_by: Optional[list[SupportingTextInReference]] = Field(default=None, description="""Supporting evidence for the assessment""", json_schema_extra = { "linkml_meta": {'alias': 'supported_by',
         'domain_of': ['Review',
                       'CoreFunction',
                       'ProposedOntologyTerm',
                       'RuleReview',
                       'ParsimonyAssessment',
                       'LiteratureSupportAssessment',
                       'ConditionOverlapAssessment',
                       'GOSpecificityAssessment',
                       'TaxonomicScopeAssessment',
                       'PredictionAssessment']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
GeneReview.model_rebuild()
AlternativeProduct.model_rebuild()
FunctionalIsoform.model_rebuild()
FunctionalIsoformMapping.model_rebuild()
Term.model_rebuild()
Reference.model_rebuild()
ReferenceReview.model_rebuild()
Finding.model_rebuild()
FindingReview.model_rebuild()
SupportingTextInReference.model_rebuild()
EvidenceItem.model_rebuild()
Descriptor.model_rebuild()
ChemicalEntityDescriptor.model_rebuild()
GeneDescriptor.model_rebuild()
GeneProductDescriptor.model_rebuild()
FamilyDescriptor.model_rebuild()
DomainDescriptor.model_rebuild()
CellularComponentDescriptor.model_rebuild()
ProteinComplexDescriptor.model_rebuild()
ComplexUnit.model_rebuild()
CellTypeDescriptor.model_rebuild()
AnatomicalEntityDescriptor.model_rebuild()
DevelopmentalStageDescriptor.model_rebuild()
TaxonDescriptor.model_rebuild()
MolecularFunctionDescriptor.model_rebuild()
BiologicalProcessDescriptor.model_rebuild()
RelationDescriptor.model_rebuild()
ModuleReview.model_rebuild()
ModuleNode.model_rebuild()
ModulePart.model_rebuild()
ModuleVariantSet.model_rebuild()
ModuleAnnoton.model_rebuild()
ParticipantSelector.model_rebuild()
ModuleContext.model_rebuild()
ModuleConnection.model_rebuild()
ExistingAnnotation.model_rebuild()
Review.model_rebuild()
CoreFunction.model_rebuild()
AnnotationExtension.model_rebuild()
TermMapping.model_rebuild()
ProposedOntologyTerm.model_rebuild()
KnowledgeGap.model_rebuild()
Experiment.model_rebuild()
Question.model_rebuild()
RuleReview.model_rebuild()
EmbeddedRule.model_rebuild()
RuleConditionSet.model_rebuild()
RuleCondition.model_rebuild()
RuleGOAnnotation.model_rebuild()
PairwiseOverlap.model_rebuild()
RuleReviewEntry.model_rebuild()
RelatedEntry.model_rebuild()
InterPro2GORedundancy.model_rebuild()
RedundantAnnotation.model_rebuild()
ParsimonyAssessment.model_rebuild()
LiteratureSupportAssessment.model_rebuild()
ConditionOverlapAssessment.model_rebuild()
GOSpecificityAssessment.model_rebuild()
TaxonomicScopeAssessment.model_rebuild()
PredictionReview.model_rebuild()
PredictedAnnotation.model_rebuild()
PredictionAssessment.model_rebuild()

