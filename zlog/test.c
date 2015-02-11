#include "stdio.h"
#include "zlog.h"

int main(int argc,char **argv)
{
	int rc1;
	zlog_category_t *log1,*log2;
	rc1 = zlog_init("./zlog.conf");
	if(rc1){
		printf("zlog init failed!\n");
		return -1;
	}
	log1 = zlog_get_category("my_cat");
	log2 = zlog_get_category("my_cat2");
	if(!log1&&!log2){
		printf("get cat failed!\n");
		zlog_fini();
		return -2;
	}
	zlog_info(log1,"hello world,^_^o(∩∩)o...哈哈");
	zlog_info(log2,"hello log2\n");
	zlog_fini();

	return 0;
}
