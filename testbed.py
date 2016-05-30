# Read and create testbed_config.dat and similar files

import configparser

class parser:
    def __init__(self, ctext):
        self.config = configparser.ConfigParser()
        self.config.read_string(ctext)
        return None

    def getSections(self):
        return self.config.sections()

