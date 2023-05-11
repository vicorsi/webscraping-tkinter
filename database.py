import sqlite3

var = sqlite3.connect("database.db")
cur = var.cursor()
cur.execute(f"CREATE TABLE IF NOT EXISTS tenis (marca text, nome text, preço text)")
var.commit()
