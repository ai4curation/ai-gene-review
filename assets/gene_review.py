# Auto generated from gene_review.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-09-11T21:18:31
# Schema: gene_review
#
# id: https://ai4curation.io/ai-gene-review
# description: Schema for gene curation Top level entity is a GeneReview, which is about a single gene (and its equivalent swiss-prot entry). It contains a high level summary of the gene, plus a review of all existing annotations. It also contains a list of core functions, which are GO-CAM-like annotons describing the core evolved functions of the gene.
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Float, Integer, String
from linkml_runtime.utils.metamodelcore import Bool

metamodel_version = "1.7.0"
version = None

# Namespaces
ECO = CurieNamespace('ECO', 'http://purl.obolibrary.org/obo/ECO_')
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
SO = CurieNamespace('SO', 'http://purl.obolibrary.org/obo/SO_')
DCAT = CurieNamespace('dcat', 'http://www.w3.org/ns/dcat#')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
GENE_REVIEW = CurieNamespace('gene_review', 'https://w3id.org/ai4curation/gene_review/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OA = CurieNamespace('oa', 'http://www.w3.org/ns/oa#')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = GENE_REVIEW


# Types

# Class references
class GeneReviewId(extended_str):
    pass


class AlternativeProductId(extended_str):
    pass


class FunctionalIsoformId(extended_str):
    pass


class TermId(extended_str):
    pass


class ReferenceId(extended_str):
    pass


class ModuleReviewId(extended_str):
    pass


class ModuleNodeId(extended_str):
    pass


class GoCamReviewModel(extended_str):
    pass


class RuleReviewId(extended_str):
    pass


class RuleReviewEntryId(extended_str):
    pass


class PredictionReviewId(extended_str):
    pass


@dataclass(repr=False)
class GeneReview(YAMLRoot):
    """
    Complete review for a gene
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["GeneReview"]
    class_class_curie: ClassVar[str] = "gene_review:GeneReview"
    class_name: ClassVar[str] = "GeneReview"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.GeneReview

    id: Union[str, GeneReviewId] = None
    gene_symbol: str = None
    taxon: Union[dict, "Term"] = None
    product_type: Optional[Union[str, "ProductTypeEnum"]] = None
    aliases: Optional[Union[str, list[str]]] = empty_list()
    tags: Optional[Union[str, list[str]]] = empty_list()
    status: Optional[Union[str, "GeneReviewStatusEnum"]] = None
    description: Optional[str] = None
    alternative_products: Optional[Union[dict[Union[str, AlternativeProductId], Union[dict, "AlternativeProduct"]], list[Union[dict, "AlternativeProduct"]]]] = empty_dict()
    functional_isoforms: Optional[Union[dict[Union[str, FunctionalIsoformId], Union[dict, "FunctionalIsoform"]], list[Union[dict, "FunctionalIsoform"]]]] = empty_dict()
    references: Optional[Union[dict[Union[str, ReferenceId], Union[dict, "Reference"]], list[Union[dict, "Reference"]]]] = empty_dict()
    existing_annotations: Optional[Union[Union[dict, "ExistingAnnotation"], list[Union[dict, "ExistingAnnotation"]]]] = empty_list()
    core_functions: Optional[Union[Union[dict, "CoreFunction"], list[Union[dict, "CoreFunction"]]]] = empty_list()
    proposed_new_terms: Optional[Union[Union[dict, "ProposedOntologyTerm"], list[Union[dict, "ProposedOntologyTerm"]]]] = empty_list()
    suggested_questions: Optional[Union[Union[dict, "Question"], list[Union[dict, "Question"]]]] = empty_list()
    suggested_experiments: Optional[Union[Union[dict, "Experiment"], list[Union[dict, "Experiment"]]]] = empty_list()
    knowledge_gaps: Optional[Union[Union[dict, "KnowledgeGap"], list[Union[dict, "KnowledgeGap"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneReviewId):
            self.id = GeneReviewId(self.id)

        if self._is_empty(self.gene_symbol):
            self.MissingRequiredField("gene_symbol")
        if not isinstance(self.gene_symbol, str):
            self.gene_symbol = str(self.gene_symbol)

        if self._is_empty(self.taxon):
            self.MissingRequiredField("taxon")
        if not isinstance(self.taxon, Term):
            self.taxon = Term(**as_dict(self.taxon))

        if self.product_type is not None and not isinstance(self.product_type, ProductTypeEnum):
            self.product_type = ProductTypeEnum(self.product_type)

        if not isinstance(self.aliases, list):
            self.aliases = [self.aliases] if self.aliases is not None else []
        self.aliases = [v if isinstance(v, str) else str(v) for v in self.aliases]

        if not isinstance(self.tags, list):
            self.tags = [self.tags] if self.tags is not None else []
        self.tags = [v if isinstance(v, str) else str(v) for v in self.tags]

        if self.status is not None and not isinstance(self.status, GeneReviewStatusEnum):
            self.status = GeneReviewStatusEnum(self.status)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="alternative_products", slot_type=AlternativeProduct, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="functional_isoforms", slot_type=FunctionalIsoform, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="references", slot_type=Reference, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="existing_annotations", slot_type=ExistingAnnotation, key_name="evidence_type", keyed=False)

        if not isinstance(self.core_functions, list):
            self.core_functions = [self.core_functions] if self.core_functions is not None else []
        self.core_functions = [v if isinstance(v, CoreFunction) else CoreFunction(**as_dict(v)) for v in self.core_functions]

        self._normalize_inlined_as_list(slot_name="proposed_new_terms", slot_type=ProposedOntologyTerm, key_name="proposed_name", keyed=False)

        self._normalize_inlined_as_list(slot_name="suggested_questions", slot_type=Question, key_name="question", keyed=False)

        self._normalize_inlined_as_list(slot_name="suggested_experiments", slot_type=Experiment, key_name="description", keyed=False)

        self._normalize_inlined_as_list(slot_name="knowledge_gaps", slot_type=KnowledgeGap, key_name="gap_statement", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AlternativeProduct(YAMLRoot):
    """
    An alternative splicing product (isoform) of the gene. Corresponds to UniProt isoform entries. Use this to
    document isoform-specific functions where different isoforms have distinct or even antagonistic biological
    activities. DEPRECATED: Use FunctionalIsoform instead for curated functional classes.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["AlternativeProduct"]
    class_class_curie: ClassVar[str] = "gene_review:AlternativeProduct"
    class_name: ClassVar[str] = "AlternativeProduct"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.AlternativeProduct

    id: Union[str, AlternativeProductId] = None
    name: Optional[str] = None
    sequence_note: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AlternativeProductId):
            self.id = AlternativeProductId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.sequence_note is not None and not isinstance(self.sequence_note, str):
            self.sequence_note = str(self.sequence_note)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FunctionalIsoform(YAMLRoot):
    """
    A curated functional isoform class. Unlike AlternativeProduct (which maps 1:1 to UniProt isoforms), this captures
    FUNCTIONALLY RELEVANT distinctions that may: - Group multiple UniProt isoforms into a functional class (e.g., WT1
    +KTS isoforms) - Represent cleavage products from polyproteins (e.g., POMC peptides) - Describe modification
    states or conformational variants Only create entries when there ARE functionally distinct forms worth
    documenting.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["FunctionalIsoform"]
    class_class_curie: ClassVar[str] = "gene_review:FunctionalIsoform"
    class_name: ClassVar[str] = "FunctionalIsoform"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.FunctionalIsoform

    id: Union[str, FunctionalIsoformId] = None
    name: str = None
    type: Union[str, "FunctionalIsoformTypeEnum"] = None
    description: str = None
    maps_to: Optional[Union[Union[dict, "FunctionalIsoformMapping"], list[Union[dict, "FunctionalIsoformMapping"]]]] = empty_list()
    isoform_specific_terms: Optional[Union[dict[Union[str, TermId], Union[dict, "Term"]], list[Union[dict, "Term"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FunctionalIsoformId):
            self.id = FunctionalIsoformId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, FunctionalIsoformTypeEnum):
            self.type = FunctionalIsoformTypeEnum(self.type)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="maps_to", slot_type=FunctionalIsoformMapping, key_name="type", keyed=False)

        self._normalize_inlined_as_list(slot_name="isoform_specific_terms", slot_type=Term, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FunctionalIsoformMapping(YAMLRoot):
    """
    A mapping from a functional isoform class to underlying UniProt identifiers. Allows grouping multiple UniProt
    isoforms or chains into a single functional class.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["FunctionalIsoformMapping"]
    class_class_curie: ClassVar[str] = "gene_review:FunctionalIsoformMapping"
    class_name: ClassVar[str] = "FunctionalIsoformMapping"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.FunctionalIsoformMapping

    type: Union[str, "FunctionalIsoformMappingTypeEnum"] = None
    ids: Union[str, list[str]] = None
    residues: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, FunctionalIsoformMappingTypeEnum):
            self.type = FunctionalIsoformMappingTypeEnum(self.type)

        if self._is_empty(self.ids):
            self.MissingRequiredField("ids")
        if not isinstance(self.ids, list):
            self.ids = [self.ids] if self.ids is not None else []
        self.ids = [v if isinstance(v, str) else str(v) for v in self.ids]

        if self.residues is not None and not isinstance(self.residues, str):
            self.residues = str(self.residues)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Term(YAMLRoot):
    """
    A term in a specific ontology
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["Term"]
    class_class_curie: ClassVar[str] = "gene_review:Term"
    class_name: ClassVar[str] = "Term"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.Term

    id: Union[str, TermId] = None
    label: str = None
    description: Optional[str] = None
    ontology: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TermId):
            self.id = TermId(self.id)

        if self._is_empty(self.label):
            self.MissingRequiredField("label")
        if not isinstance(self.label, str):
            self.label = str(self.label)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.ontology is not None and not isinstance(self.ontology, str):
            self.ontology = str(self.ontology)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Reference(YAMLRoot):
    """
    A reference is a published text that describes a finding or a method. References might be formal publications
    (where the ID is a PMID), or for methods, a GO_REF. Additionally, a reference to a local ad-hoc analysis or review
    can be made by using the `file:` prefix.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["Reference"]
    class_class_curie: ClassVar[str] = "gene_review:Reference"
    class_name: ClassVar[str] = "Reference"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.Reference

    id: Union[str, ReferenceId] = None
    title: str = None
    findings: Optional[Union[Union[dict, "Finding"], list[Union[dict, "Finding"]]]] = empty_list()
    is_invalid: Optional[Union[bool, Bool]] = None
    publication_type: Optional[Union[str, "PublicationTypeEnum"]] = None
    full_text_unavailable: Optional[Union[bool, Bool]] = None
    reference_review: Optional[Union[dict, "ReferenceReview"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReferenceId):
            self.id = ReferenceId(self.id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.findings, list):
            self.findings = [self.findings] if self.findings is not None else []
        self.findings = [v if isinstance(v, Finding) else Finding(**as_dict(v)) for v in self.findings]

        if self.is_invalid is not None and not isinstance(self.is_invalid, Bool):
            self.is_invalid = Bool(self.is_invalid)

        if self.publication_type is not None and not isinstance(self.publication_type, PublicationTypeEnum):
            self.publication_type = PublicationTypeEnum(self.publication_type)

        if self.full_text_unavailable is not None and not isinstance(self.full_text_unavailable, Bool):
            self.full_text_unavailable = Bool(self.full_text_unavailable)

        if self.reference_review is not None and not isinstance(self.reference_review, ReferenceReview):
            self.reference_review = ReferenceReview(**as_dict(self.reference_review))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ReferenceReview(YAMLRoot):
    """
    Manual reviewer assessment of a reference - how relevant it is to the gene's function, and whether it is correctly
    cited and scientifically sound. Distinct from the machine-fetched id/title fields; all fields are optional and
    reviewer-supplied.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["ReferenceReview"]
    class_class_curie: ClassVar[str] = "gene_review:ReferenceReview"
    class_name: ClassVar[str] = "ReferenceReview"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.ReferenceReview

    relevance: Optional[Union[str, "ReferenceRelevanceEnum"]] = None
    correctness: Optional[Union[str, "ReferenceCorrectnessEnum"]] = None
    review_notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.relevance is not None and not isinstance(self.relevance, ReferenceRelevanceEnum):
            self.relevance = ReferenceRelevanceEnum(self.relevance)

        if self.correctness is not None and not isinstance(self.correctness, ReferenceCorrectnessEnum):
            self.correctness = ReferenceCorrectnessEnum(self.correctness)

        if self.review_notes is not None and not isinstance(self.review_notes, str):
            self.review_notes = str(self.review_notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Finding(YAMLRoot):
    """
    A finding is a statement about a gene, which is supported by a reference. Similar to "comments" in uniprot
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["Finding"]
    class_class_curie: ClassVar[str] = "gene_review:Finding"
    class_name: ClassVar[str] = "Finding"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.Finding

    statement: Optional[str] = None
    supporting_text: Optional[str] = None
    full_text_unavailable: Optional[Union[bool, Bool]] = None
    reference_section_type: Optional[Union[str, "ManuscriptSection"]] = None
    finding_review: Optional[Union[dict, "FindingReview"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.statement is not None and not isinstance(self.statement, str):
            self.statement = str(self.statement)

        if self.supporting_text is not None and not isinstance(self.supporting_text, str):
            self.supporting_text = str(self.supporting_text)

        if self.full_text_unavailable is not None and not isinstance(self.full_text_unavailable, Bool):
            self.full_text_unavailable = Bool(self.full_text_unavailable)

        if self.reference_section_type is not None and not isinstance(self.reference_section_type, ManuscriptSection):
            self.reference_section_type = ManuscriptSection(self.reference_section_type)

        if self.finding_review is not None and not isinstance(self.finding_review, FindingReview):
            self.finding_review = FindingReview(**as_dict(self.finding_review))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FindingReview(YAMLRoot):
    """
    Manual reviewer assessment of a specific finding within a reference - in particular whether it remains current, is
    disputed, or has been overturned/superseded by later evidence. This is finer-grained than reference_review (which
    assesses the whole reference); a paper may contain some findings that stand and others that are overturned. All
    fields optional and reviewer-supplied.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["FindingReview"]
    class_class_curie: ClassVar[str] = "gene_review:FindingReview"
    class_name: ClassVar[str] = "FindingReview"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.FindingReview

    finding_status: Optional[Union[str, "FindingReviewStatusEnum"]] = None
    superseded_by: Optional[Union[Union[str, ReferenceId], list[Union[str, ReferenceId]]]] = empty_list()
    review_notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.finding_status is not None and not isinstance(self.finding_status, FindingReviewStatusEnum):
            self.finding_status = FindingReviewStatusEnum(self.finding_status)

        if not isinstance(self.superseded_by, list):
            self.superseded_by = [self.superseded_by] if self.superseded_by is not None else []
        self.superseded_by = [v if isinstance(v, ReferenceId) else ReferenceId(v) for v in self.superseded_by]

        if self.review_notes is not None and not isinstance(self.review_notes, str):
            self.review_notes = str(self.review_notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SupportingTextInReference(YAMLRoot):
    """
    A supporting text in a reference.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["SupportingTextInReference"]
    class_class_curie: ClassVar[str] = "gene_review:SupportingTextInReference"
    class_name: ClassVar[str] = "SupportingTextInReference"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.SupportingTextInReference

    reference_id: Union[str, ReferenceId] = None
    supporting_text: Optional[str] = None
    supporting_text_fulltext: Optional[str] = None
    full_text_unavailable: Optional[Union[bool, Bool]] = None
    reference_section_type: Optional[Union[str, "ManuscriptSection"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.reference_id):
            self.MissingRequiredField("reference_id")
        if not isinstance(self.reference_id, ReferenceId):
            self.reference_id = ReferenceId(self.reference_id)

        if self.supporting_text is not None and not isinstance(self.supporting_text, str):
            self.supporting_text = str(self.supporting_text)

        if self.supporting_text_fulltext is not None and not isinstance(self.supporting_text_fulltext, str):
            self.supporting_text_fulltext = str(self.supporting_text_fulltext)

        if self.full_text_unavailable is not None and not isinstance(self.full_text_unavailable, Bool):
            self.full_text_unavailable = Bool(self.full_text_unavailable)

        if self.reference_section_type is not None and not isinstance(self.reference_section_type, ManuscriptSection):
            self.reference_section_type = ManuscriptSection(self.reference_section_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EvidenceItem(YAMLRoot):
    """
    A lightweight citable source for module-level assertions. The source may be a PMID, DOI, database record, local
    file, pathway record, issue, or any other citable artifact. When a literature source_id (PMID/DOI) is paired with
    a supporting_text, that quote is validated verbatim (normalized substring) against the cached publication by the
    project's module supporting-text check (ai_gene_review.validation.module_validator), using the same matcher as
    gene reviews; non-literature source_ids (GO, file:, Reactome, PANTHER, ...) carry no supporting_text quote and are
    not fetched.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["EvidenceItem"]
    class_class_curie: ClassVar[str] = "gene_review:EvidenceItem"
    class_name: ClassVar[str] = "EvidenceItem"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.EvidenceItem

    source_id: str = None
    title: Optional[str] = None
    statement: Optional[str] = None
    supporting_text: Optional[str] = None
    url: Optional[str] = None
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.source_id):
            self.MissingRequiredField("source_id")
        if not isinstance(self.source_id, str):
            self.source_id = str(self.source_id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.statement is not None and not isinstance(self.statement, str):
            self.statement = str(self.statement)

        if self.supporting_text is not None and not isinstance(self.supporting_text, str):
            self.supporting_text = str(self.supporting_text)

        if self.url is not None and not isinstance(self.url, str):
            self.url = str(self.url)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Descriptor(YAMLRoot):
    """
    A human-friendly descriptor with optional ontology/database grounding. The preferred_term may be more nuanced than
    the term label, and the term may be absent when no good identifier exists yet.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["Descriptor"]
    class_class_curie: ClassVar[str] = "gene_review:Descriptor"
    class_name: ClassVar[str] = "Descriptor"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.Descriptor

    preferred_term: str = None
    description: Optional[str] = None
    term: Optional[Union[dict, Term]] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.preferred_term):
            self.MissingRequiredField("preferred_term")
        if not isinstance(self.preferred_term, str):
            self.preferred_term = str(self.preferred_term)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.term is not None and not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        self._normalize_inlined_as_list(slot_name="evidence", slot_type=EvidenceItem, key_name="source_id", keyed=False)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChemicalEntityDescriptor(Descriptor):
    """
    A descriptor for a chemical entity, metabolite, cofactor, ion, or small molecule.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["ChemicalEntityDescriptor"]
    class_class_curie: ClassVar[str] = "gene_review:ChemicalEntityDescriptor"
    class_name: ClassVar[str] = "ChemicalEntityDescriptor"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.ChemicalEntityDescriptor

    preferred_term: str = None

@dataclass(repr=False)
class GeneDescriptor(Descriptor):
    """
    A descriptor for a gene or locus.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["GeneDescriptor"]
    class_class_curie: ClassVar[str] = "gene_review:GeneDescriptor"
    class_name: ClassVar[str] = "GeneDescriptor"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.GeneDescriptor

    preferred_term: str = None

@dataclass(repr=False)
class GeneProductDescriptor(Descriptor):
    """
    A descriptor for a gene product, protein, isoform, or gene-product form.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["GeneProductDescriptor"]
    class_class_curie: ClassVar[str] = "gene_review:GeneProductDescriptor"
    class_name: ClassVar[str] = "GeneProductDescriptor"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.GeneProductDescriptor

    preferred_term: str = None

@dataclass(repr=False)
class FamilyDescriptor(Descriptor):
    """
    A descriptor for a protein family, orthogroup, or other evolutionary grouping.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["FamilyDescriptor"]
    class_class_curie: ClassVar[str] = "gene_review:FamilyDescriptor"
    class_name: ClassVar[str] = "FamilyDescriptor"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.FamilyDescriptor

    preferred_term: str = None
    family_terms: Optional[Union[dict[Union[str, TermId], Union[dict, Term]], list[Union[dict, Term]]]] = empty_dict()
    representative_members: Optional[Union[Union[dict, GeneProductDescriptor], list[Union[dict, GeneProductDescriptor]]]] = empty_list()
    ancestral_nodes: Optional[Union[Union[dict, "AncestralNodeDescriptor"], list[Union[dict, "AncestralNodeDescriptor"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="family_terms", slot_type=Term, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="representative_members", slot_type=GeneProductDescriptor, key_name="preferred_term", keyed=False)

        self._normalize_inlined_as_list(slot_name="ancestral_nodes", slot_type=AncestralNodeDescriptor, key_name="preferred_term", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AncestralNodeDescriptor(Descriptor):
    """
    A PANTHER/PAINT ancestral node (a PTN identifier, e.g. PANTHER:PTN000299444) used to ground an evolutionary
    inference about a function. Asserting an ancestral node states that the function associated with the enclosing
    annoton is inferred to have arisen at, or been present in, the last common ancestor represented by this node, and
    is therefore inferred to be retained in extant descendant proteins barring divergence, neofunctionalization, or
    loss of key residues. This is a stronger, clade-level claim than a representative member. Such nodes can be
    resolved from the IBA WITH/FROM column (GO_REF:0000033) of a representative member's GOA record rather than
    guessed.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["AncestralNodeDescriptor"]
    class_class_curie: ClassVar[str] = "gene_review:AncestralNodeDescriptor"
    class_name: ClassVar[str] = "AncestralNodeDescriptor"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.AncestralNodeDescriptor

    preferred_term: str = None

@dataclass(repr=False)
class DomainDescriptor(Descriptor):
    """
    A descriptor for a protein domain, motif, site, or architectural feature.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["DomainDescriptor"]
    class_class_curie: ClassVar[str] = "gene_review:DomainDescriptor"
    class_name: ClassVar[str] = "DomainDescriptor"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.DomainDescriptor

    preferred_term: str = None

@dataclass(repr=False)
class CellularComponentDescriptor(Descriptor):
    """
    A descriptor for a cellular component, organelle, compartment, or complex location.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["CellularComponentDescriptor"]
    class_class_curie: ClassVar[str] = "gene_review:CellularComponentDescriptor"
    class_name: ClassVar[str] = "CellularComponentDescriptor"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.CellularComponentDescriptor

    preferred_term: str = None

@dataclass(repr=False)
class ProteinComplexDescriptor(CellularComponentDescriptor):
    """
    A descriptor for a protein-containing complex or subcomplex.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["ProteinComplexDescriptor"]
    class_class_curie: ClassVar[str] = "gene_review:ProteinComplexDescriptor"
    class_name: ClassVar[str] = "ProteinComplexDescriptor"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.ProteinComplexDescriptor

    preferred_term: str = None
    active_units: Optional[Union[Union[dict, "ComplexUnit"], list[Union[dict, "ComplexUnit"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.active_units, list):
            self.active_units = [self.active_units] if self.active_units is not None else []
        self.active_units = [v if isinstance(v, ComplexUnit) else ComplexUnit(**as_dict(v)) for v in self.active_units]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ComplexUnit(YAMLRoot):
    """
    A role-bearing unit within a protein complex descriptor.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["ComplexUnit"]
    class_class_curie: ClassVar[str] = "gene_review:ComplexUnit"
    class_name: ClassVar[str] = "ComplexUnit"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.ComplexUnit

    id: Optional[str] = None
    label: Optional[str] = None
    participant: Optional[Union[dict, "ParticipantSelector"]] = None
    role: Optional[str] = None
    stoichiometry: Optional[str] = None
    function: Optional[Union[dict, "MolecularFunctionDescriptor"]] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.participant is not None and not isinstance(self.participant, ParticipantSelector):
            self.participant = ParticipantSelector(**as_dict(self.participant))

        if self.role is not None and not isinstance(self.role, str):
            self.role = str(self.role)

        if self.stoichiometry is not None and not isinstance(self.stoichiometry, str):
            self.stoichiometry = str(self.stoichiometry)

        if self.function is not None and not isinstance(self.function, MolecularFunctionDescriptor):
            self.function = MolecularFunctionDescriptor(**as_dict(self.function))

        self._normalize_inlined_as_list(slot_name="evidence", slot_type=EvidenceItem, key_name="source_id", keyed=False)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CellTypeDescriptor(Descriptor):
    """
    A descriptor for a cell type or cell state.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["CellTypeDescriptor"]
    class_class_curie: ClassVar[str] = "gene_review:CellTypeDescriptor"
    class_name: ClassVar[str] = "CellTypeDescriptor"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.CellTypeDescriptor

    preferred_term: str = None

@dataclass(repr=False)
class AnatomicalEntityDescriptor(Descriptor):
    """
    A descriptor for an anatomical entity, tissue, organismal region, or structure.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["AnatomicalEntityDescriptor"]
    class_class_curie: ClassVar[str] = "gene_review:AnatomicalEntityDescriptor"
    class_name: ClassVar[str] = "AnatomicalEntityDescriptor"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.AnatomicalEntityDescriptor

    preferred_term: str = None

@dataclass(repr=False)
class DevelopmentalStageDescriptor(Descriptor):
    """
    A descriptor for a developmental stage, life-cycle stage, or temporal window.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["DevelopmentalStageDescriptor"]
    class_class_curie: ClassVar[str] = "gene_review:DevelopmentalStageDescriptor"
    class_name: ClassVar[str] = "DevelopmentalStageDescriptor"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.DevelopmentalStageDescriptor

    preferred_term: str = None

@dataclass(repr=False)
class TaxonDescriptor(Descriptor):
    """
    A descriptor for a taxon or taxonomic scope.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["TaxonDescriptor"]
    class_class_curie: ClassVar[str] = "gene_review:TaxonDescriptor"
    class_name: ClassVar[str] = "TaxonDescriptor"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.TaxonDescriptor

    preferred_term: str = None

@dataclass(repr=False)
class MolecularFunctionDescriptor(Descriptor):
    """
    A descriptor for a molecular function. Extra slots capture common functional nuance without requiring formal
    post-composition.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["MolecularFunctionDescriptor"]
    class_class_curie: ClassVar[str] = "gene_review:MolecularFunctionDescriptor"
    class_name: ClassVar[str] = "MolecularFunctionDescriptor"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.MolecularFunctionDescriptor

    preferred_term: str = None
    substrates: Optional[Union[Union[dict, Descriptor], list[Union[dict, Descriptor]]]] = empty_list()
    products: Optional[Union[Union[dict, Descriptor], list[Union[dict, Descriptor]]]] = empty_list()
    cofactors: Optional[Union[Union[dict, Descriptor], list[Union[dict, Descriptor]]]] = empty_list()
    targets: Optional[Union[Union[dict, Descriptor], list[Union[dict, Descriptor]]]] = empty_list()
    cargo: Optional[Union[Union[dict, Descriptor], list[Union[dict, Descriptor]]]] = empty_list()
    source_location: Optional[Union[dict, CellularComponentDescriptor]] = None
    destination_location: Optional[Union[dict, CellularComponentDescriptor]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="substrates", slot_type=Descriptor, key_name="preferred_term", keyed=False)

        self._normalize_inlined_as_list(slot_name="products", slot_type=Descriptor, key_name="preferred_term", keyed=False)

        self._normalize_inlined_as_list(slot_name="cofactors", slot_type=Descriptor, key_name="preferred_term", keyed=False)

        self._normalize_inlined_as_list(slot_name="targets", slot_type=Descriptor, key_name="preferred_term", keyed=False)

        self._normalize_inlined_as_list(slot_name="cargo", slot_type=Descriptor, key_name="preferred_term", keyed=False)

        if self.source_location is not None and not isinstance(self.source_location, CellularComponentDescriptor):
            self.source_location = CellularComponentDescriptor(**as_dict(self.source_location))

        if self.destination_location is not None and not isinstance(self.destination_location, CellularComponentDescriptor):
            self.destination_location = CellularComponentDescriptor(**as_dict(self.destination_location))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BiologicalProcessDescriptor(Descriptor):
    """
    A descriptor for a biological process, pathway, reaction, or process-like module grounding.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["BiologicalProcessDescriptor"]
    class_class_curie: ClassVar[str] = "gene_review:BiologicalProcessDescriptor"
    class_name: ClassVar[str] = "BiologicalProcessDescriptor"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.BiologicalProcessDescriptor

    preferred_term: str = None
    inputs: Optional[Union[Union[dict, Descriptor], list[Union[dict, Descriptor]]]] = empty_list()
    outputs: Optional[Union[Union[dict, Descriptor], list[Union[dict, Descriptor]]]] = empty_list()
    occurs_in: Optional[Union[Union[dict, Descriptor], list[Union[dict, Descriptor]]]] = empty_list()
    starts_with: Optional[Union[dict, Descriptor]] = None
    ends_with: Optional[Union[dict, Descriptor]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="inputs", slot_type=Descriptor, key_name="preferred_term", keyed=False)

        self._normalize_inlined_as_list(slot_name="outputs", slot_type=Descriptor, key_name="preferred_term", keyed=False)

        self._normalize_inlined_as_list(slot_name="occurs_in", slot_type=Descriptor, key_name="preferred_term", keyed=False)

        if self.starts_with is not None and not isinstance(self.starts_with, Descriptor):
            self.starts_with = Descriptor(**as_dict(self.starts_with))

        if self.ends_with is not None and not isinstance(self.ends_with, Descriptor):
            self.ends_with = Descriptor(**as_dict(self.ends_with))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RelationDescriptor(Descriptor):
    """
    A descriptor for a relation or connection predicate.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["RelationDescriptor"]
    class_class_curie: ClassVar[str] = "gene_review:RelationDescriptor"
    class_name: ClassVar[str] = "RelationDescriptor"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.RelationDescriptor

    preferred_term: str = None

@dataclass(repr=False)
class ModuleReview(YAMLRoot):
    """
    Review or curation record for a recursively decomposable biological module. This can describe a pathway, organelle
    lifecycle, protein complex, molecular function, developmental process, or abstract/evolutionary functional plan.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["ModuleReview"]
    class_class_curie: ClassVar[str] = "gene_review:ModuleReview"
    class_name: ClassVar[str] = "ModuleReview"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.ModuleReview

    id: Union[str, ModuleReviewId] = None
    title: str = None
    module: Union[dict, "ModuleNode"] = None
    description: Optional[str] = None
    references: Optional[Union[dict[Union[str, ReferenceId], Union[dict, Reference]], list[Union[dict, Reference]]]] = empty_dict()
    knowledge_gaps: Optional[Union[Union[dict, "KnowledgeGap"], list[Union[dict, "KnowledgeGap"]]]] = empty_list()
    status: Optional[str] = None
    scope: Optional[Union[str, "ModuleScopeEnum"]] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ModuleReviewId):
            self.id = ModuleReviewId(self.id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.module):
            self.MissingRequiredField("module")
        if not isinstance(self.module, ModuleNode):
            self.module = ModuleNode(**as_dict(self.module))

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="references", slot_type=Reference, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="knowledge_gaps", slot_type=KnowledgeGap, key_name="gap_statement", keyed=False)

        if self.status is not None and not isinstance(self.status, str):
            self.status = str(self.status)

        if self.scope is not None and not isinstance(self.scope, ModuleScopeEnum):
            self.scope = ModuleScopeEnum(self.scope)

        self._normalize_inlined_as_list(slot_name="evidence", slot_type=EvidenceItem, key_name="source_id", keyed=False)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ModuleNode(YAMLRoot):
    """
    A node in a module. Nodes can be recursively decomposed using parts and variant_sets, and may also carry leaf
    annotons and connections.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["ModuleNode"]
    class_class_curie: ClassVar[str] = "gene_review:ModuleNode"
    class_name: ClassVar[str] = "ModuleNode"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.ModuleNode

    id: Union[str, ModuleNodeId] = None
    label: str = None
    knowledge_gaps: Optional[Union[Union[dict, "KnowledgeGap"], list[Union[dict, "KnowledgeGap"]]]] = empty_list()
    module_type: Optional[Union[str, "ModuleTypeEnum"]] = None
    description: Optional[str] = None
    concepts: Optional[Union[Union[dict, Descriptor], list[Union[dict, Descriptor]]]] = empty_list()
    context: Optional[Union[dict, "ModuleContext"]] = None
    annotons: Optional[Union[Union[dict, "ModuleAnnoton"], list[Union[dict, "ModuleAnnoton"]]]] = empty_list()
    parts: Optional[Union[Union[dict, "ModulePart"], list[Union[dict, "ModulePart"]]]] = empty_list()
    variant_sets: Optional[Union[Union[dict, "ModuleVariantSet"], list[Union[dict, "ModuleVariantSet"]]]] = empty_list()
    connections: Optional[Union[Union[dict, "ModuleConnection"], list[Union[dict, "ModuleConnection"]]]] = empty_list()
    conforms_to: Optional[Union[Union[dict, "Conformance"], list[Union[dict, "Conformance"]]]] = empty_list()
    gocam_associations: Optional[Union[Union[dict, "GoCamAssociation"], list[Union[dict, "GoCamAssociation"]]]] = empty_list()
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ModuleNodeId):
            self.id = ModuleNodeId(self.id)

        if self._is_empty(self.label):
            self.MissingRequiredField("label")
        if not isinstance(self.label, str):
            self.label = str(self.label)

        self._normalize_inlined_as_list(slot_name="knowledge_gaps", slot_type=KnowledgeGap, key_name="gap_statement", keyed=False)

        if self.module_type is not None and not isinstance(self.module_type, ModuleTypeEnum):
            self.module_type = ModuleTypeEnum(self.module_type)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="concepts", slot_type=Descriptor, key_name="preferred_term", keyed=False)

        if self.context is not None and not isinstance(self.context, ModuleContext):
            self.context = ModuleContext(**as_dict(self.context))

        self._normalize_inlined_as_list(slot_name="annotons", slot_type=ModuleAnnoton, key_name="id", keyed=False)

        if not isinstance(self.parts, list):
            self.parts = [self.parts] if self.parts is not None else []
        self.parts = [v if isinstance(v, ModulePart) else ModulePart(**as_dict(v)) for v in self.parts]

        self._normalize_inlined_as_list(slot_name="variant_sets", slot_type=ModuleVariantSet, key_name="id", keyed=False)

        self._normalize_inlined_as_list(slot_name="connections", slot_type=ModuleConnection, key_name="source", keyed=False)

        self._normalize_inlined_as_list(slot_name="conforms_to", slot_type=Conformance, key_name="template", keyed=False)

        self._normalize_inlined_as_list(slot_name="gocam_associations", slot_type=GoCamAssociation, key_name="model", keyed=False)

        self._normalize_inlined_as_list(slot_name="evidence", slot_type=EvidenceItem, key_name="source_id", keyed=False)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Conformance(YAMLRoot):
    """
    Assertion that a module node (together with its parts and connections) is an instance of a reusable template
    module or motif, optionally recording how it deviates from that template. Modeled after the dismech conforms_to
    pattern: conformance is a consistency check, not inheritance.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["Conformance"]
    class_class_curie: ClassVar[str] = "gene_review:Conformance"
    class_name: ClassVar[str] = "Conformance"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.Conformance

    template: str = None
    status: Optional[Union[str, "ConformanceStatusEnum"]] = None
    deviations: Optional[Union[str, list[str]]] = empty_list()
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.template):
            self.MissingRequiredField("template")
        if not isinstance(self.template, str):
            self.template = str(self.template)

        if self.status is not None and not isinstance(self.status, ConformanceStatusEnum):
            self.status = ConformanceStatusEnum(self.status)

        if not isinstance(self.deviations, list):
            self.deviations = [self.deviations] if self.deviations is not None else []
        self.deviations = [v if isinstance(v, str) else str(v) for v in self.deviations]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ModulePart(YAMLRoot):
    """
    A conjunctive part or step of a module node.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["ModulePart"]
    class_class_curie: ClassVar[str] = "gene_review:ModulePart"
    class_name: ClassVar[str] = "ModulePart"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.ModulePart

    node: Union[dict, ModuleNode] = None
    order: Optional[int] = None
    role: Optional[str] = None
    optional: Optional[Union[bool, Bool]] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.node):
            self.MissingRequiredField("node")
        if not isinstance(self.node, ModuleNode):
            self.node = ModuleNode(**as_dict(self.node))

        if self.order is not None and not isinstance(self.order, int):
            self.order = int(self.order)

        if self.role is not None and not isinstance(self.role, str):
            self.role = str(self.role)

        if self.optional is not None and not isinstance(self.optional, Bool):
            self.optional = Bool(self.optional)

        self._normalize_inlined_as_list(slot_name="evidence", slot_type=EvidenceItem, key_name="source_id", keyed=False)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ModuleVariantSet(YAMLRoot):
    """
    A set of alternative implementations for a module node or part. Variants may themselves contain parts, annotons,
    connections, and nested variant sets.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["ModuleVariantSet"]
    class_class_curie: ClassVar[str] = "gene_review:ModuleVariantSet"
    class_name: ClassVar[str] = "ModuleVariantSet"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.ModuleVariantSet

    id: str = None
    variants: Union[dict[Union[str, ModuleNodeId], Union[dict, ModuleNode]], list[Union[dict, ModuleNode]]] = empty_dict()
    label: Optional[str] = None
    axis: Optional[str] = None
    selection: Optional[Union[str, "VariantSelectionEnum"]] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.variants):
            self.MissingRequiredField("variants")
        self._normalize_inlined_as_list(slot_name="variants", slot_type=ModuleNode, key_name="id", keyed=True)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.axis is not None and not isinstance(self.axis, str):
            self.axis = str(self.axis)

        if self.selection is not None and not isinstance(self.selection, VariantSelectionEnum):
            self.selection = VariantSelectionEnum(self.selection)

        self._normalize_inlined_as_list(slot_name="evidence", slot_type=EvidenceItem, key_name="source_id", keyed=False)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ModuleAnnoton(YAMLRoot):
    """
    A leaf role assertion in a module. The participant may be a concrete gene or an abstract selector, and the
    function/process/location fields are descriptor holders rather than direct GO annotation exports.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["ModuleAnnoton"]
    class_class_curie: ClassVar[str] = "gene_review:ModuleAnnoton"
    class_name: ClassVar[str] = "ModuleAnnoton"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.ModuleAnnoton

    id: str = None
    label: Optional[str] = None
    participant: Optional[Union[dict, "ParticipantSelector"]] = None
    function: Optional[Union[dict, MolecularFunctionDescriptor]] = None
    processes: Optional[Union[Union[dict, BiologicalProcessDescriptor], list[Union[dict, BiologicalProcessDescriptor]]]] = empty_list()
    locations: Optional[Union[Union[dict, CellularComponentDescriptor], list[Union[dict, CellularComponentDescriptor]]]] = empty_list()
    role_description: Optional[str] = None
    gocam_associations: Optional[Union[Union[dict, "GoCamAssociation"], list[Union[dict, "GoCamAssociation"]]]] = empty_list()
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.participant is not None and not isinstance(self.participant, ParticipantSelector):
            self.participant = ParticipantSelector(**as_dict(self.participant))

        if self.function is not None and not isinstance(self.function, MolecularFunctionDescriptor):
            self.function = MolecularFunctionDescriptor(**as_dict(self.function))

        self._normalize_inlined_as_list(slot_name="processes", slot_type=BiologicalProcessDescriptor, key_name="preferred_term", keyed=False)

        self._normalize_inlined_as_list(slot_name="locations", slot_type=CellularComponentDescriptor, key_name="preferred_term", keyed=False)

        if self.role_description is not None and not isinstance(self.role_description, str):
            self.role_description = str(self.role_description)

        self._normalize_inlined_as_list(slot_name="gocam_associations", slot_type=GoCamAssociation, key_name="model", keyed=False)

        self._normalize_inlined_as_list(slot_name="evidence", slot_type=EvidenceItem, key_name="source_id", keyed=False)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GoCamAssociation(YAMLRoot):
    """
    A reference from a module element to a production GO-CAM (Gene Ontology Causal Activity Model), optionally pinned
    to a specific activity (annoton) within that model. The referenced model is expected to be cached under
    gocams/<model_id>/<model_id>-src.yaml.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["GoCamAssociation"]
    class_class_curie: ClassVar[str] = "gene_review:GoCamAssociation"
    class_name: ClassVar[str] = "GoCamAssociation"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.GoCamAssociation

    model: str = None
    activity: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.model):
            self.MissingRequiredField("model")
        if not isinstance(self.model, str):
            self.model = str(self.model)

        if self.activity is not None and not isinstance(self.activity, str):
            self.activity = str(self.activity)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="evidence", slot_type=EvidenceItem, key_name="source_id", keyed=False)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GoCamReview(YAMLRoot):
    """
    A reviewer's assessment of a cached production GO-CAM model (gocams/<model_id>/<model_id>-src.yaml), recorded
    alongside it as gocams/<model_id>/<model_id>-review.yaml. Captures a standalone reading of the model, per-activity
    (annoton) QC against GO-CAM best practice, and the consistency of each activity with the corresponding gene
    annotation review. Validate standalone with `-C GoCamReview`.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["GoCamReview"]
    class_class_curie: ClassVar[str] = "gene_review:GoCamReview"
    class_name: ClassVar[str] = "GoCamReview"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.GoCamReview

    model: Union[str, GoCamReviewModel] = None
    title: str = None
    description: Optional[str] = None
    references: Optional[Union[dict[Union[str, ReferenceId], Union[dict, Reference]], list[Union[dict, Reference]]]] = empty_dict()
    taxon: Optional[str] = None
    summary: Optional[str] = None
    status: Optional[Union[str, "GoCamReviewStatusEnum"]] = None
    activity_reviews: Optional[Union[Union[dict, "GoCamActivityReview"], list[Union[dict, "GoCamActivityReview"]]]] = empty_list()
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.model):
            self.MissingRequiredField("model")
        if not isinstance(self.model, GoCamReviewModel):
            self.model = GoCamReviewModel(self.model)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="references", slot_type=Reference, key_name="id", keyed=True)

        if self.taxon is not None and not isinstance(self.taxon, str):
            self.taxon = str(self.taxon)

        if self.summary is not None and not isinstance(self.summary, str):
            self.summary = str(self.summary)

        if self.status is not None and not isinstance(self.status, GoCamReviewStatusEnum):
            self.status = GoCamReviewStatusEnum(self.status)

        self._normalize_inlined_as_list(slot_name="activity_reviews", slot_type=GoCamActivityReview, key_name="activity_id", keyed=False)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GoCamActivityReview(YAMLRoot):
    """
    Review of a single GO-CAM activity (annoton): the cached gene product / molecular function / process / location, a
    best-practice QC verdict, and how the activity relates to the gene's annotation review.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["GoCamActivityReview"]
    class_class_curie: ClassVar[str] = "gene_review:GoCamActivityReview"
    class_name: ClassVar[str] = "GoCamActivityReview"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.GoCamActivityReview

    activity_id: str = None
    gene_product: Optional[str] = None
    molecular_function: Optional[str] = None
    biological_process: Optional[str] = None
    cellular_component: Optional[str] = None
    verdict: Optional[Union[str, "GoCamClaimVerdictEnum"]] = None
    qc_flags: Optional[Union[Union[str, "GoCamQcFlagEnum"], list[Union[str, "GoCamQcFlagEnum"]]]] = empty_list()
    consistency: Optional[Union[str, "GoCamConsistencyEnum"]] = None
    gene_review: Optional[str] = None
    supporting_text: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.activity_id):
            self.MissingRequiredField("activity_id")
        if not isinstance(self.activity_id, str):
            self.activity_id = str(self.activity_id)

        if self.gene_product is not None and not isinstance(self.gene_product, str):
            self.gene_product = str(self.gene_product)

        if self.molecular_function is not None and not isinstance(self.molecular_function, str):
            self.molecular_function = str(self.molecular_function)

        if self.biological_process is not None and not isinstance(self.biological_process, str):
            self.biological_process = str(self.biological_process)

        if self.cellular_component is not None and not isinstance(self.cellular_component, str):
            self.cellular_component = str(self.cellular_component)

        if self.verdict is not None and not isinstance(self.verdict, GoCamClaimVerdictEnum):
            self.verdict = GoCamClaimVerdictEnum(self.verdict)

        if not isinstance(self.qc_flags, list):
            self.qc_flags = [self.qc_flags] if self.qc_flags is not None else []
        self.qc_flags = [v if isinstance(v, GoCamQcFlagEnum) else GoCamQcFlagEnum(v) for v in self.qc_flags]

        if self.consistency is not None and not isinstance(self.consistency, GoCamConsistencyEnum):
            self.consistency = GoCamConsistencyEnum(self.consistency)

        if self.gene_review is not None and not isinstance(self.gene_review, str):
            self.gene_review = str(self.gene_review)

        if self.supporting_text is not None and not isinstance(self.supporting_text, str):
            self.supporting_text = str(self.supporting_text)

        self._normalize_inlined_as_list(slot_name="evidence", slot_type=EvidenceItem, key_name="source_id", keyed=False)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ParticipantSelector(YAMLRoot):
    """
    A selector for a concrete or abstract participant in a module annoton. This can ground to a gene, gene product,
    complex, family, domain, ortholog, homolog, or any entity satisfying a functional/domain constraint.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["ParticipantSelector"]
    class_class_curie: ClassVar[str] = "gene_review:ParticipantSelector"
    class_name: ClassVar[str] = "ParticipantSelector"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.ParticipantSelector

    selector_type: Union[str, "ParticipantSelectorTypeEnum"] = None
    gene: Optional[Union[dict, GeneDescriptor]] = None
    gene_product: Optional[Union[dict, GeneProductDescriptor]] = None
    protein_complex: Optional[Union[dict, ProteinComplexDescriptor]] = None
    family: Optional[Union[dict, FamilyDescriptor]] = None
    domain: Optional[Union[dict, DomainDescriptor]] = None
    homolog_of: Optional[Union[dict, GeneDescriptor]] = None
    ortholog_of: Optional[Union[dict, GeneDescriptor]] = None
    required_function: Optional[Union[dict, MolecularFunctionDescriptor]] = None
    required_domain: Optional[Union[dict, DomainDescriptor]] = None
    taxon: Optional[Union[dict, TaxonDescriptor]] = None
    description: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.selector_type):
            self.MissingRequiredField("selector_type")
        if not isinstance(self.selector_type, ParticipantSelectorTypeEnum):
            self.selector_type = ParticipantSelectorTypeEnum(self.selector_type)

        if self.gene is not None and not isinstance(self.gene, GeneDescriptor):
            self.gene = GeneDescriptor(**as_dict(self.gene))

        if self.gene_product is not None and not isinstance(self.gene_product, GeneProductDescriptor):
            self.gene_product = GeneProductDescriptor(**as_dict(self.gene_product))

        if self.protein_complex is not None and not isinstance(self.protein_complex, ProteinComplexDescriptor):
            self.protein_complex = ProteinComplexDescriptor(**as_dict(self.protein_complex))

        if self.family is not None and not isinstance(self.family, FamilyDescriptor):
            self.family = FamilyDescriptor(**as_dict(self.family))

        if self.domain is not None and not isinstance(self.domain, DomainDescriptor):
            self.domain = DomainDescriptor(**as_dict(self.domain))

        if self.homolog_of is not None and not isinstance(self.homolog_of, GeneDescriptor):
            self.homolog_of = GeneDescriptor(**as_dict(self.homolog_of))

        if self.ortholog_of is not None and not isinstance(self.ortholog_of, GeneDescriptor):
            self.ortholog_of = GeneDescriptor(**as_dict(self.ortholog_of))

        if self.required_function is not None and not isinstance(self.required_function, MolecularFunctionDescriptor):
            self.required_function = MolecularFunctionDescriptor(**as_dict(self.required_function))

        if self.required_domain is not None and not isinstance(self.required_domain, DomainDescriptor):
            self.required_domain = DomainDescriptor(**as_dict(self.required_domain))

        if self.taxon is not None and not isinstance(self.taxon, TaxonDescriptor):
            self.taxon = TaxonDescriptor(**as_dict(self.taxon))

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="evidence", slot_type=EvidenceItem, key_name="source_id", keyed=False)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ModuleContext(YAMLRoot):
    """
    Context that applies to a module node, variant, annoton, or connection.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["ModuleContext"]
    class_class_curie: ClassVar[str] = "gene_review:ModuleContext"
    class_name: ClassVar[str] = "ModuleContext"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.ModuleContext

    taxa: Optional[Union[Union[dict, TaxonDescriptor], list[Union[dict, TaxonDescriptor]]]] = empty_list()
    cell_types: Optional[Union[Union[dict, CellTypeDescriptor], list[Union[dict, CellTypeDescriptor]]]] = empty_list()
    anatomical_locations: Optional[Union[Union[dict, AnatomicalEntityDescriptor], list[Union[dict, AnatomicalEntityDescriptor]]]] = empty_list()
    developmental_stages: Optional[Union[Union[dict, DevelopmentalStageDescriptor], list[Union[dict, DevelopmentalStageDescriptor]]]] = empty_list()
    cellular_components: Optional[Union[Union[dict, CellularComponentDescriptor], list[Union[dict, CellularComponentDescriptor]]]] = empty_list()
    conditions: Optional[Union[Union[dict, Descriptor], list[Union[dict, Descriptor]]]] = empty_list()
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="taxa", slot_type=TaxonDescriptor, key_name="preferred_term", keyed=False)

        self._normalize_inlined_as_list(slot_name="cell_types", slot_type=CellTypeDescriptor, key_name="preferred_term", keyed=False)

        self._normalize_inlined_as_list(slot_name="anatomical_locations", slot_type=AnatomicalEntityDescriptor, key_name="preferred_term", keyed=False)

        self._normalize_inlined_as_list(slot_name="developmental_stages", slot_type=DevelopmentalStageDescriptor, key_name="preferred_term", keyed=False)

        self._normalize_inlined_as_list(slot_name="cellular_components", slot_type=CellularComponentDescriptor, key_name="preferred_term", keyed=False)

        self._normalize_inlined_as_list(slot_name="conditions", slot_type=Descriptor, key_name="preferred_term", keyed=False)

        self._normalize_inlined_as_list(slot_name="evidence", slot_type=EvidenceItem, key_name="source_id", keyed=False)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ModuleConnection(YAMLRoot):
    """
    A connection between module nodes, annotons, or other named elements. Source and target are IDs scoped to the
    module document.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["ModuleConnection"]
    class_class_curie: ClassVar[str] = "gene_review:ModuleConnection"
    class_name: ClassVar[str] = "ModuleConnection"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.ModuleConnection

    source: str = None
    target: str = None
    connection_type: Optional[Union[str, "ModuleConnectionTypeEnum"]] = None
    predicate: Optional[Union[dict, RelationDescriptor]] = None
    description: Optional[str] = None
    context: Optional[Union[dict, ModuleContext]] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = empty_list()
    chaining_status: Optional[Union[str, "ChainingStatusEnum"]] = None
    chaining_note: Optional[str] = None
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, str):
            self.source = str(self.source)

        if self._is_empty(self.target):
            self.MissingRequiredField("target")
        if not isinstance(self.target, str):
            self.target = str(self.target)

        if self.connection_type is not None and not isinstance(self.connection_type, ModuleConnectionTypeEnum):
            self.connection_type = ModuleConnectionTypeEnum(self.connection_type)

        if self.predicate is not None and not isinstance(self.predicate, RelationDescriptor):
            self.predicate = RelationDescriptor(**as_dict(self.predicate))

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.context is not None and not isinstance(self.context, ModuleContext):
            self.context = ModuleContext(**as_dict(self.context))

        self._normalize_inlined_as_list(slot_name="evidence", slot_type=EvidenceItem, key_name="source_id", keyed=False)

        if self.chaining_status is not None and not isinstance(self.chaining_status, ChainingStatusEnum):
            self.chaining_status = ChainingStatusEnum(self.chaining_status)

        if self.chaining_note is not None and not isinstance(self.chaining_note, str):
            self.chaining_note = str(self.chaining_note)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExistingAnnotation(YAMLRoot):
    """
    An existing annotation from the GO database, plus a review of the annotation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["ExistingAnnotation"]
    class_class_curie: ClassVar[str] = "gene_review:ExistingAnnotation"
    class_name: ClassVar[str] = "ExistingAnnotation"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.ExistingAnnotation

    evidence_type: Union[str, "EvidenceType"] = None
    term: Optional[Union[dict, Term]] = None
    qualifier: Optional[Union[str, "AnnotationQualifierEnum"]] = None
    extensions: Optional[Union[Union[dict, "AnnotationExtension"], list[Union[dict, "AnnotationExtension"]]]] = empty_list()
    negated: Optional[Union[bool, Bool]] = None
    original_reference_id: Optional[Union[str, ReferenceId]] = None
    retired: Optional[Union[bool, Bool]] = None
    isoform: Optional[str] = None
    supporting_entities: Optional[Union[str, list[str]]] = empty_list()
    review: Optional[Union[dict, "Review"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.evidence_type):
            self.MissingRequiredField("evidence_type")
        if not isinstance(self.evidence_type, EvidenceType):
            self.evidence_type = EvidenceType(self.evidence_type)

        if self.term is not None and not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        if self.qualifier is not None and not isinstance(self.qualifier, AnnotationQualifierEnum):
            self.qualifier = AnnotationQualifierEnum(self.qualifier)

        self._normalize_inlined_as_list(slot_name="extensions", slot_type=AnnotationExtension, key_name="predicate", keyed=False)

        if self.negated is not None and not isinstance(self.negated, Bool):
            self.negated = Bool(self.negated)

        if self.original_reference_id is not None and not isinstance(self.original_reference_id, ReferenceId):
            self.original_reference_id = ReferenceId(self.original_reference_id)

        if self.retired is not None and not isinstance(self.retired, Bool):
            self.retired = Bool(self.retired)

        if self.isoform is not None and not isinstance(self.isoform, str):
            self.isoform = str(self.isoform)

        if not isinstance(self.supporting_entities, list):
            self.supporting_entities = [self.supporting_entities] if self.supporting_entities is not None else []
        self.supporting_entities = [v if isinstance(v, str) else str(v) for v in self.supporting_entities]

        if self.review is not None and not isinstance(self.review, Review):
            self.review = Review(**as_dict(self.review))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Review(YAMLRoot):
    """
    A review of an existing annotation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["Review"]
    class_class_curie: ClassVar[str] = "gene_review:Review"
    class_name: ClassVar[str] = "Review"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.Review

    action: Union[str, "ActionEnum"] = None
    summary: Optional[str] = None
    reason: Optional[str] = None
    proposed_replacement_terms: Optional[Union[dict[Union[str, TermId], Union[dict, Term]], list[Union[dict, Term]]]] = empty_dict()
    additional_reference_ids: Optional[Union[Union[str, ReferenceId], list[Union[str, ReferenceId]]]] = empty_list()
    supported_by: Optional[Union[Union[dict, SupportingTextInReference], list[Union[dict, SupportingTextInReference]]]] = empty_list()
    knowledge_gaps: Optional[Union[Union[dict, "KnowledgeGap"], list[Union[dict, "KnowledgeGap"]]]] = empty_list()
    propagation_review: Optional[Union[dict, "PropagationReview"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.action):
            self.MissingRequiredField("action")
        if not isinstance(self.action, ActionEnum):
            self.action = ActionEnum(self.action)

        if self.summary is not None and not isinstance(self.summary, str):
            self.summary = str(self.summary)

        if self.reason is not None and not isinstance(self.reason, str):
            self.reason = str(self.reason)

        self._normalize_inlined_as_list(slot_name="proposed_replacement_terms", slot_type=Term, key_name="id", keyed=True)

        if not isinstance(self.additional_reference_ids, list):
            self.additional_reference_ids = [self.additional_reference_ids] if self.additional_reference_ids is not None else []
        self.additional_reference_ids = [v if isinstance(v, ReferenceId) else ReferenceId(v) for v in self.additional_reference_ids]

        if not isinstance(self.supported_by, list):
            self.supported_by = [self.supported_by] if self.supported_by is not None else []
        self.supported_by = [v if isinstance(v, SupportingTextInReference) else SupportingTextInReference(**as_dict(v)) for v in self.supported_by]

        self._normalize_inlined_as_list(slot_name="knowledge_gaps", slot_type=KnowledgeGap, key_name="gap_statement", keyed=False)

        if self.propagation_review is not None and not isinstance(self.propagation_review, PropagationReview):
            self.propagation_review = PropagationReview(**as_dict(self.propagation_review))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PropagationReview(YAMLRoot):
    """
    Structured, mechanical assessment of a propagated or inferred annotation. The detailed biological rationale
    remains in review.reason; this object records the reusable taxonomy and optional per-source-gene/node comments.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["PropagationReview"]
    class_class_curie: ClassVar[str] = "gene_review:PropagationReview"
    class_name: ClassVar[str] = "PropagationReview"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.PropagationReview

    root_cause: Union[str, "PropagationRootCauseEnum"] = None
    failure_modes: Optional[Union[Union[str, "PropagationFailureModeEnum"], list[Union[str, "PropagationFailureModeEnum"]]]] = empty_list()
    source_entities: Optional[Union[Union[dict, "PropagationSource"], list[Union[dict, "PropagationSource"]]]] = empty_list()
    residue_claims: Optional[Union[Union[dict, "ResidueClaim"], list[Union[dict, "ResidueClaim"]]]] = empty_list()
    residue_claims_not_applicable: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.root_cause):
            self.MissingRequiredField("root_cause")
        if not isinstance(self.root_cause, PropagationRootCauseEnum):
            self.root_cause = PropagationRootCauseEnum(self.root_cause)

        if not isinstance(self.failure_modes, list):
            self.failure_modes = [self.failure_modes] if self.failure_modes is not None else []
        self.failure_modes = [v if isinstance(v, PropagationFailureModeEnum) else PropagationFailureModeEnum(v) for v in self.failure_modes]

        self._normalize_inlined_as_list(slot_name="source_entities", slot_type=PropagationSource, key_name="source_id", keyed=False)

        self._normalize_inlined_as_list(slot_name="residue_claims", slot_type=ResidueClaim, key_name="claim_type", keyed=False)

        if self.residue_claims_not_applicable is not None and not isinstance(self.residue_claims_not_applicable, str):
            self.residue_claims_not_applicable = str(self.residue_claims_not_applicable)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ResidueClaim(YAMLRoot):
    """
    A claim that a specific position in THIS gene's protein does or does not carry the residue an anchor protein has
    at the corresponding position.
    Both sides carry an explicit position and residue, which is what makes the claim checkable without an alignment:
    the anchor and target residues are each resolved directly against their own sequences. The alignment is only
    needed to confirm the two positions genuinely correspond, so a claim remains partially verifiable even when no
    alignment is pinned.
    Positions are always in each protein's own native numbering, never an alignment column -- columns shift when
    PANTHER re-releases a family, and a stale column still resolves, to the wrong residue.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["ResidueClaim"]
    class_class_curie: ClassVar[str] = "gene_review:ResidueClaim"
    class_name: ClassVar[str] = "ResidueClaim"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.ResidueClaim

    claim_type: Union[str, "ResidueClaimEnum"] = None
    anchor: Union[dict, "ResiduePosition"] = None
    method: Union[str, "ResidueClaimMethodEnum"] = None
    site_ref: Optional[str] = None
    target: Optional[Union[dict, "ResiduePosition"]] = None
    role: Optional[str] = None
    alignment_release: Optional[str] = None
    comment: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.claim_type):
            self.MissingRequiredField("claim_type")
        if not isinstance(self.claim_type, ResidueClaimEnum):
            self.claim_type = ResidueClaimEnum(self.claim_type)

        if self._is_empty(self.anchor):
            self.MissingRequiredField("anchor")
        if not isinstance(self.anchor, ResiduePosition):
            self.anchor = ResiduePosition(**as_dict(self.anchor))

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, ResidueClaimMethodEnum):
            self.method = ResidueClaimMethodEnum(self.method)

        if self.site_ref is not None and not isinstance(self.site_ref, str):
            self.site_ref = str(self.site_ref)

        if self.target is not None and not isinstance(self.target, ResiduePosition):
            self.target = ResiduePosition(**as_dict(self.target))

        if self.role is not None and not isinstance(self.role, str):
            self.role = str(self.role)

        if self.alignment_release is not None and not isinstance(self.alignment_release, str):
            self.alignment_release = str(self.alignment_release)

        if self.comment is not None and not isinstance(self.comment, str):
            self.comment = str(self.comment)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ResiduePosition(YAMLRoot):
    """
    A single residue in a named protein, in that protein's own numbering.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["ResiduePosition"]
    class_class_curie: ClassVar[str] = "gene_review:ResiduePosition"
    class_name: ClassVar[str] = "ResiduePosition"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.ResiduePosition

    accession: str = None
    position: int = None
    residue: str = None
    sequence_version: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.accession):
            self.MissingRequiredField("accession")
        if not isinstance(self.accession, str):
            self.accession = str(self.accession)

        if self._is_empty(self.position):
            self.MissingRequiredField("position")
        if not isinstance(self.position, int):
            self.position = int(self.position)

        if self._is_empty(self.residue):
            self.MissingRequiredField("residue")
        if not isinstance(self.residue, str):
            self.residue = str(self.residue)

        if self.sequence_version is not None and not isinstance(self.sequence_version, int):
            self.sequence_version = int(self.sequence_version)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PropagationSource(YAMLRoot):
    """
    A source entity considered while reviewing an inferred annotation. This is intentionally compact: use comment for
    source-specific caveats, not for restating the whole review rationale.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["PropagationSource"]
    class_class_curie: ClassVar[str] = "gene_review:PropagationSource"
    class_name: ClassVar[str] = "PropagationSource"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.PropagationSource

    source_id: str = None
    source_label: Optional[str] = None
    source_status: Optional[Union[str, "PropagationSourceStatusEnum"]] = None
    comment: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.source_id):
            self.MissingRequiredField("source_id")
        if not isinstance(self.source_id, str):
            self.source_id = str(self.source_id)

        if self.source_label is not None and not isinstance(self.source_label, str):
            self.source_label = str(self.source_label)

        if self.source_status is not None and not isinstance(self.source_status, PropagationSourceStatusEnum):
            self.source_status = PropagationSourceStatusEnum(self.source_status)

        if self.comment is not None and not isinstance(self.comment, str):
            self.comment = str(self.comment)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CoreFunction(YAMLRoot):
    """
    A core function is a GO-CAM-like annotation of the core evolved functions of a gene. This is a synthesis of the
    reviewed core annotations, brought together into a unified GO-CAM-like representation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["CoreFunction"]
    class_class_curie: ClassVar[str] = "gene_review:CoreFunction"
    class_name: ClassVar[str] = "CoreFunction"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.CoreFunction

    knowledge_gaps: Optional[Union[Union[dict, "KnowledgeGap"], list[Union[dict, "KnowledgeGap"]]]] = empty_list()
    description: Optional[str] = None
    supported_by: Optional[Union[Union[dict, SupportingTextInReference], list[Union[dict, SupportingTextInReference]]]] = empty_list()
    molecular_function: Optional[Union[dict, Term]] = None
    contributes_to_molecular_function: Optional[Union[dict, Term]] = None
    directly_involved_in: Optional[Union[dict[Union[str, TermId], Union[dict, Term]], list[Union[dict, Term]]]] = empty_dict()
    locations: Optional[Union[dict[Union[str, TermId], Union[dict, Term]], list[Union[dict, Term]]]] = empty_dict()
    anatomical_locations: Optional[Union[dict[Union[str, TermId], Union[dict, Term]], list[Union[dict, Term]]]] = empty_dict()
    substrates: Optional[Union[dict[Union[str, TermId], Union[dict, Term]], list[Union[dict, Term]]]] = empty_dict()
    in_complex: Optional[Union[dict, Term]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="knowledge_gaps", slot_type=KnowledgeGap, key_name="gap_statement", keyed=False)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.supported_by, list):
            self.supported_by = [self.supported_by] if self.supported_by is not None else []
        self.supported_by = [v if isinstance(v, SupportingTextInReference) else SupportingTextInReference(**as_dict(v)) for v in self.supported_by]

        if self.molecular_function is not None and not isinstance(self.molecular_function, Term):
            self.molecular_function = Term(**as_dict(self.molecular_function))

        if self.contributes_to_molecular_function is not None and not isinstance(self.contributes_to_molecular_function, Term):
            self.contributes_to_molecular_function = Term(**as_dict(self.contributes_to_molecular_function))

        self._normalize_inlined_as_list(slot_name="directly_involved_in", slot_type=Term, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="locations", slot_type=Term, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="anatomical_locations", slot_type=Term, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="substrates", slot_type=Term, key_name="id", keyed=True)

        if self.in_complex is not None and not isinstance(self.in_complex, Term):
            self.in_complex = Term(**as_dict(self.in_complex))

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AnnotationExtension(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["AnnotationExtension"]
    class_class_curie: ClassVar[str] = "gene_review:AnnotationExtension"
    class_name: ClassVar[str] = "AnnotationExtension"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.AnnotationExtension

    predicate: str = None
    term: Optional[Union[dict, Term]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, str):
            self.predicate = str(self.predicate)

        if self.term is not None and not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TermMapping(YAMLRoot):
    """
    A mapping between the proposed term and an equivalent term in another ontology
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["TermMapping"]
    class_class_curie: ClassVar[str] = "gene_review:TermMapping"
    class_name: ClassVar[str] = "TermMapping"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.TermMapping

    predicate: str = None
    target_term: Union[dict, Term] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, str):
            self.predicate = str(self.predicate)

        if self._is_empty(self.target_term):
            self.MissingRequiredField("target_term")
        if not isinstance(self.target_term, Term):
            self.target_term = Term(**as_dict(self.target_term))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProposedOntologyTerm(YAMLRoot):
    """
    A proposed new ontology term that should exist but doesn't currently
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["ProposedOntologyTerm"]
    class_class_curie: ClassVar[str] = "gene_review:ProposedOntologyTerm"
    class_name: ClassVar[str] = "ProposedOntologyTerm"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.ProposedOntologyTerm

    proposed_name: str = None
    proposed_definition: str = None
    justification: Optional[str] = None
    proposed_parent: Optional[Union[dict, Term]] = None
    proposed_mappings: Optional[Union[Union[dict, TermMapping], list[Union[dict, TermMapping]]]] = empty_list()
    supported_by: Optional[Union[Union[dict, SupportingTextInReference], list[Union[dict, SupportingTextInReference]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.proposed_name):
            self.MissingRequiredField("proposed_name")
        if not isinstance(self.proposed_name, str):
            self.proposed_name = str(self.proposed_name)

        if self._is_empty(self.proposed_definition):
            self.MissingRequiredField("proposed_definition")
        if not isinstance(self.proposed_definition, str):
            self.proposed_definition = str(self.proposed_definition)

        if self.justification is not None and not isinstance(self.justification, str):
            self.justification = str(self.justification)

        if self.proposed_parent is not None and not isinstance(self.proposed_parent, Term):
            self.proposed_parent = Term(**as_dict(self.proposed_parent))

        self._normalize_inlined_as_list(slot_name="proposed_mappings", slot_type=TermMapping, key_name="predicate", keyed=False)

        if not isinstance(self.supported_by, list):
            self.supported_by = [self.supported_by] if self.supported_by is not None else []
        self.supported_by = [v if isinstance(v, SupportingTextInReference) else SupportingTextInReference(**as_dict(v)) for v in self.supported_by]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class KnowledgeGap(YAMLRoot):
    """
    A curated, literature-grounded statement of what is NOT known about a gene product, core function, module, or step
    — its molecular activity, mechanism, partner(s), localization, or biological role. A knowledge gap is a reviewer
    judgment reached by reading the primary literature, NOT a pattern in the annotations: a heavily annotated gene can
    hide a gaping mechanistic hole, and a sparsely annotated one can be perfectly understood and merely under-curated.
    Each gap is a small, defensible scholarly object with the same evidentiary discipline used for positive claims.
    See projects/FUNCTION_KNOWLEDGE_GAPS.md for the methodology and worked exemplars.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["KnowledgeGap"]
    class_class_curie: ClassVar[str] = "gene_review:KnowledgeGap"
    class_name: ClassVar[str] = "KnowledgeGap"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.KnowledgeGap

    gap_statement: str = None
    boundary: Optional[str] = None
    gap_kind: Optional[Union[Union[str, "KnowledgeGapKindEnum"], list[Union[str, "KnowledgeGapKindEnum"]]]] = empty_list()
    dark_aspect: Optional[Union[str, "KnowledgeGapAspectEnum"]] = None
    status: Optional[Union[str, "KnowledgeGapStatusEnum"]] = None
    significance: Optional[str] = None
    resolution: Optional[str] = None
    provenance: Optional[Union[Union[dict, SupportingTextInReference], list[Union[dict, SupportingTextInReference]]]] = empty_list()
    proposed_terms: Optional[Union[Union[dict, ProposedOntologyTerm], list[Union[dict, ProposedOntologyTerm]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.gap_statement):
            self.MissingRequiredField("gap_statement")
        if not isinstance(self.gap_statement, str):
            self.gap_statement = str(self.gap_statement)

        if self.boundary is not None and not isinstance(self.boundary, str):
            self.boundary = str(self.boundary)

        if not isinstance(self.gap_kind, list):
            self.gap_kind = [self.gap_kind] if self.gap_kind is not None else []
        self.gap_kind = [v if isinstance(v, KnowledgeGapKindEnum) else KnowledgeGapKindEnum(v) for v in self.gap_kind]

        if self.dark_aspect is not None and not isinstance(self.dark_aspect, KnowledgeGapAspectEnum):
            self.dark_aspect = KnowledgeGapAspectEnum(self.dark_aspect)

        if self.status is not None and not isinstance(self.status, KnowledgeGapStatusEnum):
            self.status = KnowledgeGapStatusEnum(self.status)

        if self.significance is not None and not isinstance(self.significance, str):
            self.significance = str(self.significance)

        if self.resolution is not None and not isinstance(self.resolution, str):
            self.resolution = str(self.resolution)

        if not isinstance(self.provenance, list):
            self.provenance = [self.provenance] if self.provenance is not None else []
        self.provenance = [v if isinstance(v, SupportingTextInReference) else SupportingTextInReference(**as_dict(v)) for v in self.provenance]

        self._normalize_inlined_as_list(slot_name="proposed_terms", slot_type=ProposedOntologyTerm, key_name="proposed_name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Experiment(YAMLRoot):
    """
    A suggested experiment to answer a question about the gene
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["Experiment"]
    class_class_curie: ClassVar[str] = "gene_review:Experiment"
    class_name: ClassVar[str] = "Experiment"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.Experiment

    description: str = None
    hypothesis: Optional[str] = None
    experiment_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self.hypothesis is not None and not isinstance(self.hypothesis, str):
            self.hypothesis = str(self.hypothesis)

        if self.experiment_type is not None and not isinstance(self.experiment_type, str):
            self.experiment_type = str(self.experiment_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Question(YAMLRoot):
    """
    A question to be answered about the gene
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["Question"]
    class_class_curie: ClassVar[str] = "gene_review:Question"
    class_name: ClassVar[str] = "Question"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.Question

    question: str = None
    experts: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.question):
            self.MissingRequiredField("question")
        if not isinstance(self.question, str):
            self.question = str(self.question)

        if not isinstance(self.experts, list):
            self.experts = [self.experts] if self.experts is not None else []
        self.experts = [v if isinstance(v, str) else str(v) for v in self.experts]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RuleReview(YAMLRoot):
    """
    A review of a UniProt annotation rule (ARBA or UniRule). Each review covers ONE rule and assesses its quality,
    literature support, and biological appropriateness.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["RuleReview"]
    class_class_curie: ClassVar[str] = "gene_review:RuleReview"
    class_name: ClassVar[str] = "RuleReview"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.RuleReview

    id: Union[str, RuleReviewId] = None
    rule_type: Union[str, "RuleTypeEnum"] = None
    rule: Union[dict, "EmbeddedRule"] = None
    action: Union[str, "RuleActionEnum"] = None
    description: Optional[str] = None
    references: Optional[Union[dict[Union[str, ReferenceId], Union[dict, Reference]], list[Union[dict, Reference]]]] = empty_dict()
    status: Optional[Union[str, "RuleReviewStatusEnum"]] = None
    review_summary: Optional[str] = None
    action_rationale: Optional[str] = None
    suggested_modifications: Optional[Union[str, list[str]]] = empty_list()
    parsimony: Optional[Union[dict, "ParsimonyAssessment"]] = None
    literature_support: Optional[Union[dict, "LiteratureSupportAssessment"]] = None
    condition_overlap: Optional[Union[dict, "ConditionOverlapAssessment"]] = None
    go_specificity: Optional[Union[dict, "GOSpecificityAssessment"]] = None
    taxonomic_scope: Optional[Union[dict, "TaxonomicScopeAssessment"]] = None
    confidence: Optional[float] = None
    supported_by: Optional[Union[Union[dict, SupportingTextInReference], list[Union[dict, SupportingTextInReference]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RuleReviewId):
            self.id = RuleReviewId(self.id)

        if self._is_empty(self.rule_type):
            self.MissingRequiredField("rule_type")
        if not isinstance(self.rule_type, RuleTypeEnum):
            self.rule_type = RuleTypeEnum(self.rule_type)

        if self._is_empty(self.rule):
            self.MissingRequiredField("rule")
        if not isinstance(self.rule, EmbeddedRule):
            self.rule = EmbeddedRule(**as_dict(self.rule))

        if self._is_empty(self.action):
            self.MissingRequiredField("action")
        if not isinstance(self.action, RuleActionEnum):
            self.action = RuleActionEnum(self.action)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="references", slot_type=Reference, key_name="id", keyed=True)

        if self.status is not None and not isinstance(self.status, RuleReviewStatusEnum):
            self.status = RuleReviewStatusEnum(self.status)

        if self.review_summary is not None and not isinstance(self.review_summary, str):
            self.review_summary = str(self.review_summary)

        if self.action_rationale is not None and not isinstance(self.action_rationale, str):
            self.action_rationale = str(self.action_rationale)

        if not isinstance(self.suggested_modifications, list):
            self.suggested_modifications = [self.suggested_modifications] if self.suggested_modifications is not None else []
        self.suggested_modifications = [v if isinstance(v, str) else str(v) for v in self.suggested_modifications]

        if self.parsimony is not None and not isinstance(self.parsimony, ParsimonyAssessment):
            self.parsimony = ParsimonyAssessment(**as_dict(self.parsimony))

        if self.literature_support is not None and not isinstance(self.literature_support, LiteratureSupportAssessment):
            self.literature_support = LiteratureSupportAssessment(**as_dict(self.literature_support))

        if self.condition_overlap is not None and not isinstance(self.condition_overlap, ConditionOverlapAssessment):
            self.condition_overlap = ConditionOverlapAssessment(**as_dict(self.condition_overlap))

        if self.go_specificity is not None and not isinstance(self.go_specificity, GOSpecificityAssessment):
            self.go_specificity = GOSpecificityAssessment(**as_dict(self.go_specificity))

        if self.taxonomic_scope is not None and not isinstance(self.taxonomic_scope, TaxonomicScopeAssessment):
            self.taxonomic_scope = TaxonomicScopeAssessment(**as_dict(self.taxonomic_scope))

        if self.confidence is not None and not isinstance(self.confidence, float):
            self.confidence = float(self.confidence)

        if not isinstance(self.supported_by, list):
            self.supported_by = [self.supported_by] if self.supported_by is not None else []
        self.supported_by = [v if isinstance(v, SupportingTextInReference) else SupportingTextInReference(**as_dict(v)) for v in self.supported_by]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EmbeddedRule(YAMLRoot):
    """
    An embedded representation of an ARBA or UniRule for storage in YAML. Captures the essential structure: conditions
    (antecedent) and GO annotations (consequent).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["EmbeddedRule"]
    class_class_curie: ClassVar[str] = "gene_review:EmbeddedRule"
    class_name: ClassVar[str] = "EmbeddedRule"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.EmbeddedRule

    rule_id: str = None
    condition_sets: Union[Union[dict, "RuleConditionSet"], list[Union[dict, "RuleConditionSet"]]] = None
    entries: Union[dict[Union[str, RuleReviewEntryId], Union[dict, "RuleReviewEntry"]], list[Union[dict, "RuleReviewEntry"]]] = empty_dict()
    go_annotations: Optional[Union[Union[dict, "RuleGOAnnotation"], list[Union[dict, "RuleGOAnnotation"]]]] = empty_list()
    ipr2go_redundancy: Optional[Union[dict, "InterPro2GORedundancy"]] = None
    reviewed_protein_count: Optional[int] = None
    unreviewed_protein_count: Optional[int] = None
    created_date: Optional[str] = None
    modified_date: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.rule_id):
            self.MissingRequiredField("rule_id")
        if not isinstance(self.rule_id, str):
            self.rule_id = str(self.rule_id)

        if self._is_empty(self.condition_sets):
            self.MissingRequiredField("condition_sets")
        self._normalize_inlined_as_list(slot_name="condition_sets", slot_type=RuleConditionSet, key_name="number", keyed=False)

        if self._is_empty(self.entries):
            self.MissingRequiredField("entries")
        self._normalize_inlined_as_list(slot_name="entries", slot_type=RuleReviewEntry, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="go_annotations", slot_type=RuleGOAnnotation, key_name="go_id", keyed=False)

        if self.ipr2go_redundancy is not None and not isinstance(self.ipr2go_redundancy, InterPro2GORedundancy):
            self.ipr2go_redundancy = InterPro2GORedundancy(**as_dict(self.ipr2go_redundancy))

        if self.reviewed_protein_count is not None and not isinstance(self.reviewed_protein_count, int):
            self.reviewed_protein_count = int(self.reviewed_protein_count)

        if self.unreviewed_protein_count is not None and not isinstance(self.unreviewed_protein_count, int):
            self.unreviewed_protein_count = int(self.unreviewed_protein_count)

        if self.created_date is not None and not isinstance(self.created_date, str):
            self.created_date = str(self.created_date)

        if self.modified_date is not None and not isinstance(self.modified_date, str):
            self.modified_date = str(self.modified_date)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RuleConditionSet(YAMLRoot):
    """
    A set of conditions that must ALL be true (conjunction/AND). Multiple condition sets in a rule are OR-ed together
    (disjunction).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["RuleConditionSet"]
    class_class_curie: ClassVar[str] = "gene_review:RuleConditionSet"
    class_name: ClassVar[str] = "RuleConditionSet"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.RuleConditionSet

    number: int = None
    conditions: Union[Union[dict, "RuleCondition"], list[Union[dict, "RuleCondition"]]] = None
    notes: Optional[str] = None
    pairwise_overlap: Optional[Union[Union[dict, "PairwiseOverlap"], list[Union[dict, "PairwiseOverlap"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.number):
            self.MissingRequiredField("number")
        if not isinstance(self.number, int):
            self.number = int(self.number)

        if self._is_empty(self.conditions):
            self.MissingRequiredField("conditions")
        self._normalize_inlined_as_list(slot_name="conditions", slot_type=RuleCondition, key_name="condition_type", keyed=False)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        self._normalize_inlined_as_list(slot_name="pairwise_overlap", slot_type=PairwiseOverlap, key_name="condition_a", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RuleCondition(YAMLRoot):
    """
    A single condition in a rule antecedent
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["RuleCondition"]
    class_class_curie: ClassVar[str] = "gene_review:RuleCondition"
    class_name: ClassVar[str] = "RuleCondition"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.RuleCondition

    condition_type: Union[str, "ConditionTypeEnum"] = None
    value: str = None
    curie: Optional[str] = None
    label: Optional[str] = None
    interpro_type: Optional[Union[str, "InterProTypeEnum"]] = None
    negated: Optional[Union[bool, Bool]] = None
    protein_count: Optional[int] = None
    protein_database: Optional[Union[str, "ProteinDatabaseEnum"]] = None
    uniqueness_score: Optional[float] = None
    sample_proteins: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.condition_type):
            self.MissingRequiredField("condition_type")
        if not isinstance(self.condition_type, ConditionTypeEnum):
            self.condition_type = ConditionTypeEnum(self.condition_type)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self.curie is not None and not isinstance(self.curie, str):
            self.curie = str(self.curie)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.interpro_type is not None and not isinstance(self.interpro_type, InterProTypeEnum):
            self.interpro_type = InterProTypeEnum(self.interpro_type)

        if self.negated is not None and not isinstance(self.negated, Bool):
            self.negated = Bool(self.negated)

        if self.protein_count is not None and not isinstance(self.protein_count, int):
            self.protein_count = int(self.protein_count)

        if self.protein_database is not None and not isinstance(self.protein_database, ProteinDatabaseEnum):
            self.protein_database = ProteinDatabaseEnum(self.protein_database)

        if self.uniqueness_score is not None and not isinstance(self.uniqueness_score, float):
            self.uniqueness_score = float(self.uniqueness_score)

        if not isinstance(self.sample_proteins, list):
            self.sample_proteins = [self.sample_proteins] if self.sample_proteins is not None else []
        self.sample_proteins = [v if isinstance(v, str) else str(v) for v in self.sample_proteins]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RuleGOAnnotation(YAMLRoot):
    """
    A GO annotation produced by the rule
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["RuleGOAnnotation"]
    class_class_curie: ClassVar[str] = "gene_review:RuleGOAnnotation"
    class_name: ClassVar[str] = "RuleGOAnnotation"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.RuleGOAnnotation

    go_id: str = None
    go_label: Optional[str] = None
    aspect: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.go_id):
            self.MissingRequiredField("go_id")
        if not isinstance(self.go_id, str):
            self.go_id = str(self.go_id)

        if self.go_label is not None and not isinstance(self.go_label, str):
            self.go_label = str(self.go_label)

        if self.aspect is not None and not isinstance(self.aspect, str):
            self.aspect = str(self.aspect)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PairwiseOverlap(YAMLRoot):
    """
    Overlap statistics between two domain conditions (InterPro, FunFam, etc.) in the same condition set. Provides set
    difference metrics to measure uniqueness and redundancy.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["PairwiseOverlap"]
    class_class_curie: ClassVar[str] = "gene_review:PairwiseOverlap"
    class_name: ClassVar[str] = "PairwiseOverlap"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.PairwiseOverlap

    condition_a: str = None
    condition_b: str = None
    protein_database: Union[str, "ProteinDatabaseEnum"] = None
    count_a: int = None
    count_b: int = None
    intersection_count: int = None
    a_minus_b_count: int = None
    b_minus_a_count: int = None
    jaccard_similarity: float = None
    containment_a_in_b: float = None
    containment_b_in_a: float = None
    condition_a_label: Optional[str] = None
    condition_b_label: Optional[str] = None
    interpretation: Optional[Union[str, "OverlapInterpretationEnum"]] = None
    condition_a_in_sets: Optional[Union[int, list[int]]] = empty_list()
    condition_b_in_sets: Optional[Union[int, list[int]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.condition_a):
            self.MissingRequiredField("condition_a")
        if not isinstance(self.condition_a, str):
            self.condition_a = str(self.condition_a)

        if self._is_empty(self.condition_b):
            self.MissingRequiredField("condition_b")
        if not isinstance(self.condition_b, str):
            self.condition_b = str(self.condition_b)

        if self._is_empty(self.protein_database):
            self.MissingRequiredField("protein_database")
        if not isinstance(self.protein_database, ProteinDatabaseEnum):
            self.protein_database = ProteinDatabaseEnum(self.protein_database)

        if self._is_empty(self.count_a):
            self.MissingRequiredField("count_a")
        if not isinstance(self.count_a, int):
            self.count_a = int(self.count_a)

        if self._is_empty(self.count_b):
            self.MissingRequiredField("count_b")
        if not isinstance(self.count_b, int):
            self.count_b = int(self.count_b)

        if self._is_empty(self.intersection_count):
            self.MissingRequiredField("intersection_count")
        if not isinstance(self.intersection_count, int):
            self.intersection_count = int(self.intersection_count)

        if self._is_empty(self.a_minus_b_count):
            self.MissingRequiredField("a_minus_b_count")
        if not isinstance(self.a_minus_b_count, int):
            self.a_minus_b_count = int(self.a_minus_b_count)

        if self._is_empty(self.b_minus_a_count):
            self.MissingRequiredField("b_minus_a_count")
        if not isinstance(self.b_minus_a_count, int):
            self.b_minus_a_count = int(self.b_minus_a_count)

        if self._is_empty(self.jaccard_similarity):
            self.MissingRequiredField("jaccard_similarity")
        if not isinstance(self.jaccard_similarity, float):
            self.jaccard_similarity = float(self.jaccard_similarity)

        if self._is_empty(self.containment_a_in_b):
            self.MissingRequiredField("containment_a_in_b")
        if not isinstance(self.containment_a_in_b, float):
            self.containment_a_in_b = float(self.containment_a_in_b)

        if self._is_empty(self.containment_b_in_a):
            self.MissingRequiredField("containment_b_in_a")
        if not isinstance(self.containment_b_in_a, float):
            self.containment_b_in_a = float(self.containment_b_in_a)

        if self.condition_a_label is not None and not isinstance(self.condition_a_label, str):
            self.condition_a_label = str(self.condition_a_label)

        if self.condition_b_label is not None and not isinstance(self.condition_b_label, str):
            self.condition_b_label = str(self.condition_b_label)

        if self.interpretation is not None and not isinstance(self.interpretation, OverlapInterpretationEnum):
            self.interpretation = OverlapInterpretationEnum(self.interpretation)

        if not isinstance(self.condition_a_in_sets, list):
            self.condition_a_in_sets = [self.condition_a_in_sets] if self.condition_a_in_sets is not None else []
        self.condition_a_in_sets = [v if isinstance(v, int) else int(v) for v in self.condition_a_in_sets]

        if not isinstance(self.condition_b_in_sets, list):
            self.condition_b_in_sets = [self.condition_b_in_sets] if self.condition_b_in_sets is not None else []
        self.condition_b_in_sets = [v if isinstance(v, int) else int(v) for v in self.condition_b_in_sets]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RuleReviewEntry(YAMLRoot):
    """
    An entity in the rule - either a domain/family condition or a GO term target. Each entry tracks its relationships
    (predictions, predicted-by, equivalence) to other entries.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["RuleReviewEntry"]
    class_class_curie: ClassVar[str] = "gene_review:RuleReviewEntry"
    class_name: ClassVar[str] = "RuleReviewEntry"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.RuleReviewEntry

    id: Union[str, RuleReviewEntryId] = None
    type: Union[str, "EntryTypeEnum"] = None
    label: Optional[str] = None
    appears_in_condition_sets: Optional[Union[int, list[int]]] = empty_list()
    protein_count: Optional[int] = None
    source: Optional[str] = None
    asserted_predicted_go_terms: Optional[Union[str, list[str]]] = empty_list()
    related_entries: Optional[Union[Union[dict, "RelatedEntry"], list[Union[dict, "RelatedEntry"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RuleReviewEntryId):
            self.id = RuleReviewEntryId(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, EntryTypeEnum):
            self.type = EntryTypeEnum(self.type)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if not isinstance(self.appears_in_condition_sets, list):
            self.appears_in_condition_sets = [self.appears_in_condition_sets] if self.appears_in_condition_sets is not None else []
        self.appears_in_condition_sets = [v if isinstance(v, int) else int(v) for v in self.appears_in_condition_sets]

        if self.protein_count is not None and not isinstance(self.protein_count, int):
            self.protein_count = int(self.protein_count)

        if self.source is not None and not isinstance(self.source, str):
            self.source = str(self.source)

        if not isinstance(self.asserted_predicted_go_terms, list):
            self.asserted_predicted_go_terms = [self.asserted_predicted_go_terms] if self.asserted_predicted_go_terms is not None else []
        self.asserted_predicted_go_terms = [v if isinstance(v, str) else str(v) for v in self.asserted_predicted_go_terms]

        self._normalize_inlined_as_list(slot_name="related_entries", slot_type=RelatedEntry, key_name="relationship", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RelatedEntry(YAMLRoot):
    """
    A relationship from this entry to another entry in the rule. Categorized as PREDICTS (this → other), PREDICTED_BY
    (other → this), or EQUIV (bidirectional).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["RelatedEntry"]
    class_class_curie: ClassVar[str] = "gene_review:RelatedEntry"
    class_name: ClassVar[str] = "RelatedEntry"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.RelatedEntry

    relationship: Union[str, "EntryRelationshipEnum"] = None
    target_id: str = None
    containment: Optional[float] = None
    jaccard_similarity: Optional[float] = None
    intersection_count: Optional[int] = None
    exclusive_count: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.relationship):
            self.MissingRequiredField("relationship")
        if not isinstance(self.relationship, EntryRelationshipEnum):
            self.relationship = EntryRelationshipEnum(self.relationship)

        if self._is_empty(self.target_id):
            self.MissingRequiredField("target_id")
        if not isinstance(self.target_id, str):
            self.target_id = str(self.target_id)

        if self.containment is not None and not isinstance(self.containment, float):
            self.containment = float(self.containment)

        if self.jaccard_similarity is not None and not isinstance(self.jaccard_similarity, float):
            self.jaccard_similarity = float(self.jaccard_similarity)

        if self.intersection_count is not None and not isinstance(self.intersection_count, int):
            self.intersection_count = int(self.intersection_count)

        if self.exclusive_count is not None and not isinstance(self.exclusive_count, int):
            self.exclusive_count = int(self.exclusive_count)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InterPro2GORedundancy(YAMLRoot):
    """
    Analysis of whether rule GO annotations are redundant with existing InterPro2GO mappings from the GO Consortium.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["InterPro2GORedundancy"]
    class_class_curie: ClassVar[str] = "gene_review:InterPro2GORedundancy"
    class_name: ClassVar[str] = "InterPro2GORedundancy"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.InterPro2GORedundancy

    redundant_annotations: Optional[Union[Union[dict, "RedundantAnnotation"], list[Union[dict, "RedundantAnnotation"]]]] = empty_list()
    novel_annotations: Optional[Union[str, list[str]]] = empty_list()
    summary: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="redundant_annotations", slot_type=RedundantAnnotation, key_name="go_id", keyed=False)

        if not isinstance(self.novel_annotations, list):
            self.novel_annotations = [self.novel_annotations] if self.novel_annotations is not None else []
        self.novel_annotations = [v if isinstance(v, str) else str(v) for v in self.novel_annotations]

        if self.summary is not None and not isinstance(self.summary, str):
            self.summary = str(self.summary)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RedundantAnnotation(YAMLRoot):
    """
    A GO annotation that is redundant with an existing InterPro2GO mapping
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["RedundantAnnotation"]
    class_class_curie: ClassVar[str] = "gene_review:RedundantAnnotation"
    class_name: ClassVar[str] = "RedundantAnnotation"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.RedundantAnnotation

    go_id: str = None
    interpro_source: str = None
    go_label: Optional[str] = None
    interpro_label: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.go_id):
            self.MissingRequiredField("go_id")
        if not isinstance(self.go_id, str):
            self.go_id = str(self.go_id)

        if self._is_empty(self.interpro_source):
            self.MissingRequiredField("interpro_source")
        if not isinstance(self.interpro_source, str):
            self.interpro_source = str(self.interpro_source)

        if self.go_label is not None and not isinstance(self.go_label, str):
            self.go_label = str(self.go_label)

        if self.interpro_label is not None and not isinstance(self.interpro_label, str):
            self.interpro_label = str(self.interpro_label)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ParsimonyAssessment(YAMLRoot):
    """
    Assessment of rule parsimony (simplicity vs complexity)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["ParsimonyAssessment"]
    class_class_curie: ClassVar[str] = "gene_review:ParsimonyAssessment"
    class_name: ClassVar[str] = "ParsimonyAssessment"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.ParsimonyAssessment

    assessment: Union[str, "ParsimonyEnum"] = None
    notes: Optional[str] = None
    supported_by: Optional[Union[Union[dict, SupportingTextInReference], list[Union[dict, SupportingTextInReference]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.assessment):
            self.MissingRequiredField("assessment")
        if not isinstance(self.assessment, ParsimonyEnum):
            self.assessment = ParsimonyEnum(self.assessment)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if not isinstance(self.supported_by, list):
            self.supported_by = [self.supported_by] if self.supported_by is not None else []
        self.supported_by = [v if isinstance(v, SupportingTextInReference) else SupportingTextInReference(**as_dict(v)) for v in self.supported_by]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LiteratureSupportAssessment(YAMLRoot):
    """
    Assessment of literature support for the rule
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["LiteratureSupportAssessment"]
    class_class_curie: ClassVar[str] = "gene_review:LiteratureSupportAssessment"
    class_name: ClassVar[str] = "LiteratureSupportAssessment"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.LiteratureSupportAssessment

    assessment: Union[str, "LiteratureSupportEnum"] = None
    notes: Optional[str] = None
    supported_by: Optional[Union[Union[dict, SupportingTextInReference], list[Union[dict, SupportingTextInReference]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.assessment):
            self.MissingRequiredField("assessment")
        if not isinstance(self.assessment, LiteratureSupportEnum):
            self.assessment = LiteratureSupportEnum(self.assessment)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if not isinstance(self.supported_by, list):
            self.supported_by = [self.supported_by] if self.supported_by is not None else []
        self.supported_by = [v if isinstance(v, SupportingTextInReference) else SupportingTextInReference(**as_dict(v)) for v in self.supported_by]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConditionOverlapAssessment(YAMLRoot):
    """
    Assessment of overlap between rule conditions
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["ConditionOverlapAssessment"]
    class_class_curie: ClassVar[str] = "gene_review:ConditionOverlapAssessment"
    class_name: ClassVar[str] = "ConditionOverlapAssessment"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.ConditionOverlapAssessment

    assessment: Union[str, "OverlapEnum"] = None
    notes: Optional[str] = None
    supported_by: Optional[Union[Union[dict, SupportingTextInReference], list[Union[dict, SupportingTextInReference]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.assessment):
            self.MissingRequiredField("assessment")
        if not isinstance(self.assessment, OverlapEnum):
            self.assessment = OverlapEnum(self.assessment)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if not isinstance(self.supported_by, list):
            self.supported_by = [self.supported_by] if self.supported_by is not None else []
        self.supported_by = [v if isinstance(v, SupportingTextInReference) else SupportingTextInReference(**as_dict(v)) for v in self.supported_by]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GOSpecificityAssessment(YAMLRoot):
    """
    Assessment of GO term specificity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["GOSpecificityAssessment"]
    class_class_curie: ClassVar[str] = "gene_review:GOSpecificityAssessment"
    class_name: ClassVar[str] = "GOSpecificityAssessment"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.GOSpecificityAssessment

    assessment: Union[str, "SpecificityEnum"] = None
    notes: Optional[str] = None
    supported_by: Optional[Union[Union[dict, SupportingTextInReference], list[Union[dict, SupportingTextInReference]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.assessment):
            self.MissingRequiredField("assessment")
        if not isinstance(self.assessment, SpecificityEnum):
            self.assessment = SpecificityEnum(self.assessment)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if not isinstance(self.supported_by, list):
            self.supported_by = [self.supported_by] if self.supported_by is not None else []
        self.supported_by = [v if isinstance(v, SupportingTextInReference) else SupportingTextInReference(**as_dict(v)) for v in self.supported_by]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TaxonomicScopeAssessment(YAMLRoot):
    """
    Assessment of taxonomic restriction appropriateness
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["TaxonomicScopeAssessment"]
    class_class_curie: ClassVar[str] = "gene_review:TaxonomicScopeAssessment"
    class_name: ClassVar[str] = "TaxonomicScopeAssessment"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.TaxonomicScopeAssessment

    assessment: Union[str, "TaxonomicScopeEnum"] = None
    notes: Optional[str] = None
    supported_by: Optional[Union[Union[dict, SupportingTextInReference], list[Union[dict, SupportingTextInReference]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.assessment):
            self.MissingRequiredField("assessment")
        if not isinstance(self.assessment, TaxonomicScopeEnum):
            self.assessment = TaxonomicScopeEnum(self.assessment)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if not isinstance(self.supported_by, list):
            self.supported_by = [self.supported_by] if self.supported_by is not None else []
        self.supported_by = [v if isinstance(v, SupportingTextInReference) else SupportingTextInReference(**as_dict(v)) for v in self.supported_by]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PredictionReview(YAMLRoot):
    """
    Review of computational/ML predictions for a gene that are NOT in the curated GOA/UniProt annotations. This
    captures predictions from methods like DeepECTF, PANTHER/IBA, InterPro2GO, CLEAN, GloEC, MAPred, etc. and
    evaluates them against literature and bioinformatic evidence. Inspired by the systematic evaluation in de
    Crécy-Lagard et al. 2025 (PMID:40703034).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["PredictionReview"]
    class_class_curie: ClassVar[str] = "gene_review:PredictionReview"
    class_name: ClassVar[str] = "PredictionReview"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.PredictionReview

    id: Union[str, PredictionReviewId] = None
    gene_symbol: str = None
    taxon: Union[dict, Term] = None
    description: Optional[str] = None
    references: Optional[Union[dict[Union[str, ReferenceId], Union[dict, Reference]], list[Union[dict, Reference]]]] = empty_dict()
    status: Optional[Union[str, "GeneReviewStatusEnum"]] = None
    locus_tag: Optional[str] = None
    source_documents: Optional[Union[str, list[str]]] = empty_list()
    predictions: Optional[Union[Union[dict, "PredictedAnnotation"], list[Union[dict, "PredictedAnnotation"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PredictionReviewId):
            self.id = PredictionReviewId(self.id)

        if self._is_empty(self.gene_symbol):
            self.MissingRequiredField("gene_symbol")
        if not isinstance(self.gene_symbol, str):
            self.gene_symbol = str(self.gene_symbol)

        if self._is_empty(self.taxon):
            self.MissingRequiredField("taxon")
        if not isinstance(self.taxon, Term):
            self.taxon = Term(**as_dict(self.taxon))

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="references", slot_type=Reference, key_name="id", keyed=True)

        if self.status is not None and not isinstance(self.status, GeneReviewStatusEnum):
            self.status = GeneReviewStatusEnum(self.status)

        if self.locus_tag is not None and not isinstance(self.locus_tag, str):
            self.locus_tag = str(self.locus_tag)

        if not isinstance(self.source_documents, list):
            self.source_documents = [self.source_documents] if self.source_documents is not None else []
        self.source_documents = [v if isinstance(v, str) else str(v) for v in self.source_documents]

        self._normalize_inlined_as_list(slot_name="predictions", slot_type=PredictedAnnotation, key_name="source_method", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PredictedAnnotation(YAMLRoot):
    """
    A single computational prediction and its review. Each prediction comes from a specific method and predicts a term
    (EC number, GO term, etc.) for the gene.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["PredictedAnnotation"]
    class_class_curie: ClassVar[str] = "gene_review:PredictedAnnotation"
    class_name: ClassVar[str] = "PredictedAnnotation"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.PredictedAnnotation

    source_method: str = None
    predicted_term: Union[dict, Term] = None
    predicted_term_type: Union[str, "PredictedTermTypeEnum"] = None
    review: Union[dict, "PredictionAssessment"] = None
    source_version: Optional[str] = None
    source_reference_id: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.source_method):
            self.MissingRequiredField("source_method")
        if not isinstance(self.source_method, str):
            self.source_method = str(self.source_method)

        if self._is_empty(self.predicted_term):
            self.MissingRequiredField("predicted_term")
        if not isinstance(self.predicted_term, Term):
            self.predicted_term = Term(**as_dict(self.predicted_term))

        if self._is_empty(self.predicted_term_type):
            self.MissingRequiredField("predicted_term_type")
        if not isinstance(self.predicted_term_type, PredictedTermTypeEnum):
            self.predicted_term_type = PredictedTermTypeEnum(self.predicted_term_type)

        if self._is_empty(self.review):
            self.MissingRequiredField("review")
        if not isinstance(self.review, PredictionAssessment):
            self.review = PredictionAssessment(**as_dict(self.review))

        if self.source_version is not None and not isinstance(self.source_version, str):
            self.source_version = str(self.source_version)

        if self.source_reference_id is not None and not isinstance(self.source_reference_id, str):
            self.source_reference_id = str(self.source_reference_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PredictionAssessment(YAMLRoot):
    """
    Assessment of a single computational prediction. Uses categories from de Crécy-Lagard et al. 2025 (PMID:40703034)
    plus extensions for GO predictions.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["PredictionAssessment"]
    class_class_curie: ClassVar[str] = "gene_review:PredictionAssessment"
    class_name: ClassVar[str] = "PredictionAssessment"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.PredictionAssessment

    assessment: Union[str, "PredictionAssessmentEnum"] = None
    confidence_score: int = None
    summary: str = None
    error_type: Optional[Union[str, "PredictionErrorTypeEnum"]] = None
    supported_by: Optional[Union[Union[dict, SupportingTextInReference], list[Union[dict, SupportingTextInReference]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.assessment):
            self.MissingRequiredField("assessment")
        if not isinstance(self.assessment, PredictionAssessmentEnum):
            self.assessment = PredictionAssessmentEnum(self.assessment)

        if self._is_empty(self.confidence_score):
            self.MissingRequiredField("confidence_score")
        if not isinstance(self.confidence_score, int):
            self.confidence_score = int(self.confidence_score)

        if self._is_empty(self.summary):
            self.MissingRequiredField("summary")
        if not isinstance(self.summary, str):
            self.summary = str(self.summary)

        if self.error_type is not None and not isinstance(self.error_type, PredictionErrorTypeEnum):
            self.error_type = PredictionErrorTypeEnum(self.error_type)

        if not isinstance(self.supported_by, list):
            self.supported_by = [self.supported_by] if self.supported_by is not None else []
        self.supported_by = [v if isinstance(v, SupportingTextInReference) else SupportingTextInReference(**as_dict(v)) for v in self.supported_by]

        super().__post_init__(**kwargs)


# Enumerations
class ModuleScopeEnum(EnumDefinitionImpl):
    """
    How concrete the module document is expected to be.
    """
    CONCRETE = PermissibleValue(
        text="CONCRETE",
        description="""A module representing a specific pathway, complex, process, or taxon-scoped realization where terminal steps should generally ground to representative members.""")
    ABSTRACT = PermissibleValue(
        text="ABSTRACT",
        description="""A reusable motif or template that intentionally uses abstract participant selectors and is not expected to ground each terminal node to concrete representative proteins.""")

    _defn = EnumDefinition(
        name="ModuleScopeEnum",
        description="How concrete the module document is expected to be.",
    )

class ModuleTypeEnum(EnumDefinitionImpl):
    """
    Broad type of biological module node.
    """
    MODULE = PermissibleValue(
        text="MODULE",
        description="Generic or unspecified module.")
    BIOLOGICAL_PROCESS = PermissibleValue(
        text="BIOLOGICAL_PROCESS",
        description="Biological-process-like module.")
    MOLECULAR_FUNCTION = PermissibleValue(
        text="MOLECULAR_FUNCTION",
        description="Molecular-function-like module.")
    METABOLIC_PATHWAY = PermissibleValue(
        text="METABOLIC_PATHWAY",
        description="Metabolic pathway or pathway segment.")
    SIGNALING_PATHWAY = PermissibleValue(
        text="SIGNALING_PATHWAY",
        description="Signaling pathway or pathway segment.")
    DEVELOPMENTAL_PROCESS = PermissibleValue(
        text="DEVELOPMENTAL_PROCESS",
        description="Developmental process, stage, or program.")
    CELLULAR_COMPONENT = PermissibleValue(
        text="CELLULAR_COMPONENT",
        description="Cellular component or structure viewed as a module.")
    ORGANELLE_LIFECYCLE = PermissibleValue(
        text="ORGANELLE_LIFECYCLE",
        description="Assembly, maintenance, operation, and turnover of an organelle.")
    PROTEIN_COMPLEX = PermissibleValue(
        text="PROTEIN_COMPLEX",
        description="Protein complex or complex lifecycle.")
    REACTION = PermissibleValue(
        text="REACTION",
        description="Reaction-like module step.")
    TRANSPORT_STEP = PermissibleValue(
        text="TRANSPORT_STEP",
        description="Transport or translocation step.")
    REGULATORY_STEP = PermissibleValue(
        text="REGULATORY_STEP",
        description="Regulatory or control step.")

    _defn = EnumDefinition(
        name="ModuleTypeEnum",
        description="Broad type of biological module node.",
    )

class VariantSelectionEnum(EnumDefinitionImpl):
    """
    How variants in a variant set may be selected in a realization.
    """
    EXACTLY_ONE = PermissibleValue(
        text="EXACTLY_ONE",
        description="Exactly one variant applies.")
    ONE_OR_MORE = PermissibleValue(
        text="ONE_OR_MORE",
        description="One or more variants may apply.")
    ZERO_OR_MORE = PermissibleValue(
        text="ZERO_OR_MORE",
        description="Variants are optional and any number may apply.")

    _defn = EnumDefinition(
        name="VariantSelectionEnum",
        description="How variants in a variant set may be selected in a realization.",
    )

class ChainingStatusEnum(EnumDefinitionImpl):
    """
    Curator adjudication of reaction continuity across a module connection (whether the upstream reaction's product is
    consumed as the downstream reaction's substrate). Used as an explicit override for the advisory, non-blocking
    automated chaining check.
    """
    VERIFIED = PermissibleValue(
        text="VERIFIED",
        description="""The upstream product is confirmed to be the downstream substrate (curator-confirmed continuity).""")
    KNOWLEDGE_GAP = PermissibleValue(
        text="KNOWLEDGE_GAP",
        description="""The connecting intermediate or enzyme is genuinely not known; the break reflects missing biological knowledge, not a modelling error.""")
    MAPPING_GAP = PermissibleValue(
        text="MAPPING_GAP",
        description="""The chemistry is known but the GO/RHEA (or GO/ChEBI) mapping does not yet capture the link, so the automated check cannot see the continuity.""")
    NOT_APPLICABLE = PermissibleValue(
        text="NOT_APPLICABLE",
        description="""Chaining does not apply to this connection (e.g. a regulatory or non-metabolic edge, or a spiral re-entry handled elsewhere).""")
    UNVERIFIED = PermissibleValue(
        text="UNVERIFIED",
        description="Continuity has not been assessed (explicitly, as opposed to simply leaving the field unset).")

    _defn = EnumDefinition(
        name="ChainingStatusEnum",
        description="""Curator adjudication of reaction continuity across a module connection (whether the upstream reaction's product is consumed as the downstream reaction's substrate). Used as an explicit override for the advisory, non-blocking automated chaining check.""",
    )

class ConformanceStatusEnum(EnumDefinitionImpl):
    """
    How closely a module node matches a template motif it conforms to.
    """
    EXACT = PermissibleValue(
        text="EXACT",
        description="""The node matches the template motif exactly: same steps, function terms, and connection topology, with no recorded deviations.""")
    WITH_DEVIATIONS = PermissibleValue(
        text="WITH_DEVIATIONS",
        description="""The node matches the template motif apart from the differences listed in deviations (e.g. a merged or missing tier, a substituted term).""")
    EXTENDS = PermissibleValue(
        text="EXTENDS",
        description="The node contains the full template motif and adds further steps or structure beyond it.")

    _defn = EnumDefinition(
        name="ConformanceStatusEnum",
        description="How closely a module node matches a template motif it conforms to.",
    )

class ParticipantSelectorTypeEnum(EnumDefinitionImpl):
    """
    How a module annoton participant is selected.
    """
    GENE = PermissibleValue(
        text="GENE",
        description="A concrete gene.")
    GENE_PRODUCT = PermissibleValue(
        text="GENE_PRODUCT",
        description="A concrete gene product, protein, isoform, or form.")
    PROTEIN_COMPLEX = PermissibleValue(
        text="PROTEIN_COMPLEX",
        description="A concrete protein-containing complex or subcomplex.")
    FAMILY = PermissibleValue(
        text="FAMILY",
        description="Any member of a specified family or orthogroup.")
    DOMAIN = PermissibleValue(
        text="DOMAIN",
        description="Any entity with a specified domain, motif, or site.")
    ORTHOLOG_OF = PermissibleValue(
        text="ORTHOLOG_OF",
        description="Any ortholog of a specified gene.")
    HOMOLOG_OF = PermissibleValue(
        text="HOMOLOG_OF",
        description="Any homolog of a specified gene.")
    ANY_WITH_FUNCTION = PermissibleValue(
        text="ANY_WITH_FUNCTION",
        description="Any participant satisfying the specified molecular function descriptor.")
    ANY_WITH_DOMAIN = PermissibleValue(
        text="ANY_WITH_DOMAIN",
        description="Any participant satisfying the specified domain descriptor.")
    ANY_PARTICIPANT = PermissibleValue(
        text="ANY_PARTICIPANT",
        description="An unspecified participant.")

    _defn = EnumDefinition(
        name="ParticipantSelectorTypeEnum",
        description="How a module annoton participant is selected.",
    )

class ModuleConnectionTypeEnum(EnumDefinitionImpl):
    """
    Common connection types between module elements.
    """
    PRECEDES = PermissibleValue(
        text="PRECEDES",
        description="The source occurs before the target.")
    CAUSES = PermissibleValue(
        text="CAUSES",
        description="The source causally promotes or produces the target.")
    POSITIVELY_REGULATES = PermissibleValue(
        text="POSITIVELY_REGULATES",
        description="The source positively regulates the target.")
    NEGATIVELY_REGULATES = PermissibleValue(
        text="NEGATIVELY_REGULATES",
        description="The source negatively regulates the target.")
    PROVIDES_INPUT_FOR = PermissibleValue(
        text="PROVIDES_INPUT_FOR",
        description="The source provides material, signal, or context used by the target.")
    HAS_INPUT = PermissibleValue(
        text="HAS_INPUT",
        description="The target has the source as input.")
    HAS_OUTPUT = PermissibleValue(
        text="HAS_OUTPUT",
        description="The source has the target as output.")
    PART_OF = PermissibleValue(
        text="PART_OF",
        description="The source is part of the target.")

    _defn = EnumDefinition(
        name="ModuleConnectionTypeEnum",
        description="Common connection types between module elements.",
    )

class EvidenceType(EnumDefinitionImpl):
    """
    Gene Ontology evidence codes mapped to Evidence and Conclusion Ontology (ECO) terms
    """
    EXP = PermissibleValue(
        text="EXP",
        description="Inferred from Experiment",
        meaning=ECO["0000269"])
    IDA = PermissibleValue(
        text="IDA",
        description="Inferred from Direct Assay",
        meaning=ECO["0000314"])
    IPI = PermissibleValue(
        text="IPI",
        description="Inferred from Physical Interaction",
        meaning=ECO["0000353"])
    IMP = PermissibleValue(
        text="IMP",
        description="Inferred from Mutant Phenotype",
        meaning=ECO["0000315"])
    IGI = PermissibleValue(
        text="IGI",
        description="Inferred from Genetic Interaction",
        meaning=ECO["0000316"])
    IEP = PermissibleValue(
        text="IEP",
        description="Inferred from Expression Pattern",
        meaning=ECO["0000270"])
    HTP = PermissibleValue(
        text="HTP",
        description="Inferred from High Throughput Experiment",
        meaning=ECO["0006056"])
    HDA = PermissibleValue(
        text="HDA",
        description="Inferred from High Throughput Direct Assay",
        meaning=ECO["0007005"])
    HMP = PermissibleValue(
        text="HMP",
        description="Inferred from High Throughput Mutant Phenotype",
        meaning=ECO["0007001"])
    HGI = PermissibleValue(
        text="HGI",
        description="Inferred from High Throughput Genetic Interaction",
        meaning=ECO["0007003"])
    HEP = PermissibleValue(
        text="HEP",
        description="Inferred from High Throughput Expression Pattern",
        meaning=ECO["0007007"])
    IBA = PermissibleValue(
        text="IBA",
        description="Inferred from Biological aspect of Ancestor",
        meaning=ECO["0000318"])
    IBD = PermissibleValue(
        text="IBD",
        description="Inferred from Biological aspect of Descendant",
        meaning=ECO["0000319"])
    IKR = PermissibleValue(
        text="IKR",
        description="Inferred from Key Residues",
        meaning=ECO["0000320"])
    IRD = PermissibleValue(
        text="IRD",
        description="Inferred from Rapid Divergence",
        meaning=ECO["0000321"])
    ISS = PermissibleValue(
        text="ISS",
        description="Inferred from Sequence or structural Similarity",
        meaning=ECO["0000250"])
    ISO = PermissibleValue(
        text="ISO",
        description="Inferred from Sequence Orthology",
        meaning=ECO["0000266"])
    ISA = PermissibleValue(
        text="ISA",
        description="Inferred from Sequence Alignment",
        meaning=ECO["0000247"])
    ISM = PermissibleValue(
        text="ISM",
        description="Inferred from Sequence Model",
        meaning=ECO["0000255"])
    IGC = PermissibleValue(
        text="IGC",
        description="Inferred from Genomic Context",
        meaning=ECO["0000317"])
    RCA = PermissibleValue(
        text="RCA",
        description="Inferred from Reviewed Computational Analysis",
        meaning=ECO["0000245"])
    TAS = PermissibleValue(
        text="TAS",
        description="Traceable Author Statement",
        meaning=ECO["0000304"])
    NAS = PermissibleValue(
        text="NAS",
        description="Non-traceable Author Statement",
        meaning=ECO["0000303"])
    IC = PermissibleValue(
        text="IC",
        description="Inferred by Curator",
        meaning=ECO["0000305"])
    ND = PermissibleValue(
        text="ND",
        description="No biological Data available",
        meaning=ECO["0000307"])
    IEA = PermissibleValue(
        text="IEA",
        description="Inferred from Electronic Annotation",
        meaning=ECO["0000501"])

    _defn = EnumDefinition(
        name="EvidenceType",
        description="Gene Ontology evidence codes mapped to Evidence and Conclusion Ontology (ECO) terms",
    )

class PropagationRootCauseEnum(EnumDefinitionImpl):
    """
    Mechanical root-cause classification for propagated or inferred annotations. This distinguishes bad source
    annotations from bad propagation decisions and term-scoping issues.
    """
    NO_FAILURE_CORE = PermissibleValue(
        text="NO_FAILURE_CORE",
        description="The propagated annotation is correct and core for the target.")
    NO_FAILURE_NON_CORE = PermissibleValue(
        text="NO_FAILURE_NON_CORE",
        description="The propagated annotation is biologically defensible but contextual, secondary, or generic.")
    SOURCE_BAD = PermissibleValue(
        text="SOURCE_BAD",
        description="The source annotation is wrong, miscited, homonym-confused, or contradicted.")
    SOURCE_STALE_OR_MISSING = PermissibleValue(
        text="SOURCE_STALE_OR_MISSING",
        description="""The transferred term no longer appears on the current source record, or donor tracing cannot recover it.""")
    SOURCE_WEAK_OR_INFERRED = PermissibleValue(
        text="SOURCE_WEAK_OR_INFERRED",
        description="The source exists but is only inferred, statement-level, or otherwise weak for propagation.")
    EVIDENCE_CIRCULAR_OR_REDUNDANT = PermissibleValue(
        text="EVIDENCE_CIRCULAR_OR_REDUNDANT",
        description="""The propagation chain transfers from another transfer, or the target already has stronger direct evidence.""")
    PROPAGATION_BAD = PermissibleValue(
        text="PROPAGATION_BAD",
        description="The source annotation is sound, but the term should not propagate to this target.")
    TERM_SCOPING_PROBLEM = PermissibleValue(
        text="TERM_SCOPING_PROBLEM",
        description="""The biology is related, but the GO term is too broad, too specific, or has the wrong role or qualifier.""")
    UNRESOLVED = PermissibleValue(
        text="UNRESOLVED",
        description="The propagation issue was investigated but could not be classified confidently.")

    _defn = EnumDefinition(
        name="PropagationRootCauseEnum",
        description="""Mechanical root-cause classification for propagated or inferred annotations. This distinguishes bad source annotations from bad propagation decisions and term-scoping issues.""",
    )

class PropagationFailureModeEnum(EnumDefinitionImpl):
    """
    Biological subtype for a propagation or inference issue.
    """
    WRONG_ORTHOLOG_OR_PARALOG = PermissibleValue(
        text="WRONG_ORTHOLOG_OR_PARALOG",
        description="Donor/source is a paralog, expanded family member, or wrong subfamily.")
    FUNCTIONAL_DIVERGENCE = PermissibleValue(
        text="FUNCTIONAL_DIVERGENCE",
        description="Target retained fold or orthology but changed substrate, product, activity, or pathway role.")
    PSEUDO_OR_SUBACTIVITY_LOSS = PermissibleValue(
        text="PSEUDO_OR_SUBACTIVITY_LOSS",
        description="Catalytic residues or a specific sub-activity are lost even though the domain remains.")
    CONTEXT_OR_TISSUE_MISMATCH = PermissibleValue(
        text="CONTEXT_OR_TISSUE_MISMATCH",
        description="Donor evidence is tissue, developmental, organismal, or disease-context specific.")
    LINEAGE_OR_TAXON_MISMATCH = PermissibleValue(
        text="LINEAGE_OR_TAXON_MISMATCH",
        description="Process does not occur in the target lineage or organelle system.")
    COMPARTMENT_OR_COMPLEX_MISMATCH = PermissibleValue(
        text="COMPARTMENT_OR_COMPLEX_MISMATCH",
        description="Localization, complex membership, or pathway compartment does not transfer.")
    REGULATORY_SIGN_INVERSION = PermissibleValue(
        text="REGULATORY_SIGN_INVERSION",
        description="""Family contains activators and inhibitors, and a positive/negative regulatory term leaks across members.""")
    ROLE_CONFLATION = PermissibleValue(
        text="ROLE_CONFLATION",
        description="""Substrate, regulator, effector, or specificity subunit is annotated as the agent or core machinery.""")
    GRANULARITY_MISMATCH = PermissibleValue(
        text="GRANULARITY_MISMATCH",
        description="Parent term is true but uninformative, or child term overstates specificity.")
    SOURCE_MISCITATION = PermissibleValue(
        text="SOURCE_MISCITATION",
        description="Source evidence points to the wrong gene, organism, publication, or homonym.")
    SOURCE_EVIDENCE_WEAK = PermissibleValue(
        text="SOURCE_EVIDENCE_WEAK",
        description="""Source evidence is inferred, statement-level, stale, or otherwise too weak for confident propagation.""")
    CIRCULAR_PROPAGATION = PermissibleValue(
        text="CIRCULAR_PROPAGATION",
        description="""Propagation chain depends on another propagated annotation rather than independent source evidence.""")

    _defn = EnumDefinition(
        name="PropagationFailureModeEnum",
        description="Biological subtype for a propagation or inference issue.",
    )

class ResidueClaimEnum(EnumDefinitionImpl):
    """
    What a residue claim asserts about the target protein.
    """
    LOST = PermissibleValue(
        text="LOST",
        description="""The target does not carry the anchor's functional residue -- it is substituted, or no residue aligns to that position at all.""")
    RETAINED = PermissibleValue(
        text="RETAINED",
        description="""The target does carry the residue. Worth recording explicitly: a retained site refutes a \"lacks the catalytic residue\" argument, which is how the CASP12 and LPA errors would have been caught.""")
    SUBSTITUTED = PermissibleValue(
        text="SUBSTITUTED",
        description="""The residue differs but the substitution is conservative or otherwise argued not to abolish function. Distinct from LOST, which asserts the function is gone.""")

    _defn = EnumDefinition(
        name="ResidueClaimEnum",
        description="What a residue claim asserts about the target protein.",
    )

class ResidueClaimMethodEnum(EnumDefinitionImpl):
    """
    How the anchor-to-target position correspondence was established.
    """
    MSA = PermissibleValue(
        text="MSA",
        description="Multiple sequence alignment; record the alignment_release.")
    STRUCTURE = PermissibleValue(
        text="STRUCTURE",
        description="Structural superposition or a solved complex.")
    UNIPROT_FEATURE = PermissibleValue(
        text="UNIPROT_FEATURE",
        description="Both positions read from UniProt feature tables on their own records, with no alignment step.")
    LITERATURE = PermissibleValue(
        text="LITERATURE",
        description="A publication states the correspondence directly; cite it in review.supported_by.")

    _defn = EnumDefinition(
        name="ResidueClaimMethodEnum",
        description="How the anchor-to-target position correspondence was established.",
    )

class PropagationSourceStatusEnum(EnumDefinitionImpl):
    """
    Mechanical status of a source entity with respect to a propagated target annotation.
    """
    SUPPORTS_TRANSFER = PermissibleValue(
        text="SUPPORTS_TRANSFER",
        description="Source evidence supports the term and the transfer to the target.")
    SUPPORTS_SOURCE_BUT_NOT_TARGET = PermissibleValue(
        text="SUPPORTS_SOURCE_BUT_NOT_TARGET",
        description="Source evidence supports the source annotation, but propagation to the target is unsafe.")
    SOURCE_BAD = PermissibleValue(
        text="SOURCE_BAD",
        description="Source annotation or source citation is itself wrong.")
    SOURCE_STALE_OR_MISSING = PermissibleValue(
        text="SOURCE_STALE_OR_MISSING",
        description="Current source record no longer carries the transferred term, or tracing cannot recover it.")
    SOURCE_WEAK_OR_INFERRED = PermissibleValue(
        text="SOURCE_WEAK_OR_INFERRED",
        description="Source exists but is only inferred, statement-level, or otherwise weak.")
    CIRCULAR_OR_REDUNDANT = PermissibleValue(
        text="CIRCULAR_OR_REDUNDANT",
        description="Source participates in a circular transfer chain or adds no independent support.")
    NOT_RELEVANT = PermissibleValue(
        text="NOT_RELEVANT",
        description="Source was inspected but is not relevant to the target annotation.")
    UNRESOLVED = PermissibleValue(
        text="UNRESOLVED",
        description="Source could not be classified confidently.")

    _defn = EnumDefinition(
        name="PropagationSourceStatusEnum",
        description="Mechanical status of a source entity with respect to a propagated target annotation.",
    )

class ActionEnum(EnumDefinitionImpl):

    ACCEPT = PermissibleValue(
        text="ACCEPT",
        description="""Accept the existing annotation as-is, no modifications, and retain as representing the core function of the gene""")
    KEEP_AS_NON_CORE = PermissibleValue(
        text="KEEP_AS_NON_CORE",
        description="""Keep the existing annotation as-is, but mark it as non-core. For pleiotropic genes, this may be the developmental processes, or other processes that are not the core function of the gene.""")
    REMOVE = PermissibleValue(
        text="REMOVE",
        description="Remove the existing annotation, as it is unlikely to be correct or not consistent with GO annotation guidelines")
    MODIFY = PermissibleValue(
        text="MODIFY",
        description="""The essence of the annotation is sound, but there are better terms to use (use in combination with proposed_replacement_terms). if the term is too general, then MODIFY should be used, with a proposed replacement term for the correct specific function. sometimes terms can also be overly specific and contorted, so in some cases you might want to generalize""")
    MARK_AS_OVER_ANNOTATED = PermissibleValue(
        text="MARK_AS_OVER_ANNOTATED",
        description="The term is not entirely wrong, but likely represents an over-annotation of the gene")
    UNDECIDED = PermissibleValue(
        text="UNDECIDED",
        description="""The annotation is not clear, and the reviewer is not sure what to do with it. ALWAYS USE THIS IF YOU ARE UNABLE TO ACCESS RELEVANT PUBLICATIONS""")
    PENDING = PermissibleValue(
        text="PENDING",
        description="The review entry is a stub, and the review has not been completed yet.")
    NEW = PermissibleValue(
        text="NEW",
        description="""This is a proposed annotation, not one that exists in the existing GO annotations. Use this to propose a new annotation not covered by the existing GO annotations. Use this conservatively, do not over-annotate, especially for biological process. Do not use for indirect or pleiotropic effects. Be sure you have good evidence, this can be from multiple sources.""")

    _defn = EnumDefinition(
        name="ActionEnum",
    )

class AnnotationQualifierEnum(EnumDefinitionImpl):
    """
    GO annotation qualifiers specifying the relationship between a gene product and a GO term. These correspond to the
    QUALIFIER column in GAF/GPAD files and the QuickGO API.
    """
    enables = PermissibleValue(
        text="enables",
        description="""The gene product has the molecular function activity (MF qualifier). The gene product independently possesses this catalytic or binding activity.""")
    contributes_to = PermissibleValue(
        text="contributes_to",
        description="""The gene product contributes to a molecular function as part of a complex (MF qualifier). The gene product does not independently have this activity but is required for the complex to have it. Typical for accessory/structural subunits of multi-protein complexes (e.g., accessory subunit of NADH dehydrogenase).""")
    involved_in = PermissibleValue(
        text="involved_in",
        description="The gene product is involved in a biological process (BP qualifier).")
    acts_upstream_of = PermissibleValue(
        text="acts_upstream_of",
        description="The gene product acts upstream of or within a biological process (BP qualifier).")
    acts_upstream_of_positive_effect = PermissibleValue(
        text="acts_upstream_of_positive_effect",
        description="Acts upstream of or within, positive effect (BP qualifier).")
    acts_upstream_of_negative_effect = PermissibleValue(
        text="acts_upstream_of_negative_effect",
        description="Acts upstream of or within, negative effect (BP qualifier).")
    acts_upstream_of_or_within = PermissibleValue(
        text="acts_upstream_of_or_within",
        description="Acts upstream of or within a biological process (BP qualifier).")
    acts_upstream_of_or_within_positive_effect = PermissibleValue(
        text="acts_upstream_of_or_within_positive_effect",
        description="Acts upstream of or within, positive effect (BP qualifier).")
    acts_upstream_of_or_within_negative_effect = PermissibleValue(
        text="acts_upstream_of_or_within_negative_effect",
        description="Acts upstream of or within, negative effect (BP qualifier).")
    located_in = PermissibleValue(
        text="located_in",
        description="The gene product is located in a cellular component (CC qualifier).")
    is_active_in = PermissibleValue(
        text="is_active_in",
        description="""The gene product is active in a cellular component (CC qualifier). Stronger than located_in -- implies the gene product carries out its molecular function in this location.""")
    part_of = PermissibleValue(
        text="part_of",
        description="The gene product is part of a cellular component, typically a complex (CC qualifier).")
    colocalizes_with = PermissibleValue(
        text="colocalizes_with",
        description="""The gene product colocalizes with a cellular component (CC qualifier). Weaker than located_in or part_of.""")

    _defn = EnumDefinition(
        name="AnnotationQualifierEnum",
        description="""GO annotation qualifiers specifying the relationship between a gene product and a GO term. These correspond to the QUALIFIER column in GAF/GPAD files and the QuickGO API.""",
    )

class GOTermEnum(EnumDefinitionImpl):
    """
    A term in the GO ontology (including roots, to allow ND annotations)
    """
    _defn = EnumDefinition(
        name="GOTermEnum",
        description="A term in the GO ontology (including roots, to allow ND annotations)",
    )

class GOMolecularActivityEnum(EnumDefinitionImpl):
    """
    A molecular activity term in the GO ontology
    """
    _defn = EnumDefinition(
        name="GOMolecularActivityEnum",
        description="A molecular activity term in the GO ontology",
    )

class GOBiologicalProcessEnum(EnumDefinitionImpl):
    """
    A biological process term in the GO ontology
    """
    _defn = EnumDefinition(
        name="GOBiologicalProcessEnum",
        description="A biological process term in the GO ontology",
    )

class GOCellularLocationEnum(EnumDefinitionImpl):
    """
    A cellular location term in the GO ontology (excludes protein-containing complexes)
    """
    _defn = EnumDefinition(
        name="GOCellularLocationEnum",
        description="A cellular location term in the GO ontology (excludes protein-containing complexes)",
    )

class GOProteinContainingComplexEnum(EnumDefinitionImpl):
    """
    A protein-containing complex term in the GO ontology
    """
    _defn = EnumDefinition(
        name="GOProteinContainingComplexEnum",
        description="A protein-containing complex term in the GO ontology",
    )

class ROTermEnum(EnumDefinitionImpl):
    """
    A term in the relation ontology
    """
    _defn = EnumDefinition(
        name="ROTermEnum",
        description="A term in the relation ontology",
    )

class ProductTypeEnum(EnumDefinitionImpl):
    """
    Type of gene product
    """
    PROTEIN = PermissibleValue(
        text="PROTEIN",
        description="Protein-coding gene",
        meaning=SO["0001217"])
    MIRNA = PermissibleValue(
        text="MIRNA",
        description="microRNA",
        meaning=SO["0000276"])
    LNCRNA = PermissibleValue(
        text="LNCRNA",
        description="Long non-coding RNA",
        meaning=SO["0001877"])
    SNORNA = PermissibleValue(
        text="SNORNA",
        description="Small nucleolar RNA",
        meaning=SO["0000275"])
    SNRNA = PermissibleValue(
        text="SNRNA",
        description="Small nuclear RNA",
        meaning=SO["0000274"])
    TRNA = PermissibleValue(
        text="TRNA",
        description="Transfer RNA",
        meaning=SO["0000253"])
    RRNA = PermissibleValue(
        text="RRNA",
        description="Ribosomal RNA",
        meaning=SO["0000252"])
    PIRNA = PermissibleValue(
        text="PIRNA",
        description="PIWI-interacting RNA",
        meaning=SO["0001035"])
    ANTISENSE_RNA = PermissibleValue(
        text="ANTISENSE_RNA",
        description="Antisense RNA",
        meaning=SO["0000644"])
    PSEUDOGENE = PermissibleValue(
        text="PSEUDOGENE",
        description="Pseudogene",
        meaning=SO["0000336"])
    OTHER_NCRNA = PermissibleValue(
        text="OTHER_NCRNA",
        description="Other non-coding RNA",
        meaning=SO["0000655"])

    _defn = EnumDefinition(
        name="ProductTypeEnum",
        description="Type of gene product",
    )

class GeneReviewStatusEnum(EnumDefinitionImpl):
    """
    Status of the gene review process
    """
    INITIALIZED = PermissibleValue(
        text="INITIALIZED",
        description="All annotations have action PENDING - review has been initialized but not started")
    IN_PROGRESS = PermissibleValue(
        text="IN_PROGRESS",
        description="""At least one annotation is PENDING and at least one annotation is not PENDING - review is underway""")
    DRAFT = PermissibleValue(
        text="DRAFT",
        description="""No PENDING annotations, but may have validation warnings - review is complete but needs refinement""")
    COMPLETE = PermissibleValue(
        text="COMPLETE",
        description="No PENDING annotations and no validation warnings - review is fully complete and validated")

    _defn = EnumDefinition(
        name="GeneReviewStatusEnum",
        description="Status of the gene review process",
    )

class ManuscriptSection(EnumDefinitionImpl):
    """
    Sections of a scientific manuscript or publication
    """
    TITLE = PermissibleValue(
        text="TITLE",
        description="Title section",
        meaning=IAO["0000305"])
    ABSTRACT = PermissibleValue(
        text="ABSTRACT",
        description="Abstract",
        meaning=IAO["0000315"])
    KEYWORDS = PermissibleValue(
        text="KEYWORDS",
        description="Keywords",
        meaning=IAO["0000630"])
    INTRODUCTION = PermissibleValue(
        text="INTRODUCTION",
        description="Introduction/Background",
        meaning=IAO["0000316"])
    LITERATURE_REVIEW = PermissibleValue(
        text="LITERATURE_REVIEW",
        description="Literature review",
        meaning=IAO["0000639"])
    METHODS = PermissibleValue(
        text="METHODS",
        description="Methods/Materials and Methods",
        meaning=IAO["0000317"])
    RESULTS = PermissibleValue(
        text="RESULTS",
        description="Results",
        meaning=IAO["0000318"])
    DISCUSSION = PermissibleValue(
        text="DISCUSSION",
        description="Discussion",
        meaning=IAO["0000319"])
    CONCLUSIONS = PermissibleValue(
        text="CONCLUSIONS",
        description="Conclusions",
        meaning=IAO["0000615"])
    APPENDICES = PermissibleValue(
        text="APPENDICES",
        description="Appendices",
        meaning=IAO["0000326"])
    SUPPLEMENTARY_MATERIAL = PermissibleValue(
        text="SUPPLEMENTARY_MATERIAL",
        description="Supplementary material",
        meaning=IAO["0000326"])
    DATABASE_ENTRY = PermissibleValue(
        text="DATABASE_ENTRY",
        description="Database entry")
    OTHER = PermissibleValue(
        text="OTHER",
        description="Other main text section")

    _defn = EnumDefinition(
        name="ManuscriptSection",
        description="Sections of a scientific manuscript or publication",
    )

class RuleTypeEnum(EnumDefinitionImpl):
    """
    Type of UniProt annotation rule
    """
    ARBA = PermissibleValue(
        text="ARBA",
        description="Association-Rule-Based Annotator rule (automatically mined)")
    UNIRULE = PermissibleValue(
        text="UNIRULE",
        description="Expert-curated UniRule")

    _defn = EnumDefinition(
        name="RuleTypeEnum",
        description="Type of UniProt annotation rule",
    )

class RuleReviewStatusEnum(EnumDefinitionImpl):
    """
    Status of the rule review
    """
    PENDING = PermissibleValue(
        text="PENDING",
        description="Review has not been started")
    IN_PROGRESS = PermissibleValue(
        text="IN_PROGRESS",
        description="Review is underway")
    COMPLETE = PermissibleValue(
        text="COMPLETE",
        description="Review is complete")

    _defn = EnumDefinition(
        name="RuleReviewStatusEnum",
        description="Status of the rule review",
    )

class RuleActionEnum(EnumDefinitionImpl):
    """
    Recommended action for the rule
    """
    ACCEPT = PermissibleValue(
        text="ACCEPT",
        description="Rule is correct and should be kept as-is")
    MODIFY = PermissibleValue(
        text="MODIFY",
        description="Rule needs modification (see suggested_modifications)")
    DEPRECATE = PermissibleValue(
        text="DEPRECATE",
        description="Rule should be removed or retired")
    SPLIT = PermissibleValue(
        text="SPLIT",
        description="Rule should be split into multiple more specific rules")
    MERGE = PermissibleValue(
        text="MERGE",
        description="Rule should be merged with another related rule")
    UNDECIDED = PermissibleValue(
        text="UNDECIDED",
        description="Unable to determine appropriate action")

    _defn = EnumDefinition(
        name="RuleActionEnum",
        description="Recommended action for the rule",
    )

class ParsimonyEnum(EnumDefinitionImpl):
    """
    Assessment of rule parsimony (simplicity vs complexity)
    """
    PARSIMONIOUS = PermissibleValue(
        text="PARSIMONIOUS",
        description="Rule is appropriately simple - conditions are necessary and sufficient")
    ACCEPTABLE = PermissibleValue(
        text="ACCEPTABLE",
        description="Rule complexity is reasonable given the biological context")
    REDUNDANT = PermissibleValue(
        text="REDUNDANT",
        description="Some conditions are redundant and could be removed")
    OVERLY_COMPLEX = PermissibleValue(
        text="OVERLY_COMPLEX",
        description="Rule has unnecessary complexity that should be simplified")

    _defn = EnumDefinition(
        name="ParsimonyEnum",
        description="Assessment of rule parsimony (simplicity vs complexity)",
    )

class LiteratureSupportEnum(EnumDefinitionImpl):
    """
    Level of literature support for the rule
    """
    STRONG = PermissibleValue(
        text="STRONG",
        description="Multiple high-quality papers directly support the domain-function relationship")
    MODERATE = PermissibleValue(
        text="MODERATE",
        description="Some supporting evidence exists but not comprehensive")
    WEAK = PermissibleValue(
        text="WEAK",
        description="Limited evidence, mostly indirect or from computational studies")
    NONE = PermissibleValue(
        text="NONE",
        description="No literature support found")
    CONTRADICTED = PermissibleValue(
        text="CONTRADICTED",
        description="Literature contradicts the rule's predicted function")

    _defn = EnumDefinition(
        name="LiteratureSupportEnum",
        description="Level of literature support for the rule",
    )

class OverlapEnum(EnumDefinitionImpl):
    """
    Assessment of condition overlap/redundancy
    """
    NONE = PermissibleValue(
        text="NONE",
        description="Conditions are independent and non-overlapping")
    MINOR = PermissibleValue(
        text="MINOR",
        description="Slight overlap but conditions add meaningful specificity")
    SIGNIFICANT = PermissibleValue(
        text="SIGNIFICANT",
        description="Substantial overlap - conditions may be capturing the same thing")
    COMPLETE = PermissibleValue(
        text="COMPLETE",
        description="Conditions are essentially equivalent/redundant")

    _defn = EnumDefinition(
        name="OverlapEnum",
        description="Assessment of condition overlap/redundancy",
    )

class SpecificityEnum(EnumDefinitionImpl):
    """
    Assessment of GO term specificity
    """
    TOO_BROAD = PermissibleValue(
        text="TOO_BROAD",
        description="GO term is too general - a more specific term should be used")
    APPROPRIATE = PermissibleValue(
        text="APPROPRIATE",
        description="GO term specificity matches the evidence")
    TOO_NARROW = PermissibleValue(
        text="TOO_NARROW",
        description="GO term is overly specific for what the domains predict")
    MISMATCHED = PermissibleValue(
        text="MISMATCHED",
        description="GO term is in wrong branch or aspect")

    _defn = EnumDefinition(
        name="SpecificityEnum",
        description="Assessment of GO term specificity",
    )

class TaxonomicScopeEnum(EnumDefinitionImpl):
    """
    Assessment of taxonomic restriction appropriateness
    """
    TOO_BROAD = PermissibleValue(
        text="TOO_BROAD",
        description="Taxon is too inclusive - should be restricted further")
    APPROPRIATE = PermissibleValue(
        text="APPROPRIATE",
        description="Taxonomic scope matches the domain's evolutionary distribution")
    TOO_NARROW = PermissibleValue(
        text="TOO_NARROW",
        description="Taxon is overly restrictive - function applies more broadly")
    MISSING = PermissibleValue(
        text="MISSING",
        description="Rule lacks necessary taxonomic restriction")
    UNNECESSARY = PermissibleValue(
        text="UNNECESSARY",
        description="Taxonomic restriction is not needed for this domain")

    _defn = EnumDefinition(
        name="TaxonomicScopeEnum",
        description="Assessment of taxonomic restriction appropriateness",
    )

class ConditionTypeEnum(EnumDefinitionImpl):
    """
    Types of conditions in rule antecedents
    """
    INTERPRO = PermissibleValue(
        text="INTERPRO",
        description="InterPro domain/family")
    FUNFAM = PermissibleValue(
        text="FUNFAM",
        description="CATH FunFam functional family")
    PANTHER = PermissibleValue(
        text="PANTHER",
        description="PANTHER family")
    PFAM = PermissibleValue(
        text="PFAM",
        description="Pfam domain")
    TAXON = PermissibleValue(
        text="TAXON",
        description="Taxonomic constraint")
    SEQUENCE_LENGTH = PermissibleValue(
        text="SEQUENCE_LENGTH",
        description="Sequence length constraint")
    OTHER = PermissibleValue(
        text="OTHER",
        description="Other condition type")

    _defn = EnumDefinition(
        name="ConditionTypeEnum",
        description="Types of conditions in rule antecedents",
    )

class ProteinDatabaseEnum(EnumDefinitionImpl):
    """
    Protein database types for rule analysis
    """
    SWISSPROT = PermissibleValue(
        text="SWISSPROT",
        description="Swiss-Prot (reviewed, manually curated proteins)")
    TREMBL = PermissibleValue(
        text="TREMBL",
        description="TrEMBL (unreviewed, automatically annotated proteins)")
    UNIPROT = PermissibleValue(
        text="UNIPROT",
        description="Full UniProtKB (Swiss-Prot + TrEMBL)")

    _defn = EnumDefinition(
        name="ProteinDatabaseEnum",
        description="Protein database types for rule analysis",
    )

class InterProTypeEnum(EnumDefinitionImpl):
    """
    InterPro entry types categorizing protein signatures
    """
    FAMILY = PermissibleValue(
        text="FAMILY",
        description="Protein family (groups of proteins sharing similar sequence and function)")
    DOMAIN = PermissibleValue(
        text="DOMAIN",
        description="Protein domain (distinct functional or structural unit)")
    ACTIVE_SITE = PermissibleValue(
        text="ACTIVE_SITE",
        description="Active site (residues directly involved in catalysis)")
    BINDING_SITE = PermissibleValue(
        text="BINDING_SITE",
        description="Binding site (residues involved in binding substrates/ligands)")
    CONSERVED_SITE = PermissibleValue(
        text="CONSERVED_SITE",
        description="Conserved site (conserved residues with functional significance)")
    REPEAT = PermissibleValue(
        text="REPEAT",
        description="Repeat (short sequence motif that occurs multiple times)")
    HOMOLOGOUS_SUPERFAMILY = PermissibleValue(
        text="HOMOLOGOUS_SUPERFAMILY",
        description="Homologous superfamily (proteins with distant evolutionary relationships)")
    PTM = PermissibleValue(
        text="PTM",
        description="Post-translational modification site")

    _defn = EnumDefinition(
        name="InterProTypeEnum",
        description="InterPro entry types categorizing protein signatures",
    )

class OverlapInterpretationEnum(EnumDefinitionImpl):
    """
    Automated interpretation of domain overlap patterns
    """
    REDUNDANT = PermissibleValue(
        text="REDUNDANT",
        description="Very high overlap (Jaccard > 0.9), conditions are nearly identical")
    SUBSET = PermissibleValue(
        text="SUBSET",
        description="One condition is a subset of the other (containment > 0.95)")
    HIGH_OVERLAP = PermissibleValue(
        text="HIGH_OVERLAP",
        description="High overlap (Jaccard > 0.5), conditions are similar")
    MODERATE = PermissibleValue(
        text="MODERATE",
        description="Moderate overlap (0.2 < Jaccard <= 0.5)")
    LOW = PermissibleValue(
        text="LOW",
        description="Low overlap (Jaccard <= 0.2), conditions are mostly distinct")
    DISJOINT = PermissibleValue(
        text="DISJOINT",
        description="No overlap (intersection = 0), conditions are completely distinct")

    _defn = EnumDefinition(
        name="OverlapInterpretationEnum",
        description="Automated interpretation of domain overlap patterns",
    )

class EntryTypeEnum(EnumDefinitionImpl):
    """
    Type of entry in a rule review (domain/family condition or GO term target)
    """
    INTERPRO = PermissibleValue(
        text="INTERPRO",
        description="InterPro entry (domain, family, repeat, etc.)")
    FUNFAM = PermissibleValue(
        text="FUNFAM",
        description="CATH FunFam (functional family from CATH database)")
    PANTHER = PermissibleValue(
        text="PANTHER",
        description="PANTHER family or subfamily")
    GO_TERM = PermissibleValue(
        text="GO_TERM",
        description="Gene Ontology term (annotation target)")

    _defn = EnumDefinition(
        name="EntryTypeEnum",
        description="Type of entry in a rule review (domain/family condition or GO term target)",
    )

class EntryRelationshipEnum(EnumDefinitionImpl):
    """
    Type of relationship between entries in a rule
    """
    PREDICTS = PermissibleValue(
        text="PREDICTS",
        description="""This entry predicts the target (this ⊆ target). Selected when containment_a_in_b is highest among {jaccard+0.05, containment_a_in_b, containment_b_in_a}.""")
    PREDICTED_BY = PermissibleValue(
        text="PREDICTED_BY",
        description="""This entry is predicted by the target (target ⊆ this). Selected when containment_b_in_a is highest among {jaccard+0.05, containment_a_in_b, containment_b_in_a}.""")
    EQUIV = PermissibleValue(
        text="EQUIV",
        description="""This entry is equivalent to the target (bidirectional high similarity). Selected when jaccard_boosted (jaccard + 0.05) is highest among {jaccard+0.05, containment_a_in_b, containment_b_in_a}.""")

    _defn = EnumDefinition(
        name="EntryRelationshipEnum",
        description="Type of relationship between entries in a rule",
    )

class FunctionalIsoformTypeEnum(EnumDefinitionImpl):
    """
    Type of functional isoform or product. Distinguishes between different mechanisms that produce functionally
    distinct forms of a gene product.
    """
    SPLICE_VARIANT = PermissibleValue(
        text="SPLICE_VARIANT",
        description="""Alternative splicing produces functionally distinct isoforms. Maps to one or more UniProt isoform IDs (e.g., P19544-1, P19544-2).""")
    SPLICE_CLASS = PermissibleValue(
        text="SPLICE_CLASS",
        description="""A class of splice variants that share functional properties. Groups multiple UniProt isoform IDs that have similar functions. Example: WT1 +KTS isoforms (multiple UniProt IDs) vs -KTS isoforms.""")
    CLEAVAGE_PRODUCT = PermissibleValue(
        text="CLEAVAGE_PRODUCT",
        description="""Post-translational proteolytic cleavage produces distinct peptides. Maps to UniProt chain IDs (PRO_NNNNNNN from FT PEPTIDE lines). Example: POMC cleavage into ACTH, alpha-MSH, beta-endorphin.""")
    MODIFICATION_STATE = PermissibleValue(
        text="MODIFICATION_STATE",
        description="""Post-translational modification creates functionally distinct forms. Example: Phosphorylated vs unphosphorylated forms with different activities.""")
    CONFORMATIONAL_STATE = PermissibleValue(
        text="CONFORMATIONAL_STATE",
        description="""Different conformational states with distinct functions. Example: GTP-bound vs GDP-bound forms of GTPases.""")

    _defn = EnumDefinition(
        name="FunctionalIsoformTypeEnum",
        description="""Type of functional isoform or product. Distinguishes between different mechanisms that produce functionally distinct forms of a gene product.""",
    )

class FunctionalIsoformMappingTypeEnum(EnumDefinitionImpl):
    """
    Type of identifier that a functional isoform maps to
    """
    UNIPROT_ISOFORM = PermissibleValue(
        text="UNIPROT_ISOFORM",
        description="UniProt isoform ID (e.g., P19544-1, Q07817-2)")
    UNIPROT_CHAIN = PermissibleValue(
        text="UNIPROT_CHAIN",
        description="UniProt chain/peptide ID from FT PEPTIDE (e.g., PRO_0000024969)")

    _defn = EnumDefinition(
        name="FunctionalIsoformMappingTypeEnum",
        description="Type of identifier that a functional isoform maps to",
    )

class PredictedTermTypeEnum(EnumDefinitionImpl):
    """
    Type of predicted annotation term
    """
    EC = PermissibleValue(
        text="EC",
        description="Enzyme Commission number (e.g., EC:2.7.7.87)")
    GO_MF = PermissibleValue(
        text="GO_MF",
        description="GO Molecular Function term")
    GO_BP = PermissibleValue(
        text="GO_BP",
        description="GO Biological Process term")
    GO_CC = PermissibleValue(
        text="GO_CC",
        description="GO Cellular Component term")

    _defn = EnumDefinition(
        name="PredictedTermTypeEnum",
        description="Type of predicted annotation term",
    )

class PredictionAssessmentEnum(EnumDefinitionImpl):
    """
    Assessment categories for computational predictions, based on de Crécy-Lagard et al. 2025 (PMID:40703034) Fig. 4.
    """
    COR = PermissibleValue(
        text="COR",
        description="""Correct prediction - validated by literature/bioinformatic evidence as a genuinely novel correct prediction (CS=2)""")
    CNN = PermissibleValue(
        text="CNN",
        description="""Correct but Not Novel - the prediction matches an annotation already present in UniProt or in the training data. Not a novel discovery (CS=2)""")
    LSP = PermissibleValue(
        text="LSP",
        description="""Less Precise - the prediction is more generic than the existing annotation. Correct at a higher level but not informative (CS=2)""")
    UNC = PermissibleValue(
        text="UNC",
        description="""Uncertain - the prediction cannot be validated or refuted with available evidence. Requires additional experiments or data (CS=1)""")
    PLI = PermissibleValue(
        text="PLI",
        description="""Paralog Incorrect - wrong prediction due to failure to distinguish nonisofunctional paralogs within a protein superfamily (CS=0)""")
    NPI = PermissibleValue(
        text="NPI",
        description="""Nonparalog Incorrect - wrong prediction refuted by evidence: pathway absent in organism, activity belongs to a different gene, or published data contradict the prediction (CS=0)""")
    REP = PermissibleValue(
        text="REP",
        description="""Repetition - frequency-biased duplication of a common EC/GO term. The model assigns a high-frequency term (e.g., histidine kinase) to proteins with no sequence similarity to that family (CS=0)""")

    _defn = EnumDefinition(
        name="PredictionAssessmentEnum",
        description="""Assessment categories for computational predictions, based on de Crécy-Lagard et al. 2025 (PMID:40703034) Fig. 4.""",
    )

class PredictionErrorTypeEnum(EnumDefinitionImpl):
    """
    Types of errors that lead to incorrect functional predictions. The first block is based on Table 1 of de
    Crécy-Lagard et al. 2025 (PMID:40703034); the trailing values capture additional, recurrent failure patterns
    observed when evaluating sequence- and LLM-based function predictors (e.g. ProtNLM2, BioReason-Pro) that Table 1
    does not name explicitly.
    """
    FAILURE_TO_CAPTURE_LITERATURE = PermissibleValue(
        text="FAILURE_TO_CAPTURE_LITERATURE",
        description="""Type 1: Function is known and published but not captured in the database used for training. The protein is falsely labeled as unknown.""")
    NAMING_INCONSISTENCY = PermissibleValue(
        text="NAMING_INCONSISTENCY",
        description="""Type 2: Inconsistent naming of the same entity across databases leads to missed or incorrect propagation.""")
    MULTIPLE_FUNCTIONS = PermissibleValue(
        text="MULTIPLE_FUNCTIONS",
        description="""Type 3: Protein has multiple functions (fusion, moonlighting, promiscuity) and only one function is captured or a non-primary function is predicted.""")
    CURATION_MISTAKE = PermissibleValue(
        text="CURATION_MISTAKE",
        description="""Type 4: The training data contain an incorrect annotation from a biocuration error or an outdated annotation that has since been corrected.""")
    EXPERIMENTAL_MISTAKE = PermissibleValue(
        text="EXPERIMENTAL_MISTAKE",
        description="""Type 5: The training data are based on experimental findings that have been refuted or are inconclusive.""")
    PARALOG_OVERANNOTATION = PermissibleValue(
        text="PARALOG_OVERANNOTATION",
        description="""Type 6: Annotation wrongly propagated to a nonisofunctional paralog. The model fails to distinguish between paralogs with different substrate specificities or functions within the same superfamily.""")
    FREQUENCY_BIAS = PermissibleValue(
        text="FREQUENCY_BIAS",
        description="""The model makes predictions biased toward high-frequency labels in the training data, regardless of sequence features. Common with EC numbers like histidine kinase (2.7.13.3) or PTS transporter (2.7.1.69).""")
    TRAINING_DATA_CONTAMINATION = PermissibleValue(
        text="TRAINING_DATA_CONTAMINATION",
        description="""The prediction appears novel but the annotation was already present in the version of the database used to build the training set.""")
    PATHWAY_CONTEXT_IGNORED = PermissibleValue(
        text="PATHWAY_CONTEXT_IGNORED",
        description="""The model ignores metabolic/pathway context. The predicted activity requires a pathway that is absent from the organism's genome.""")
    IN_VITRO_NOT_IN_VIVO = PermissibleValue(
        text="IN_VITRO_NOT_IN_VIVO",
        description="""The predicted activity can be demonstrated in vitro but does not represent the in vivo biological function (e.g., promiscuous activity at orders of magnitude lower rate than the dedicated enzyme).""")
    PSEUDOENZYME_OVERANNOTATION = PermissibleValue(
        text="PSEUDOENZYME_OVERANNOTATION",
        description="""The model assigns the ancestral catalytic activity of a domain family to a member that retains the fold but has lost or degraded the catalytic residues (a pseudoenzyme), failing to detect substituted/missing active-site residues. E.g. predicting demethylase activity for a JmjC protein with a degenerate active site, chitinase activity for a member lacking the catalytic glutamate, or peroxidase activity for a peroxiredoxin that has lost its resolving cysteine and instead acts as a chaperone. A special case of MULTIPLE_FUNCTIONS / neofunctionalization where the divergence is specifically loss of catalysis.""")
    LOCALIZATION_DEFAULT = PermissibleValue(
        text="LOCALIZATION_DEFAULT",
        description="""The model defaults to a cytosolic/cytoplasmic subcellular localization when no transmembrane or signal-sequence features are detected, mislocalizing secreted, periplasmic, organellar (mitochondrial, ER, vacuolar), or membrane proteins. Tends to succeed only when a domain/family name explicitly encodes the compartment (e.g. BiP/KAR2 -> ER).""")
    TAXON_CONSTRAINT_VIOLATION = PermissibleValue(
        text="TAXON_CONSTRAINT_VIOLATION",
        description="""The predicted term is valid only in a lineage/kingdom different from the organism (e.g. animal-specific 'neuronal cell body' or adaptive-immune terms predicted for a plant or bacterial protein), reflecting homology transfer from a better-studied taxon. Distinct from PATHWAY_CONTEXT_IGNORED (a missing metabolic pathway) in that the violated constraint is taxonomic rather than pathway-level.""")
    WRONG_INPUT_SEQUENCE = PermissibleValue(
        text="WRONG_INPUT_SEQUENCE",
        description="""A data-pipeline error rather than a model-reasoning error: the predictor was supplied the wrong input (e.g. the sequence of a different gene), so every output describes the wrong protein. Recorded to distinguish upstream pipeline mistakes from genuine model mispredictions.""")
    DOMAIN_ARCHITECTURE_MISMATCH = PermissibleValue(
        text="DOMAIN_ARCHITECTURE_MISMATCH",
        description="""The predicted activity requires a domain, catalytic region, or complete architecture absent from the selected protein. Includes transfer of a multidomain donor's activity through a shared noncatalytic domain. Does not establish that the target is a fold-retaining pseudoenzyme, that its gene model is wrong, or that the historical model input differed.""")
    COMPLEX_ACTIVITY_TRANSFER = PermissibleValue(
        text="COMPLEX_ACTIVITY_TRANSFER",
        description="""Intrinsic catalytic activity of a molecular complex is assigned to a noncatalytic accessory subunit. Participation in the complex or its biological process does not establish that the subunit catalyzes the reaction.""")

    _defn = EnumDefinition(
        name="PredictionErrorTypeEnum",
        description="""Types of errors that lead to incorrect functional predictions. The first block is based on Table 1 of de Crécy-Lagard et al. 2025 (PMID:40703034); the trailing values capture additional, recurrent failure patterns observed when evaluating sequence- and LLM-based function predictors (e.g. ProtNLM2, BioReason-Pro) that Table 1 does not name explicitly.""",
    )

class ReferenceRelevanceEnum(EnumDefinitionImpl):
    """
    Reviewer's assessment of how relevant a reference is to the gene's function and review.
    """
    HIGH = PermissibleValue(
        text="HIGH",
        description="""Directly establishes or strongly informs the gene's function, mechanism, process, or localization""")
    MEDIUM = PermissibleValue(
        text="MEDIUM",
        description="Provides supporting or corroborating evidence for a function or annotation")
    LOW = PermissibleValue(
        text="LOW",
        description="Background or contextual only (e.g. family/pathway reviews, methods, or a passing mention)")
    NONE = PermissibleValue(
        text="NONE",
        description="Not relevant to this gene's function (a candidate for removal from the references)")

    _defn = EnumDefinition(
        name="ReferenceRelevanceEnum",
        description="Reviewer's assessment of how relevant a reference is to the gene's function and review.",
    )

class ReferenceCorrectnessEnum(EnumDefinitionImpl):
    """
    Reviewer's overall manual assessment of a reference's trustworthiness, spanning both citation correctness (does
    the identifier point to the intended paper that supports its use) and scientific soundness (is that paper's claim
    reliable). Single-valued: record the most salient issue and elaborate in review_notes. Complements is_invalid
    (retracted/replaced) and full_text_unavailable.
    """
    VERIFIED = PermissibleValue(
        text="VERIFIED",
        description="""Identifier resolves to the intended paper, which supports how it is used, with no soundness concerns""")
    UNVERIFIED = PermissibleValue(
        text="UNVERIFIED",
        description="Not yet manually checked (the default state)")
    WRONG_IDENTIFIER = PermissibleValue(
        text="WRONG_IDENTIFIER",
        description="""Identifier resolves to a DIFFERENT paper than intended (e.g. a PMID pointing to an unrelated article)""")
    MISCITED = PermissibleValue(
        text="MISCITED",
        description="Paper is correctly identified but does not actually support the claim it is cited for")
    DISPUTED = PermissibleValue(
        text="DISPUTED",
        description="Correctly cited, but the paper's central claim is contradicted or contested by other evidence")
    LOW_QUALITY = PermissibleValue(
        text="LOW_QUALITY",
        description="Correctly cited, but methodologically weak or preliminary; treat its conclusions with caution")

    _defn = EnumDefinition(
        name="ReferenceCorrectnessEnum",
        description="""Reviewer's overall manual assessment of a reference's trustworthiness, spanning both citation correctness (does the identifier point to the intended paper that supports its use) and scientific soundness (is that paper's claim reliable). Single-valued: record the most salient issue and elaborate in review_notes. Complements is_invalid (retracted/replaced) and full_text_unavailable.""",
    )

class FindingReviewStatusEnum(EnumDefinitionImpl):
    """
    Reviewer's assessment of the empirical standing of a specific finding (a statement extracted from a reference) in
    light of other evidence. Unlike ReferenceCorrectnessEnum, which judges a whole reference, this applies per
    finding: a paper may have some findings that stand and others that have been overturned. Use superseded_by to
    point to the reference(s) responsible.
    """
    CURRENT = PermissibleValue(
        text="CURRENT",
        description="The finding is consistent with the body of evidence and can be curated from")
    CORROBORATED = PermissibleValue(
        text="CORROBORATED",
        description="The finding is independently supported by additional evidence")
    DISPUTED = PermissibleValue(
        text="DISPUTED",
        description="""The finding is contested or contradicted by other evidence, but not definitively refuted; curate with caution""")
    OVERTURNED = PermissibleValue(
        text="OVERTURNED",
        description="""The finding has been refuted or superseded by later, stronger evidence and should NOT be curated from; record the overturning reference(s) in superseded_by""")
    UNVERIFIED = PermissibleValue(
        text="UNVERIFIED",
        description="The finding has not yet been manually assessed (default)")

    _defn = EnumDefinition(
        name="FindingReviewStatusEnum",
        description="""Reviewer's assessment of the empirical standing of a specific finding (a statement extracted from a reference) in light of other evidence. Unlike ReferenceCorrectnessEnum, which judges a whole reference, this applies per finding: a paper may have some findings that stand and others that have been overturned. Use superseded_by to point to the reference(s) responsible.""",
    )

class KnowledgeGapKindEnum(EnumDefinitionImpl):
    """
    The kind of ignorance a knowledge gap represents, which determines who can resolve it. A single gap may carry
    several values when it is a blend.
    """
    BIOLOGY = PermissibleValue(
        text="BIOLOGY",
        description="""Nobody knows; resolvable only by new experiments. This is the unknome and the primary target of the Function Knowledge Gaps project.""")
    CURATION = PermissibleValue(
        text="CURATION",
        description="""The knowledge exists in the literature but is not yet annotated, or is annotated too generically. Resolvable by curation.""")
    ONTOLOGY = PermissibleValue(
        text="ONTOLOGY",
        description="""The knowledge exists but no GO/ontology term can express it (e.g. \"structural subunit of complex X\", or a novel activity). Resolvable by ontology development; usually paired with proposed_new_terms.""")

    _defn = EnumDefinition(
        name="KnowledgeGapKindEnum",
        description="""The kind of ignorance a knowledge gap represents, which determines who can resolve it. A single gap may carry several values when it is a blend.""",
    )

class KnowledgeGapAspectEnum(EnumDefinitionImpl):
    """
    Which GO aspect (or pattern) is dark for a knowledge gap. Most "dark" genes are not uniformly dark.
    """
    MF_DARK = PermissibleValue(
        text="MF_DARK",
        description="""Process/location known, molecular mechanism unknown. The most common and most insidious case — rich BP/CC make the gene look known. The \"protein binding\" smell lives here.""")
    BP_DARK = PermissibleValue(
        text="BP_DARK",
        description="An activity is known but not what it is for (common in microbial/plant metabolism).")
    CC_DARK = PermissibleValue(
        text="CC_DARK",
        description="Function known, but where/when unknown.")
    WHOLLY_DARK = PermissibleValue(
        text="WHOLLY_DARK",
        description="Only root terms / IEA / \"protein binding\" survive review (the deep unknome).")
    RESIDUAL_SUBGAP = PermissibleValue(
        text="RESIDUAL_SUBGAP",
        description="""The core function is textbook-solid, but one sharp, load-bearing mechanistic hole remains (e.g. an unidentified GEF/GAP, a catalysis-independent scaffolding mechanism, an unidentified recruit). Easy to miss because the gene looks finished.""")

    _defn = EnumDefinition(
        name="KnowledgeGapAspectEnum",
        description="""Which GO aspect (or pattern) is dark for a knowledge gap. Most \"dark\" genes are not uniformly dark.""",
    )

class KnowledgeGapStatusEnum(EnumDefinitionImpl):
    """
    Lifecycle status of a knowledge gap, tracking progress toward resolution.
    """
    OPEN = PermissibleValue(
        text="OPEN",
        description="Unresolved and not under active, evidence-producing investigation.")
    NARROWING = PermissibleValue(
        text="NARROWING",
        description="Under active investigation with emerging but still incomplete evidence.")
    CLOSING = PermissibleValue(
        text="CLOSING",
        description="""Function-defining evidence exists (e.g. recent preprints) but has not yet propagated to peer-reviewed, GO-curated form.""")
    RESOLVED = PermissibleValue(
        text="RESOLVED",
        description="The gap has been closed; retained for provenance/history.")

    _defn = EnumDefinition(
        name="KnowledgeGapStatusEnum",
        description="Lifecycle status of a knowledge gap, tracking progress toward resolution.",
    )

class PublicationTypeEnum(EnumDefinitionImpl):
    """
    The kind of publication or source a reference is. For PMIDs this is inferred from the PubMed publication-type
    ('PT') metadata; for non-literature references it is inferred from the identifier scheme. Used to test hypotheses
    about which evidence sources (primary papers, reviews, abstracts, deep research) suffice for GO annotation review.
    """
    PRIMARY_RESEARCH = PermissibleValue(
        text="PRIMARY_RESEARCH",
        description="""An original/primary research article reporting new experimental or observational results (PubMed 'Journal Article' without a more specific review/secondary type).""")
    REVIEW = PermissibleValue(
        text="REVIEW",
        description="""A narrative review article that synthesizes prior literature (PubMed PT 'Review'). Reviews often carry phylogenetic/comparative reasoning and broad functional context.""")
    SYSTEMATIC_REVIEW = PermissibleValue(
        text="SYSTEMATIC_REVIEW",
        description="A systematic review (PubMed PT 'Systematic Review').")
    META_ANALYSIS = PermissibleValue(
        text="META_ANALYSIS",
        description="A meta-analysis combining results across studies (PubMed PT 'Meta-Analysis').")
    COMMENT_EDITORIAL = PermissibleValue(
        text="COMMENT_EDITORIAL",
        description="""A comment, editorial, letter, or news item (PubMed PT 'Comment', 'Editorial', 'Letter', 'News').""")
    CASE_REPORT = PermissibleValue(
        text="CASE_REPORT",
        description="A clinical case report (PubMed PT 'Case Reports').")
    PREPRINT = PermissibleValue(
        text="PREPRINT",
        description="A preprint or other not-yet-peer-reviewed manuscript (PubMed PT 'Preprint').")
    DATABASE = PermissibleValue(
        text="DATABASE",
        description="""A database record or curated method reference rather than a narrative publication (e.g. a GO_REF, Reactome pathway, or UniProt entry).""")
    BIOINFORMATICS = PermissibleValue(
        text="BIOINFORMATICS",
        description="""A local ad-hoc bioinformatics analysis carried out for this review, referenced via a 'file:' identifier (e.g. a bioinformatics RESULTS.md).""")
    DEEP_RESEARCH = PermissibleValue(
        text="DEEP_RESEARCH",
        description="""An AI/LLM deep-research report generated for this review, referenced via a 'file:' identifier (e.g. GENE-deep-research-PROVIDER.md).""")
    OTHER = PermissibleValue(
        text="OTHER",
        description="A publication or source that does not fit the other categories.")
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        description="The publication type could not be determined (e.g. PubMed metadata unavailable).")

    _defn = EnumDefinition(
        name="PublicationTypeEnum",
        description="""The kind of publication or source a reference is. For PMIDs this is inferred from the PubMed publication-type ('PT') metadata; for non-literature references it is inferred from the identifier scheme. Used to test hypotheses about which evidence sources (primary papers, reviews, abstracts, deep research) suffice for GO annotation review.""",
    )

class GoCamReviewStatusEnum(EnumDefinitionImpl):
    """
    Progress state of a GO-CAM model review.
    """
    DRAFT = PermissibleValue(
        text="DRAFT",
        description="Review started; activities not yet fully assessed.")
    IN_PROGRESS = PermissibleValue(
        text="IN_PROGRESS",
        description="Some activities reviewed; review ongoing.")
    COMPLETE = PermissibleValue(
        text="COMPLETE",
        description="All activities reviewed.")

    _defn = EnumDefinition(
        name="GoCamReviewStatusEnum",
        description="Progress state of a GO-CAM model review.",
    )

class GoCamClaimVerdictEnum(EnumDefinitionImpl):
    """
    Forensic-review verdict for a GO-CAM activity, mirroring the OK / UNCERTAIN / WRONG scale used for claim
    validation: does the asserted activity hold up against the cited evidence and GO-CAM best practice?
    """
    OK = PermissibleValue(
        text="OK",
        description="""The activity is well supported and follows best practice (correct MF specificity, correct causal/has-input usage, adequate evidence).""")
    UNCERTAIN = PermissibleValue(
        text="UNCERTAIN",
        description="""Defensible but imprecise or under-supported; a minor best-practice or evidence issue that needs qualification.""")
    WRONG = PermissibleValue(
        text="WRONG",
        description="""The activity contradicts the evidence or violates a hard best-practice rule (e.g. binding-as-function, wrong causal directionality).""")

    _defn = EnumDefinition(
        name="GoCamClaimVerdictEnum",
        description="""Forensic-review verdict for a GO-CAM activity, mirroring the OK / UNCERTAIN / WRONG scale used for claim validation: does the asserted activity hold up against the cited evidence and GO-CAM best practice?""",
    )

class GoCamConsistencyEnum(EnumDefinitionImpl):
    """
    How a GO-CAM activity relates to the corresponding gene's annotation review (genes/**/<gene>-ai-review.yaml).
    """
    CONSISTENT = PermissibleValue(
        text="CONSISTENT",
        description="The activity's function matches an accepted core function in the gene review.")
    MORE_SPECIFIC = PermissibleValue(
        text="MORE_SPECIFIC",
        description="The activity asserts a more specific function than the gene review.")
    MORE_GENERAL = PermissibleValue(
        text="MORE_GENERAL",
        description="The activity asserts a more general function than the gene review.")
    RELATED = PermissibleValue(
        text="RELATED",
        description="Same general area but neither a clean subsumption nor a match.")
    CONFLICT = PermissibleValue(
        text="CONFLICT",
        description="The activity asserts a function the gene review removed, negated, or marked as over-annotated.")
    NOT_IN_REVIEW = PermissibleValue(
        text="NOT_IN_REVIEW",
        description="The function is not represented in the gene review (candidate gap).")
    NO_GENE_REVIEW = PermissibleValue(
        text="NO_GENE_REVIEW",
        description="No gene review exists yet for this gene product.")

    _defn = EnumDefinition(
        name="GoCamConsistencyEnum",
        description="""How a GO-CAM activity relates to the corresponding gene's annotation review (genes/**/<gene>-ai-review.yaml).""",
    )

class GoCamQcFlagEnum(EnumDefinitionImpl):
    """
    Specific GO-CAM best-practice issues observed for an activity. Derived from the GO-CAM annotation best-practice
    checklist (see gocams/BEST_PRACTICE.md).
    """
    BINDING_AS_FUNCTION = PermissibleValue(
        text="BINDING_AS_FUNCTION",
        description="""Molecular function is a bare 'binding' term with no functional consequence specified (use catalytic/receptor/adaptor/sequestering MF).""")
    GENERIC_MF = PermissibleValue(
        text="GENERIC_MF",
        description="An overly generic MF term is used where a specific child term applies.")
    HAS_INPUT_MISUSE = PermissibleValue(
        text="HAS_INPUT_MISUSE",
        description="""'has input' used incorrectly, e.g. a receptor's ligand or a TF's DNA instead of the substrate/target gene/downstream effector.""")
    DIRECT_VS_INDIRECT_CAUSAL = PermissibleValue(
        text="DIRECT_VS_INDIRECT_CAUSAL",
        description="Direct regulation asserted for a multi-step (indirect) mechanism, or vice versa.")
    INCORRECT_DIRECTIONALITY = PermissibleValue(
        text="INCORRECT_DIRECTIONALITY",
        description="Causal edge directionality (subject -> object) appears reversed.")
    MISSING_LOCATION = PermissibleValue(
        text="MISSING_LOCATION",
        description="Activity lacks an 'occurs in' cellular component.")
    MISSING_PROCESS = PermissibleValue(
        text="MISSING_PROCESS",
        description="Activity is not connected to a biological process via 'part of'.")
    ORPHAN_ACTIVITY = PermissibleValue(
        text="ORPHAN_ACTIVITY",
        description="Activity has no causal connections to the rest of the model.")
    MISSING_EVIDENCE = PermissibleValue(
        text="MISSING_EVIDENCE",
        description="An activity or relationship lacks an evidence code / reference.")
    COMPLEX_SUBUNIT_REPRESENTATION = PermissibleValue(
        text="COMPLEX_SUBUNIT_REPRESENTATION",
        description="""Complex represented with a complex term where a specific active subunit is known (or vice versa).""")

    _defn = EnumDefinition(
        name="GoCamQcFlagEnum",
        description="""Specific GO-CAM best-practice issues observed for an activity. Derived from the GO-CAM annotation best-practice checklist (see gocams/BEST_PRACTICE.md).""",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=GENE_REVIEW.id, name="id", curie=GENE_REVIEW.curie('id'),
                   model_uri=GENE_REVIEW.id, domain=None, range=URIRef)

slots.label = Slot(uri=RDFS.label, name="label", curie=RDFS.curie('label'),
                   model_uri=GENE_REVIEW.label, domain=None, range=str)

slots.gene_symbol = Slot(uri=GENE_REVIEW.gene_symbol, name="gene_symbol", curie=GENE_REVIEW.curie('gene_symbol'),
                   model_uri=GENE_REVIEW.gene_symbol, domain=None, range=str)

slots.product_type = Slot(uri=GENE_REVIEW.product_type, name="product_type", curie=GENE_REVIEW.curie('product_type'),
                   model_uri=GENE_REVIEW.product_type, domain=None, range=Optional[Union[str, "ProductTypeEnum"]])

slots.title = Slot(uri=DCTERMS.title, name="title", curie=DCTERMS.curie('title'),
                   model_uri=GENE_REVIEW.title, domain=None, range=str)

slots.aliases = Slot(uri=GENE_REVIEW.aliases, name="aliases", curie=GENE_REVIEW.curie('aliases'),
                   model_uri=GENE_REVIEW.aliases, domain=None, range=Optional[Union[str, list[str]]])

slots.name = Slot(uri=GENE_REVIEW.name, name="name", curie=GENE_REVIEW.curie('name'),
                   model_uri=GENE_REVIEW.name, domain=None, range=Optional[str])

slots.sequence_note = Slot(uri=GENE_REVIEW.sequence_note, name="sequence_note", curie=GENE_REVIEW.curie('sequence_note'),
                   model_uri=GENE_REVIEW.sequence_note, domain=None, range=Optional[str])

slots.tags = Slot(uri=GENE_REVIEW.tags, name="tags", curie=GENE_REVIEW.curie('tags'),
                   model_uri=GENE_REVIEW.tags, domain=None, range=Optional[Union[str, list[str]]])

slots.description = Slot(uri=DCTERMS.description, name="description", curie=DCTERMS.curie('description'),
                   model_uri=GENE_REVIEW.description, domain=None, range=Optional[str])

slots.statement = Slot(uri=GENE_REVIEW.statement, name="statement", curie=GENE_REVIEW.curie('statement'),
                   model_uri=GENE_REVIEW.statement, domain=None, range=Optional[str])

slots.references = Slot(uri=GENE_REVIEW.references, name="references", curie=GENE_REVIEW.curie('references'),
                   model_uri=GENE_REVIEW.references, domain=None, range=Optional[Union[dict[Union[str, ReferenceId], Union[dict, Reference]], list[Union[dict, Reference]]]])

slots.findings = Slot(uri=GENE_REVIEW.findings, name="findings", curie=GENE_REVIEW.curie('findings'),
                   model_uri=GENE_REVIEW.findings, domain=None, range=Optional[Union[Union[dict, Finding], list[Union[dict, Finding]]]])

slots.supported_by = Slot(uri=GENE_REVIEW.supported_by, name="supported_by", curie=GENE_REVIEW.curie('supported_by'),
                   model_uri=GENE_REVIEW.supported_by, domain=None, range=Optional[Union[Union[dict, SupportingTextInReference], list[Union[dict, SupportingTextInReference]]]])

slots.summary = Slot(uri=GENE_REVIEW.summary, name="summary", curie=GENE_REVIEW.curie('summary'),
                   model_uri=GENE_REVIEW.summary, domain=None, range=Optional[str])

slots.supporting_text = Slot(uri=GENE_REVIEW.supporting_text, name="supporting_text", curie=GENE_REVIEW.curie('supporting_text'),
                   model_uri=GENE_REVIEW.supporting_text, domain=None, range=Optional[str])

slots.supporting_text_fulltext = Slot(uri=GENE_REVIEW.supporting_text_fulltext, name="supporting_text_fulltext", curie=GENE_REVIEW.curie('supporting_text_fulltext'),
                   model_uri=GENE_REVIEW.supporting_text_fulltext, domain=None, range=Optional[str])

slots.full_text_unavailable = Slot(uri=GENE_REVIEW.full_text_unavailable, name="full_text_unavailable", curie=GENE_REVIEW.curie('full_text_unavailable'),
                   model_uri=GENE_REVIEW.full_text_unavailable, domain=None, range=Optional[Union[bool, Bool]])

slots.evidence_type = Slot(uri=GENE_REVIEW.evidence_type, name="evidence_type", curie=GENE_REVIEW.curie('evidence_type'),
                   model_uri=GENE_REVIEW.evidence_type, domain=None, range=Union[str, "EvidenceType"])

slots.term = Slot(uri=GENE_REVIEW.term, name="term", curie=GENE_REVIEW.curie('term'),
                   model_uri=GENE_REVIEW.term, domain=None, range=Optional[Union[dict, Term]])

slots.predicate = Slot(uri=RDF.predicate, name="predicate", curie=RDF.curie('predicate'),
                   model_uri=GENE_REVIEW.predicate, domain=None, range=str)

slots.taxon = Slot(uri=GENE_REVIEW.taxon, name="taxon", curie=GENE_REVIEW.curie('taxon'),
                   model_uri=GENE_REVIEW.taxon, domain=None, range=Union[dict, Term])

slots.alternative_products = Slot(uri=GENE_REVIEW.alternative_products, name="alternative_products", curie=GENE_REVIEW.curie('alternative_products'),
                   model_uri=GENE_REVIEW.alternative_products, domain=None, range=Optional[Union[dict[Union[str, AlternativeProductId], Union[dict, AlternativeProduct]], list[Union[dict, AlternativeProduct]]]])

slots.functional_isoforms = Slot(uri=GENE_REVIEW.functional_isoforms, name="functional_isoforms", curie=GENE_REVIEW.curie('functional_isoforms'),
                   model_uri=GENE_REVIEW.functional_isoforms, domain=None, range=Optional[Union[dict[Union[str, FunctionalIsoformId], Union[dict, FunctionalIsoform]], list[Union[dict, FunctionalIsoform]]]])

slots.existing_annotations = Slot(uri=GENE_REVIEW.existing_annotations, name="existing_annotations", curie=GENE_REVIEW.curie('existing_annotations'),
                   model_uri=GENE_REVIEW.existing_annotations, domain=None, range=Optional[Union[Union[dict, ExistingAnnotation], list[Union[dict, ExistingAnnotation]]]])

slots.core_functions = Slot(uri=GENE_REVIEW.core_functions, name="core_functions", curie=GENE_REVIEW.curie('core_functions'),
                   model_uri=GENE_REVIEW.core_functions, domain=None, range=Optional[Union[Union[dict, CoreFunction], list[Union[dict, CoreFunction]]]])

slots.action = Slot(uri=GENE_REVIEW.action, name="action", curie=GENE_REVIEW.curie('action'),
                   model_uri=GENE_REVIEW.action, domain=None, range=Union[str, "ActionEnum"])

slots.reason = Slot(uri=GENE_REVIEW.reason, name="reason", curie=GENE_REVIEW.curie('reason'),
                   model_uri=GENE_REVIEW.reason, domain=None, range=Optional[str])

slots.proposed_replacement_terms = Slot(uri=GENE_REVIEW.proposed_replacement_terms, name="proposed_replacement_terms", curie=GENE_REVIEW.curie('proposed_replacement_terms'),
                   model_uri=GENE_REVIEW.proposed_replacement_terms, domain=None, range=Optional[Union[dict[Union[str, TermId], Union[dict, Term]], list[Union[dict, Term]]]])

slots.extensions = Slot(uri=GENE_REVIEW.extensions, name="extensions", curie=GENE_REVIEW.curie('extensions'),
                   model_uri=GENE_REVIEW.extensions, domain=None, range=Optional[Union[Union[dict, AnnotationExtension], list[Union[dict, AnnotationExtension]]]])

slots.qualifier = Slot(uri=GENE_REVIEW.qualifier, name="qualifier", curie=GENE_REVIEW.curie('qualifier'),
                   model_uri=GENE_REVIEW.qualifier, domain=None, range=Optional[Union[str, "AnnotationQualifierEnum"]])

slots.negated = Slot(uri=GENE_REVIEW.negated, name="negated", curie=GENE_REVIEW.curie('negated'),
                   model_uri=GENE_REVIEW.negated, domain=None, range=Optional[Union[bool, Bool]])

slots.reference_id = Slot(uri=GENE_REVIEW.reference_id, name="reference_id", curie=GENE_REVIEW.curie('reference_id'),
                   model_uri=GENE_REVIEW.reference_id, domain=None, range=Union[str, ReferenceId])

slots.original_reference_id = Slot(uri=GENE_REVIEW.original_reference_id, name="original_reference_id", curie=GENE_REVIEW.curie('original_reference_id'),
                   model_uri=GENE_REVIEW.original_reference_id, domain=None, range=Optional[Union[str, ReferenceId]])

slots.retired = Slot(uri=GENE_REVIEW.retired, name="retired", curie=GENE_REVIEW.curie('retired'),
                   model_uri=GENE_REVIEW.retired, domain=None, range=Optional[Union[bool, Bool]])

slots.isoform = Slot(uri=GENE_REVIEW.isoform, name="isoform", curie=GENE_REVIEW.curie('isoform'),
                   model_uri=GENE_REVIEW.isoform, domain=None, range=Optional[str])

slots.review = Slot(uri=GENE_REVIEW.review, name="review", curie=GENE_REVIEW.curie('review'),
                   model_uri=GENE_REVIEW.review, domain=None, range=Optional[Union[dict, Review]])

slots.reference_review = Slot(uri=GENE_REVIEW.reference_review, name="reference_review", curie=GENE_REVIEW.curie('reference_review'),
                   model_uri=GENE_REVIEW.reference_review, domain=None, range=Optional[Union[dict, ReferenceReview]])

slots.relevance = Slot(uri=GENE_REVIEW.relevance, name="relevance", curie=GENE_REVIEW.curie('relevance'),
                   model_uri=GENE_REVIEW.relevance, domain=None, range=Optional[Union[str, "ReferenceRelevanceEnum"]])

slots.correctness = Slot(uri=GENE_REVIEW.correctness, name="correctness", curie=GENE_REVIEW.curie('correctness'),
                   model_uri=GENE_REVIEW.correctness, domain=None, range=Optional[Union[str, "ReferenceCorrectnessEnum"]])

slots.review_notes = Slot(uri=GENE_REVIEW.review_notes, name="review_notes", curie=GENE_REVIEW.curie('review_notes'),
                   model_uri=GENE_REVIEW.review_notes, domain=None, range=Optional[str])

slots.finding_review = Slot(uri=GENE_REVIEW.finding_review, name="finding_review", curie=GENE_REVIEW.curie('finding_review'),
                   model_uri=GENE_REVIEW.finding_review, domain=None, range=Optional[Union[dict, FindingReview]])

slots.finding_status = Slot(uri=GENE_REVIEW.finding_status, name="finding_status", curie=GENE_REVIEW.curie('finding_status'),
                   model_uri=GENE_REVIEW.finding_status, domain=None, range=Optional[Union[str, "FindingReviewStatusEnum"]])

slots.superseded_by = Slot(uri=GENE_REVIEW.superseded_by, name="superseded_by", curie=GENE_REVIEW.curie('superseded_by'),
                   model_uri=GENE_REVIEW.superseded_by, domain=None, range=Optional[Union[Union[str, ReferenceId], list[Union[str, ReferenceId]]]])

slots.ontology = Slot(uri=GENE_REVIEW.ontology, name="ontology", curie=GENE_REVIEW.curie('ontology'),
                   model_uri=GENE_REVIEW.ontology, domain=None, range=Optional[str])

slots.supporting_entities = Slot(uri=GENE_REVIEW.supporting_entities, name="supporting_entities", curie=GENE_REVIEW.curie('supporting_entities'),
                   model_uri=GENE_REVIEW.supporting_entities, domain=None, range=Optional[Union[str, list[str]]])

slots.additional_reference_ids = Slot(uri=GENE_REVIEW.additional_reference_ids, name="additional_reference_ids", curie=GENE_REVIEW.curie('additional_reference_ids'),
                   model_uri=GENE_REVIEW.additional_reference_ids, domain=None, range=Optional[Union[Union[str, ReferenceId], list[Union[str, ReferenceId]]]])

slots.is_invalid = Slot(uri=GENE_REVIEW.is_invalid, name="is_invalid", curie=GENE_REVIEW.curie('is_invalid'),
                   model_uri=GENE_REVIEW.is_invalid, domain=None, range=Optional[Union[bool, Bool]])

slots.publication_type = Slot(uri=GENE_REVIEW.publication_type, name="publication_type", curie=GENE_REVIEW.curie('publication_type'),
                   model_uri=GENE_REVIEW.publication_type, domain=None, range=Optional[Union[str, "PublicationTypeEnum"]])

slots.reference_section_type = Slot(uri=GENE_REVIEW.reference_section_type, name="reference_section_type", curie=GENE_REVIEW.curie('reference_section_type'),
                   model_uri=GENE_REVIEW.reference_section_type, domain=None, range=Optional[Union[str, "ManuscriptSection"]])

slots.proposed_new_terms = Slot(uri=GENE_REVIEW.proposed_new_terms, name="proposed_new_terms", curie=GENE_REVIEW.curie('proposed_new_terms'),
                   model_uri=GENE_REVIEW.proposed_new_terms, domain=None, range=Optional[Union[Union[dict, ProposedOntologyTerm], list[Union[dict, ProposedOntologyTerm]]]])

slots.suggested_questions = Slot(uri=GENE_REVIEW.suggested_questions, name="suggested_questions", curie=GENE_REVIEW.curie('suggested_questions'),
                   model_uri=GENE_REVIEW.suggested_questions, domain=None, range=Optional[Union[Union[dict, Question], list[Union[dict, Question]]]])

slots.suggested_experiments = Slot(uri=GENE_REVIEW.suggested_experiments, name="suggested_experiments", curie=GENE_REVIEW.curie('suggested_experiments'),
                   model_uri=GENE_REVIEW.suggested_experiments, domain=None, range=Optional[Union[Union[dict, Experiment], list[Union[dict, Experiment]]]])

slots.knowledge_gaps = Slot(uri=GENE_REVIEW.knowledge_gaps, name="knowledge_gaps", curie=GENE_REVIEW.curie('knowledge_gaps'),
                   model_uri=GENE_REVIEW.knowledge_gaps, domain=None, range=Optional[Union[Union[dict, KnowledgeGap], list[Union[dict, KnowledgeGap]]]])

slots.propagation_review = Slot(uri=GENE_REVIEW.propagation_review, name="propagation_review", curie=GENE_REVIEW.curie('propagation_review'),
                   model_uri=GENE_REVIEW.propagation_review, domain=None, range=Optional[Union[dict, PropagationReview]])

slots.status = Slot(uri=GENE_REVIEW.status, name="status", curie=GENE_REVIEW.curie('status'),
                   model_uri=GENE_REVIEW.status, domain=None, range=Optional[Union[str, "GeneReviewStatusEnum"]])

slots.functionalIsoform__id = Slot(uri=GENE_REVIEW.id, name="functionalIsoform__id", curie=GENE_REVIEW.curie('id'),
                   model_uri=GENE_REVIEW.functionalIsoform__id, domain=None, range=URIRef)

slots.functionalIsoform__name = Slot(uri=GENE_REVIEW.name, name="functionalIsoform__name", curie=GENE_REVIEW.curie('name'),
                   model_uri=GENE_REVIEW.functionalIsoform__name, domain=None, range=str)

slots.functionalIsoform__type = Slot(uri=GENE_REVIEW.type, name="functionalIsoform__type", curie=GENE_REVIEW.curie('type'),
                   model_uri=GENE_REVIEW.functionalIsoform__type, domain=None, range=Union[str, "FunctionalIsoformTypeEnum"])

slots.functionalIsoform__maps_to = Slot(uri=GENE_REVIEW.maps_to, name="functionalIsoform__maps_to", curie=GENE_REVIEW.curie('maps_to'),
                   model_uri=GENE_REVIEW.functionalIsoform__maps_to, domain=None, range=Optional[Union[Union[dict, FunctionalIsoformMapping], list[Union[dict, FunctionalIsoformMapping]]]])

slots.functionalIsoform__description = Slot(uri=GENE_REVIEW.description, name="functionalIsoform__description", curie=GENE_REVIEW.curie('description'),
                   model_uri=GENE_REVIEW.functionalIsoform__description, domain=None, range=str)

slots.functionalIsoform__isoform_specific_terms = Slot(uri=GENE_REVIEW.isoform_specific_terms, name="functionalIsoform__isoform_specific_terms", curie=GENE_REVIEW.curie('isoform_specific_terms'),
                   model_uri=GENE_REVIEW.functionalIsoform__isoform_specific_terms, domain=None, range=Optional[Union[dict[Union[str, TermId], Union[dict, Term]], list[Union[dict, Term]]]])

slots.functionalIsoformMapping__type = Slot(uri=GENE_REVIEW.type, name="functionalIsoformMapping__type", curie=GENE_REVIEW.curie('type'),
                   model_uri=GENE_REVIEW.functionalIsoformMapping__type, domain=None, range=Union[str, "FunctionalIsoformMappingTypeEnum"])

slots.functionalIsoformMapping__ids = Slot(uri=GENE_REVIEW.ids, name="functionalIsoformMapping__ids", curie=GENE_REVIEW.curie('ids'),
                   model_uri=GENE_REVIEW.functionalIsoformMapping__ids, domain=None, range=Union[str, list[str]])

slots.functionalIsoformMapping__residues = Slot(uri=GENE_REVIEW.residues, name="functionalIsoformMapping__residues", curie=GENE_REVIEW.curie('residues'),
                   model_uri=GENE_REVIEW.functionalIsoformMapping__residues, domain=None, range=Optional[str])

slots.evidenceItem__source_id = Slot(uri=GENE_REVIEW.source_id, name="evidenceItem__source_id", curie=GENE_REVIEW.curie('source_id'),
                   model_uri=GENE_REVIEW.evidenceItem__source_id, domain=None, range=str)

slots.evidenceItem__title = Slot(uri=GENE_REVIEW.title, name="evidenceItem__title", curie=GENE_REVIEW.curie('title'),
                   model_uri=GENE_REVIEW.evidenceItem__title, domain=None, range=Optional[str])

slots.evidenceItem__statement = Slot(uri=GENE_REVIEW.statement, name="evidenceItem__statement", curie=GENE_REVIEW.curie('statement'),
                   model_uri=GENE_REVIEW.evidenceItem__statement, domain=None, range=Optional[str])

slots.evidenceItem__supporting_text = Slot(uri=GENE_REVIEW.supporting_text, name="evidenceItem__supporting_text", curie=GENE_REVIEW.curie('supporting_text'),
                   model_uri=GENE_REVIEW.evidenceItem__supporting_text, domain=None, range=Optional[str])

slots.evidenceItem__url = Slot(uri=GENE_REVIEW.url, name="evidenceItem__url", curie=GENE_REVIEW.curie('url'),
                   model_uri=GENE_REVIEW.evidenceItem__url, domain=None, range=Optional[str])

slots.evidenceItem__notes = Slot(uri=GENE_REVIEW.notes, name="evidenceItem__notes", curie=GENE_REVIEW.curie('notes'),
                   model_uri=GENE_REVIEW.evidenceItem__notes, domain=None, range=Optional[str])

slots.descriptor__preferred_term = Slot(uri=GENE_REVIEW.preferred_term, name="descriptor__preferred_term", curie=GENE_REVIEW.curie('preferred_term'),
                   model_uri=GENE_REVIEW.descriptor__preferred_term, domain=None, range=str)

slots.descriptor__description = Slot(uri=GENE_REVIEW.description, name="descriptor__description", curie=GENE_REVIEW.curie('description'),
                   model_uri=GENE_REVIEW.descriptor__description, domain=None, range=Optional[str])

slots.descriptor__term = Slot(uri=GENE_REVIEW.term, name="descriptor__term", curie=GENE_REVIEW.curie('term'),
                   model_uri=GENE_REVIEW.descriptor__term, domain=None, range=Optional[Union[dict, Term]])

slots.descriptor__evidence = Slot(uri=GENE_REVIEW.evidence, name="descriptor__evidence", curie=GENE_REVIEW.curie('evidence'),
                   model_uri=GENE_REVIEW.descriptor__evidence, domain=None, range=Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]])

slots.descriptor__notes = Slot(uri=GENE_REVIEW.notes, name="descriptor__notes", curie=GENE_REVIEW.curie('notes'),
                   model_uri=GENE_REVIEW.descriptor__notes, domain=None, range=Optional[str])

slots.familyDescriptor__family_terms = Slot(uri=GENE_REVIEW.family_terms, name="familyDescriptor__family_terms", curie=GENE_REVIEW.curie('family_terms'),
                   model_uri=GENE_REVIEW.familyDescriptor__family_terms, domain=None, range=Optional[Union[dict[Union[str, TermId], Union[dict, Term]], list[Union[dict, Term]]]])

slots.familyDescriptor__representative_members = Slot(uri=GENE_REVIEW.representative_members, name="familyDescriptor__representative_members", curie=GENE_REVIEW.curie('representative_members'),
                   model_uri=GENE_REVIEW.familyDescriptor__representative_members, domain=None, range=Optional[Union[Union[dict, GeneProductDescriptor], list[Union[dict, GeneProductDescriptor]]]])

slots.familyDescriptor__ancestral_nodes = Slot(uri=GENE_REVIEW.ancestral_nodes, name="familyDescriptor__ancestral_nodes", curie=GENE_REVIEW.curie('ancestral_nodes'),
                   model_uri=GENE_REVIEW.familyDescriptor__ancestral_nodes, domain=None, range=Optional[Union[Union[dict, AncestralNodeDescriptor], list[Union[dict, AncestralNodeDescriptor]]]])

slots.proteinComplexDescriptor__active_units = Slot(uri=GENE_REVIEW.active_units, name="proteinComplexDescriptor__active_units", curie=GENE_REVIEW.curie('active_units'),
                   model_uri=GENE_REVIEW.proteinComplexDescriptor__active_units, domain=None, range=Optional[Union[Union[dict, ComplexUnit], list[Union[dict, ComplexUnit]]]])

slots.complexUnit__id = Slot(uri=GENE_REVIEW.id, name="complexUnit__id", curie=GENE_REVIEW.curie('id'),
                   model_uri=GENE_REVIEW.complexUnit__id, domain=None, range=Optional[str])

slots.complexUnit__label = Slot(uri=GENE_REVIEW.label, name="complexUnit__label", curie=GENE_REVIEW.curie('label'),
                   model_uri=GENE_REVIEW.complexUnit__label, domain=None, range=Optional[str])

slots.complexUnit__participant = Slot(uri=GENE_REVIEW.participant, name="complexUnit__participant", curie=GENE_REVIEW.curie('participant'),
                   model_uri=GENE_REVIEW.complexUnit__participant, domain=None, range=Optional[Union[dict, ParticipantSelector]])

slots.complexUnit__role = Slot(uri=GENE_REVIEW.role, name="complexUnit__role", curie=GENE_REVIEW.curie('role'),
                   model_uri=GENE_REVIEW.complexUnit__role, domain=None, range=Optional[str])

slots.complexUnit__stoichiometry = Slot(uri=GENE_REVIEW.stoichiometry, name="complexUnit__stoichiometry", curie=GENE_REVIEW.curie('stoichiometry'),
                   model_uri=GENE_REVIEW.complexUnit__stoichiometry, domain=None, range=Optional[str])

slots.complexUnit__function = Slot(uri=GENE_REVIEW.function, name="complexUnit__function", curie=GENE_REVIEW.curie('function'),
                   model_uri=GENE_REVIEW.complexUnit__function, domain=None, range=Optional[Union[dict, MolecularFunctionDescriptor]])

slots.complexUnit__evidence = Slot(uri=GENE_REVIEW.evidence, name="complexUnit__evidence", curie=GENE_REVIEW.curie('evidence'),
                   model_uri=GENE_REVIEW.complexUnit__evidence, domain=None, range=Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]])

slots.complexUnit__notes = Slot(uri=GENE_REVIEW.notes, name="complexUnit__notes", curie=GENE_REVIEW.curie('notes'),
                   model_uri=GENE_REVIEW.complexUnit__notes, domain=None, range=Optional[str])

slots.molecularFunctionDescriptor__substrates = Slot(uri=GENE_REVIEW.substrates, name="molecularFunctionDescriptor__substrates", curie=GENE_REVIEW.curie('substrates'),
                   model_uri=GENE_REVIEW.molecularFunctionDescriptor__substrates, domain=None, range=Optional[Union[Union[dict, Descriptor], list[Union[dict, Descriptor]]]])

slots.molecularFunctionDescriptor__products = Slot(uri=GENE_REVIEW.products, name="molecularFunctionDescriptor__products", curie=GENE_REVIEW.curie('products'),
                   model_uri=GENE_REVIEW.molecularFunctionDescriptor__products, domain=None, range=Optional[Union[Union[dict, Descriptor], list[Union[dict, Descriptor]]]])

slots.molecularFunctionDescriptor__cofactors = Slot(uri=GENE_REVIEW.cofactors, name="molecularFunctionDescriptor__cofactors", curie=GENE_REVIEW.curie('cofactors'),
                   model_uri=GENE_REVIEW.molecularFunctionDescriptor__cofactors, domain=None, range=Optional[Union[Union[dict, Descriptor], list[Union[dict, Descriptor]]]])

slots.molecularFunctionDescriptor__targets = Slot(uri=GENE_REVIEW.targets, name="molecularFunctionDescriptor__targets", curie=GENE_REVIEW.curie('targets'),
                   model_uri=GENE_REVIEW.molecularFunctionDescriptor__targets, domain=None, range=Optional[Union[Union[dict, Descriptor], list[Union[dict, Descriptor]]]])

slots.molecularFunctionDescriptor__cargo = Slot(uri=GENE_REVIEW.cargo, name="molecularFunctionDescriptor__cargo", curie=GENE_REVIEW.curie('cargo'),
                   model_uri=GENE_REVIEW.molecularFunctionDescriptor__cargo, domain=None, range=Optional[Union[Union[dict, Descriptor], list[Union[dict, Descriptor]]]])

slots.molecularFunctionDescriptor__source_location = Slot(uri=GENE_REVIEW.source_location, name="molecularFunctionDescriptor__source_location", curie=GENE_REVIEW.curie('source_location'),
                   model_uri=GENE_REVIEW.molecularFunctionDescriptor__source_location, domain=None, range=Optional[Union[dict, CellularComponentDescriptor]])

slots.molecularFunctionDescriptor__destination_location = Slot(uri=GENE_REVIEW.destination_location, name="molecularFunctionDescriptor__destination_location", curie=GENE_REVIEW.curie('destination_location'),
                   model_uri=GENE_REVIEW.molecularFunctionDescriptor__destination_location, domain=None, range=Optional[Union[dict, CellularComponentDescriptor]])

slots.biologicalProcessDescriptor__inputs = Slot(uri=GENE_REVIEW.inputs, name="biologicalProcessDescriptor__inputs", curie=GENE_REVIEW.curie('inputs'),
                   model_uri=GENE_REVIEW.biologicalProcessDescriptor__inputs, domain=None, range=Optional[Union[Union[dict, Descriptor], list[Union[dict, Descriptor]]]])

slots.biologicalProcessDescriptor__outputs = Slot(uri=GENE_REVIEW.outputs, name="biologicalProcessDescriptor__outputs", curie=GENE_REVIEW.curie('outputs'),
                   model_uri=GENE_REVIEW.biologicalProcessDescriptor__outputs, domain=None, range=Optional[Union[Union[dict, Descriptor], list[Union[dict, Descriptor]]]])

slots.biologicalProcessDescriptor__occurs_in = Slot(uri=GENE_REVIEW.occurs_in, name="biologicalProcessDescriptor__occurs_in", curie=GENE_REVIEW.curie('occurs_in'),
                   model_uri=GENE_REVIEW.biologicalProcessDescriptor__occurs_in, domain=None, range=Optional[Union[Union[dict, Descriptor], list[Union[dict, Descriptor]]]])

slots.biologicalProcessDescriptor__starts_with = Slot(uri=GENE_REVIEW.starts_with, name="biologicalProcessDescriptor__starts_with", curie=GENE_REVIEW.curie('starts_with'),
                   model_uri=GENE_REVIEW.biologicalProcessDescriptor__starts_with, domain=None, range=Optional[Union[dict, Descriptor]])

slots.biologicalProcessDescriptor__ends_with = Slot(uri=GENE_REVIEW.ends_with, name="biologicalProcessDescriptor__ends_with", curie=GENE_REVIEW.curie('ends_with'),
                   model_uri=GENE_REVIEW.biologicalProcessDescriptor__ends_with, domain=None, range=Optional[Union[dict, Descriptor]])

slots.moduleReview__status = Slot(uri=GENE_REVIEW.status, name="moduleReview__status", curie=GENE_REVIEW.curie('status'),
                   model_uri=GENE_REVIEW.moduleReview__status, domain=None, range=Optional[str])

slots.moduleReview__scope = Slot(uri=GENE_REVIEW.scope, name="moduleReview__scope", curie=GENE_REVIEW.curie('scope'),
                   model_uri=GENE_REVIEW.moduleReview__scope, domain=None, range=Optional[Union[str, "ModuleScopeEnum"]])

slots.moduleReview__module = Slot(uri=GENE_REVIEW.module, name="moduleReview__module", curie=GENE_REVIEW.curie('module'),
                   model_uri=GENE_REVIEW.moduleReview__module, domain=None, range=Union[dict, ModuleNode])

slots.moduleReview__evidence = Slot(uri=GENE_REVIEW.evidence, name="moduleReview__evidence", curie=GENE_REVIEW.curie('evidence'),
                   model_uri=GENE_REVIEW.moduleReview__evidence, domain=None, range=Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]])

slots.moduleReview__notes = Slot(uri=GENE_REVIEW.notes, name="moduleReview__notes", curie=GENE_REVIEW.curie('notes'),
                   model_uri=GENE_REVIEW.moduleReview__notes, domain=None, range=Optional[str])

slots.moduleNode__id = Slot(uri=GENE_REVIEW.id, name="moduleNode__id", curie=GENE_REVIEW.curie('id'),
                   model_uri=GENE_REVIEW.moduleNode__id, domain=None, range=URIRef)

slots.moduleNode__label = Slot(uri=GENE_REVIEW.label, name="moduleNode__label", curie=GENE_REVIEW.curie('label'),
                   model_uri=GENE_REVIEW.moduleNode__label, domain=None, range=str)

slots.moduleNode__module_type = Slot(uri=GENE_REVIEW.module_type, name="moduleNode__module_type", curie=GENE_REVIEW.curie('module_type'),
                   model_uri=GENE_REVIEW.moduleNode__module_type, domain=None, range=Optional[Union[str, "ModuleTypeEnum"]])

slots.moduleNode__description = Slot(uri=GENE_REVIEW.description, name="moduleNode__description", curie=GENE_REVIEW.curie('description'),
                   model_uri=GENE_REVIEW.moduleNode__description, domain=None, range=Optional[str])

slots.moduleNode__concepts = Slot(uri=GENE_REVIEW.concepts, name="moduleNode__concepts", curie=GENE_REVIEW.curie('concepts'),
                   model_uri=GENE_REVIEW.moduleNode__concepts, domain=None, range=Optional[Union[Union[dict, Descriptor], list[Union[dict, Descriptor]]]])

slots.moduleNode__context = Slot(uri=GENE_REVIEW.context, name="moduleNode__context", curie=GENE_REVIEW.curie('context'),
                   model_uri=GENE_REVIEW.moduleNode__context, domain=None, range=Optional[Union[dict, ModuleContext]])

slots.moduleNode__annotons = Slot(uri=GENE_REVIEW.annotons, name="moduleNode__annotons", curie=GENE_REVIEW.curie('annotons'),
                   model_uri=GENE_REVIEW.moduleNode__annotons, domain=None, range=Optional[Union[Union[dict, ModuleAnnoton], list[Union[dict, ModuleAnnoton]]]])

slots.moduleNode__parts = Slot(uri=GENE_REVIEW.parts, name="moduleNode__parts", curie=GENE_REVIEW.curie('parts'),
                   model_uri=GENE_REVIEW.moduleNode__parts, domain=None, range=Optional[Union[Union[dict, ModulePart], list[Union[dict, ModulePart]]]])

slots.moduleNode__variant_sets = Slot(uri=GENE_REVIEW.variant_sets, name="moduleNode__variant_sets", curie=GENE_REVIEW.curie('variant_sets'),
                   model_uri=GENE_REVIEW.moduleNode__variant_sets, domain=None, range=Optional[Union[Union[dict, ModuleVariantSet], list[Union[dict, ModuleVariantSet]]]])

slots.moduleNode__connections = Slot(uri=GENE_REVIEW.connections, name="moduleNode__connections", curie=GENE_REVIEW.curie('connections'),
                   model_uri=GENE_REVIEW.moduleNode__connections, domain=None, range=Optional[Union[Union[dict, ModuleConnection], list[Union[dict, ModuleConnection]]]])

slots.moduleNode__conforms_to = Slot(uri=GENE_REVIEW.conforms_to, name="moduleNode__conforms_to", curie=GENE_REVIEW.curie('conforms_to'),
                   model_uri=GENE_REVIEW.moduleNode__conforms_to, domain=None, range=Optional[Union[Union[dict, Conformance], list[Union[dict, Conformance]]]])

slots.moduleNode__gocam_associations = Slot(uri=GENE_REVIEW.gocam_associations, name="moduleNode__gocam_associations", curie=GENE_REVIEW.curie('gocam_associations'),
                   model_uri=GENE_REVIEW.moduleNode__gocam_associations, domain=None, range=Optional[Union[Union[dict, GoCamAssociation], list[Union[dict, GoCamAssociation]]]])

slots.moduleNode__evidence = Slot(uri=GENE_REVIEW.evidence, name="moduleNode__evidence", curie=GENE_REVIEW.curie('evidence'),
                   model_uri=GENE_REVIEW.moduleNode__evidence, domain=None, range=Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]])

