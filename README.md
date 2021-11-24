# ZendeskTicketViewer
A terminal based program written in Python that can view Zendesk tickets.

## Usage
After cloning the repository, use "python3 main.py" to run the program from the root directory
Works best in fullscreen terminal

To view all tickets enter "view"
You can scroll through pages of tickets using "next"
If you want to exit the ticket viewer enter "exit"

To view a specific ticket enter "select"
You will then be prompted to enter a ticket id
Once you are done viewing this ticket enter "exit" to return to the main command interface


To search for tickets with specific parameters enter "params"
You will be prompted to input parameters for ticket status, date created and sorting order
Tickets that match these parameters will be shown

To quit the ticket viewer enter "quit"

## Testing
The ZendeskTicketViewer contains unittests that check the implementation of ticket retrieval and parameter setting
