import requests


class SessionManager:
    BASE_SITE_FOR_SESSION_URL = "https://www.ryanair.com/ie/en"

    def __init__(self, session: requests.Session):
        # Allow for a custom session object to handle user proxies, headers, etc.
        self.session = session
        self._update_session_cookie()

    def _update_session_cookie(self):
        # Visit main website to get session cookies
        self.session.get(self.BASE_SITE_FOR_SESSION_URL)
