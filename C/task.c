#include <stdio.h>
#include <string.h>
FILE  *tskf;	
void help()
{
    printf("Usage :-\n");
    printf("$ ./task add 2 hello world    # Add a new item with priority 2 and text \"hello world\" to the list\n");
    printf("$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order\n");
    printf("$ ./task del INDEX            # Delete the incomplete item with the given index\n");
    printf("$ ./task done INDEX           # Mark the incomplete item with the given index as complete\n");
    printf("$ ./task help                 # Show usage\n");
    printf("$ ./task report               # Statistics\n");
}
int noOfLines(char filename[20])						//A FUNCTION TO COUNT NUMBER OF LINES IN A FILE
{
		tskf = fopen(filename,"r");					//FILE OPEN
		if (tskf == NULL)								
		{	
			printf("Unable to open task.txt");			//FILE CHECK
			return 0;
		}
		int tlno = 0;
		char c;
		for(c = getc(tskf);c != EOF;c = getc(tskf))
			if ( c == '\n')
				tlno++;
		fclose(tskf);
		return tlno;
}
int main(int argc, char *argv[])
{
    if(argc > 1)																			 
    {
        if(strcmp(argv[1], "add") == 0)                                                      //ADD
        {
			int tlno = noOfLines("task.txt");
        }
        else if(strcmp(argv[1], "ls") == 0)                                                  //LIST
        {
			return 0;
        }
        else if(strcmp(argv[1], "del") == 0)                                                 //DELETE
        {
			return 0;
        }
        else if(strcmp(argv[1], "done") == 0)                                                //DONE
        {
			return 0;
        }
        else if(strcmp(argv[1], "help") == 0)                                                //HELP
        {
            help();
			return 0;
        }
        else if(strcmp(argv[1], "report") == 0)                                              //REPORT
        {
			return 0;
        }
        
        else                                                                      //DEFAULT HELP
        {
            help();
			return 0;
        }

    }
    else                                                                          //DEFAULT
    {
        help();
		return 0;
    }
}

