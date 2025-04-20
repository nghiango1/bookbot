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

### Lession 2: ...
