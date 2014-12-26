from tinycss.css21 import CSS21Parser, ParseError

class FontFaceRule(object):
    """
    A parsed @font rule

    .. attribute:: at_keyword

        Always ``'@font-face'``


    """
    at_keyword = '@font-face'

    def __init__(self, body, line, column):
        self.body = body
        self.line = line
        self.column = column

    def __repr__(self):
        return ('<{0.__class__.__name__} {0.line}:{0.column}'.format(self))


class CSSFontfaceParser(CSS21Parser):

    def parse_at_rule(self, rule, previous_rules, errors, context):
        if rule.at_keyword == '@font-face':
            if context != 'stylesheet':
                raise ParseError(
                    rule, 
                    '@font-face rule not allowed in ' + context)
            if rule.head:
                raise ParseError(
                    rule, 'no head declaratons allowed for  @font-face')
            if rule.body is None:
                raise ParseError(
                    rule,
                    'invalid {0} rule: missing block'.format(rule.at_keyword))
            return FontFaceRule(rule.body, rule.line, rule.column)
        else:
            return super(MyCSSParser, self).parse_at_rule(
                rule, previous_rules, errors, context)



