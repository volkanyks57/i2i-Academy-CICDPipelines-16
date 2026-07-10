# Basit uygulama modulu: email format dogrulama fonksiyonu.

import re

EMAIL_PATTERN = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")


def is_valid_email(email: str) -> bool:
    # Verilen string gecerli bir email adresi mi kontrol eder.
    if not email or not isinstance(email, str):
        return False
    return bool(EMAIL_PATTERN.match(email))