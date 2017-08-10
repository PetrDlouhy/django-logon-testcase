__version__ = '0.1.0'


# Backport from newer Django versions
def force_login(self, user, backend=None):
    def get_backend():
        from django.contrib.auth import load_backend
        from django.conf import settings
        for backend_path in settings.AUTHENTICATION_BACKENDS:
            backend = load_backend(backend_path)
            if hasattr(backend, 'get_user'):
                return backend_path
    if backend is None:
        backend = get_backend()
    user.backend = backend
    self._login(user, backend)


class LogonTestCaseMixin(object):
    def get_user(self):
        from django.contrib.auth.models import User
        return User.objects.create()

    def setUp(self):
        super(LogonTestCaseMixin, self).setUp()
        self.user = self.get_user()

        try:  # Django >= 1.9
            self.client.force_login(self.user)
        except AttributeError:
            force_login(self.client, self.user)