slots.moduleNode__notes = Slot(uri=GENE_REVIEW.notes, name="moduleNode__notes", curie=GENE_REVIEW.curie('notes'),
                   model_uri=GENE_REVIEW.moduleNode__notes, domain=None, range=Optional[str])

slots.conformance__template = Slot(uri=GENE_REVIEW.template, name="conformance__template", curie=GENE_REVIEW.curie('template'),
                   model_uri=GENE_REVIEW.conformance__template, domain=None, range=str)

slots.conformance__status = Slot(uri=GENE_REVIEW.status, name="conformance__status", curie=GENE_REVIEW.curie('status'),
                   model_uri=GENE_REVIEW.conformance__status, domain=None, range=Optional[Union[str, "ConformanceStatusEnum"]])

slots.conformance__deviations = Slot(uri=GENE_REVIEW.deviations, name="conformance__deviations", curie=GENE_REVIEW.curie('deviations'),
                   model_uri=GENE_REVIEW.conformance__deviations, domain=None, range=Optional[Union[str, list[str]]])

slots.conformance__notes = Slot(uri=GENE_REVIEW.notes, name="conformance__notes", curie=GENE_REVIEW.curie('notes'),
                   model_uri=GENE_REVIEW.conformance__notes, domain=None, range=Optional[str])

