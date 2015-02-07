#include "stdio.h"
#include "stdint.h"
#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

//DASP message format
typedef	 struct DASP_STRUCT
{
	uint16_t		sessionId;
	uint16_t		seqNum;
	uint8_t		msgOpt;	//[0..3]:msgType [4..7]:numFields
	void 		*headerFields;
	uint8_t		*payload;
}DASP_STRUCT;

typedef struct  SOX_STRUCT
{
	uint8_t		cmd;
	uint8_t		replyNum;
	uint8_t		*payload;
}SOX_STRUCT;

typedef struct readComp
{
	uint16_t		componentId;
	uint8_t		what;
}readComp;

DASP_STRUCT* createdasp(const SOX_STRUCT *sox)
{
	DASP_STRUCT *dasp;
	dasp = malloc(sizeof(DASP_STRUCT));
	printf("dasp size:%d\n", sizeof(DASP_STRUCT));
	dasp->sessionId = 0xffff;
	dasp->seqNum = 1;
	dasp->msgOpt = 0x10;
	//dasp->msgOpt |= 0;
	dasp->payload = sox;
	return dasp;
}

SOX_STRUCT* createsox(uint8_t cmd,uint8_t replyNum,uint16_t componentId,uint8_t what)
{
	SOX_STRUCT *sox;
	sox = malloc(sizeof(SOX_STRUCT));
	readComp *rc;
	rc = malloc(sizeof(readComp));
	rc->componentId = componentId;
	rc->what = what;
	sox->cmd = cmd;
	sox->replyNum = replyNum;
	sox->payload = rc;
	return sox;
}

void dasp_debug(DASP_STRUCT *dasp)
{
	SOX_STRUCT *sox;
	readComp *rc;

	sox = (SOX_STRUCT*)dasp->payload;
	rc = (readComp*)sox->payload;

	printf("dasp->sessionId:\tuint16_t   %d\n",dasp->sessionId);
	printf("dasp->seqNum:\t\t uint8_t   %d\n",dasp->seqNum);
	printf("dasp->msgOpt:\t\t uint8_t   %d\n",dasp->msgOpt);
	printf("sox->cmd:\t\t uint8_t   %c\n",sox->cmd);
	printf("sox->replyNum:\t\tuint16_t   %d\n",sox->replyNum);
	printf("rc->componentId:\tuint16_t   %d\n",rc->componentId);
	printf("rc->what:\t\t uint8_t   %c\n",rc->what);
	printf("sizeof(dasp):\t\t uint8_t   %d\n", sizeof(dasp));
}

int main(int argc, char const *argv[])
{
	int client_sockfd;
	int len,sox_len=10,i;
	struct sockaddr_in remote_addr; //服务器端网络地址结构体
	int sin_size;
	char *buffer;

	DASP_STRUCT *dasp;
	SOX_STRUCT *sox;

	sox = createsox('c',1,12,'t');
	dasp = createdasp(sox);
	dasp_debug(dasp);

	memset(&remote_addr,0,sizeof(remote_addr)); //数据初始化--清零
	remote_addr.sin_family=AF_INET; //设置为IP通信
	remote_addr.sin_addr.s_addr=inet_addr("127.0.0.1");//服务器IP地址
	remote_addr.sin_port=htons(1876); //服务器端口号

	/*创建客户端套接字--IPv4协议，面向无连接通信，UDP协议*/
	if((client_sockfd=socket(PF_INET,SOCK_DGRAM,0))<0)
	{
		perror("socket");
		return 1;
	}
	sin_size=sizeof(struct sockaddr_in);

	/*向服务器发送数据包*/
	if((len=sendto(client_sockfd,dasp,sox_len,0,(struct sockaddr *)&remote_addr,sizeof(struct sockaddr)))<0)
	{
		perror("recvfrom");
		return 1;
	}else{
		recvfrom(client_sockfd,buffer,sizeof(buffer),0,(struct sockaddr *)&remote_addr,&len);
		printf("len:%d\n", len);
		for (i = 0; i < len; i++)
		{
			printf("%p\t", buffer++);
		}
		printf("\n");
	}
	close(client_sockfd);
	return 0;
}