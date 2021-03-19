from connections.connection import data
import psycopg2
import traceback
from psycopg2.extras import RealDictCursor
import json


class DesignerDAO():
    def insert_on_db(self, name):
        success = False
        try:
            _connect = psycopg2.connect(
                host=data['host'],
                database=data['database'],
                user=data['user'],
                password=data['password'])
            _cursor = _connect.cursor()
            _cursor.execute(f"INSERT INTO designer(nome)VALUES ('{name}');")
            id = _cursor.execute(f"SELECT max(id) from designer")
            _connect.commit()
            success = (_cursor.rowcount == 1)

        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if(_connect):
                _cursor.close()
                _connect.close()

        if(success):
            return "success"
        else:
            return "fail"

    def remove_from_db(self, id):
        success = False
        try:
            _connect = psycopg2.connect(
                host=data['host'],
                database=data['database'],
                user=data['user'],
                password=data['password'])
            _cursor = _connect.cursor()
            _cursor.execute(f"DELETE FROM designer WHERE id = {str(id)}")
            _connect.commit()
            success = (_cursor.rowcount == 1)

        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if(_connect):
                _cursor.close()
                _connect.close()

        if(success):
            return "success"
        else:
            return "fail"

    def update_on_db(self, id, nome):
        success = False
        try:
            _connect = psycopg2.connect(
                host=data['host'],
                database=data['database'],
                user=data['user'],
                password=data['password'])

            _cursor = _connect.cursor()
            _cursor.execute(
                f"UPDATE designer set nome='{nome}' WHERE id={str(id)};")
            _connect.commit()

            success = (_cursor.rowcount == 1)

        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if(_connect):
                _cursor.close()
                _connect.close()
        if(success):
            return "success"
        else:
            return "fail"

    def select_all_from_db(self):
        results = []
        try:
            _connect = psycopg2.connect(
                host=data['host'],
                database=data['database'],
                user=data['user'],
                password=data['password'])

            _cursor = _connect.cursor(cursor_factory=RealDictCursor)
            _cursor.execute(f"select id,nome from designer")
            _connect.commit()

            response = _cursor.fetchall()

        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
            return "error"
        finally:
            if(_connect):
                _cursor.close()
                _connect.close()

        response = json.dumps(response)
        return response

    def select_from_db(self, id):
        designer = None
        try:
            _connect = psycopg2.connect(
                host=data['host'],
                database=data['database'],
                user=data['user'],
                password=data['password'])

            _cursor = _connect.cursor(cursor_factory=RealDictCursor)
            _cursor.execute(
                f"select id,nome from designer where id = {str(id)}")
            _connect.commit()

            response = _cursor.fetchone()

        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
            return "error"
        finally:
            if(_connect):
                _cursor.close()
                _connect.close()

        designer = json.dumps(response)
        return designer