slots.modulePart__order = Slot(uri=GENE_REVIEW.order, name="modulePart__order", curie=GENE_REVIEW.curie('order'),
                   model_uri=GENE_REVIEW.modulePart__order, domain=None, range=Optional[int])

slots.modulePart__role = Slot(uri=GENE_REVIEW.role, name="modulePart__role", curie=GENE_REVIEW.curie('role'),
                   model_uri=GENE_REVIEW.modulePart__role, domain=None, range=Optional[str])

slots.modulePart__optional = Slot(uri=GENE_REVIEW.optional, name="modulePart__optional", curie=GENE_REVIEW.curie('optional'),
                   model_uri=GENE_REVIEW.modulePart__optional, domain=None, range=Optional[Union[bool, Bool]])

slots.modulePart__node = Slot(uri=GENE_REVIEW.node, name="modulePart__node", curie=GENE_REVIEW.curie('node'),
                   model_uri=GENE_REVIEW.modulePart__node, domain=None, range=Union[dict, ModuleNode])

slots.modulePart__evidence = Slot(uri=GENE_REVIEW.evidence, name="modulePart__evidence", curie=GENE_REVIEW.curie('evidence'),
                   model_uri=GENE_REVIEW.modulePart__evidence, domain=None, range=Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]])

slots.modulePart__notes = Slot(uri=GENE_REVIEW.notes, name="modulePart__notes", curie=GENE_REVIEW.curie('notes'),
                   model_uri=GENE_REVIEW.modulePart__notes, domain=None, range=Optional[str])

