class BackEnd:
    def __init__(self, signals, filters, outputconfigs):
        self.signals = signals
        self.filters = filters
        self.outputConfigs = outputconfigs


class Signal:
    def __init__(self, name):
        self.properties = {"A" : 0 , "w" : 0}
        self.name = name


class Filter:
    def __init__(self, name):
        self.properties = {"wo": 0, "K": 0}
        self.name = name


class outputConfig:
    def __init__(self, name):
        self.properties = {"Bode": 0, "K": 0}
        self.name = name

