
import psycopg


class DB_DAO:

    def __init__(self):
        conn = psycopg.connect("dbname=double_0_db user=postgres")
        self.cur = conn.cursor()

    def select_record_by_id(self, id):
        select_query: str = "SELECT * FROM images WHERE id=%s;"

        return self.cur.execute(select_query, (id,)).fetchone()

    def insert_record(self, image_filename, image_uuid, image_location):
        insert_query: str = (
            "INSERT INTO images "
            "(image_filename, image_uuid, image_location)"
            "VALUES"
            "(%s, %s, %s);"
        )

        self.cur.execute(
            insert_query,
            (image_filename, image_uuid, image_location)
        )
