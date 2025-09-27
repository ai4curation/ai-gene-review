"""Validator for checking supporting_text against cached publications.

This module validates that supporting_text in annotations actually appears
in the referenced cached publications.
"""

import re
from dataclasses import dataclass, field
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml

from ai_gene_review.validation.base_validator import BaseValidator

DEFAULT_SIMILARITY_THRESHOLD = 0.85


@dataclass
class SupportingTextValidationResult:
    """Result of validating supporting_text against publication."""

    is_valid: bool = True
    annotation_path: str = ""
    reference_id: str = ""
    supporting_text: str = ""
    error_message: Optional[str] = None
    found_in_publication: bool = False
    similarity_score: float = 0.0
    suggested_fix: Optional[str] = None
    best_match: Optional[str] = None


@dataclass
class SupportingTextValidationReport:
    """Overall validation report for supporting_text checks."""

    is_valid: bool = True
    results: List[SupportingTextValidationResult] = field(default_factory=list)
    total_annotations: int = 0
    annotations_with_supporting_text: int = 0
    valid_supporting_texts: int = 0
    invalid_supporting_texts: int = 0

    @property
    def validation_rate(self) -> float:
        """Percentage of annotations that have supporting_text."""
        if self.total_annotations == 0:
            return 0.0
        return (self.annotations_with_supporting_text / self.total_annotations) * 100

    @property
    def accuracy_rate(self) -> float:
        """Percentage of supporting_texts that are valid."""
        if self.annotations_with_supporting_text == 0:
            return 0.0
        return (
            self.valid_supporting_texts / self.annotations_with_supporting_text
        ) * 100


