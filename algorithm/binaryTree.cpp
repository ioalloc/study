#include <cstdio>
#include <iostream>
#include <unistd.h>
#include <sys/stat.h>
#include <stdlib.h>
#include <fcntl.h>
#include "binaryTree.h"


using namespace std;

const int MAX_BUFF_SIZE = 1024;

class treeNode
{
public:
	treeNode *left;
	treeNode *right;
	char *dat;
public:
	treeNode();
	treeNode(char *dat,treeNode *left,treeNode *right);
	~treeNode();

};

treeNode::treeNode(){}

treeNode::treeNode(char *dat,treeNode *left,treeNode *right){
	this->dat = dat;
	this->left = left;
	this->right = right;
}

treeNode::~treeNode(){}

class binaryTree
{
public:
	treeNode *root;
	int deepth;
	int child_count;
public:
	binaryTree();
	binaryTree(char *buff);
	~binaryTree();
};

binaryTree::binaryTree(){}

binaryTree::binaryTree(char *buff){

}

binaryTree::~binaryTree(){}


int main(int argc, char const *argv[])
{
	binaryTree bt;
	int dat = -1,result = -1;
	char buff[MAX_BUFF_SIZE] = {'\0'};
	dat = open(argv[1],O_RDONLY);
	if (dat == -1)
	{
		printf("File %s not exists!\n", argv[1]);
		return -1;
	}

	read(dat,buff,MAX_BUFF_SIZE);
	printf("%s\n", buff);

	close(dat);
	return 0;
}