# -*- coding: utf-8 -*-
from .name_parser import NameParser


class Enum(object):
    """ Enum """

    def __init__(self, package, template_env, pb_enum):
        self._package = NameParser(package)
        self._template = template_env.get_template("enum.j2")
        self._name = NameParser(pb_enum.name)
        self._values = []

        for value in pb_enum.value:
            self._values.append(NameParser(value.name))

    def __repr__(self):
        return self._template.render(name=self._name,
                                     values=self._values,
                                     package=self._package)

    @staticmethod
    def collect_enums(package, enums, template_env):
        _enums = {}

        for enum in enums:
            _enums[enum.name] = Enum(package, template_env, enum)

        return _enums