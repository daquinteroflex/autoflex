from autoflex.types.core import AutoflexBaseModel
from sphinx.ext.autodoc import ClassDocumenter

from sphinx.util import inspect, logging


logger = logging.getLogger(__name__)

class AutoflexDocumenter(ClassDocumenter):
    objtype = 'flex'
    # Optionally set a priority to override standard documenters if necessary
    priority = 10  # higher priority wins if multiple documenters match

    @classmethod
    def can_document_member(cls, member, membername, isattr, parent):
        # Determine if this documenter should handle the given member
        logger.error(f"cls: {cls}")
        return isinstance(member, AutoflexBaseModel)

    def add_directive_header(self, sig):
        # Customize the directive header if necessary
        self.add_line(f".. autoflex:: {self.name}", self.get_sourcename())
        super().add_directive_header(sig)


    def add_content(self, more_content, no_docstring=False):
        # Handle content based on the no_docstring flag if necessary
        if not no_docstring:
            # Add additional content if no_docstring is False
            super().add_content(more_content)

    def generate(self, *args, **kwargs):
        # Customize generation logic if necessary
        logger.error(f"self: {self}")
        logger.error(f"*args: {args}")
        logger.error(f"**kwargs: {kwargs}")
        # super().generate(*args, **kwargs)

