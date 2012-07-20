# -*- coding: utf-8 -*-
from django.conf import settings
from django.utils.encoding import force_unicode
from django.contrib.sessions.backends.base import SessionBase, CreateError
from sharedance import Sharedance

SHAREDANCE_HOST    = getattr(settings, 'SHAREDANCE_HOST', 'localhost')
SHAREDANCE_PORT    = getattr(settings, 'SHAREDANCE_PORT', 1042)
SHAREDANCE_TIMEOUT = getattr(settings, 'SHAREDANCE_TIMEOUT', 5)

class SessionStore(SessionBase):
    """
    A Sharedance based session store.
    """
    def __init__(self, session_key):
        super(SessionStore, self).__init__(session_key)
        self._session_key = session_key
        self._hSharedance = Sharedance(SHAREDANCE_HOST, SHAREDANCE_PORT, SHAREDANCE_TIMEOUT)

    def load(self):
        session_data = self._hSharedance.Fetch(self._get_or_create_session_key())
        if session_data == None:
            self.create()
            return {}
        return self.decode(session_data)

    def create(self):
        while True:
            self._session_key = self._get_new_session_key()
            
            try:
                self.save(must_create=True)
            except CreateError:
                continue
            self.modified = True
            return

    def save(self, must_create=False):
        if must_create and self.exists(self._get_or_create_session_key()):
            raise CreateError
        data = self.encode(self._get_session(no_load=must_create))
        self._hSharedance.Set(self._get_or_create_session_key(), data)

    def exists(self, session_key):
        val = self._hSharedance.Fetch(session_key)
        return False if val == None else True

    def delete(self, session_key=None):
        if session_key:
            self._hSharedance.Delete(session_key)

    def cycle_key(self):
        pass
