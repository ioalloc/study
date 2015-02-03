obj=main.o datetimeStd_DateTimeServiceStd.o inet_Crypto_sha1.o inet_TcpServerSocket_std.o \
	inet_TcpSocket_std.o inet_UdpSocket_std.o inet_sha1.o inet_util_std.o nativetable.o \
	sys_Component.o sys_File_std.o sys_FileStore_std.o sys_PlatformService_unix.o \
	sys_StdOutStream_std.o sys_Str.o sys_Sys.o sys_Sys_std.o sys_Sys_unix.o sys_Test.o sys_Type.o vm.o \
	nativeTest_Mynative.o

svm:$(obj)
	gcc -o svm $(obj)

debug:$(obj)
	gcc -o svm $(obj) -DDEBUG

clean:
	rm  svm $(obj)