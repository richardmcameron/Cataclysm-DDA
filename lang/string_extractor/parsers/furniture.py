from ..helper import get_singular_name
from ..write_text import write_text
from .examine_action import parse_examine_action


def parse_furniture(json, origin):
    name = get_singular_name(json.get("name", json["id"]))
    if "name" in json:
        write_text(json["name"], origin, comment="Furniture name")
    if "description" in json:
        write_text(json["description"], origin,
                   comment="Description of furniture \"{}\"".format(name))
    if "bash" in json:
        if "sound" in json["bash"]:
            write_text(json["bash"]["sound"], origin,
                       comment="Bashing sound of furniture \"{}\"".
                       format(name))
        if "sound_fail" in json["bash"]:
            write_text(json["bash"]["sound_fail"], origin,
                       comment="Bashing failed sound of furniture \"{}\""
                       .format(name))
    if "examine_action" in json:
        parse_examine_action(json["examine_action"], origin,
                             "furniture \"{}\"".format(name))
