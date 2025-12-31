import re

LINK_REGEX = re.compile(
    r'(?i)(?:'
    # ASCII domains with protocol or www
    r'(?:https?://|http://|www\.)[a-z0-9\-_]+(?:\.[a-z0-9\-_]+)+(?:\:\d+)?(?:/[^\s]*)?'
    r'|'
    # Cyrillic domains and local domains
    r'(?:[a-z0-9\-_а-яёїіє]+\.)+[a-z0-9а-яёїіє]{2,}(?:\:\d+)?(?:/[^\s]*)?'
    r'|'
    # @username mentions
    r'@[\w\d_]+'
    r'|'
    # IP addresses
    r'\b\d{1,3}(?:\.\d{1,3}){3}\b'
    r'|'
    # SMS or TEL links with optional +
    # r'(?:sms|tel):\+?\d+'
    # r'|'
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