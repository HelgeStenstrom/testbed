# Read and create testbed_config.dat and similar files

import configparser

class parser:
    def __init__(self, fd):
        self.config = configparser.ConfigParser()
        self.config.optionxform = lambda x: x
        self.config.read_file(fd)
        return None

    def getSections(self):
        return self.config.sections()

    def putFile(self, handle):
        self.config.write(handle, space_around_delimiters=False)