slots.moduleVariantSet__id = Slot(uri=GENE_REVIEW.id, name="moduleVariantSet__id", curie=GENE_REVIEW.curie('id'),
                   model_uri=GENE_REVIEW.moduleVariantSet__id, domain=None, range=str)

slots.moduleVariantSet__label = Slot(uri=GENE_REVIEW.label, name="moduleVariantSet__label", curie=GENE_REVIEW.curie('label'),
                   model_uri=GENE_REVIEW.moduleVariantSet__label, domain=None, range=Optional[str])

slots.moduleVariantSet__axis = Slot(uri=GENE_REVIEW.axis, name="moduleVariantSet__axis", curie=GENE_REVIEW.curie('axis'),
                   model_uri=GENE_REVIEW.moduleVariantSet__axis, domain=None, range=Optional[str])

slots.moduleVariantSet__selection = Slot(uri=GENE_REVIEW.selection, name="moduleVariantSet__selection", curie=GENE_REVIEW.curie('selection'),
                   model_uri=GENE_REVIEW.moduleVariantSet__selection, domain=None, range=Optional[Union[str, "VariantSelectionEnum"]])

slots.moduleVariantSet__variants = Slot(uri=GENE_REVIEW.variants, name="moduleVariantSet__variants", curie=GENE_REVIEW.curie('variants'),
                   model_uri=GENE_REVIEW.moduleVariantSet__variants, domain=None, range=Union[dict[Union[str, ModuleNodeId], Union[dict, ModuleNode]], list[Union[dict, ModuleNode]]])

