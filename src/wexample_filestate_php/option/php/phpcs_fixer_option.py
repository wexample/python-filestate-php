from __future__ import annotations

from typing import TYPE_CHECKING

from wexample_filestate.option.mixin.with_docker_option_mixin import WithDockerOptionMixin
from wexample_helpers.decorator.base_class import base_class
from .abstract_php_file_content_option import AbstractPhpFileContentOption

if TYPE_CHECKING:
    from wexample_filestate.const.types_state_items import TargetFileOrDirectoryType


@base_class
class PhpcsFixerOption(AbstractPhpFileContentOption):
    def get_description(self) -> str:
        return "Fix PHP code style using PHP-CS-Fixer."

    def _apply_content_change(self, target: TargetFileOrDirectoryType) -> str:
        """Fix PHP code style using PHP-CS-Fixer via Docker."""
        # Get current content
        super()._execute_in_docker(
            command="phpcs_fixer",
            target=target
        )

        # TODO: Implement Docker integration to run PHP-CS-Fixer
        # Steps to implement:
        # 1. Start Docker container with PHP-CS-Fixer installed
        # 2. Mount the file or pass content to the container
        # 3. Execute php-cs-fixer fix command
        # 4. Retrieve the fixed content
        # 5. Return the fixed content
        #
        # Example command that will be executed in Docker:
        # php-cs-fixer fix --rules=@PSR12 <file_path>
        #
        # For now, return unchanged content
        # return current_content

        # For now, return the same text saying nothing changes.
        return target.read_text()
