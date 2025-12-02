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
        # Get the relative path of the file within the mounted volume
        app_root = target.get_root().get_path()
        file_path = target.get_path()
        relative_path = file_path.replace(app_root, "").lstrip("/")
        container_file_path = f"/var/www/html/{relative_path}"

        # Execute php-cs-fixer in Docker
        self._execute_in_docker(
            target=target,
            command=[
                "php-cs-fixer",
                "fix",
                "--rules=@PSR12",
                container_file_path
            ]
        )

        # Read the fixed content from the file (it was modified in place)
        return target.read_text()
