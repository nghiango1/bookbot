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
sudo -u postgres psql -d localdb -f CH1-L01-SELECT.sql
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

- Now let have some alias, as I don't want to type such a lengthy command

```sh
alias run="sudo -u postgres psql -d localdb -f"

# or I already prepare above command in the courses/sql/.alias file, just source it is enough
# relative path is used here, assumming we in the Chapter_1 directory
source ../.alias
```

- Now we can `run` the code assigment

```
run CH1-L01-SELECT.sql
```

### Lession 2: SELECT again

Single and multi field select, Just stop using `*` and remember to have `;` at the end of each statement.

Now: Requested a report asking for all the `names` and `balances` of all of our `users`. Complete `CH1-L02-SELECT-2.sql` file

```sh
run CH1-L02-SELECT-2.sql
```

### Lession 3: Database's SQL is different

While I using `posgresql`, the course use `SQLite`. There should be some different

Now: Select all of the `ids`, `names`, and `is_admin` flags from the `users` table.

```sh
run CH1-L03-SELECT-3.sql
```

### Lession 4-6: NoSQL vs SQL

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

> Quiz time:
>
> - Each NoSQL Database tends to use _different_ query language(s)
> - _SQL_ compatible databases tend to be more similar in their functionality than _NoSQL_ databases
> - Which type of database always uses table structures? SQL

### Lession 7: Comparing

While there is a lot of SQL database, we only care about these two:

- SQLite, which is choosen from the course side, is lightweight and embeddable. This mean it has the ability to run within applications, or serverless database management system
- PostgreSQL, which is what I currently use, is a traditional client-server Database.

Both of them is open-source and production-ready, and can be seen commonly enough.

From my work experience, which is quite trouble some:

- MySQL is use as client side, ship with application self management batabase. It quite short live though, as we need quick solution where Server can't really reach
- Oracle (DB) for client-server: A very well round solution, which fit well with any reuseable project that come from Java 8 era (Oracle's Java) that we refuse to give up on
- MongoDB for some of object storage: Idk, we gonna have new solution later. Something is better than Blob field in our Oracle DB instance

Assignment is not that relevant though:

- SQL have lossen logic when it come to type enforcement, or I'd say it automatically cast user input into collums coresponsed type
- SQLite, and PosgreSQL both allow me to instert `1` as a `TEXT` value. Even without encapsulate it with single quote `''`

```sql
-- Create user table
CREATE TABLE users (id INTEGER, name TEXT, age INTEGER);
INSERT into users (id, name, age) values (1, 'John Doe', 21);
INSERT into users (id, name, age) values (2, 1, 33);
SELECT * FROM users;
```
