from ._abstract_pipeline_event import AbstractPipelineEvent


class ModuleEnabledEvent(AbstractPipelineEvent):
    """A module was enabled

    module - the module that was enabled.
    """

    def __init__(self, module):
        """Constructor

        module - the module that was enabled
        """
        super(self.__class__, self).__init__(is_pipeline_modification=True)
        self.module = module

    def event_type(self):
        return "Module enabled"