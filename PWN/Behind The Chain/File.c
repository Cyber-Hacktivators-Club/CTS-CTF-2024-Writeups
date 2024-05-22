#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/prctl.h>
#include <linux/seccomp.h>
#include <linux/filter.h>
#include <stddef.h>
#include <sys/syscall.h>

void banner(){
    printf("*********************************\n");
    printf("Welcome to Comsats\n");
    printf("*********************************\n");
    fflush(stdout);
}

void install_seccomp() {
     struct sock_filter filter[] = {
        BPF_STMT(BPF_LD | BPF_W | BPF_ABS, offsetof(struct seccomp_data, nr)),
        BPF_JUMP(BPF_JMP | BPF_JEQ | BPF_K, __NR_execve, 0, 13),           
        BPF_JUMP(BPF_JMP | BPF_JEQ | BPF_K, __NR_brk, 0, 12),           
        BPF_JUMP(BPF_JMP | BPF_JEQ | BPF_K, __NR_arch_prctl, 0, 11),     
        BPF_JUMP(BPF_JMP | BPF_JEQ | BPF_K, __NR_set_tid_address, 0, 10), 
        BPF_JUMP(BPF_JMP | BPF_JEQ | BPF_K, __NR_set_robust_list, 0, 9),   
        BPF_JUMP(BPF_JMP | BPF_JEQ | BPF_K, __NR_rseq, 0, 8),           
        BPF_JUMP(BPF_JMP | BPF_JEQ | BPF_K, __NR_prlimit64, 0, 7),     
        BPF_JUMP(BPF_JMP | BPF_JEQ | BPF_K, __NR_readlinkat, 0, 6),   
        BPF_JUMP(BPF_JMP | BPF_JEQ | BPF_K, __NR_getrandom, 0, 5),         
        BPF_JUMP(BPF_JMP | BPF_JEQ | BPF_K, __NR_mprotect, 0, 4),      
        BPF_JUMP(BPF_JMP | BPF_JEQ | BPF_K, __NR_newfstatat, 0, 3),  
        BPF_JUMP(BPF_JMP | BPF_JEQ | BPF_K, __NR_write, 0, 2),    
        BPF_JUMP(BPF_JMP | BPF_JEQ | BPF_K, __NR_read, 0, 1),              


        BPF_JUMP(BPF_JMP | BPF_JEQ | BPF_K, __NR_exit_group, 0, 1),
        BPF_STMT(BPF_RET | BPF_K, SECCOMP_RET_ALLOW),


        BPF_STMT(BPF_RET | BPF_K, SECCOMP_RET_KILL),
    };

    struct sock_fprog prog = {
        .len = (unsigned short)(sizeof(filter) / sizeof(filter[0])),
        .filter = filter,
    };

    if (prctl(PR_SET_NO_NEW_PRIVS, 1, 0, 0, 0) != 0) {
        perror("prctl(PR_SET_NO_NEW_PRIVS)");
        exit(EXIT_FAILURE);
    }

    if (prctl(PR_SET_SECCOMP, SECCOMP_MODE_FILTER, &prog) != 0) {
        perror("prctl(PR_SET_SECCOMP)");
        exit(EXIT_FAILURE);
    }
}


void gadgets(){

  __asm__("pop rsi");
  __asm__("ret");

  __asm__("pop rdx");
  __asm__("ret");

  __asm__("pop rdi"); 
  __asm__("ret");

  __asm__("ret");
  __asm__("pop rax");
  __asm__("ret");

  __asm__("mov [rdi], rax");
  __asm__("ret");

  __asm__("syscall");
  __asm__("ret");

}

int main(){
  
  char buffer[2100];
  install_seccomp();
  banner();

  gets(buffer);
  return 0;
}
