import pickle

import psycopg2, os, sys
from psycopg2.extensions import adapt

# Import postgres credentials from environment
postgres_database   = os.environ[ 'POSTGRES_DATABASE' ]
postgres_user       = os.environ[ 'POSTGRES_USER' ]
postgres_password   = os.environ[ 'POSTGRES_PASS' ]
postgres_host       = os.environ[ 'POSTGRES_HOST' ]
work_dir            = os.environ[ 'WORK_DIR' ]

sys.path.insert(0, work_dir + "/") # Hack to work before we've started our project
from ethereum.ethereum import Ethereum

def main():

    # print the connection string we will use to connect
    print ("[initialSetup] Connecting to database\n"
           "    -> database:'%s' user:'%s' host:'%s'" % (postgres_database, postgres_user, postgres_host) )

    # get a connection, if a connect cannot be made an exception will be raised here
    connection = psycopg2.connect(database=postgres_database, user=postgres_user, host=postgres_host, password=postgres_password)
    cursor = connection.cursor()

    print( "[initialSetup] Creating tables if they do not exist." )

    # Table to hold token request information

    cursor.execute( "CREATE TABLE IF NOT EXISTS available_ballots ("
                        "ballot_id serial UNIQUE PRIMARY KEY, "
                        "ballot_name varchar(500) UNIQUE NOT NULL, "
                        "ballot_address varchar(500) UNIQUE NOT NULL, "
                        "created_on timestamp DEFAULT CURRENT_TIMESTAMP, "
                        "ballot_interface varchar(6000) NOT NULL, "
                        "ballot_end_date integer NOT NULL"
                    ");")

    cursor.execute( "CREATE TABLE IF NOT EXISTS ballot_register ("
                        "ballot_register_id serial UNIQUE PRIMARY KEY, "
                        "user_id integer NOT NULL, "
                        "ballot_id integer NOT NULL REFERENCES available_ballots(ballot_id) ON DELETE CASCADE, "
                        "created_on timestamp DEFAULT CURRENT_TIMESTAMP, "
                        "UNIQUE (user_id, ballot_id)"
                    ");")

    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()
