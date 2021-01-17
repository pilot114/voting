#!/bin/bash

set -e

# it is */database/initial_setup.py

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE TABLE IF NOT EXISTS available_ballots (
        ballot_id serial UNIQUE PRIMARY KEY,
        ballot_name varchar(500) UNIQUE NOT NULL,
        ballot_address varchar(500) UNIQUE NOT NULL,
        created_on timestamp DEFAULT CURRENT_TIMESTAMP,
        ballot_interface varchar(6000) NOT NULL,
        ballot_end_date integer NOT NULL
    );

    CREATE TABLE IF NOT EXISTS ballot_register (
        ballot_register_id serial UNIQUE PRIMARY KEY,
        user_id integer NOT NULL,
        ballot_id integer NOT NULL REFERENCES available_ballots(ballot_id) ON DELETE CASCADE,
        created_on timestamp DEFAULT CURRENT_TIMESTAMP,
        UNIQUE (user_id, ballot_id)
    );

    CREATE TABLE IF NOT EXISTS token_request (
        token_request_id serial PRIMARY KEY,
        blind_token_hash varchar(1000) UNIQUE,
        user_id integer NOT NULL,
        ballot_id integer NOT NULL,
        created_on timestamp DEFAULT CURRENT_TIMESTAMP,
        UNIQUE (user_id, ballot_id)
    );

    CREATE TABLE IF NOT EXISTS register_vote (
        register_vote_id serial PRIMARY KEY,
        signed_token_hash varchar(1000) UNIQUE,
        voter_address varchar(50) NOT NULL,
        ballot_id integer NOT NULL,
        created_on timestamp DEFAULT CURRENT_TIMESTAMP,
        UNIQUE (voter_address, ballot_id)
    );
EOSQL