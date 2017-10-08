from sqlalchemy import create_engine


DB_URL = 'mysql://root:password@db/kiki'
engine = create_engine(DB_URL)
