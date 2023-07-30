import xmltodict
import json
import argparse
import sys

def convert(filename):
    with open(filename) as xml_file:
        parsed_data = xmltodict.parse(xml_file.read())
        xml_file.close()
        json_conversion = json.dumps(parsed_data)
        with open('output.json', 'w') as json_file:
            json_file.write(json_conversion)
            json_file.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f','--filename',nargs=1,required=True,help="name of the xml file")
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
    arg = parser.parse_args()
    convert(arg.filename)