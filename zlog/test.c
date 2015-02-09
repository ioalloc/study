#include "stdio.h"
#include "zlog.h"

int main(int argc,char **argv)
{
	int rc;
	zlog_category_t *c,*c2;
	rc = zlog_init("./zlog.conf");
	if(rc){
		printf("zlog init failed!\n");
		return -1;
	}

	c = zlog_get_category("my_cat");
	c2 = zlog_get_category("my_cat2");
	if(!c&&!c2){
		printf("get cat failed!\n");
		zlog_fini();
		return -2;
	}
	zlog_info(c,"hello world,^_^o(∩∩)o...哈哈");
	zlog_info(c2,"hello c2\n");
	zlog_fini();

	return 0;
}
