#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <fcntl.h>
void get_flag(){
  char c;
  int fp = open("/flag.txt", O_RDONLY);
  printf("You managed to open the door! Here is the password for the next one: ");
  while ( read(fp, &c, 1) > 0 )
    fprintf(stdout, "%c", c);
  close(fp);
}

void printBanner() {
printf("                                                                                                            \n");
printf(" ▄████▄   ▒█████   ███▄ ▄███▓  ██████  ▄▄▄     ▄▄▄█████▓  ██████    ▒██   ██▒    ▄████▄   ██░ ██  ▄████▄    \n");
printf("▒██▀ ▀█  ▒██▒  ██▒▓██▒▀█▀ ██▒▒██    ▒ ▒████▄   ▓  ██▒ ▓▒▒██    ▒    ▒▒ █ █ ▒░   ▒██▀ ▀█  ▓██░ ██▒▒██▀ ▀█    \n");
printf("▒▓█    ▄ ▒██░  ██▒▓██    ▓██░░ ▓██▄   ▒██  ▀█▄ ▒ ▓██░ ▒░░ ▓██▄      ░░  █   ░   ▒▓█    ▄ ▒██▀▀██░▒▓█    ▄   \n");
printf("▒▓▓▄ ▄██▒▒██   ██░▒██    ▒██   ▒   ██▒░██▄▄▄▄██░ ▓██▓ ░   ▒   ██▒    ░ █ █ ▒    ▒▓▓▄ ▄██▒░▓█ ░██ ▒▓▓▄ ▄██▒  \n");
printf("▒ ▓███▀ ░░ ████▓▒░▒██▒   ░██▒▒██████▒▒ ▓█   ▓██▒ ▒██▒ ░ ▒██████▒▒   ▒██▒ ▒██▒   ▒ ▓███▀ ░░▓█▒░██▓▒ ▓███▀ ░  \n");
printf("░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ░  ░▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░ ▒ ░░   ▒ ▒▓▒ ▒ ░   ▒▒ ░ ░▓ ░   ░ ░▒ ▒  ░ ▒ ░░▒░▒░ ░▒ ▒  ░  \n");
printf("  ░  ▒     ░ ▒ ▒░ ░  ░      ░░ ░▒  ░ ░  ▒   ▒▒ ░   ░    ░ ░▒  ░ ░   ░░   ░▒ ░     ░  ▒    ▒ ░▒░ ░  ░  ▒     \n");
printf("░        ░ ░ ░ ▒  ░      ░   ░  ░  ░    ░   ▒    ░      ░  ░  ░      ░    ░     ░         ░  ░░ ░░          \n");
printf("░ ░          ░ ░         ░         ░        ░  ░              ░      ░    ░     ░ ░       ░  ░  ░░ ░        \n");
printf("░                                                                               ░                ░          \n");
printf("                                                                                                            \n");
}

int main(void){
    printBanner();
    setvbuf(stdin,  NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    char user_input[6]; 
    char pass[15] = "CHC{Dummy_FLAG}";
    read(0, user_input, 7);
    strcmp(user_input, pass) == 0 ? get_flag() :printf("Error");
    return 0;
}