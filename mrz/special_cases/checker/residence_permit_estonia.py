# -*- Coding: UTF-8 -*-
#
# GNU General Public License v3.0
#
# https://www.gnu.org/licenses/gpl-3.0.html
#
# (ɔ) Iván Rincón 2019

from mrz.checker.td1 import *
from mrz.base.functions import hash_is_ok


class TD1RpESTCodeChecker(TD1CodeChecker):

    @property
    def document_type(self) -> bool:
        ok = self._document_type.upper() == "RP"
        return self.report.add("document type format", ok)

    @property
    def country(self) -> bool:
        ok = self._country.upper() == "EST"
        return self.report.add("valid country code", ok)