class SupportingTextValidator(BaseValidator):
    """Validates supporting_text fields against cached publications."""

    def __init__(
        self,
        publications_dir: Path = Path("publications"),
        gene_dir: Path = Path("genes"),
        reactome_dir: Path = Path("reactome"),
    ):
        """Initialize validator with publications directory.

        Args:
            publications_dir: Path to directory containing cached publications
            gene_dir: Path to directory containing gene folders with UniProt files
            reactome_dir: Path to directory containing cached Reactome pathways
        """
        self.publications_dir = publications_dir
        self.gene_dir = gene_dir
        self.reactome_dir = reactome_dir
        self.cached_publications: Dict[str, str] = {}
        self.cached_uniprot_files: Dict[str, str] = {}
        self.cached_reactome_files: Dict[str, str] = {}
        self.similarity_threshold = DEFAULT_SIMILARITY_THRESHOLD

    def load_publication(self, pmid: str) -> Optional[str]:
        """Load a cached publication by PMID.

        Attempts to load a publication from the local cache directory.
        Publications should be stored as markdown files with the naming
        convention PMID_<pmid>.md in the publications directory.
        Uses an in-memory cache to avoid re-reading the same file.

        Args:
            pmid: PubMed ID without prefix (e.g., "12345678" not "PMID:12345678")

        Returns:
            Full text of publication in markdown format, or None if not found

        Examples:
            >>> from pathlib import Path
            >>> import tempfile
            >>> with tempfile.TemporaryDirectory() as tmpdir:
            ...     # Create a test publication
            ...     pub_dir = Path(tmpdir)
            ...     pub_file = pub_dir / "PMID_12345678.md"
            ...     _ = pub_file.write_text("# Test Publication\\n\\nTest content")
            ...     # Load it
            ...     validator = SupportingTextValidator(pub_dir)
            ...     content = validator.load_publication("12345678")
            ...     print("Loaded" if content else "Not found")
            Loaded
        """
        # Check cache first
        if pmid in self.cached_publications:
            return self.cached_publications[pmid]

        # Try to load from file
        pub_file = self.publications_dir / f"PMID_{pmid}.md"
        if pub_file.exists():
            try:
                with open(pub_file, "r", encoding="utf-8") as f:
                    content = f.read()
                    self.cached_publications[pmid] = content
                    return content
            except Exception as e:
                print(f"Error loading publication {pmid}: {e}")

        return None

    def extract_pmid_from_reference(self, reference_id: str) -> Optional[str]:
        """Extract PMID from various reference formats.

        Args:
            reference_id: Reference ID like "PMID:12345678" or "GO_REF:0000033"

        Returns:
            PMID string or None if not a PMID reference

        Examples:
            >>> validator = SupportingTextValidator()
            >>> validator.extract_pmid_from_reference("PMID:12345678")
            '12345678'
            >>> validator.extract_pmid_from_reference("GO_REF:0000033")
            >>> validator.extract_pmid_from_reference("pmid:99999")
            '99999'
        """
        if reference_id.upper().startswith("PMID:"):
            return reference_id[5:]  # Skip "PMID:" or "pmid:"
        return None

    def extract_uniprot_from_reference(self, reference_id: str) -> Optional[str]:
        """Extract UniProt ID from reference.

        Args:
            reference_id: Reference ID like "uniprot:P12345" or "UniProtKB:Q99999"

        Returns:
            UniProt ID string or None if not a UniProt reference

        Examples:
            >>> validator = SupportingTextValidator()
            >>> validator.extract_uniprot_from_reference("uniprot:P12345")
            'P12345'
            >>> validator.extract_uniprot_from_reference("UniProtKB:Q99999")
            'Q99999'
            >>> validator.extract_uniprot_from_reference("UNIPROT:A0B297")
            'A0B297'
            >>> validator.extract_uniprot_from_reference("PMID:12345")
        """
        ref_upper = reference_id.upper()
        if ref_upper.startswith("UNIPROT:"):
            return reference_id[8:]  # Skip "uniprot:" or "UNIPROT:"
        elif ref_upper.startswith("UNIPROTKB:"):
            return reference_id[10:]  # Skip "UniProtKB:" or "UNIPROTKB:"
        return None

    def extract_reactome_from_reference(self, reference_id: str) -> Optional[str]:
        """Extract Reactome ID from reference.

        Args:
            reference_id: Reference ID like "Reactome:R-HSA-9927247"

        Returns:
            Reactome ID string or None if not a Reactome reference

        Examples:
            >>> validator = SupportingTextValidator()
            >>> validator.extract_reactome_from_reference("Reactome:R-HSA-9927247")
            'R-HSA-9927247'
            >>> validator.extract_reactome_from_reference("reactome:R-HSA-1234567")
            'R-HSA-1234567'
            >>> validator.extract_reactome_from_reference("REACTOME:R-HSA-9927247")
            'R-HSA-9927247'
            >>> validator.extract_reactome_from_reference("PMID:12345")
        """
        ref_upper = reference_id.upper()
        if ref_upper.startswith("REACTOME:"):
            return reference_id[9:]  # Skip "Reactome:" or "REACTOME:"
        return None

    def load_uniprot_file(self, uniprot_id: str, yaml_data: Dict[str, Any] = None) -> Optional[str]:
        """Load a UniProt file for a given ID.

        Attempts to find and load the UniProt file from the gene directory structure.
        The file should be named <GENE>-uniprot.txt in the appropriate species/gene folder.

        Args:
            uniprot_id: UniProt ID (e.g., "P12345", "A0B297")
            yaml_data: Optional YAML data containing gene_symbol and taxon info to help locate file

        Returns:
            Full text of UniProt file, or None if not found

        Examples:
            >>> from pathlib import Path
            >>> import tempfile
            >>> with tempfile.TemporaryDirectory() as tmpdir:
            ...     # Create a test UniProt file
            ...     gene_dir = Path(tmpdir) / "BURCH" / "A0B297"
            ...     gene_dir.mkdir(parents=True)
            ...     uniprot_file = gene_dir / "A0B297-uniprot.txt"
            ...     _ = uniprot_file.write_text("ID   RGMG2_BURCH\\nAC   A0B297;\\nCC   Test content")
            ...     # Load it
            ...     validator = SupportingTextValidator(gene_dir=Path(tmpdir))
            ...     content = validator.load_uniprot_file("A0B297")
            ...     print("Loaded" if content else "Not found")
            Loaded
        """
        # Check cache first
        if uniprot_id in self.cached_uniprot_files:
            return self.cached_uniprot_files[uniprot_id]

        # Try to find the UniProt file
        # First check if we can use the yaml_data to get the gene_symbol
        gene_symbol = None
        if yaml_data:
            gene_symbol = yaml_data.get("gene_symbol")
            # Also check if the id field matches the uniprot_id
            if not gene_symbol and yaml_data.get("id") == uniprot_id:
                gene_symbol = uniprot_id

        # Search for the UniProt file in the gene directory structure
        # Pattern: genes/<species>/<gene>/<gene>-uniprot.txt
        if gene_symbol:
            # Try to find in any species folder
            for species_dir in self.gene_dir.iterdir():
                if species_dir.is_dir():
                    gene_path = species_dir / gene_symbol
                    if gene_path.exists():
                        uniprot_file = gene_path / f"{gene_symbol}-uniprot.txt"
                        if uniprot_file.exists():
                            try:
                                with open(uniprot_file, "r", encoding="utf-8") as f:
                                    content = f.read()
                                    self.cached_uniprot_files[uniprot_id] = content
                                    return content
                            except Exception as e:
                                print(f"Error loading UniProt file for {uniprot_id}: {e}")

        # Also try searching by UniProt ID directly in case it's used as the gene folder name
        for species_dir in self.gene_dir.iterdir():
            if species_dir.is_dir():
                gene_path = species_dir / uniprot_id
                if gene_path.exists():
                    uniprot_file = gene_path / f"{uniprot_id}-uniprot.txt"
                    if uniprot_file.exists():
                        try:
                            with open(uniprot_file, "r", encoding="utf-8") as f:
                                content = f.read()
                                self.cached_uniprot_files[uniprot_id] = content
                                return content
                        except Exception as e:
                            print(f"Error loading UniProt file for {uniprot_id}: {e}")

        return None

    def load_reactome_file(self, reactome_id: str) -> Optional[str]:
        """Load a cached Reactome pathway file by ID.

        Attempts to load a Reactome pathway from the local cache directory.
        Reactome pathways should be stored as markdown files with the naming
        convention R-HSA-<id>.md in the reactome directory.
        Uses an in-memory cache to avoid re-reading the same file.

        Args:
            reactome_id: Reactome ID without prefix (e.g., "R-HSA-9927247")

        Returns:
            Full text of Reactome pathway in markdown format, or None if not found

        Examples:
            >>> from pathlib import Path
            >>> import tempfile
            >>> with tempfile.TemporaryDirectory() as tmpdir:
            ...     # Create a test Reactome file
            ...     reactome_dir = Path(tmpdir)
            ...     reactome_file = reactome_dir / "R-HSA-9927247.md"
            ...     _ = reactome_file.write_text("# ISGylation\\n\\nTest pathway content")
            ...     # Load it
            ...     validator = SupportingTextValidator(reactome_dir=reactome_dir)
            ...     content = validator.load_reactome_file("R-HSA-9927247")
            ...     print("Loaded" if content else "Not found")
            Loaded
        """
        # Check cache first
        if reactome_id in self.cached_reactome_files:
            return self.cached_reactome_files[reactome_id]

        # Try to load from file
        reactome_file = self.reactome_dir / f"{reactome_id}.md"
        if reactome_file.exists():
            try:
                with open(reactome_file, "r", encoding="utf-8") as f:
                    content = f.read()
                    self.cached_reactome_files[reactome_id] = content
                    return content
            except Exception as e:
                print(f"Error loading Reactome pathway {reactome_id}: {e}")

        return None

    def preprocess_uniprot_content(self, content: str) -> str:
        """Preprocess UniProt file content to remove line prefixes and join continuation lines.
        
        UniProt files have specific line prefixes (like CC, FT, DE) that should be removed
        for text matching. Also handles continuation lines that are split across multiple lines.
        
        Args:
            content: Raw UniProt file content
            
        Returns:
            Preprocessed content with line prefixes removed
            
        Examples:
            >>> validator = SupportingTextValidator()
            >>> uniprot = '''CC   -!- FUNCTION: Part of an ABC transporter.
            ... CC       More text here.
            ... FT   DOMAIN          14..251
            ... FT                   /note="ABC transporter 1"'''
            >>> processed = validator.preprocess_uniprot_content(uniprot)
            >>> "FUNCTION: Part of an ABC transporter. More text here" in processed
            True
            >>> 'DOMAIN          14..251 /note="ABC transporter 1"' in processed
            True
        """
        lines = content.split('\n')
        processed_lines = []
        current_section = None
        current_text = []
        
        for line in lines:
            if not line.strip():
                continue
                
            # Check if line starts with a two-letter code
            if len(line) >= 2 and line[:2].isupper() and (len(line) < 3 or line[2] == ' '):
                prefix = line[:2]
                rest = line[5:] if len(line) > 5 else ""  # Skip prefix and spaces
                
                # If we're switching sections, save the previous one
                if current_section and current_section != prefix:
                    if current_text:
                        processed_lines.append(' '.join(current_text))
                    current_text = []
                
                current_section = prefix
                if rest.strip():
                    # Handle FT lines specially to preserve structure
                    if prefix == 'FT':
                        # Remove extra spaces but keep the structure
                        rest = rest.strip()
                        if rest and not rest.startswith('/'):
                            # This is a feature location line
                            current_text.append(rest)
                        elif rest.startswith('/'):
                            # This is a qualifier line, append to previous
                            if current_text:
                                current_text[-1] = current_text[-1] + ' ' + rest
                            else:
                                current_text.append(rest)
                    else:
                        current_text.append(rest.strip())
            elif current_section:
                # Continuation line without prefix
                continuation = line.strip()
                if continuation:
                    if current_section == 'FT' and continuation.startswith('/'):
                        # FT qualifier continuation
                        if current_text:
                            current_text[-1] = current_text[-1] + ' ' + continuation
                        else:
                            current_text.append(continuation)
                    else:
                        current_text.append(continuation)
        
        # Don't forget the last section
        if current_text:
            processed_lines.append(' '.join(current_text))
        
        # Join all processed lines with newlines to maintain some structure
        return '\n'.join(processed_lines)

    def find_text_in_publication(
        self, text: str, publication_content: str
    ) -> tuple[bool, float, Optional[str]]:
        """Find text in publication, allowing for minor variations.

        This method performs fuzzy matching to find supporting text in publications.
        It first tries exact matching, then uses similarity scoring with a threshold
        (default 0.85) to account for minor variations in wording.

        Text in square brackets [like this] is treated as editorial notes and ignored
        during matching. Multiple text segments can be separated by "..." to indicate
        non-contiguous quotes.

        Args:
            text: Text to search for (the supporting_text from annotation)
            publication_content: Full publication content (markdown format)

        Returns:
            Tuple of (found, similarity_score, best_match) where:
            - found: True if text was found with similarity >= threshold
            - similarity_score: Float between 0.0 and 1.0 indicating match quality
            - best_match: The best matching sentence from the publication

        Examples:
            >>> validator = SupportingTextValidator()
            >>> pub = "JAK1 is a tyrosine kinase. It binds to cytokine receptors."
            >>> found, score, match = validator.find_text_in_publication(
            ...     "It binds to cytokine receptors", pub
            ... )
            >>> print(f"Found: {found}, Score: {score:.2f}")
            Found: True, Score: 1.00

            >>> # Test with substring
            >>> found, score, match= validator.find_text_in_publication(
            ...     "JAK1 is a tyrosine", pub
            ... )
            >>> print(f"Found: {found}, Score: {score:.2f}")
            Found: True, Score: 1.00

            >>> # Test with substring + modification
            >>> found, score, match= validator.find_text_in_publication(
            ...     "JAK1 is a tyrosine fooase", pub
            ... )
            >>> print(f"Found: {found}, Score: {score:.2f}")
            Found: True, Score: 0.88

            >>> # Test with substring + insertion
            >>> found, score, match= validator.find_text_in_publication(
            ...     "JAK1 is a very special tyrosine kinase", pub
            ... )
            >>> print(f"Found: {found}, Score: {score:.2f}")
            Found: False, Score: 0.79

            >>> # Test with partial match - doesn't find due to threshold
            >>> found2, score2, match2 = validator.find_text_in_publication(
            ...     "completely different text", pub
            ... )
            >>> print(f"Found: {found2}")
            Found: False

            >>> # Test with editorial notes in square brackets - brackets are ignored
            >>> found3, score3, match3 = validator.find_text_in_publication(
            ...     "JAK1 is a [non-receptor] tyrosine kinase", pub
            ... )
            >>> print(f"Found: {found3}, Score: {score3:.2f}")
            Found: True, Score: 1.00

            >>> # Test with multiple bracketed sections
            >>> pub2 = "CFAP300 shows interaction with DNAAF2 assembly factor"
            >>> found4, score4, match4 = validator.find_text_in_publication(
            ...     "[The protein] CFAP300 shows interaction [directly] with DNAAF2 [cytoplasmic] assembly factor",
            ...     pub2
            ... )
            >>> print(f"Found: {found4}, Score: {score4:.2f}")
            Found: True, Score: 1.00

            >>> # Test with multi-part quotes using ...
            >>> pub3 = "The protein functions in the cytoplasm. It helps with assembly of motors."
            >>> found5, score5, match5 = validator.find_text_in_publication(
            ...     "protein functions in the cytoplasm ... assembly of motors",
            ...     pub3
            ... )
            >>> print(f"Found: {found5}, Score: {score5:.2f}")
            Found: True, Score: 1.00

            >>> # Test complex case with brackets and ellipsis
            >>> found6, score6, match6 = validator.find_text_in_publication(
            ...     "[The] protein functions [mainly] in the cytoplasm ... [It helps with] assembly of motors",
            ...     pub3
            ... )
            >>> print(f"Found: {found6}, Score: {score6:.2f}")
            Found: True, Score: 1.00
        """
        # Remove editorial notes in square brackets before processing
        # Use a more robust approach for nested brackets
        while "[" in text:
            # Find innermost brackets first and remove them
            text = re.sub(r"\[[^\[\]]*\]", "", text)
        text_without_brackets = text.strip()

        # Handle multi-part quotes separated by "..."
        if "..." in text_without_brackets:
            # Split on ... and validate each part separately
            parts = [p.strip() for p in text_without_brackets.split("...") if p.strip()]
            all_found = True
            min_score = 1.0
            matches = []

            for part in parts:
                found, score, match = self._find_single_text_in_publication(
                    part, publication_content
                )
                if not found:
                    all_found = False
                min_score = min(min_score, score)
                if match:
                    matches.append(match)

            # Return combined result
            return (all_found, min_score, " ... ".join(matches) if matches else None)
        else:
            # Single text segment
            return self._find_single_text_in_publication(
                text_without_brackets, publication_content
            )

    def _find_single_text_in_publication(
        self, text: str, publication_content: str
    ) -> tuple[bool, float, Optional[str]]:
        """Find a single text segment in publication (internal helper method)."""
        # Clean and normalize text
        text_clean = self.normalize_text(text)
        pub_clean = self.normalize_text(publication_content)

        # First try exact match
        if text_clean in pub_clean:
            return (True, 1.0, text)

        # Try fuzzy matching with sliding window
        text_words = text_clean.split()
        text_length = len(text_words)

        if text_length < 5:
            # For very short texts, require exact match
            return (False, 0.0, None)

        # NEW: Try sliding window on the full normalized text BEFORE sentence splitting
        # This handles cases where text spans multiple lines/sentences
        pub_words = pub_clean.split()
        best_score = 0.0
        best_match = None

        # Slide a window of the same size as the text
        for i in range(len(pub_words) - text_length + 1):
            window = ' '.join(pub_words[i:i + text_length])
            similarity = SequenceMatcher(None, text_clean, window).ratio()

            if similarity > best_score:
                best_score = similarity
                best_match = window

            # If we find an excellent match, we can stop early
            if similarity >= 0.95:
                return (True, similarity, best_match)

        # If we found a good match with sliding window, return it
        if best_score >= self.similarity_threshold:
            return (True, best_score, best_match)

        # Split publication into sentences for better matching
        sentences = self.split_into_sentences(publication_content)

        for sentence in sentences:
            sentence_clean = self.normalize_text(sentence)
            similarity = SequenceMatcher(None, text_clean, sentence_clean).ratio()

            if similarity > best_score:
                best_score = similarity
                best_match = sentence

            # If we find a very good match, stop searching
            if similarity >= self.similarity_threshold:
                return (True, similarity, sentence)

        # Also try to find partial matches (at least 70% of the words)
        text_words_set = set(text_words)
        for sentence in sentences:
            sentence_words = set(self.normalize_text(sentence).split())
            common_words = text_words_set.intersection(sentence_words)

            if len(common_words) >= len(text_words_set) * 0.7:
                # Found most words, calculate similarity
                sentence_clean = self.normalize_text(sentence)
                similarity = SequenceMatcher(None, text_clean, sentence_clean).ratio()
                if similarity > best_score:
                    best_score = similarity
                    best_match = sentence

        return (best_score >= self.similarity_threshold, best_score, best_match)

    def normalize_text(self, text: str) -> str:
        """Normalize text for comparison.

        Args:
            text: Text to normalize

        Returns:
            Normalized text

        Examples:
            >>> validator = SupportingTextValidator()
            >>> validator.normalize_text("  This is   a TEST   string!  ")
            'this is a test string!'
            >>> validator.normalize_text("JAK1-mediated (STAT) activation")
            'jak1-mediated stat activation'
            >>> validator.normalize_text("65% (P < 0.001).")
            '65% p 0 001'
        """
        # First, normalize all whitespace (including newlines) to single spaces
        text = re.sub(r"\s+", " ", text)
        # Remove most punctuation but keep hyphens and exclamation marks
        # Remove parentheses, periods, commas, semicolons, colons, quotes, etc.
        text = re.sub(r"[().,;:\"'<>=]+", " ", text)
        # Normalize whitespace again after removing some punctuation
        text = re.sub(r"\s+", " ", text)
        # Convert to lowercase and strip
        text = text.lower().strip()
        return text

    def split_into_sentences(self, text: str) -> List[str]:
        """Split text into sentences.

        Args:
            text: Text to split

        Returns:
            List of sentences (only those > 20 chars)

        Examples:
            >>> validator = SupportingTextValidator()
            >>> text = "This is a long first sentence. This is a long second sentence!"
            >>> sentences = validator.split_into_sentences(text)
            >>> len(sentences)
            2
            >>> text = "Short.\\nThis is a longer sentence that exceeds twenty characters."
            >>> sentences = validator.split_into_sentences(text)
            >>> len(sentences)  # Only the long sentence
            1
        """
        # First normalize whitespace to join lines that are part of the same sentence
        # Replace single newlines with spaces, preserve double newlines as paragraph breaks
        text = re.sub(r"(?<!\n)\n(?!\n)", " ", text)
        # Normalize multiple spaces to single spaces
        text = re.sub(r"\s+", " ", text)

        # Simple sentence splitting on punctuation followed by whitespace
        sentences = re.split(r"[.!?]\s+", text)

        # Filter out empty sentences and clean up
        return [s.strip() for s in sentences if s.strip() and len(s.strip()) > 20]

    def validate_supporting_text_against_reference(
        self,
        supporting_text: str,
        reference_id: str,
        annotation_path: str,
        yaml_data: Dict[str, Any] = None,
    ) -> Optional[SupportingTextValidationResult]:
        """Core validation method for checking supporting text against a reference.

        This method contains the shared logic for validating supporting_text
        against a referenced publication, UniProt entry, or Reactome pathway. It handles 
        PMID/UniProt/Reactome extraction, content loading, text matching, and error message generation.

        Only validates PMID, UniProt and Reactome references. Returns None for other references
        (like GO_REF or file: references) since they don't have text to validate against.

        Args:
            supporting_text: The text to validate
            reference_id: Reference ID (e.g., "PMID:12345678", "uniprot:P12345", "GO_REF:0000120")
            annotation_path: Path for error reporting (e.g., "references[0].findings[1].supporting_text")
            yaml_data: Optional YAML data to help locate UniProt files

        Returns:
            SupportingTextValidationResult with validation details, or None if not a validatable reference
        """
        # Try PMID first
        pmid = self.extract_pmid_from_reference(reference_id)
        if pmid:
            # Create result object for PMID validation
            result = SupportingTextValidationResult(
                annotation_path=annotation_path,
                supporting_text=supporting_text,
                reference_id=reference_id,
            )

            # Load publication
            publication_content = self.load_publication(pmid)
            if not publication_content:
                result.error_message = f"Publication {reference_id} not found in cache"
                result.is_valid = False
                return result

            # Check if supporting_text appears in publication
            is_found, similarity, best_match = self.find_text_in_publication(
                supporting_text, publication_content
            )

            result.found_in_publication = is_found
            result.similarity_score = similarity
            result.is_valid = is_found
            result.best_match = best_match

            # Generate error message if text not found
            if not is_found:
                # Truncate supporting text for display
                text_preview = (
                    (supporting_text[:80] + "...")
                    if len(supporting_text) > 80
                    else supporting_text
                )

                if similarity > 0.5:
                    result.error_message = (
                        f'Supporting text "{text_preview}" not found in {reference_id} '
                        f"(best similarity: {similarity:.1%})"
                    )
                else:
                    result.error_message = (
                        f'Supporting text "{text_preview}" not found in {reference_id}'
                    )

            return result

        # Try UniProt
        uniprot_id = self.extract_uniprot_from_reference(reference_id)
        if uniprot_id:
            # Create result object for UniProt validation
            result = SupportingTextValidationResult(
                annotation_path=annotation_path,
                supporting_text=supporting_text,
                reference_id=reference_id,
            )

            # Load UniProt file
            uniprot_content = self.load_uniprot_file(uniprot_id, yaml_data)
            if not uniprot_content:
                result.error_message = f"UniProt file for {reference_id} not found"
                result.is_valid = False
                return result

            # Preprocess UniProt content to remove line prefixes
            processed_content = self.preprocess_uniprot_content(uniprot_content)
            
            # Check if supporting_text appears in UniProt file
            is_found, similarity, best_match = self.find_text_in_publication(
                supporting_text, processed_content
            )

            result.found_in_publication = is_found
            result.similarity_score = similarity
            result.is_valid = is_found
            result.best_match = best_match

            # Generate error message if text not found
            if not is_found:
                # Truncate supporting text for display
                text_preview = (
                    (supporting_text[:80] + "...")
                    if len(supporting_text) > 80
                    else supporting_text
                )

                if similarity > 0.5:
                    result.error_message = (
                        f'Supporting text "{text_preview}" not found in {reference_id} '
                        f"(best similarity: {similarity:.1%})"
                    )
                else:
                    result.error_message = (
                        f'Supporting text "{text_preview}" not found in {reference_id}'
                    )

            return result

        # Try Reactome
        reactome_id = self.extract_reactome_from_reference(reference_id)
        if reactome_id:
            # Create result object for Reactome validation
            result = SupportingTextValidationResult(
                annotation_path=annotation_path,
                supporting_text=supporting_text,
                reference_id=reference_id,
            )

            # Load Reactome file
            reactome_content = self.load_reactome_file(reactome_id)
            if not reactome_content:
                result.error_message = f"Reactome pathway file for {reference_id} not found"
                result.is_valid = False
                return result

            # Check if supporting_text appears in Reactome file
            is_found, similarity, best_match = self.find_text_in_publication(
                supporting_text, reactome_content
            )

            result.found_in_publication = is_found
            result.similarity_score = similarity
            result.is_valid = is_found
            result.best_match = best_match

            # Generate error message if text not found
            if not is_found:
                # Truncate supporting text for display
                text_preview = (
                    (supporting_text[:80] + "...")
                    if len(supporting_text) > 80
                    else supporting_text
                )

                if similarity > 0.5:
                    result.error_message = (
                        f'Supporting text "{text_preview}" not found in {reference_id} '
                        f"(best similarity: {similarity:.1%})"
                    )
                else:
                    result.error_message = (
                        f'Supporting text "{text_preview}" not found in {reference_id}'
                    )

            return result

        # Not a PMID, UniProt or Reactome reference - skip validation
        # GO_REF references are computational/method references without text
        # file: references should be validated separately if needed
        return None

    def validate_annotation_supported_by(
        self, annotation: Dict[str, Any], annotation_index: int, data: Dict[str, Any]
    ) -> List[SupportingTextValidationResult]:
        """Validate supported_by entries for a single annotation.

        This method checks if the supporting_text in each supported_by entry
        can be found in the referenced publication.

        Args:
            annotation: Single annotation dictionary
            annotation_index: Index in existing_annotations list
            data: Full gene review data

        Returns:
            List of validation results for each supported_by entry
        """
        results: List[SupportingTextValidationResult] = []

        if "review" not in annotation:
            return results

        review = annotation["review"]
        if "supported_by" not in review:
            return results

        supported_by_list = review.get("supported_by", [])
        if not isinstance(supported_by_list, list):
            return results

        for sb_idx, supported_by in enumerate(supported_by_list):
            if not isinstance(supported_by, dict):
                continue

            reference_id = supported_by.get("reference_id", "")
            supporting_text = supported_by.get("supporting_text", "")

            if not supporting_text or not reference_id:
                continue

            # Use the core validation method
            annotation_path = f"existing_annotations[{annotation_index}].review.supported_by[{sb_idx}].supporting_text"
            result = self.validate_supporting_text_against_reference(
                supporting_text, reference_id, annotation_path, data
            )
            # Only add result if it's a validatable reference (PMID or UniProt)
            if result:
                results.append(result)

        return results

    def validate_finding_supporting_text(
        self,
        finding: Dict[str, Any],
        reference_id: str,
        finding_index: int,
        ref_index: int,
        data: Dict[str, Any] = None,
    ) -> Optional[SupportingTextValidationResult]:
        """Validate supporting_text for a single finding in references section.

        Args:
            finding: Single finding dictionary with statement and supporting_text
            reference_id: The reference ID (e.g., "PMID:12345678")
            finding_index: Index in findings list
            ref_index: Index in references list

        Returns:
            Validation result or None if no supporting_text
        """
        if "supporting_text" not in finding:
            return None

        supporting_text = finding["supporting_text"]
        if not supporting_text:
            return None

        # Use the core validation method
        annotation_path = (
            f"references[{ref_index}].findings[{finding_index}].supporting_text"
        )
        return self.validate_supporting_text_against_reference(
            supporting_text, reference_id, annotation_path, data
        )

    def validate(
        self, data: Dict[str, Any], yaml_file: Optional[Path] = None
    ) -> List[SupportingTextValidationReport]:
        """Validate all supporting_text fields in gene review data.

        Validates supporting_text in both:
        1. existing_annotations[].review.supporting_text
        2. references[].findings[].supporting_text

        Args:
            data: Parsed YAML data from gene review file

        Returns:
            Validation report with detailed results including:
            - Total annotations/findings count
            - Count with supporting_text
            - Count of valid vs invalid supporting texts
            - Individual validation results
            - Overall validation rate and accuracy rate

        Examples:
            >>> from pathlib import Path
            >>> validator = SupportingTextValidator(Path("publications"))
            >>> data = {
            ...     "existing_annotations": [
            ...         {
            ...             "term": {"id": "GO:0032147", "label": "activation of protein kinase activity"},
            ...             "evidence_type": "IDA",
            ...             "original_reference_id": "PMID:10688190",
            ...             "review": {
            ...                 "action": "ACCEPT",
            ...                 "reason": "Demonstrated by yeast two-hybrid assay",
            ...                 "supported_by": [{
            ...                     "reference_id": "PMID:10688190",
            ...                     "supporting_text": "MTC7 activates downstream kinases in telomere maintenance"
            ...                 }]
            ...             }
            ...         }
            ...     ]
            ... }
            >>> report = validator.validate(data)
            >>> print(f"Total annotations: {report.total_annotations}")
            Total annotations: 1
            >>> print(f"With supporting text: {report.annotations_with_supporting_text}")
            With supporting text: 1

            >>> # Test warning for PMID references without supporting_text
            >>> data_with_pmid = {
            ...     "references": [
            ...         {
            ...             "id": "PMID:12345678",
            ...             "title": "Test publication",
            ...             "findings": [
            ...                 {"statement": "Important finding"}  # Missing supporting_text
            ...             ]
            ...         }
            ...     ]
            ... }
            >>> report2 = validator.validate(data_with_pmid)
            >>> print(f"Valid: {report2.is_valid}")
            Valid: False
            >>> print(report2.results[0].error_message)
            Reference PMID:12345678 has finding without supporting_text - findings from publications/UniProt/Reactome must be supported with quotes
        """
        report = SupportingTextValidationReport()

        # Check references.findings first
        if "references" in data:
            references = data.get("references", [])
            for ref_idx, reference in enumerate(references):
                if not isinstance(reference, dict):
                    continue

                ref_id = reference.get("id", "")
                findings = reference.get("findings", [])

                for finding_idx, finding in enumerate(findings):
                    if not isinstance(finding, dict):
                        continue

                    # Count as an annotation for reporting purposes
                    report.total_annotations += 1

                    # NEW: Add warning if PMID, UniProt or Reactome reference has findings without supporting_text
                    if (
                        ref_id.startswith("PMID:")
                        or ref_id.lower().startswith("uniprot:")
                        or ref_id.upper().startswith("REACTOME:")
                    ) and findings:
                        supporting_text = finding.get("supporting_text", "").strip()
                        if not supporting_text:
                            # Create a warning result for PMID findings without supporting_text
                            warning_result = SupportingTextValidationResult(
                                is_valid=False,  # Mark as invalid to trigger warning
                                annotation_path=f"references[{ref_idx}].findings[{finding_idx}]",
                                reference_id=ref_id,
                                supporting_text="",
                                error_message=f"Reference {ref_id} has finding without supporting_text - findings from publications/UniProt/Reactome must be supported with quotes",
                                found_in_publication=False,
                                similarity_score=0.0,
                            )
                            report.results.append(warning_result)
                            report.invalid_supporting_texts += 1
                            report.is_valid = False
                            continue

                    result = self.validate_finding_supporting_text(
                        finding, ref_id, finding_idx, ref_idx, data
                    )

                    if result:
                        report.annotations_with_supporting_text += 1
                        report.results.append(result)

                        if result.is_valid:
                            report.valid_supporting_texts += 1
                        else:
                            report.invalid_supporting_texts += 1
                            report.is_valid = False

        # Check existing_annotations
        annotations = data.get("existing_annotations", [])
        report.total_annotations += len(annotations)

        for i, annotation in enumerate(annotations):
            if not isinstance(annotation, dict):
                continue

            # Check the new supported_by field
            supported_by_results = self.validate_annotation_supported_by(
                annotation, i, data
            )
            for sb_result in supported_by_results:
                report.annotations_with_supporting_text += 1
                report.results.append(sb_result)

                if sb_result.is_valid:
                    report.valid_supporting_texts += 1
                else:
                    report.invalid_supporting_texts += 1
                    report.is_valid = False

        return [report]
