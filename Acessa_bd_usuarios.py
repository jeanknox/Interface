import psycopg2

connexao = psycopg2.connect('dbname=usuarios user=myuser')
cur = connexao.cursor()
