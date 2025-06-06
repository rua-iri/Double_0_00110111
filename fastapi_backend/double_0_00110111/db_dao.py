
import psycopg
from psycopg.rows import dict_row, TupleRow
import os


class DB_DAO:

    def __init__(self):

        db_conn_string: str | None = os.getenv("db_conn_string")

        if not db_conn_string:
            raise Exception("Invalid database connection string")

        self.conn = psycopg.connect(
            db_conn_string,
            row_factory=dict_row
        )
        self.cur = self.conn.cursor()

    def select_record_by_uuid(self, uuid: str) -> dict | None:
        select_query: str = "SELECT * FROM images WHERE image_uuid=%s;"

        return self.cur.execute(select_query, (uuid,)).fetchone()

    def insert_record(self, image_filename, image_uuid, image_location):
        insert_query: str = (
            "INSERT INTO images "
            "(image_filename, image_uuid, image_location) "
            "VALUES "
            "(%s, %s, %s);"
        )

        self.cur.execute(
            insert_query,
            (image_filename, image_uuid, image_location)
        )

        self.conn.commit()

    def update_image_processed_status(self, image_location, image_uuid):
        update_query: str = (
            "UPDATE images "
            "SET is_processed=true, "
            "image_location=%s "
            "WHERE image_uuid=%s;"
        )

        self.cur.execute(
            update_query,
            (image_location, image_uuid, )
        )
        self.conn.commit()
