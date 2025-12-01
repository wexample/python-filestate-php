from __future__ import annotations

from wexample_filestate.option.abstract_file_content_option import (
    AbstractFileContentOption,
)
from wexample_helpers.decorator.base_class import base_class


@base_class
class AbstractPhpFileContentOption(AbstractFileContentOption):
    """Base class for PHP file content transformation options."""
    pass
