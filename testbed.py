# Read and create testbed_config.dat and similar files

import configparser

class parser:
    def __init__(self, fd):
        self.config = configparser.ConfigParser()
        self.config.read_file(fd)
        return None

    def getSections(self):
        return self.config.sections()

    def putFile(self, f):
        with f as thefile:
            self.config.write(thefile)

