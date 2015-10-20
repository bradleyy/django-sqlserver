from __future__ import absolute_import, unicode_literals

import django
from django.db.utils import DatabaseError
from django.db.transaction import TransactionManagementError
from django.db.models.sql import compiler
import re
import six
import sqlserver_ado.compiler

NEEDS_AGGREGATES_FIX = django.VERSION[:2] < (1, 7)

_re_order_limit_offset = re.compile(
    r'(?:ORDER BY\s+(.+?))?\s*(?:LIMIT\s+(\d+))?\s*(?:OFFSET\s+(\d+))?$')


def _get_order_limit_offset(sql):
    return _re_order_limit_offset.search(sql).groups()


def _remove_order_limit_offset(sql):
    return _re_order_limit_offset.sub('', sql).split(None, 1)[1]


class SQLCompiler(sqlserver_ado.compiler.SQLCompiler):
    pass

class SQLInsertCompiler(sqlserver_ado.compiler.SQLInsertCompiler, SQLCompiler):
    pass


class SQLDeleteCompiler(sqlserver_ado.compiler.SQLDeleteCompiler, SQLCompiler):
    pass


class SQLUpdateCompiler(sqlserver_ado.compiler.SQLUpdateCompiler, SQLCompiler):
    pass


class SQLAggregateCompiler(sqlserver_ado.compiler.SQLAggregateCompiler, SQLCompiler):
    pass


