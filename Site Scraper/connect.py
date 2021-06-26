import csv
import psycopg2

conn = psycopg2.connect(user="djpoucmhkewvrh", password="e1a533e45aa586bf82ff18dcc021969e6fb438333e501973f5236ab9257aea9c",
                        host="ec2-174-129-209-212.compute-1.amazonaws.com", port="5432", database="d24ubplectbqas", sslmode='require')
cur = conn.cursor()

cur.execute("SELECT COUNT(*) FROM games")
unique_id = cur.fetchone()
unique_id = unique_id[0]
# Maybe check id of the last entry here to ensure this works even with deleted entries

input_file = {
    'LCK Data.csv',
    'LEC Data.csv',
    'LCO Data.csv',
    'LFL Data.csv',
    'LVP_SuperLiga Data.csv',
    'LMS Data.csv',
    'LCS Data.csv',
    'LLA Data.csv',
    'Ultraliga Data.csv'
}

for file in input_file:
    print("Adding matches from " + file + ' to the database')
    with open(file, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row

        for (index, row) in enumerate(reader):
            print(index)
            unique_id = unique_id+1
            cur.execute("INSERT INTO games VALUES (" +
                        str(unique_id) + " , %s, %s, %s, %s, %s, %s)", row[:6])
            cur.execute(
                "INSERT INTO match_data VALUES (%s, %s, %s, %s, %s, %s, %s, " + str(unique_id) + ")", row[6:])

print("Commiting files to the database")
conn.commit()
