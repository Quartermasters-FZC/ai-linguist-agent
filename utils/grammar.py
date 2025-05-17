import language_tool_python

def check_grammar(text):
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(text)
    corrected = language_tool_python.utils.correct(text, matches)
    return f"Suggestions: {len(matches)}\nCorrected Version:\n{corrected}"
