import re

LINK_REGEX = re.compile(
    r'(?i)(?:'
    # ASCII domains with protocol or www
    r'(?:https?://|http://|www\.)[a-z0-9\-_]+(?:\.[a-z0-9\-_]+)+(?:\:\d+)?(?:/[^\s]*)?'
    r'|'
    # @username mentions
    r'@[\w\d_]+'
    r'|'
    # tg:// links
    r'tg://[^\s]+'
    r')',
    re.UNICODE
)


LOCALHOST_REGEX = re.compile(
    r'(?i)'  # Case-insensitive matching
    r'(?:'   # Start non-capturing group for all alternatives
        # Optional protocol (http or https)
        r'(?:https?://|http://)?'
        # Hostname "localhost"
        r'localhost'
        # Optional port e.g. :8000
        r'(?:\:\d+)?'
        # Optional path e.g. /path/to/page
        r'(?:/[^\s]*)?'
    r')\b',   # Word boundary to prevent partial matches
    re.UNICODE
)