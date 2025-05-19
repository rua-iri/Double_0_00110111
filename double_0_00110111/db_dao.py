
import psycopg


class DB_DAO:

    def __init__(self):
        self.conn = psycopg.connect(
            "postgresql://postgres:password@localhost:5435/double_0_db"
        )
        self.cur = self.conn.cursor()

    def select_record_by_uuid(self, uuid: str):
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

    def update_image_processed_status(self, image_uuid):
        update_query: str = (
            "UPDATE images "
            "SET is_processed=true "
            "WHERE image_uuid=%s;"
        )

        self.cur.execute(
            update_query,
            (image_uuid, )
        )
        self.conn.commit()
