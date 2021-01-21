This program searches every line from text file for symbols

   <> / {} / [] / () / "" / ''

and checks that they have a counterpart. "" and '' has to be on the same line.


RUN THE FILE FROM COMMAND LINE LIKE:
- - - - - - - - - - - - - - - - - - 
python FindMS.py <filename>
python FinsMS.py readme.txt


EXAMPLE:
<	This is an "example" text for program >
{	[It searches (every		)]
<	{},[],(),<>, "" and '' from the text file 	>
{[(	There always has to be opening 
	{ / [ / ( / <
	and closing 
	> / ) / ] / } for it				)]}
	And there has to be even number of " / ' in the line or it will give "/'-warning
}