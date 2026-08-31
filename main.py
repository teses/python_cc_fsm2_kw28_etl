



# get config
config = ""

# get db connection
db_conn = ""

# logger initialisieren
logger = ""

# Pipeline instanzieieren
#p = ETlPricefile(db_conn, logger, config)
#p = ETlGPRS(db_conn, logger, config)
#p.run()


pipelines = [
    ETLPricefile(config, logger, db_conn),
    ETLGPRS(config, logger, db_conn)
]
for pipeline in pipelines:
    try:
        pipeline.run()
    except Exception as e:
        print(f"Fehler in {pipeline.__class__.__name__}: {e}")
