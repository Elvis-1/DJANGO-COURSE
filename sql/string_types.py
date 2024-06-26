'''
You can use a string datatype to define the columns datatype, particularly in instances when it accepts both numeric and text characters.

When you create a table in a database, it is important for data integrity to ensure that only valid values are inserted in your table. For example, you should use string datatype when you intend to store data that contains a mix of character types.

If you define a column as a string, then any type of text can be inserted. This includes alphabet characters, numeric characters, and special characters.

String datatype is a generic term used for different string datatypes in the database. The most used string datatypes are CHAR, which stands for character. This datatype is used to hold characters of a fixed length. VARCHAR stands for variable character. This holds characters of the variable length.

Let's explore these string data types further. CHAR means that the given length of the characters is predetermined. It can't be changed after declaration. Column attributes are defined as CHAR followed by a character length in parentheses.

For example, CHAR (50) means that a column only permits 50 characters of space in each field. CHAR is the best option if you've predefined size of character that you want to maintain. In the student table, you can set a maximum length of 50 characters for the username column in SQL with CHAR (50). For example, the table contains the records for a student with a username Mark 1 2 3, which is a total of seven characters. However, because the column is defined as CHAR (50), this username occupies the length of 50 characters within the space.

The VARCHAR datatype works in a similar way to CHAR. However it is a variable length. This means that the length can be changed. It's not fixed. VARCHAR are often used when you're not sure how many characters might be inserted in the column field. You can type VARCHAR(50) in SQL to allow for any input up to maximum of 50 characters. In the student table example, the student name column would most likely contain names of varying length. You could define the student name column as VARCHAR(50) in SQL

This means that the name of each student only occupies as much space as there are characters in their name. For example, Mark Simpson occupies far less than 50 characters. But this field could hold a name up to the value of 50 characters if required.

Finally, let's briefly explore some more commonly used examples of string datatypes. TINYTEXT is used to define columns that require less than 255 characters, like short paragraphs. TEXT is used to define columns of less than 65,000 characters, like an article. MEDIUMTEXT defined columns of 16.7 million characters. For example, the text of a book. The LONGTEXT datatype stores up to four gigabytes of text data.


'''