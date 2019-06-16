doc directory contains all the documents

invert_table files contains tokens needing the special processes according to the rules in the assignment specification

query directory contains all the queries. 
The first line is the query:  You can use this to test your program

Each of the subsequent lines has 2 columns.
The first column is the document id that matches the query: you can use this to check against the results of your program ran on the query
The second column is the relevance score given by the user. Negative value means not relevant, and the higher the relevance score, the higher the document should be placed in the ranking.  So, you can check the ranking based on these relevance scores against the ranking your program comes up with.

You can also use these relevance scores as input to your relevance feedback implementation.
You don't need to worry this if you don't implement relevance feedback.