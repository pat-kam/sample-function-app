import logging
import os

import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    logging.info('START BACKING UP...')
    os.environ['PGPASSWORD'] = 'Password123'
    os.system(
        'pg_dump --host=psql-sample.postgres.database.azure.com --username=sampleuser --dbname=sampledb --file=dump.sql'
    )
    logging.info('FINISHED BACKING UP...')

    return func.HttpResponse("pg_dump completed")