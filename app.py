# import kivy
import os, sqlite3

os.environ['KIVY_NO_CONSOLELOG'] = '1'

conn = sqlite3.connect('local.db')
c = conn.cursor()
c.execute("""CREATE TABLE if not Exists projects
        (
            lp integer,
            title text, 
            description text,
            time integer,
            weight integer, 
            urgency integer, 
            price float,
            enough_funds boolean,
            enough_funds boolean,
            born_date date,
            start_time date,
            end_time date,
            crew integer,
            skills text,
            advantages text,
            risks text,
            done bool,
            
        )""")
conn.commit()
conn.close()


def base_el(l=False):
    conn = sqlite3.connect('my.db')
    c = conn.cursor()
    select_query = f"SELECT * FROM projects"
    c.execute(select_query)
    records = c.fetchall()
    conn.close()
    if l:
        return len(records)
    else:
        return records
