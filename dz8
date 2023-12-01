import sqlite3

file = "PATH//base.sqlite"

conn = sqlite3.connect(file)

cur = conn.cursor()

cur.execute("SELECT Name FROM Track  LEFT JOIN 'InvoiceLine' ON InvoiceLine.TrackId=Track.TrackId  LEFT JOIN 'Invoice' ON InvoiceLine.InvoiceId=Invoice.InvoiceId WHERE CustomerId = 3")

res = cur.fetchall()

for res2 in res:
    print(str(res2)[1:-1])
