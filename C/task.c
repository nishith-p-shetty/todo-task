#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{
    if(argc > 1)
    {
        if(strcmp(argv[1], "add") == 0)                                                      //ADD
        {
            return 0;
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
            printf("Usage :-\n");
            printf("$ ./task add 2 hello world    # Add a new item with priority 2 and text \"hello world\" to the list\n");
            printf("$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order\n");
            printf("$ ./task del INDEX            # Delete the incomplete item with the given index\n");
            printf("$ ./task done INDEX           # Mark the incomplete item with the given index as complete\n");
            printf("$ ./task help                 # Show usage\n");
            printf("$ ./task report               # Statistics\n");
            return 0;
        }
        else if(strcmp(argv[1], "report") == 0)                                              //REPORT
        {
            return 0;
        }
        
        else                                                                      //DEFAULT HELP
        {
            printf("Usage :-\n");
            printf("$ ./task add 2 hello world    # Add a new item with priority 2 and text \"hello world\" to the list\n");
            printf("$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order\n");
            printf("$ ./task del INDEX            # Delete the incomplete item with the given index\n");
            printf("$ ./task done INDEX           # Mark the incomplete item with the given index as complete\n");
            printf("$ ./task help                 # Show usage\n");
            printf("$ ./task report               # Statistics\n");
            return 0;
        }

    }
    else                                                                          //DEFAULT
    {
        printf("Usage :-\n");
        printf("$ ./task add 2 hello world    # Add a new item with priority 2 and text \"hello world\" to the list\n");
        printf("$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order\n");
        printf("$ ./task del INDEX            # Delete the incomplete item with the given index\n");
        printf("$ ./task done INDEX           # Mark the incomplete item with the given index as complete\n");
        printf("$ ./task help                 # Show usage\n");
        printf("$ ./task report               # Statistics\n");
        return 0;
    }
}