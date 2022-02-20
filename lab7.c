#include <unistdio.h>   
#include <pthread.h> 
#include <stdlib.h>
#include <unistd.h>      
void *myfunc( void *ptr );  
int main()   
{   
int status;    
char *msg1 = "Thread 1";  
char *msg2 = "Thread 2";  
pthread_t tid1,tid2;   
pthread_create(&tid1,NULL,myfunc, (void*) msg1);   
pthread_create(&tid2,NULL,myfunc, (void*) msg2);   
pthread_join(tid1,NULL);   
pthread_join(tid2,NULL);   return 0; 
}   
void *myfunc ( void *ptr )        
{       
char *message;  
message = (char *) ptr;   
for (int i=0; i<10;i++)  
{  
 printf(“%s  %d\n”, message,i);  
sleep(1); }  
return 0;  
} 