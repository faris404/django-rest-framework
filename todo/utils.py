from django.db import connection


REQ_ENVS_WEB = {
    'postman':'PostmanRuntime',
    'mozilla':'Mozilla',
    "appleWebKit":"AppleWebKit",
    "chrome":"Chrome",
    "safari":'Safari',
    "dart":'Dart'
}


def sys_type(request):

    req_from = request.headers['User-Agent']
    if REQ_ENVS_WEB['postman'] in req_from:
        return 'POSTMAN'
    if REQ_ENVS_WEB['mozilla'] in req_from or REQ_ENVS_WEB['appleWebKit'] in req_from or REQ_ENVS_WEB['chrome'] in req_from or REQ_ENVS_WEB['safari'] in req_from:
        return 'WEB'
    if REQ_ENVS_WEB['dart'] in req_from:
        return 'MOB'
    return None



def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dictfetchone(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, cursor.fetchone()))

def execute(query,data=None,many=True):
        with connection.cursor() as cursor:
            cursor.execute(query,data)
            if many:
                return dictfetchall(cursor)
            else:
                return dictfetchone(cursor)