import collections

import cobble


def paragraph(style_id=None, style_name=None, numbering=None):
    return ParagraphMatcher(style_id, style_name, numbering)


ParagraphMatcher = collections.namedtuple("ParagraphMatcher", ["style_id", "style_name", "numbering"])
ParagraphMatcher.element_type = "paragraph"


def run(style_id=None, style_name=None):
    return RunMatcher(style_id, style_name)


RunMatcher = collections.namedtuple("RunMatcher", ["style_id", "style_name"])
RunMatcher.element_type = "run"


class bold(object):
    element_type = "bold"


class italic(object):
    element_type = "italic"


class underline(object):
    element_type = "underline"


class strikethrough(object):
    element_type = "strikethrough"


class comment_reference(object):
    element_type = "comment_reference"


def line_break(line_break_type=None):
    return LineBreakMatcher(line_break_type)


LineBreakMatcher = collections.namedtuple("BreakMatcher", ["line_break_type"])
LineBreakMatcher.element_type = "line_break"


def equal_to(value):
    return StringMatcher(_operator_equal_to, value)


def _operator_equal_to(first, second):
    return first.upper() == second.upper()
    
    
def starts_with(value):
    return StringMatcher(_operator_starts_with, value)


def _operator_starts_with(first, second):
    return second.upper().startswith(first.upper())


@cobble.data
class StringMatcher(object):
    operator = cobble.field()
    value = cobble.field()
    
    def matches(self, other):
        return self.operator(self.value, other)
