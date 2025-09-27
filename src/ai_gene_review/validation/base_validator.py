"""Base class for all validators."""
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, List, Optional


class BaseValidator(ABC):
    """Abstract base class for all validators."""

    @abstractmethod
    def validate(self, data: dict, yaml_file: Optional[Path] = None) -> List[Any]:
        """Validate the given data and return a list of validation results."""
        pass

    def get_cache_dir(self) -> Path:
        """Get the cache directory for validation data.

        Returns:
            Path to cache directory
        """
        cache_dir = Path.home() / ".cache" / "ai-gene-review"
        cache_dir.mkdir(parents=True, exist_ok=True)
        return cache_dir