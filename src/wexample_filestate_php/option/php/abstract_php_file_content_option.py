from __future__ import annotations

from typing import TYPE_CHECKING

from wexample_filestate.option.abstract_file_content_option import (
    AbstractFileContentOption,
)
from wexample_filestate.option.mixin.with_docker_option_mixin import WithDockerOptionMixin
from wexample_helpers.decorator.base_class import base_class

if TYPE_CHECKING:
    from wexample_filestate.const.types_state_items import TargetFileOrDirectoryType


@base_class
class AbstractPhpFileContentOption(WithDockerOptionMixin, AbstractFileContentOption):

    def _apply_content_change(self, target: TargetFileOrDirectoryType) -> str:
        """Apply content transformation to the target file.

        Args:
            target: The file to transform

        Returns:
            The transformed content as a string
        """
        self._ensure_docker_container()
        exit()
