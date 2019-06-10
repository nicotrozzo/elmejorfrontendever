class BackEnd:
    def __init__(self, signals, filters, outputconfigs):
        self.signals = signals
        self.filters = filters
        self.outputConfigs = outputconfigs


class Signal:
    def __init__(self):
        self.properties = {}
        self.name = ""