slots.moduleVariantSet__evidence = Slot(uri=GENE_REVIEW.evidence, name="moduleVariantSet__evidence", curie=GENE_REVIEW.curie('evidence'),
                   model_uri=GENE_REVIEW.moduleVariantSet__evidence, domain=None, range=Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]])

slots.moduleVariantSet__notes = Slot(uri=GENE_REVIEW.notes, name="moduleVariantSet__notes", curie=GENE_REVIEW.curie('notes'),
                   model_uri=GENE_REVIEW.moduleVariantSet__notes, domain=None, range=Optional[str])

slots.moduleAnnoton__id = Slot(uri=GENE_REVIEW.id, name="moduleAnnoton__id", curie=GENE_REVIEW.curie('id'),
                   model_uri=GENE_REVIEW.moduleAnnoton__id, domain=None, range=str)

slots.moduleAnnoton__label = Slot(uri=GENE_REVIEW.label, name="moduleAnnoton__label", curie=GENE_REVIEW.curie('label'),
                   model_uri=GENE_REVIEW.moduleAnnoton__label, domain=None, range=Optional[str])

slots.moduleAnnoton__participant = Slot(uri=GENE_REVIEW.participant, name="moduleAnnoton__participant", curie=GENE_REVIEW.curie('participant'),
                   model_uri=GENE_REVIEW.moduleAnnoton__participant, domain=None, range=Optional[Union[dict, ParticipantSelector]])

