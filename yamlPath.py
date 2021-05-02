from yamlpath.common import Parsers
from yamlpath import YAMLPath
from yamlpath.wrappers import NodeCoords
from yamlpath.wrappers import ConsolePrinter
from yamlpath import Processor

class CustomLog():
    def __init__(self):
        self.debug = False
        self.verbose = False
        self.quiet = False

class CustomYamlParse():
    def __init__(self,query,yaml_str,pathsep='.'):
        self.query = query
        self.pathsep = pathsep
        self.yaml_str = yaml_str

    def parse(self):
        yaml_path = YAMLPath(self.query, pathsep=self.pathsep)
        yaml = Parsers.get_yaml_editor()
        log = ConsolePrinter(args=CustomLog())

        yaml_data = yaml.load(self.yaml_str)

        discovered_nodes = []

        processor = Processor(log, yaml_data)
        for node in processor.get_nodes(yaml_path, mustexist=True):
            log.debug("Got node from {}:".format(yaml_path), data=node,
                      prefix="yaml_get::main:  ")
            discovered_nodes.append(NodeCoords.unwrap_node_coords(node))
     
        return discovered_nodes

        
                
