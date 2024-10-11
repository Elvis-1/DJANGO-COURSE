'''
Migrations play a significant role in
helping curve out the data tables and the interactions from the web application to the database. By now, you know that developers canm use a model to query data directly from code instead of writing SQL commands.

An advantage of this approach is that
Django directly provides a history of changes to the code base. In this video, you will learn about
the history of changes of Django migrations and how developers use them for
version control of the model code base. Every model created in the project
provides a full history of how it was created, when it was added,
and any changes that have occurred.

 Web application development requirements
tend to change quite a bit in small increments. For example, adding an extra attribute to
a model or changing an attribute name. Additionally, there are occasions when
multiple users use more than one database and migrations ensure schema changes
are applied and updated on each database. In Django, a developer must create
the change directly in the model, then apply the migration by
using the migration scripts. Another important advantage of using
migrations is to avoid repetition. Once you create some model,
writing SQL queries to create corresponding databases for
it is repetitive. Migrations generated from the models
help prevent duplication of efforts.

This is in line with one of
the core principles of Django, don't repeat yourself. So you may be wondering how Django keeps a history of all changes
made in the database. It all begins with the file structure, migration files are stored
in a migration folder. If you expand the migrations folder, notice that it automatically updates the
file system after the migration has run.

You can explore the details of
the migrations using the show migrations command. In this example, the migrations
are listed under a given model with an auto-incremental prefix such as 0001. Django automatically generates the file
names in line with the actions performed in the given migrations or the timestamp. The X symbol represents the status of
applying migrations after making them.

This is after the command make migrations,
but before the command migrate. After applying migrations,
Django does not apply a new migration to the same database again,
unless it detects changes. Behind the scenes, Django creates
a new table called Django migrations. With reference to the migration files. Let's explore this table in a little more
detail now, a new row is inserted after each migration tracking the changes,
apps and the timestamp of the migration. The first column is the ID and this is auto-incremented based
on the position in the table. The second column is the app that
the migration is associated to.

Recall that in Django, you can have
multiple applications inside the project. The third column is the name and
refers to the file name of the migration. The final column is the timestamp
of when the migration was applied. Every time a migration script is run, this
table is updated with the latest changes. This also means that it's checked
prior to the migration script running. This is done so that it knows
which scripts have been run and which ones need to be applied. Migrations can also be applied to a
specific app by placing the app name after that make migrations command. Okay, so now you know about
the migration file structure, let's explore the contents
of a migration file. Migration files are basically Python code. 

Inside the migrations class,
it will typically contain two important sequences or list items,
such as dependencies and operations. Dependencies refer to the previous
migration, that must be applied before this and operations refer to actions
performed in the given migration. Some of the commonly used
operations are CreateModel, which creates a model and drops a table. DeleteModel, which deletes a model and
drops a table. AddField which adds a database column and
field definition creations are additions.


Inside the migrations class,
it will typically contain two important sequences or list items,
such as dependencies and operations. Dependencies refer to the previous
migration, that must be applied before this and operations refer to actions
performed in the given migration. Some of the commonly used
operations are CreateModel, which creates a model and drops a table. DeleteModel, which deletes a model and
drops a table. AddField which adds a database column and
field definition creations are additions.

'''