slots.moduleAnnoton__function = Slot(uri=GENE_REVIEW.function, name="moduleAnnoton__function", curie=GENE_REVIEW.curie('function'),
                   model_uri=GENE_REVIEW.moduleAnnoton__function, domain=None, range=Optional[Union[dict, MolecularFunctionDescriptor]])

slots.moduleAnnoton__processes = Slot(uri=GENE_REVIEW.processes, name="moduleAnnoton__processes", curie=GENE_REVIEW.curie('processes'),
                   model_uri=GENE_REVIEW.moduleAnnoton__processes, domain=None, range=Optional[Union[Union[dict, BiologicalProcessDescriptor], list[Union[dict, BiologicalProcessDescriptor]]]])

slots.moduleAnnoton__locations = Slot(uri=GENE_REVIEW.locations, name="moduleAnnoton__locations", curie=GENE_REVIEW.curie('locations'),
                   model_uri=GENE_REVIEW.moduleAnnoton__locations, domain=None, range=Optional[Union[Union[dict, CellularComponentDescriptor], list[Union[dict, CellularComponentDescriptor]]]])

slots.moduleAnnoton__role_description = Slot(uri=GENE_REVIEW.role_description, name="moduleAnnoton__role_description", curie=GENE_REVIEW.curie('role_description'),
                   model_uri=GENE_REVIEW.moduleAnnoton__role_description, domain=None, range=Optional[str])

slots.moduleAnnoton__gocam_associations = Slot(uri=GENE_REVIEW.gocam_associations, name="moduleAnnoton__gocam_associations", curie=GENE_REVIEW.curie('gocam_associations'),
                   model_uri=GENE_REVIEW.moduleAnnoton__gocam_associations, domain=None, range=Optional[Union[Union[dict, GoCamAssociation], list[Union[dict, GoCamAssociation]]]])

slots.moduleAnnoton__evidence = Slot(uri=GENE_REVIEW.evidence, name="moduleAnnoton__evidence", curie=GENE_REVIEW.curie('evidence'),
                   model_uri=GENE_REVIEW.moduleAnnoton__evidence, domain=None, range=Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]])

