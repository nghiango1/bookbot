# SQL - Structure query language

Create CashPal with SQL:

- To moving data from one place (UI) into otheres place (Database)
- SQL is the language to communicate with (Relational) Database, to bringing data in and out
- Just a better Excel without using API

## Chapter 1: Introduction

### Lession 1: What is SQL?

While it great to have the friendly `run` UI, we may want to setup our own local for later progress in guess mode. I setup some basic local SQL development with Posgress here

- NixOS to install posgress: Added to config session in `/etc/nixos/configuration.nix`

```nix
  # DB with postgresql
  services.postgresql = {
    enable = true;
    ensureDatabases = [ "localdb" ];
    authentication = pkgs.lib.mkOverride 10 ''
      #type database  DBuser  auth-method
      local all       all     trust
    '';
  };
```

- To run the file, we will use bellow command

```sh
sudo -u postgres psql -d localdb -f SELECT.sql
```

- Our first expected result

```
→ sudo -u postgres psql -d localdb -f CH1-L01-SELECT.sql
DROP TABLE
CREATE TABLE
INSERT 0 1
INSERT 0 1
 id |   name    | age | is_admin
----+-----------+-----+----------
  1 | John Doe  |  27 | f
  2 | Sally Rae |  18 | t
(2 rows)

```

### Lession 2: SELECT again

Single and multi field select, Just stop using `*` and remember to have `;` at the end of each statement.

Now: Requested a report asking for all the `names` and `balances` of all of our `users`. Complete `CH1-L02-SELECT-2.sql` file

### Lession 3: Database's SQL is different

While I using `posgresql`, the course use `SQLite`. There should be some different

Now: Select all of the `ids`, `names`, and `is_admin` flags from the `users` table.

### Lession 4: NoSQL vs SQL

Let look at what I have meet:

- SQL: Oracle (DB), PostgresSQL, MySQL/MariaDB, SQLite, (Microsoft) SQL Server
- NoSQL:

  - Redis: Key-Value store (mostly using for caching user session as it run on RAM)
  - MongoDB: Json Documents store (we use it to store image :/)

More example:

- ElasticSearch
- Firebase: DB as a service providing by Google for quickly implement Application
- Cassandra: Discord moment, ditributed DB

SQL is more general purposed, while No SQL tend to serve as specific solution with some competitive edge over traditional storing method (MongoDB can be stand out as a general purposed DB too ...hmm...)

> Each NoSQL Database tends to use _different_ query language(s)
