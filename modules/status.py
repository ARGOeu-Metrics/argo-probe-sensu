class ServiceStatus:
    OK = 0
    WARNING = 1
    CRITICAL = 2
    UNKNOWN = 3

    def __init__(self):
        self._code = self.OK
        self._msg = ""

    def _set_status(self, status, msg):
        self._code = status
        self._msg = msg

    def set_ok(self, msg):
        self._set_status(status=self.OK, msg=msg)

    def set_warning(self, msg):
        self._set_status(status=self.WARNING, msg=msg)

    def set_critical(self, msg):
        self._set_status(status=self.CRITICAL, msg=msg)

    def set_unknown(self, msg):
        self._set_status(status=self.UNKNOWN, msg=msg)

    def get_message(self):
        return self._msg

    def get_code(self):
        return self._code