slots.moduleAnnoton__notes = Slot(uri=GENE_REVIEW.notes, name="moduleAnnoton__notes", curie=GENE_REVIEW.curie('notes'),
                   model_uri=GENE_REVIEW.moduleAnnoton__notes, domain=None, range=Optional[str])

slots.goCamAssociation__model = Slot(uri=GENE_REVIEW.model, name="goCamAssociation__model", curie=GENE_REVIEW.curie('model'),
                   model_uri=GENE_REVIEW.goCamAssociation__model, domain=None, range=str)

slots.goCamAssociation__activity = Slot(uri=GENE_REVIEW.activity, name="goCamAssociation__activity", curie=GENE_REVIEW.curie('activity'),
                   model_uri=GENE_REVIEW.goCamAssociation__activity, domain=None, range=Optional[str])

slots.goCamAssociation__title = Slot(uri=GENE_REVIEW.title, name="goCamAssociation__title", curie=GENE_REVIEW.curie('title'),
                   model_uri=GENE_REVIEW.goCamAssociation__title, domain=None, range=Optional[str])

slots.goCamAssociation__description = Slot(uri=GENE_REVIEW.description, name="goCamAssociation__description", curie=GENE_REVIEW.curie('description'),
                   model_uri=GENE_REVIEW.goCamAssociation__description, domain=None, range=Optional[str])

slots.goCamAssociation__evidence = Slot(uri=GENE_REVIEW.evidence, name="goCamAssociation__evidence", curie=GENE_REVIEW.curie('evidence'),
                   model_uri=GENE_REVIEW.goCamAssociation__evidence, domain=None, range=Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]])

slots.goCamAssociation__notes = Slot(uri=GENE_REVIEW.notes, name="goCamAssociation__notes", curie=GENE_REVIEW.curie('notes'),
                   model_uri=GENE_REVIEW.goCamAssociation__notes, domain=None, range=Optional[str])

slots.goCamReview__model = Slot(uri=GENE_REVIEW.model, name="goCamReview__model", curie=GENE_REVIEW.curie('model'),
                   model_uri=GENE_REVIEW.goCamReview__model, domain=None, range=URIRef)

slots.goCamReview__taxon = Slot(uri=GENE_REVIEW.taxon, name="goCamReview__taxon", curie=GENE_REVIEW.curie('taxon'),
                   model_uri=GENE_REVIEW.goCamReview__taxon, domain=None, range=Optional[str])

slots.goCamReview__summary = Slot(uri=GENE_REVIEW.summary, name="goCamReview__summary", curie=GENE_REVIEW.curie('summary'),
                   model_uri=GENE_REVIEW.goCamReview__summary, domain=None, range=Optional[str])

slots.goCamReview__status = Slot(uri=GENE_REVIEW.status, name="goCamReview__status", curie=GENE_REVIEW.curie('status'),
                   model_uri=GENE_REVIEW.goCamReview__status, domain=None, range=Optional[Union[str, "GoCamReviewStatusEnum"]])

slots.goCamReview__activity_reviews = Slot(uri=GENE_REVIEW.activity_reviews, name="goCamReview__activity_reviews", curie=GENE_REVIEW.curie('activity_reviews'),
                   model_uri=GENE_REVIEW.goCamReview__activity_reviews, domain=None, range=Optional[Union[Union[dict, GoCamActivityReview], list[Union[dict, GoCamActivityReview]]]])

slots.goCamReview__notes = Slot(uri=GENE_REVIEW.notes, name="goCamReview__notes", curie=GENE_REVIEW.curie('notes'),
                   model_uri=GENE_REVIEW.goCamReview__notes, domain=None, range=Optional[str])

slots.goCamActivityReview__activity_id = Slot(uri=GENE_REVIEW.activity_id, name="goCamActivityReview__activity_id", curie=GENE_REVIEW.curie('activity_id'),
                   model_uri=GENE_REVIEW.goCamActivityReview__activity_id, domain=None, range=str)

slots.goCamActivityReview__gene_product = Slot(uri=GENE_REVIEW.gene_product, name="goCamActivityReview__gene_product", curie=GENE_REVIEW.curie('gene_product'),
                   model_uri=GENE_REVIEW.goCamActivityReview__gene_product, domain=None, range=Optional[str])

slots.goCamActivityReview__molecular_function = Slot(uri=GENE_REVIEW.molecular_function, name="goCamActivityReview__molecular_function", curie=GENE_REVIEW.curie('molecular_function'),
                   model_uri=GENE_REVIEW.goCamActivityReview__molecular_function, domain=None, range=Optional[str])

slots.goCamActivityReview__biological_process = Slot(uri=GENE_REVIEW.biological_process, name="goCamActivityReview__biological_process", curie=GENE_REVIEW.curie('biological_process'),
                   model_uri=GENE_REVIEW.goCamActivityReview__biological_process, domain=None, range=Optional[str])

slots.goCamActivityReview__cellular_component = Slot(uri=GENE_REVIEW.cellular_component, name="goCamActivityReview__cellular_component", curie=GENE_REVIEW.curie('cellular_component'),
                   model_uri=GENE_REVIEW.goCamActivityReview__cellular_component, domain=None, range=Optional[str])

slots.goCamActivityReview__verdict = Slot(uri=GENE_REVIEW.verdict, name="goCamActivityReview__verdict", curie=GENE_REVIEW.curie('verdict'),
                   model_uri=GENE_REVIEW.goCamActivityReview__verdict, domain=None, range=Optional[Union[str, "GoCamClaimVerdictEnum"]])

slots.goCamActivityReview__qc_flags = Slot(uri=GENE_REVIEW.qc_flags, name="goCamActivityReview__qc_flags", curie=GENE_REVIEW.curie('qc_flags'),
                   model_uri=GENE_REVIEW.goCamActivityReview__qc_flags, domain=None, range=Optional[Union[Union[str, "GoCamQcFlagEnum"], list[Union[str, "GoCamQcFlagEnum"]]]])

slots.goCamActivityReview__consistency = Slot(uri=GENE_REVIEW.consistency, name="goCamActivityReview__consistency", curie=GENE_REVIEW.curie('consistency'),
                   model_uri=GENE_REVIEW.goCamActivityReview__consistency, domain=None, range=Optional[Union[str, "GoCamConsistencyEnum"]])

slots.goCamActivityReview__gene_review = Slot(uri=GENE_REVIEW.gene_review, name="goCamActivityReview__gene_review", curie=GENE_REVIEW.curie('gene_review'),
                   model_uri=GENE_REVIEW.goCamActivityReview__gene_review, domain=None, range=Optional[str])

slots.goCamActivityReview__supporting_text = Slot(uri=GENE_REVIEW.supporting_text, name="goCamActivityReview__supporting_text", curie=GENE_REVIEW.curie('supporting_text'),
                   model_uri=GENE_REVIEW.goCamActivityReview__supporting_text, domain=None, range=Optional[str])

slots.goCamActivityReview__evidence = Slot(uri=GENE_REVIEW.evidence, name="goCamActivityReview__evidence", curie=GENE_REVIEW.curie('evidence'),
                   model_uri=GENE_REVIEW.goCamActivityReview__evidence, domain=None, range=Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]])

slots.goCamActivityReview__notes = Slot(uri=GENE_REVIEW.notes, name="goCamActivityReview__notes", curie=GENE_REVIEW.curie('notes'),
                   model_uri=GENE_REVIEW.goCamActivityReview__notes, domain=None, range=Optional[str])

slots.participantSelector__selector_type = Slot(uri=GENE_REVIEW.selector_type, name="participantSelector__selector_type", curie=GENE_REVIEW.curie('selector_type'),
                   model_uri=GENE_REVIEW.participantSelector__selector_type, domain=None, range=Union[str, "ParticipantSelectorTypeEnum"])

slots.participantSelector__gene = Slot(uri=GENE_REVIEW.gene, name="participantSelector__gene", curie=GENE_REVIEW.curie('gene'),
                   model_uri=GENE_REVIEW.participantSelector__gene, domain=None, range=Optional[Union[dict, GeneDescriptor]])

slots.participantSelector__gene_product = Slot(uri=GENE_REVIEW.gene_product, name="participantSelector__gene_product", curie=GENE_REVIEW.curie('gene_product'),
                   model_uri=GENE_REVIEW.participantSelector__gene_product, domain=None, range=Optional[Union[dict, GeneProductDescriptor]])

slots.participantSelector__protein_complex = Slot(uri=GENE_REVIEW.protein_complex, name="participantSelector__protein_complex", curie=GENE_REVIEW.curie('protein_complex'),
                   model_uri=GENE_REVIEW.participantSelector__protein_complex, domain=None, range=Optional[Union[dict, ProteinComplexDescriptor]])

slots.participantSelector__family = Slot(uri=GENE_REVIEW.family, name="participantSelector__family", curie=GENE_REVIEW.curie('family'),
                   model_uri=GENE_REVIEW.participantSelector__family, domain=None, range=Optional[Union[dict, FamilyDescriptor]])

slots.participantSelector__domain = Slot(uri=GENE_REVIEW.domain, name="participantSelector__domain", curie=GENE_REVIEW.curie('domain'),
                   model_uri=GENE_REVIEW.participantSelector__domain, domain=None, range=Optional[Union[dict, DomainDescriptor]])

slots.participantSelector__homolog_of = Slot(uri=GENE_REVIEW.homolog_of, name="participantSelector__homolog_of", curie=GENE_REVIEW.curie('homolog_of'),
                   model_uri=GENE_REVIEW.participantSelector__homolog_of, domain=None, range=Optional[Union[dict, GeneDescriptor]])

slots.participantSelector__ortholog_of = Slot(uri=GENE_REVIEW.ortholog_of, name="participantSelector__ortholog_of", curie=GENE_REVIEW.curie('ortholog_of'),
                   model_uri=GENE_REVIEW.participantSelector__ortholog_of, domain=None, range=Optional[Union[dict, GeneDescriptor]])

slots.participantSelector__required_function = Slot(uri=GENE_REVIEW.required_function, name="participantSelector__required_function", curie=GENE_REVIEW.curie('required_function'),
                   model_uri=GENE_REVIEW.participantSelector__required_function, domain=None, range=Optional[Union[dict, MolecularFunctionDescriptor]])

slots.participantSelector__required_domain = Slot(uri=GENE_REVIEW.required_domain, name="participantSelector__required_domain", curie=GENE_REVIEW.curie('required_domain'),
                   model_uri=GENE_REVIEW.participantSelector__required_domain, domain=None, range=Optional[Union[dict, DomainDescriptor]])

slots.participantSelector__taxon = Slot(uri=GENE_REVIEW.taxon, name="participantSelector__taxon", curie=GENE_REVIEW.curie('taxon'),
                   model_uri=GENE_REVIEW.participantSelector__taxon, domain=None, range=Optional[Union[dict, TaxonDescriptor]])

slots.participantSelector__description = Slot(uri=GENE_REVIEW.description, name="participantSelector__description", curie=GENE_REVIEW.curie('description'),
                   model_uri=GENE_REVIEW.participantSelector__description, domain=None, range=Optional[str])

slots.participantSelector__evidence = Slot(uri=GENE_REVIEW.evidence, name="participantSelector__evidence", curie=GENE_REVIEW.curie('evidence'),
                   model_uri=GENE_REVIEW.participantSelector__evidence, domain=None, range=Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]])

slots.participantSelector__notes = Slot(uri=GENE_REVIEW.notes, name="participantSelector__notes", curie=GENE_REVIEW.curie('notes'),
                   model_uri=GENE_REVIEW.participantSelector__notes, domain=None, range=Optional[str])

slots.moduleContext__taxa = Slot(uri=GENE_REVIEW.taxa, name="moduleContext__taxa", curie=GENE_REVIEW.curie('taxa'),
                   model_uri=GENE_REVIEW.moduleContext__taxa, domain=None, range=Optional[Union[Union[dict, TaxonDescriptor], list[Union[dict, TaxonDescriptor]]]])

slots.moduleContext__cell_types = Slot(uri=GENE_REVIEW.cell_types, name="moduleContext__cell_types", curie=GENE_REVIEW.curie('cell_types'),
                   model_uri=GENE_REVIEW.moduleContext__cell_types, domain=None, range=Optional[Union[Union[dict, CellTypeDescriptor], list[Union[dict, CellTypeDescriptor]]]])

slots.moduleContext__anatomical_locations = Slot(uri=GENE_REVIEW.anatomical_locations, name="moduleContext__anatomical_locations", curie=GENE_REVIEW.curie('anatomical_locations'),
                   model_uri=GENE_REVIEW.moduleContext__anatomical_locations, domain=None, range=Optional[Union[Union[dict, AnatomicalEntityDescriptor], list[Union[dict, AnatomicalEntityDescriptor]]]])

slots.moduleContext__developmental_stages = Slot(uri=GENE_REVIEW.developmental_stages, name="moduleContext__developmental_stages", curie=GENE_REVIEW.curie('developmental_stages'),
                   model_uri=GENE_REVIEW.moduleContext__developmental_stages, domain=None, range=Optional[Union[Union[dict, DevelopmentalStageDescriptor], list[Union[dict, DevelopmentalStageDescriptor]]]])

slots.moduleContext__cellular_components = Slot(uri=GENE_REVIEW.cellular_components, name="moduleContext__cellular_components", curie=GENE_REVIEW.curie('cellular_components'),
                   model_uri=GENE_REVIEW.moduleContext__cellular_components, domain=None, range=Optional[Union[Union[dict, CellularComponentDescriptor], list[Union[dict, CellularComponentDescriptor]]]])

slots.moduleContext__conditions = Slot(uri=GENE_REVIEW.conditions, name="moduleContext__conditions", curie=GENE_REVIEW.curie('conditions'),
                   model_uri=GENE_REVIEW.moduleContext__conditions, domain=None, range=Optional[Union[Union[dict, Descriptor], list[Union[dict, Descriptor]]]])

slots.moduleContext__evidence = Slot(uri=GENE_REVIEW.evidence, name="moduleContext__evidence", curie=GENE_REVIEW.curie('evidence'),
                   model_uri=GENE_REVIEW.moduleContext__evidence, domain=None, range=Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]])

slots.moduleContext__notes = Slot(uri=GENE_REVIEW.notes, name="moduleContext__notes", curie=GENE_REVIEW.curie('notes'),
                   model_uri=GENE_REVIEW.moduleContext__notes, domain=None, range=Optional[str])

slots.moduleConnection__source = Slot(uri=GENE_REVIEW.source, name="moduleConnection__source", curie=GENE_REVIEW.curie('source'),
                   model_uri=GENE_REVIEW.moduleConnection__source, domain=None, range=str)

slots.moduleConnection__target = Slot(uri=GENE_REVIEW.target, name="moduleConnection__target", curie=GENE_REVIEW.curie('target'),
                   model_uri=GENE_REVIEW.moduleConnection__target, domain=None, range=str)

slots.moduleConnection__connection_type = Slot(uri=GENE_REVIEW.connection_type, name="moduleConnection__connection_type", curie=GENE_REVIEW.curie('connection_type'),
                   model_uri=GENE_REVIEW.moduleConnection__connection_type, domain=None, range=Optional[Union[str, "ModuleConnectionTypeEnum"]])

slots.moduleConnection__predicate = Slot(uri=GENE_REVIEW.predicate, name="moduleConnection__predicate", curie=GENE_REVIEW.curie('predicate'),
                   model_uri=GENE_REVIEW.moduleConnection__predicate, domain=None, range=Optional[Union[dict, RelationDescriptor]])

slots.moduleConnection__description = Slot(uri=GENE_REVIEW.description, name="moduleConnection__description", curie=GENE_REVIEW.curie('description'),
                   model_uri=GENE_REVIEW.moduleConnection__description, domain=None, range=Optional[str])

slots.moduleConnection__context = Slot(uri=GENE_REVIEW.context, name="moduleConnection__context", curie=GENE_REVIEW.curie('context'),
                   model_uri=GENE_REVIEW.moduleConnection__context, domain=None, range=Optional[Union[dict, ModuleContext]])

slots.moduleConnection__evidence = Slot(uri=GENE_REVIEW.evidence, name="moduleConnection__evidence", curie=GENE_REVIEW.curie('evidence'),
                   model_uri=GENE_REVIEW.moduleConnection__evidence, domain=None, range=Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]])

slots.moduleConnection__chaining_status = Slot(uri=GENE_REVIEW.chaining_status, name="moduleConnection__chaining_status", curie=GENE_REVIEW.curie('chaining_status'),
                   model_uri=GENE_REVIEW.moduleConnection__chaining_status, domain=None, range=Optional[Union[str, "ChainingStatusEnum"]])

slots.moduleConnection__chaining_note = Slot(uri=GENE_REVIEW.chaining_note, name="moduleConnection__chaining_note", curie=GENE_REVIEW.curie('chaining_note'),
                   model_uri=GENE_REVIEW.moduleConnection__chaining_note, domain=None, range=Optional[str])

slots.moduleConnection__notes = Slot(uri=GENE_REVIEW.notes, name="moduleConnection__notes", curie=GENE_REVIEW.curie('notes'),
                   model_uri=GENE_REVIEW.moduleConnection__notes, domain=None, range=Optional[str])

slots.propagationReview__root_cause = Slot(uri=GENE_REVIEW.root_cause, name="propagationReview__root_cause", curie=GENE_REVIEW.curie('root_cause'),
                   model_uri=GENE_REVIEW.propagationReview__root_cause, domain=None, range=Union[str, "PropagationRootCauseEnum"])

slots.propagationReview__failure_modes = Slot(uri=GENE_REVIEW.failure_modes, name="propagationReview__failure_modes", curie=GENE_REVIEW.curie('failure_modes'),
                   model_uri=GENE_REVIEW.propagationReview__failure_modes, domain=None, range=Optional[Union[Union[str, "PropagationFailureModeEnum"], list[Union[str, "PropagationFailureModeEnum"]]]])

slots.propagationReview__source_entities = Slot(uri=GENE_REVIEW.source_entities, name="propagationReview__source_entities", curie=GENE_REVIEW.curie('source_entities'),
                   model_uri=GENE_REVIEW.propagationReview__source_entities, domain=None, range=Optional[Union[Union[dict, PropagationSource], list[Union[dict, PropagationSource]]]])

slots.propagationReview__residue_claims = Slot(uri=GENE_REVIEW.residue_claims, name="propagationReview__residue_claims", curie=GENE_REVIEW.curie('residue_claims'),
                   model_uri=GENE_REVIEW.propagationReview__residue_claims, domain=None, range=Optional[Union[Union[dict, ResidueClaim], list[Union[dict, ResidueClaim]]]])

slots.propagationReview__residue_claims_not_applicable = Slot(uri=GENE_REVIEW.residue_claims_not_applicable, name="propagationReview__residue_claims_not_applicable", curie=GENE_REVIEW.curie('residue_claims_not_applicable'),
                   model_uri=GENE_REVIEW.propagationReview__residue_claims_not_applicable, domain=None, range=Optional[str])

slots.residueClaim__claim_type = Slot(uri=GENE_REVIEW.claim_type, name="residueClaim__claim_type", curie=GENE_REVIEW.curie('claim_type'),
                   model_uri=GENE_REVIEW.residueClaim__claim_type, domain=None, range=Union[str, "ResidueClaimEnum"])

slots.residueClaim__site_ref = Slot(uri=GENE_REVIEW.site_ref, name="residueClaim__site_ref", curie=GENE_REVIEW.curie('site_ref'),
                   model_uri=GENE_REVIEW.residueClaim__site_ref, domain=None, range=Optional[str],
                   pattern=re.compile(r'^PANTHER:PTHR[0-9]{5}#[a-z0-9_]+$'))

slots.residueClaim__anchor = Slot(uri=GENE_REVIEW.anchor, name="residueClaim__anchor", curie=GENE_REVIEW.curie('anchor'),
                   model_uri=GENE_REVIEW.residueClaim__anchor, domain=None, range=Union[dict, ResiduePosition])

slots.residueClaim__target = Slot(uri=GENE_REVIEW.target, name="residueClaim__target", curie=GENE_REVIEW.curie('target'),
                   model_uri=GENE_REVIEW.residueClaim__target, domain=None, range=Optional[Union[dict, ResiduePosition]])

slots.residueClaim__role = Slot(uri=GENE_REVIEW.role, name="residueClaim__role", curie=GENE_REVIEW.curie('role'),
                   model_uri=GENE_REVIEW.residueClaim__role, domain=None, range=Optional[str])

slots.residueClaim__method = Slot(uri=GENE_REVIEW.method, name="residueClaim__method", curie=GENE_REVIEW.curie('method'),
                   model_uri=GENE_REVIEW.residueClaim__method, domain=None, range=Union[str, "ResidueClaimMethodEnum"])

slots.residueClaim__alignment_release = Slot(uri=GENE_REVIEW.alignment_release, name="residueClaim__alignment_release", curie=GENE_REVIEW.curie('alignment_release'),
                   model_uri=GENE_REVIEW.residueClaim__alignment_release, domain=None, range=Optional[str])

slots.residueClaim__comment = Slot(uri=GENE_REVIEW.comment, name="residueClaim__comment", curie=GENE_REVIEW.curie('comment'),
                   model_uri=GENE_REVIEW.residueClaim__comment, domain=None, range=Optional[str])

slots.residuePosition__accession = Slot(uri=GENE_REVIEW.accession, name="residuePosition__accession", curie=GENE_REVIEW.curie('accession'),
                   model_uri=GENE_REVIEW.residuePosition__accession, domain=None, range=str)

slots.residuePosition__position = Slot(uri=GENE_REVIEW.position, name="residuePosition__position", curie=GENE_REVIEW.curie('position'),
                   model_uri=GENE_REVIEW.residuePosition__position, domain=None, range=int)

slots.residuePosition__residue = Slot(uri=GENE_REVIEW.residue, name="residuePosition__residue", curie=GENE_REVIEW.curie('residue'),
                   model_uri=GENE_REVIEW.residuePosition__residue, domain=None, range=str,
                   pattern=re.compile(r'^[ACDEFGHIKLMNPQRSTVWYUO]$'))

slots.residuePosition__sequence_version = Slot(uri=GENE_REVIEW.sequence_version, name="residuePosition__sequence_version", curie=GENE_REVIEW.curie('sequence_version'),
                   model_uri=GENE_REVIEW.residuePosition__sequence_version, domain=None, range=Optional[int])

slots.propagationSource__source_id = Slot(uri=GENE_REVIEW.source_id, name="propagationSource__source_id", curie=GENE_REVIEW.curie('source_id'),
                   model_uri=GENE_REVIEW.propagationSource__source_id, domain=None, range=str)

slots.propagationSource__source_label = Slot(uri=GENE_REVIEW.source_label, name="propagationSource__source_label", curie=GENE_REVIEW.curie('source_label'),
                   model_uri=GENE_REVIEW.propagationSource__source_label, domain=None, range=Optional[str])

slots.propagationSource__source_status = Slot(uri=GENE_REVIEW.source_status, name="propagationSource__source_status", curie=GENE_REVIEW.curie('source_status'),
                   model_uri=GENE_REVIEW.propagationSource__source_status, domain=None, range=Optional[Union[str, "PropagationSourceStatusEnum"]])

slots.propagationSource__comment = Slot(uri=GENE_REVIEW.comment, name="propagationSource__comment", curie=GENE_REVIEW.curie('comment'),
                   model_uri=GENE_REVIEW.propagationSource__comment, domain=None, range=Optional[str])

slots.coreFunction__description = Slot(uri=GENE_REVIEW.description, name="coreFunction__description", curie=GENE_REVIEW.curie('description'),
                   model_uri=GENE_REVIEW.coreFunction__description, domain=None, range=Optional[str])

slots.coreFunction__supported_by = Slot(uri=GENE_REVIEW.supported_by, name="coreFunction__supported_by", curie=GENE_REVIEW.curie('supported_by'),
                   model_uri=GENE_REVIEW.coreFunction__supported_by, domain=None, range=Optional[Union[Union[dict, SupportingTextInReference], list[Union[dict, SupportingTextInReference]]]])

slots.coreFunction__molecular_function = Slot(uri=GENE_REVIEW.molecular_function, name="coreFunction__molecular_function", curie=GENE_REVIEW.curie('molecular_function'),
                   model_uri=GENE_REVIEW.coreFunction__molecular_function, domain=None, range=Optional[Union[dict, Term]])

slots.coreFunction__contributes_to_molecular_function = Slot(uri=GENE_REVIEW.contributes_to_molecular_function, name="coreFunction__contributes_to_molecular_function", curie=GENE_REVIEW.curie('contributes_to_molecular_function'),
                   model_uri=GENE_REVIEW.coreFunction__contributes_to_molecular_function, domain=None, range=Optional[Union[dict, Term]])

slots.coreFunction__directly_involved_in = Slot(uri=GENE_REVIEW.directly_involved_in, name="coreFunction__directly_involved_in", curie=GENE_REVIEW.curie('directly_involved_in'),
                   model_uri=GENE_REVIEW.coreFunction__directly_involved_in, domain=None, range=Optional[Union[dict[Union[str, TermId], Union[dict, Term]], list[Union[dict, Term]]]])

slots.coreFunction__locations = Slot(uri=GENE_REVIEW.locations, name="coreFunction__locations", curie=GENE_REVIEW.curie('locations'),
                   model_uri=GENE_REVIEW.coreFunction__locations, domain=None, range=Optional[Union[dict[Union[str, TermId], Union[dict, Term]], list[Union[dict, Term]]]])

slots.coreFunction__anatomical_locations = Slot(uri=GENE_REVIEW.anatomical_locations, name="coreFunction__anatomical_locations", curie=GENE_REVIEW.curie('anatomical_locations'),
                   model_uri=GENE_REVIEW.coreFunction__anatomical_locations, domain=None, range=Optional[Union[dict[Union[str, TermId], Union[dict, Term]], list[Union[dict, Term]]]])

slots.coreFunction__substrates = Slot(uri=GENE_REVIEW.substrates, name="coreFunction__substrates", curie=GENE_REVIEW.curie('substrates'),
                   model_uri=GENE_REVIEW.coreFunction__substrates, domain=None, range=Optional[Union[dict[Union[str, TermId], Union[dict, Term]], list[Union[dict, Term]]]])

slots.coreFunction__in_complex = Slot(uri=GENE_REVIEW.in_complex, name="coreFunction__in_complex", curie=GENE_REVIEW.curie('in_complex'),
                   model_uri=GENE_REVIEW.coreFunction__in_complex, domain=None, range=Optional[Union[dict, Term]])

slots.termMapping__predicate = Slot(uri=GENE_REVIEW.predicate, name="termMapping__predicate", curie=GENE_REVIEW.curie('predicate'),
                   model_uri=GENE_REVIEW.termMapping__predicate, domain=None, range=str)

slots.termMapping__target_term = Slot(uri=GENE_REVIEW.target_term, name="termMapping__target_term", curie=GENE_REVIEW.curie('target_term'),
                   model_uri=GENE_REVIEW.termMapping__target_term, domain=None, range=Union[dict, Term])

slots.proposedOntologyTerm__proposed_name = Slot(uri=GENE_REVIEW.proposed_name, name="proposedOntologyTerm__proposed_name", curie=GENE_REVIEW.curie('proposed_name'),
                   model_uri=GENE_REVIEW.proposedOntologyTerm__proposed_name, domain=None, range=str)

slots.proposedOntologyTerm__proposed_definition = Slot(uri=GENE_REVIEW.proposed_definition, name="proposedOntologyTerm__proposed_definition", curie=GENE_REVIEW.curie('proposed_definition'),
                   model_uri=GENE_REVIEW.proposedOntologyTerm__proposed_definition, domain=None, range=str)

slots.proposedOntologyTerm__justification = Slot(uri=GENE_REVIEW.justification, name="proposedOntologyTerm__justification", curie=GENE_REVIEW.curie('justification'),
                   model_uri=GENE_REVIEW.proposedOntologyTerm__justification, domain=None, range=Optional[str])

slots.proposedOntologyTerm__proposed_parent = Slot(uri=GENE_REVIEW.proposed_parent, name="proposedOntologyTerm__proposed_parent", curie=GENE_REVIEW.curie('proposed_parent'),
                   model_uri=GENE_REVIEW.proposedOntologyTerm__proposed_parent, domain=None, range=Optional[Union[dict, Term]])

slots.proposedOntologyTerm__proposed_mappings = Slot(uri=GENE_REVIEW.proposed_mappings, name="proposedOntologyTerm__proposed_mappings", curie=GENE_REVIEW.curie('proposed_mappings'),
                   model_uri=GENE_REVIEW.proposedOntologyTerm__proposed_mappings, domain=None, range=Optional[Union[Union[dict, TermMapping], list[Union[dict, TermMapping]]]])

slots.proposedOntologyTerm__supported_by = Slot(uri=GENE_REVIEW.supported_by, name="proposedOntologyTerm__supported_by", curie=GENE_REVIEW.curie('supported_by'),
                   model_uri=GENE_REVIEW.proposedOntologyTerm__supported_by, domain=None, range=Optional[Union[Union[dict, SupportingTextInReference], list[Union[dict, SupportingTextInReference]]]])

slots.knowledgeGap__gap_statement = Slot(uri=GENE_REVIEW.gap_statement, name="knowledgeGap__gap_statement", curie=GENE_REVIEW.curie('gap_statement'),
                   model_uri=GENE_REVIEW.knowledgeGap__gap_statement, domain=None, range=str)

slots.knowledgeGap__boundary = Slot(uri=GENE_REVIEW.boundary, name="knowledgeGap__boundary", curie=GENE_REVIEW.curie('boundary'),
                   model_uri=GENE_REVIEW.knowledgeGap__boundary, domain=None, range=Optional[str])

slots.knowledgeGap__gap_kind = Slot(uri=GENE_REVIEW.gap_kind, name="knowledgeGap__gap_kind", curie=GENE_REVIEW.curie('gap_kind'),
                   model_uri=GENE_REVIEW.knowledgeGap__gap_kind, domain=None, range=Optional[Union[Union[str, "KnowledgeGapKindEnum"], list[Union[str, "KnowledgeGapKindEnum"]]]])

slots.knowledgeGap__dark_aspect = Slot(uri=GENE_REVIEW.dark_aspect, name="knowledgeGap__dark_aspect", curie=GENE_REVIEW.curie('dark_aspect'),
                   model_uri=GENE_REVIEW.knowledgeGap__dark_aspect, domain=None, range=Optional[Union[str, "KnowledgeGapAspectEnum"]])

slots.knowledgeGap__status = Slot(uri=GENE_REVIEW.status, name="knowledgeGap__status", curie=GENE_REVIEW.curie('status'),
                   model_uri=GENE_REVIEW.knowledgeGap__status, domain=None, range=Optional[Union[str, "KnowledgeGapStatusEnum"]])

slots.knowledgeGap__significance = Slot(uri=GENE_REVIEW.significance, name="knowledgeGap__significance", curie=GENE_REVIEW.curie('significance'),
                   model_uri=GENE_REVIEW.knowledgeGap__significance, domain=None, range=Optional[str])

slots.knowledgeGap__resolution = Slot(uri=GENE_REVIEW.resolution, name="knowledgeGap__resolution", curie=GENE_REVIEW.curie('resolution'),
                   model_uri=GENE_REVIEW.knowledgeGap__resolution, domain=None, range=Optional[str])

slots.knowledgeGap__provenance = Slot(uri=GENE_REVIEW.provenance, name="knowledgeGap__provenance", curie=GENE_REVIEW.curie('provenance'),
                   model_uri=GENE_REVIEW.knowledgeGap__provenance, domain=None, range=Optional[Union[Union[dict, SupportingTextInReference], list[Union[dict, SupportingTextInReference]]]])

slots.knowledgeGap__proposed_terms = Slot(uri=GENE_REVIEW.proposed_terms, name="knowledgeGap__proposed_terms", curie=GENE_REVIEW.curie('proposed_terms'),
                   model_uri=GENE_REVIEW.knowledgeGap__proposed_terms, domain=None, range=Optional[Union[Union[dict, ProposedOntologyTerm], list[Union[dict, ProposedOntologyTerm]]]])

slots.experiment__hypothesis = Slot(uri=GENE_REVIEW.hypothesis, name="experiment__hypothesis", curie=GENE_REVIEW.curie('hypothesis'),
                   model_uri=GENE_REVIEW.experiment__hypothesis, domain=None, range=Optional[str])

slots.experiment__description = Slot(uri=GENE_REVIEW.description, name="experiment__description", curie=GENE_REVIEW.curie('description'),
                   model_uri=GENE_REVIEW.experiment__description, domain=None, range=str)

slots.experiment__experiment_type = Slot(uri=GENE_REVIEW.experiment_type, name="experiment__experiment_type", curie=GENE_REVIEW.curie('experiment_type'),
                   model_uri=GENE_REVIEW.experiment__experiment_type, domain=None, range=Optional[str])

slots.question__question = Slot(uri=GENE_REVIEW.question, name="question__question", curie=GENE_REVIEW.curie('question'),
                   model_uri=GENE_REVIEW.question__question, domain=None, range=str)

slots.question__experts = Slot(uri=GENE_REVIEW.experts, name="question__experts", curie=GENE_REVIEW.curie('experts'),
                   model_uri=GENE_REVIEW.question__experts, domain=None, range=Optional[Union[str, list[str]]])

slots.ruleReview__status = Slot(uri=GENE_REVIEW.status, name="ruleReview__status", curie=GENE_REVIEW.curie('status'),
                   model_uri=GENE_REVIEW.ruleReview__status, domain=None, range=Optional[Union[str, "RuleReviewStatusEnum"]])

slots.ruleReview__rule_type = Slot(uri=GENE_REVIEW.rule_type, name="ruleReview__rule_type", curie=GENE_REVIEW.curie('rule_type'),
                   model_uri=GENE_REVIEW.ruleReview__rule_type, domain=None, range=Union[str, "RuleTypeEnum"])

slots.ruleReview__rule = Slot(uri=GENE_REVIEW.rule, name="ruleReview__rule", curie=GENE_REVIEW.curie('rule'),
                   model_uri=GENE_REVIEW.ruleReview__rule, domain=None, range=Union[dict, EmbeddedRule])

slots.ruleReview__review_summary = Slot(uri=GENE_REVIEW.review_summary, name="ruleReview__review_summary", curie=GENE_REVIEW.curie('review_summary'),
                   model_uri=GENE_REVIEW.ruleReview__review_summary, domain=None, range=Optional[str])

slots.ruleReview__action = Slot(uri=GENE_REVIEW.action, name="ruleReview__action", curie=GENE_REVIEW.curie('action'),
                   model_uri=GENE_REVIEW.ruleReview__action, domain=None, range=Union[str, "RuleActionEnum"])

slots.ruleReview__action_rationale = Slot(uri=GENE_REVIEW.action_rationale, name="ruleReview__action_rationale", curie=GENE_REVIEW.curie('action_rationale'),
                   model_uri=GENE_REVIEW.ruleReview__action_rationale, domain=None, range=Optional[str])

slots.ruleReview__suggested_modifications = Slot(uri=GENE_REVIEW.suggested_modifications, name="ruleReview__suggested_modifications", curie=GENE_REVIEW.curie('suggested_modifications'),
                   model_uri=GENE_REVIEW.ruleReview__suggested_modifications, domain=None, range=Optional[Union[str, list[str]]])

slots.ruleReview__parsimony = Slot(uri=GENE_REVIEW.parsimony, name="ruleReview__parsimony", curie=GENE_REVIEW.curie('parsimony'),
                   model_uri=GENE_REVIEW.ruleReview__parsimony, domain=None, range=Optional[Union[dict, ParsimonyAssessment]])

slots.ruleReview__literature_support = Slot(uri=GENE_REVIEW.literature_support, name="ruleReview__literature_support", curie=GENE_REVIEW.curie('literature_support'),
                   model_uri=GENE_REVIEW.ruleReview__literature_support, domain=None, range=Optional[Union[dict, LiteratureSupportAssessment]])

slots.ruleReview__condition_overlap = Slot(uri=GENE_REVIEW.condition_overlap, name="ruleReview__condition_overlap", curie=GENE_REVIEW.curie('condition_overlap'),
                   model_uri=GENE_REVIEW.ruleReview__condition_overlap, domain=None, range=Optional[Union[dict, ConditionOverlapAssessment]])

slots.ruleReview__go_specificity = Slot(uri=GENE_REVIEW.go_specificity, name="ruleReview__go_specificity", curie=GENE_REVIEW.curie('go_specificity'),
                   model_uri=GENE_REVIEW.ruleReview__go_specificity, domain=None, range=Optional[Union[dict, GOSpecificityAssessment]])

slots.ruleReview__taxonomic_scope = Slot(uri=GENE_REVIEW.taxonomic_scope, name="ruleReview__taxonomic_scope", curie=GENE_REVIEW.curie('taxonomic_scope'),
                   model_uri=GENE_REVIEW.ruleReview__taxonomic_scope, domain=None, range=Optional[Union[dict, TaxonomicScopeAssessment]])

slots.ruleReview__confidence = Slot(uri=GENE_REVIEW.confidence, name="ruleReview__confidence", curie=GENE_REVIEW.curie('confidence'),
                   model_uri=GENE_REVIEW.ruleReview__confidence, domain=None, range=Optional[float])

slots.ruleReview__supported_by = Slot(uri=GENE_REVIEW.supported_by, name="ruleReview__supported_by", curie=GENE_REVIEW.curie('supported_by'),
                   model_uri=GENE_REVIEW.ruleReview__supported_by, domain=None, range=Optional[Union[Union[dict, SupportingTextInReference], list[Union[dict, SupportingTextInReference]]]])

slots.embeddedRule__rule_id = Slot(uri=GENE_REVIEW.rule_id, name="embeddedRule__rule_id", curie=GENE_REVIEW.curie('rule_id'),
                   model_uri=GENE_REVIEW.embeddedRule__rule_id, domain=None, range=str)

slots.embeddedRule__condition_sets = Slot(uri=GENE_REVIEW.condition_sets, name="embeddedRule__condition_sets", curie=GENE_REVIEW.curie('condition_sets'),
                   model_uri=GENE_REVIEW.embeddedRule__condition_sets, domain=None, range=Union[Union[dict, RuleConditionSet], list[Union[dict, RuleConditionSet]]])

slots.embeddedRule__go_annotations = Slot(uri=GENE_REVIEW.go_annotations, name="embeddedRule__go_annotations", curie=GENE_REVIEW.curie('go_annotations'),
                   model_uri=GENE_REVIEW.embeddedRule__go_annotations, domain=None, range=Optional[Union[Union[dict, RuleGOAnnotation], list[Union[dict, RuleGOAnnotation]]]])

slots.embeddedRule__ipr2go_redundancy = Slot(uri=GENE_REVIEW.ipr2go_redundancy, name="embeddedRule__ipr2go_redundancy", curie=GENE_REVIEW.curie('ipr2go_redundancy'),
                   model_uri=GENE_REVIEW.embeddedRule__ipr2go_redundancy, domain=None, range=Optional[Union[dict, InterPro2GORedundancy]])

slots.embeddedRule__entries = Slot(uri=GENE_REVIEW.entries, name="embeddedRule__entries", curie=GENE_REVIEW.curie('entries'),
                   model_uri=GENE_REVIEW.embeddedRule__entries, domain=None, range=Union[dict[Union[str, RuleReviewEntryId], Union[dict, RuleReviewEntry]], list[Union[dict, RuleReviewEntry]]])

slots.embeddedRule__reviewed_protein_count = Slot(uri=GENE_REVIEW.reviewed_protein_count, name="embeddedRule__reviewed_protein_count", curie=GENE_REVIEW.curie('reviewed_protein_count'),
                   model_uri=GENE_REVIEW.embeddedRule__reviewed_protein_count, domain=None, range=Optional[int])

slots.embeddedRule__unreviewed_protein_count = Slot(uri=GENE_REVIEW.unreviewed_protein_count, name="embeddedRule__unreviewed_protein_count", curie=GENE_REVIEW.curie('unreviewed_protein_count'),
                   model_uri=GENE_REVIEW.embeddedRule__unreviewed_protein_count, domain=None, range=Optional[int])

slots.embeddedRule__created_date = Slot(uri=GENE_REVIEW.created_date, name="embeddedRule__created_date", curie=GENE_REVIEW.curie('created_date'),
                   model_uri=GENE_REVIEW.embeddedRule__created_date, domain=None, range=Optional[str])

slots.embeddedRule__modified_date = Slot(uri=GENE_REVIEW.modified_date, name="embeddedRule__modified_date", curie=GENE_REVIEW.curie('modified_date'),
                   model_uri=GENE_REVIEW.embeddedRule__modified_date, domain=None, range=Optional[str])

slots.ruleConditionSet__number = Slot(uri=GENE_REVIEW.number, name="ruleConditionSet__number", curie=GENE_REVIEW.curie('number'),
                   model_uri=GENE_REVIEW.ruleConditionSet__number, domain=None, range=int)

slots.ruleConditionSet__conditions = Slot(uri=GENE_REVIEW.conditions, name="ruleConditionSet__conditions", curie=GENE_REVIEW.curie('conditions'),
                   model_uri=GENE_REVIEW.ruleConditionSet__conditions, domain=None, range=Union[Union[dict, RuleCondition], list[Union[dict, RuleCondition]]])

slots.ruleConditionSet__notes = Slot(uri=GENE_REVIEW.notes, name="ruleConditionSet__notes", curie=GENE_REVIEW.curie('notes'),
                   model_uri=GENE_REVIEW.ruleConditionSet__notes, domain=None, range=Optional[str])

slots.ruleConditionSet__pairwise_overlap = Slot(uri=GENE_REVIEW.pairwise_overlap, name="ruleConditionSet__pairwise_overlap", curie=GENE_REVIEW.curie('pairwise_overlap'),
                   model_uri=GENE_REVIEW.ruleConditionSet__pairwise_overlap, domain=None, range=Optional[Union[Union[dict, PairwiseOverlap], list[Union[dict, PairwiseOverlap]]]])

slots.ruleCondition__condition_type = Slot(uri=GENE_REVIEW.condition_type, name="ruleCondition__condition_type", curie=GENE_REVIEW.curie('condition_type'),
                   model_uri=GENE_REVIEW.ruleCondition__condition_type, domain=None, range=Union[str, "ConditionTypeEnum"])

slots.ruleCondition__value = Slot(uri=GENE_REVIEW.value, name="ruleCondition__value", curie=GENE_REVIEW.curie('value'),
                   model_uri=GENE_REVIEW.ruleCondition__value, domain=None, range=str)

slots.ruleCondition__curie = Slot(uri=GENE_REVIEW.curie, name="ruleCondition__curie", curie=GENE_REVIEW.curie('curie'),
                   model_uri=GENE_REVIEW.ruleCondition__curie, domain=None, range=Optional[str])

slots.ruleCondition__label = Slot(uri=GENE_REVIEW.label, name="ruleCondition__label", curie=GENE_REVIEW.curie('label'),
                   model_uri=GENE_REVIEW.ruleCondition__label, domain=None, range=Optional[str])

slots.ruleCondition__interpro_type = Slot(uri=GENE_REVIEW.interpro_type, name="ruleCondition__interpro_type", curie=GENE_REVIEW.curie('interpro_type'),
                   model_uri=GENE_REVIEW.ruleCondition__interpro_type, domain=None, range=Optional[Union[str, "InterProTypeEnum"]])

slots.ruleCondition__negated = Slot(uri=GENE_REVIEW.negated, name="ruleCondition__negated", curie=GENE_REVIEW.curie('negated'),
                   model_uri=GENE_REVIEW.ruleCondition__negated, domain=None, range=Optional[Union[bool, Bool]])

slots.ruleCondition__protein_count = Slot(uri=GENE_REVIEW.protein_count, name="ruleCondition__protein_count", curie=GENE_REVIEW.curie('protein_count'),
                   model_uri=GENE_REVIEW.ruleCondition__protein_count, domain=None, range=Optional[int])

slots.ruleCondition__protein_database = Slot(uri=GENE_REVIEW.protein_database, name="ruleCondition__protein_database", curie=GENE_REVIEW.curie('protein_database'),
                   model_uri=GENE_REVIEW.ruleCondition__protein_database, domain=None, range=Optional[Union[str, "ProteinDatabaseEnum"]])

slots.ruleCondition__uniqueness_score = Slot(uri=GENE_REVIEW.uniqueness_score, name="ruleCondition__uniqueness_score", curie=GENE_REVIEW.curie('uniqueness_score'),
                   model_uri=GENE_REVIEW.ruleCondition__uniqueness_score, domain=None, range=Optional[float])

slots.ruleCondition__sample_proteins = Slot(uri=GENE_REVIEW.sample_proteins, name="ruleCondition__sample_proteins", curie=GENE_REVIEW.curie('sample_proteins'),
                   model_uri=GENE_REVIEW.ruleCondition__sample_proteins, domain=None, range=Optional[Union[str, list[str]]])

slots.ruleGOAnnotation__go_id = Slot(uri=GENE_REVIEW.go_id, name="ruleGOAnnotation__go_id", curie=GENE_REVIEW.curie('go_id'),
                   model_uri=GENE_REVIEW.ruleGOAnnotation__go_id, domain=None, range=str)

slots.ruleGOAnnotation__go_label = Slot(uri=GENE_REVIEW.go_label, name="ruleGOAnnotation__go_label", curie=GENE_REVIEW.curie('go_label'),
                   model_uri=GENE_REVIEW.ruleGOAnnotation__go_label, domain=None, range=Optional[str])

slots.ruleGOAnnotation__aspect = Slot(uri=GENE_REVIEW.aspect, name="ruleGOAnnotation__aspect", curie=GENE_REVIEW.curie('aspect'),
                   model_uri=GENE_REVIEW.ruleGOAnnotation__aspect, domain=None, range=Optional[str])

slots.pairwiseOverlap__condition_a = Slot(uri=GENE_REVIEW.condition_a, name="pairwiseOverlap__condition_a", curie=GENE_REVIEW.curie('condition_a'),
                   model_uri=GENE_REVIEW.pairwiseOverlap__condition_a, domain=None, range=str)

slots.pairwiseOverlap__condition_b = Slot(uri=GENE_REVIEW.condition_b, name="pairwiseOverlap__condition_b", curie=GENE_REVIEW.curie('condition_b'),
                   model_uri=GENE_REVIEW.pairwiseOverlap__condition_b, domain=None, range=str)

slots.pairwiseOverlap__condition_a_label = Slot(uri=GENE_REVIEW.condition_a_label, name="pairwiseOverlap__condition_a_label", curie=GENE_REVIEW.curie('condition_a_label'),
                   model_uri=GENE_REVIEW.pairwiseOverlap__condition_a_label, domain=None, range=Optional[str])

slots.pairwiseOverlap__condition_b_label = Slot(uri=GENE_REVIEW.condition_b_label, name="pairwiseOverlap__condition_b_label", curie=GENE_REVIEW.curie('condition_b_label'),
                   model_uri=GENE_REVIEW.pairwiseOverlap__condition_b_label, domain=None, range=Optional[str])

slots.pairwiseOverlap__protein_database = Slot(uri=GENE_REVIEW.protein_database, name="pairwiseOverlap__protein_database", curie=GENE_REVIEW.curie('protein_database'),
                   model_uri=GENE_REVIEW.pairwiseOverlap__protein_database, domain=None, range=Union[str, "ProteinDatabaseEnum"])

slots.pairwiseOverlap__count_a = Slot(uri=GENE_REVIEW.count_a, name="pairwiseOverlap__count_a", curie=GENE_REVIEW.curie('count_a'),
                   model_uri=GENE_REVIEW.pairwiseOverlap__count_a, domain=None, range=int)

slots.pairwiseOverlap__count_b = Slot(uri=GENE_REVIEW.count_b, name="pairwiseOverlap__count_b", curie=GENE_REVIEW.curie('count_b'),
                   model_uri=GENE_REVIEW.pairwiseOverlap__count_b, domain=None, range=int)

slots.pairwiseOverlap__intersection_count = Slot(uri=GENE_REVIEW.intersection_count, name="pairwiseOverlap__intersection_count", curie=GENE_REVIEW.curie('intersection_count'),
                   model_uri=GENE_REVIEW.pairwiseOverlap__intersection_count, domain=None, range=int)

slots.pairwiseOverlap__a_minus_b_count = Slot(uri=GENE_REVIEW.a_minus_b_count, name="pairwiseOverlap__a_minus_b_count", curie=GENE_REVIEW.curie('a_minus_b_count'),
                   model_uri=GENE_REVIEW.pairwiseOverlap__a_minus_b_count, domain=None, range=int)

slots.pairwiseOverlap__b_minus_a_count = Slot(uri=GENE_REVIEW.b_minus_a_count, name="pairwiseOverlap__b_minus_a_count", curie=GENE_REVIEW.curie('b_minus_a_count'),
                   model_uri=GENE_REVIEW.pairwiseOverlap__b_minus_a_count, domain=None, range=int)

slots.pairwiseOverlap__jaccard_similarity = Slot(uri=GENE_REVIEW.jaccard_similarity, name="pairwiseOverlap__jaccard_similarity", curie=GENE_REVIEW.curie('jaccard_similarity'),
                   model_uri=GENE_REVIEW.pairwiseOverlap__jaccard_similarity, domain=None, range=float)

slots.pairwiseOverlap__containment_a_in_b = Slot(uri=GENE_REVIEW.containment_a_in_b, name="pairwiseOverlap__containment_a_in_b", curie=GENE_REVIEW.curie('containment_a_in_b'),
                   model_uri=GENE_REVIEW.pairwiseOverlap__containment_a_in_b, domain=None, range=float)

slots.pairwiseOverlap__containment_b_in_a = Slot(uri=GENE_REVIEW.containment_b_in_a, name="pairwiseOverlap__containment_b_in_a", curie=GENE_REVIEW.curie('containment_b_in_a'),
                   model_uri=GENE_REVIEW.pairwiseOverlap__containment_b_in_a, domain=None, range=float)

slots.pairwiseOverlap__interpretation = Slot(uri=GENE_REVIEW.interpretation, name="pairwiseOverlap__interpretation", curie=GENE_REVIEW.curie('interpretation'),
                   model_uri=GENE_REVIEW.pairwiseOverlap__interpretation, domain=None, range=Optional[Union[str, "OverlapInterpretationEnum"]])

slots.pairwiseOverlap__condition_a_in_sets = Slot(uri=GENE_REVIEW.condition_a_in_sets, name="pairwiseOverlap__condition_a_in_sets", curie=GENE_REVIEW.curie('condition_a_in_sets'),
                   model_uri=GENE_REVIEW.pairwiseOverlap__condition_a_in_sets, domain=None, range=Optional[Union[int, list[int]]])

slots.pairwiseOverlap__condition_b_in_sets = Slot(uri=GENE_REVIEW.condition_b_in_sets, name="pairwiseOverlap__condition_b_in_sets", curie=GENE_REVIEW.curie('condition_b_in_sets'),
                   model_uri=GENE_REVIEW.pairwiseOverlap__condition_b_in_sets, domain=None, range=Optional[Union[int, list[int]]])

slots.ruleReviewEntry__id = Slot(uri=GENE_REVIEW.id, name="ruleReviewEntry__id", curie=GENE_REVIEW.curie('id'),
                   model_uri=GENE_REVIEW.ruleReviewEntry__id, domain=None, range=URIRef)

slots.ruleReviewEntry__label = Slot(uri=GENE_REVIEW.label, name="ruleReviewEntry__label", curie=GENE_REVIEW.curie('label'),
                   model_uri=GENE_REVIEW.ruleReviewEntry__label, domain=None, range=Optional[str])

slots.ruleReviewEntry__type = Slot(uri=GENE_REVIEW.type, name="ruleReviewEntry__type", curie=GENE_REVIEW.curie('type'),
                   model_uri=GENE_REVIEW.ruleReviewEntry__type, domain=None, range=Union[str, "EntryTypeEnum"])

slots.ruleReviewEntry__appears_in_condition_sets = Slot(uri=GENE_REVIEW.appears_in_condition_sets, name="ruleReviewEntry__appears_in_condition_sets", curie=GENE_REVIEW.curie('appears_in_condition_sets'),
                   model_uri=GENE_REVIEW.ruleReviewEntry__appears_in_condition_sets, domain=None, range=Optional[Union[int, list[int]]])

slots.ruleReviewEntry__protein_count = Slot(uri=GENE_REVIEW.protein_count, name="ruleReviewEntry__protein_count", curie=GENE_REVIEW.curie('protein_count'),
                   model_uri=GENE_REVIEW.ruleReviewEntry__protein_count, domain=None, range=Optional[int])

slots.ruleReviewEntry__source = Slot(uri=GENE_REVIEW.source, name="ruleReviewEntry__source", curie=GENE_REVIEW.curie('source'),
                   model_uri=GENE_REVIEW.ruleReviewEntry__source, domain=None, range=Optional[str])

slots.ruleReviewEntry__asserted_predicted_go_terms = Slot(uri=GENE_REVIEW.asserted_predicted_go_terms, name="ruleReviewEntry__asserted_predicted_go_terms", curie=GENE_REVIEW.curie('asserted_predicted_go_terms'),
                   model_uri=GENE_REVIEW.ruleReviewEntry__asserted_predicted_go_terms, domain=None, range=Optional[Union[str, list[str]]])

slots.ruleReviewEntry__related_entries = Slot(uri=GENE_REVIEW.related_entries, name="ruleReviewEntry__related_entries", curie=GENE_REVIEW.curie('related_entries'),
                   model_uri=GENE_REVIEW.ruleReviewEntry__related_entries, domain=None, range=Optional[Union[Union[dict, RelatedEntry], list[Union[dict, RelatedEntry]]]])

slots.relatedEntry__relationship = Slot(uri=GENE_REVIEW.relationship, name="relatedEntry__relationship", curie=GENE_REVIEW.curie('relationship'),
                   model_uri=GENE_REVIEW.relatedEntry__relationship, domain=None, range=Union[str, "EntryRelationshipEnum"])

slots.relatedEntry__target_id = Slot(uri=GENE_REVIEW.target_id, name="relatedEntry__target_id", curie=GENE_REVIEW.curie('target_id'),
                   model_uri=GENE_REVIEW.relatedEntry__target_id, domain=None, range=str)

slots.relatedEntry__containment = Slot(uri=GENE_REVIEW.containment, name="relatedEntry__containment", curie=GENE_REVIEW.curie('containment'),
                   model_uri=GENE_REVIEW.relatedEntry__containment, domain=None, range=Optional[float])

slots.relatedEntry__jaccard_similarity = Slot(uri=GENE_REVIEW.jaccard_similarity, name="relatedEntry__jaccard_similarity", curie=GENE_REVIEW.curie('jaccard_similarity'),
                   model_uri=GENE_REVIEW.relatedEntry__jaccard_similarity, domain=None, range=Optional[float])

slots.relatedEntry__intersection_count = Slot(uri=GENE_REVIEW.intersection_count, name="relatedEntry__intersection_count", curie=GENE_REVIEW.curie('intersection_count'),
                   model_uri=GENE_REVIEW.relatedEntry__intersection_count, domain=None, range=Optional[int])

slots.relatedEntry__exclusive_count = Slot(uri=GENE_REVIEW.exclusive_count, name="relatedEntry__exclusive_count", curie=GENE_REVIEW.curie('exclusive_count'),
                   model_uri=GENE_REVIEW.relatedEntry__exclusive_count, domain=None, range=Optional[int])

slots.interPro2GORedundancy__redundant_annotations = Slot(uri=GENE_REVIEW.redundant_annotations, name="interPro2GORedundancy__redundant_annotations", curie=GENE_REVIEW.curie('redundant_annotations'),
                   model_uri=GENE_REVIEW.interPro2GORedundancy__redundant_annotations, domain=None, range=Optional[Union[Union[dict, RedundantAnnotation], list[Union[dict, RedundantAnnotation]]]])

slots.interPro2GORedundancy__novel_annotations = Slot(uri=GENE_REVIEW.novel_annotations, name="interPro2GORedundancy__novel_annotations", curie=GENE_REVIEW.curie('novel_annotations'),
                   model_uri=GENE_REVIEW.interPro2GORedundancy__novel_annotations, domain=None, range=Optional[Union[str, list[str]]])

slots.interPro2GORedundancy__summary = Slot(uri=GENE_REVIEW.summary, name="interPro2GORedundancy__summary", curie=GENE_REVIEW.curie('summary'),
                   model_uri=GENE_REVIEW.interPro2GORedundancy__summary, domain=None, range=Optional[str])

slots.redundantAnnotation__go_id = Slot(uri=GENE_REVIEW.go_id, name="redundantAnnotation__go_id", curie=GENE_REVIEW.curie('go_id'),
                   model_uri=GENE_REVIEW.redundantAnnotation__go_id, domain=None, range=str)

slots.redundantAnnotation__go_label = Slot(uri=GENE_REVIEW.go_label, name="redundantAnnotation__go_label", curie=GENE_REVIEW.curie('go_label'),
                   model_uri=GENE_REVIEW.redundantAnnotation__go_label, domain=None, range=Optional[str])

slots.redundantAnnotation__interpro_source = Slot(uri=GENE_REVIEW.interpro_source, name="redundantAnnotation__interpro_source", curie=GENE_REVIEW.curie('interpro_source'),
                   model_uri=GENE_REVIEW.redundantAnnotation__interpro_source, domain=None, range=str)

slots.redundantAnnotation__interpro_label = Slot(uri=GENE_REVIEW.interpro_label, name="redundantAnnotation__interpro_label", curie=GENE_REVIEW.curie('interpro_label'),
                   model_uri=GENE_REVIEW.redundantAnnotation__interpro_label, domain=None, range=Optional[str])

slots.parsimonyAssessment__assessment = Slot(uri=GENE_REVIEW.assessment, name="parsimonyAssessment__assessment", curie=GENE_REVIEW.curie('assessment'),
                   model_uri=GENE_REVIEW.parsimonyAssessment__assessment, domain=None, range=Union[str, "ParsimonyEnum"])

slots.parsimonyAssessment__notes = Slot(uri=GENE_REVIEW.notes, name="parsimonyAssessment__notes", curie=GENE_REVIEW.curie('notes'),
                   model_uri=GENE_REVIEW.parsimonyAssessment__notes, domain=None, range=Optional[str])

slots.parsimonyAssessment__supported_by = Slot(uri=GENE_REVIEW.supported_by, name="parsimonyAssessment__supported_by", curie=GENE_REVIEW.curie('supported_by'),
                   model_uri=GENE_REVIEW.parsimonyAssessment__supported_by, domain=None, range=Optional[Union[Union[dict, SupportingTextInReference], list[Union[dict, SupportingTextInReference]]]])

slots.literatureSupportAssessment__assessment = Slot(uri=GENE_REVIEW.assessment, name="literatureSupportAssessment__assessment", curie=GENE_REVIEW.curie('assessment'),
                   model_uri=GENE_REVIEW.literatureSupportAssessment__assessment, domain=None, range=Union[str, "LiteratureSupportEnum"])

slots.literatureSupportAssessment__notes = Slot(uri=GENE_REVIEW.notes, name="literatureSupportAssessment__notes", curie=GENE_REVIEW.curie('notes'),
                   model_uri=GENE_REVIEW.literatureSupportAssessment__notes, domain=None, range=Optional[str])

slots.literatureSupportAssessment__supported_by = Slot(uri=GENE_REVIEW.supported_by, name="literatureSupportAssessment__supported_by", curie=GENE_REVIEW.curie('supported_by'),
                   model_uri=GENE_REVIEW.literatureSupportAssessment__supported_by, domain=None, range=Optional[Union[Union[dict, SupportingTextInReference], list[Union[dict, SupportingTextInReference]]]])

slots.conditionOverlapAssessment__assessment = Slot(uri=GENE_REVIEW.assessment, name="conditionOverlapAssessment__assessment", curie=GENE_REVIEW.curie('assessment'),
                   model_uri=GENE_REVIEW.conditionOverlapAssessment__assessment, domain=None, range=Union[str, "OverlapEnum"])

slots.conditionOverlapAssessment__notes = Slot(uri=GENE_REVIEW.notes, name="conditionOverlapAssessment__notes", curie=GENE_REVIEW.curie('notes'),
                   model_uri=GENE_REVIEW.conditionOverlapAssessment__notes, domain=None, range=Optional[str])

slots.conditionOverlapAssessment__supported_by = Slot(uri=GENE_REVIEW.supported_by, name="conditionOverlapAssessment__supported_by", curie=GENE_REVIEW.curie('supported_by'),
                   model_uri=GENE_REVIEW.conditionOverlapAssessment__supported_by, domain=None, range=Optional[Union[Union[dict, SupportingTextInReference], list[Union[dict, SupportingTextInReference]]]])

slots.gOSpecificityAssessment__assessment = Slot(uri=GENE_REVIEW.assessment, name="gOSpecificityAssessment__assessment", curie=GENE_REVIEW.curie('assessment'),
                   model_uri=GENE_REVIEW.gOSpecificityAssessment__assessment, domain=None, range=Union[str, "SpecificityEnum"])

slots.gOSpecificityAssessment__notes = Slot(uri=GENE_REVIEW.notes, name="gOSpecificityAssessment__notes", curie=GENE_REVIEW.curie('notes'),
                   model_uri=GENE_REVIEW.gOSpecificityAssessment__notes, domain=None, range=Optional[str])

slots.gOSpecificityAssessment__supported_by = Slot(uri=GENE_REVIEW.supported_by, name="gOSpecificityAssessment__supported_by", curie=GENE_REVIEW.curie('supported_by'),
                   model_uri=GENE_REVIEW.gOSpecificityAssessment__supported_by, domain=None, range=Optional[Union[Union[dict, SupportingTextInReference], list[Union[dict, SupportingTextInReference]]]])

slots.taxonomicScopeAssessment__assessment = Slot(uri=GENE_REVIEW.assessment, name="taxonomicScopeAssessment__assessment", curie=GENE_REVIEW.curie('assessment'),
                   model_uri=GENE_REVIEW.taxonomicScopeAssessment__assessment, domain=None, range=Union[str, "TaxonomicScopeEnum"])

slots.taxonomicScopeAssessment__notes = Slot(uri=GENE_REVIEW.notes, name="taxonomicScopeAssessment__notes", curie=GENE_REVIEW.curie('notes'),
                   model_uri=GENE_REVIEW.taxonomicScopeAssessment__notes, domain=None, range=Optional[str])

slots.taxonomicScopeAssessment__supported_by = Slot(uri=GENE_REVIEW.supported_by, name="taxonomicScopeAssessment__supported_by", curie=GENE_REVIEW.curie('supported_by'),
                   model_uri=GENE_REVIEW.taxonomicScopeAssessment__supported_by, domain=None, range=Optional[Union[Union[dict, SupportingTextInReference], list[Union[dict, SupportingTextInReference]]]])

slots.predictionReview__locus_tag = Slot(uri=GENE_REVIEW.locus_tag, name="predictionReview__locus_tag", curie=GENE_REVIEW.curie('locus_tag'),
                   model_uri=GENE_REVIEW.predictionReview__locus_tag, domain=None, range=Optional[str])

slots.predictionReview__source_documents = Slot(uri=GENE_REVIEW.source_documents, name="predictionReview__source_documents", curie=GENE_REVIEW.curie('source_documents'),
                   model_uri=GENE_REVIEW.predictionReview__source_documents, domain=None, range=Optional[Union[str, list[str]]])

slots.predictionReview__predictions = Slot(uri=GENE_REVIEW.predictions, name="predictionReview__predictions", curie=GENE_REVIEW.curie('predictions'),
                   model_uri=GENE_REVIEW.predictionReview__predictions, domain=None, range=Optional[Union[Union[dict, PredictedAnnotation], list[Union[dict, PredictedAnnotation]]]])

slots.predictedAnnotation__source_method = Slot(uri=GENE_REVIEW.source_method, name="predictedAnnotation__source_method", curie=GENE_REVIEW.curie('source_method'),
                   model_uri=GENE_REVIEW.predictedAnnotation__source_method, domain=None, range=str)

slots.predictedAnnotation__source_version = Slot(uri=GENE_REVIEW.source_version, name="predictedAnnotation__source_version", curie=GENE_REVIEW.curie('source_version'),
                   model_uri=GENE_REVIEW.predictedAnnotation__source_version, domain=None, range=Optional[str])

slots.predictedAnnotation__source_reference_id = Slot(uri=GENE_REVIEW.source_reference_id, name="predictedAnnotation__source_reference_id", curie=GENE_REVIEW.curie('source_reference_id'),
                   model_uri=GENE_REVIEW.predictedAnnotation__source_reference_id, domain=None, range=Optional[str])

slots.predictedAnnotation__predicted_term = Slot(uri=GENE_REVIEW.predicted_term, name="predictedAnnotation__predicted_term", curie=GENE_REVIEW.curie('predicted_term'),
                   model_uri=GENE_REVIEW.predictedAnnotation__predicted_term, domain=None, range=Union[dict, Term])

slots.predictedAnnotation__predicted_term_type = Slot(uri=GENE_REVIEW.predicted_term_type, name="predictedAnnotation__predicted_term_type", curie=GENE_REVIEW.curie('predicted_term_type'),
                   model_uri=GENE_REVIEW.predictedAnnotation__predicted_term_type, domain=None, range=Union[str, "PredictedTermTypeEnum"])

slots.predictedAnnotation__review = Slot(uri=GENE_REVIEW.review, name="predictedAnnotation__review", curie=GENE_REVIEW.curie('review'),
                   model_uri=GENE_REVIEW.predictedAnnotation__review, domain=None, range=Union[dict, PredictionAssessment])

slots.predictionAssessment__assessment = Slot(uri=GENE_REVIEW.assessment, name="predictionAssessment__assessment", curie=GENE_REVIEW.curie('assessment'),
                   model_uri=GENE_REVIEW.predictionAssessment__assessment, domain=None, range=Union[str, "PredictionAssessmentEnum"])

slots.predictionAssessment__confidence_score = Slot(uri=GENE_REVIEW.confidence_score, name="predictionAssessment__confidence_score", curie=GENE_REVIEW.curie('confidence_score'),
                   model_uri=GENE_REVIEW.predictionAssessment__confidence_score, domain=None, range=int)

slots.predictionAssessment__error_type = Slot(uri=GENE_REVIEW.error_type, name="predictionAssessment__error_type", curie=GENE_REVIEW.curie('error_type'),
                   model_uri=GENE_REVIEW.predictionAssessment__error_type, domain=None, range=Optional[Union[str, "PredictionErrorTypeEnum"]])

slots.predictionAssessment__summary = Slot(uri=GENE_REVIEW.summary, name="predictionAssessment__summary", curie=GENE_REVIEW.curie('summary'),
                   model_uri=GENE_REVIEW.predictionAssessment__summary, domain=None, range=str)

slots.predictionAssessment__supported_by = Slot(uri=GENE_REVIEW.supported_by, name="predictionAssessment__supported_by", curie=GENE_REVIEW.curie('supported_by'),
                   model_uri=GENE_REVIEW.predictionAssessment__supported_by, domain=None, range=Optional[Union[Union[dict, SupportingTextInReference], list[Union[dict, SupportingTextInReference]]]])

slots.GeneReview_description = Slot(uri=DCTERMS.description, name="GeneReview_description", curie=DCTERMS.curie('description'),
                   model_uri=GENE_REVIEW.GeneReview_description, domain=GeneReview, range=Optional[str])

slots.AlternativeProduct_id = Slot(uri=GENE_REVIEW.id, name="AlternativeProduct_id", curie=GENE_REVIEW.curie('id'),
                   model_uri=GENE_REVIEW.AlternativeProduct_id, domain=AlternativeProduct, range=Union[str, AlternativeProductId])

slots.AlternativeProduct_name = Slot(uri=GENE_REVIEW.name, name="AlternativeProduct_name", curie=GENE_REVIEW.curie('name'),
                   model_uri=GENE_REVIEW.AlternativeProduct_name, domain=AlternativeProduct, range=Optional[str])

slots.AlternativeProduct_sequence_note = Slot(uri=GENE_REVIEW.sequence_note, name="AlternativeProduct_sequence_note", curie=GENE_REVIEW.curie('sequence_note'),
                   model_uri=GENE_REVIEW.AlternativeProduct_sequence_note, domain=AlternativeProduct, range=Optional[str])

slots.AlternativeProduct_description = Slot(uri=DCTERMS.description, name="AlternativeProduct_description", curie=DCTERMS.curie('description'),
                   model_uri=GENE_REVIEW.AlternativeProduct_description, domain=AlternativeProduct, range=Optional[str])

slots.Term_id = Slot(uri=GENE_REVIEW.id, name="Term_id", curie=GENE_REVIEW.curie('id'),
                   model_uri=GENE_REVIEW.Term_id, domain=Term, range=Union[str, TermId])

slots.Term_label = Slot(uri=RDFS.label, name="Term_label", curie=RDFS.curie('label'),
                   model_uri=GENE_REVIEW.Term_label, domain=Term, range=str)

slots.Reference_id = Slot(uri=GENE_REVIEW.id, name="Reference_id", curie=GENE_REVIEW.curie('id'),
                   model_uri=GENE_REVIEW.Reference_id, domain=Reference, range=Union[str, ReferenceId])

slots.CoreFunction_description = Slot(uri=DCTERMS.description, name="CoreFunction_description", curie=DCTERMS.curie('description'),
                   model_uri=GENE_REVIEW.CoreFunction_description, domain=CoreFunction, range=Optional[str])

slots.AnnotationExtension_predicate = Slot(uri=RDF.predicate, name="AnnotationExtension_predicate", curie=RDF.curie('predicate'),
                   model_uri=GENE_REVIEW.AnnotationExtension_predicate, domain=AnnotationExtension, range=str)

slots.RuleReview_id = Slot(uri=GENE_REVIEW.id, name="RuleReview_id", curie=GENE_REVIEW.curie('id'),
                   model_uri=GENE_REVIEW.RuleReview_id, domain=RuleReview, range=Union[str, RuleReviewId])

slots.PredictionReview_id = Slot(uri=GENE_REVIEW.id, name="PredictionReview_id", curie=GENE_REVIEW.curie('id'),
                   model_uri=GENE_REVIEW.PredictionReview_id, domain=PredictionReview, range=Union[str, PredictionReviewId])

slots.PredictionReview_description = Slot(uri=DCTERMS.description, name="PredictionReview_description", curie=DCTERMS.curie('description'),
                   model_uri=GENE_REVIEW.PredictionReview_description, domain=PredictionReview, range=Optional[str])
