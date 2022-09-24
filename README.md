# CourseChecking

**课表查询**

**使用方法:**

<br>
<br>

一、下载项目

在github上面下载,或在linux环境可以直接一条命令下载 `git clone https://github.com/2528104776/CourseChecking.git`

<br>
<br>

二、在config.txt文件中添加账号信息，两种方式添加:

①编辑文件 vi,vim工具均可(windows的大家都会用,不再介绍)

②直接使用命令写入  `echo "username,password" > ~/CourseChecking/config.txt`

<br>
<br>

三、启动方式

下面两种方法都可以:

①直接输入 `python ~/CourseChecking/Code.py`

②直接输入 `~/CourseChecking/Code.py`
>第二种方法如果启动报错请给文件权限`chmod 777 ~/CourseChecking/Code.py`

<br>



**程序报错**

1.检查账号和密码

3.检查weeks参数,由于上半学期和下半学期的课表都会从第一周开始算,而我的程序只能获取当前为全年的第多少周

`当前周 - 开学周(正式上课) = 当前为上课的第x周`
以2021年我们学校春季开学为例,我们正月十六报道,也就是2月27号,正式上课为3月1日,3.1这天为全年的第8周
例如今天4.4日,程序获取的当前为全年的第13周,所以13-8 = 5 结果:当前为上课的第5周,所以程序获取的weeks需要减去8

我程序中的第32行中的`time.strftime(%W)-8` 中的8就是开学的那周为全年的第8周

>注意，到了2021年下学期，代码就需要按照上述方法手动修改上述参数 "8" 为指定数字,使得结果为指定周

3.由于在wifi情况下,特别是校园网，极有可能github被墙了，也就是运营商的域名解析服务器不提供解析国外网站,最佳解决方法是切换数据流量访问.









>最后注意,使用前请检查weeks参数是否为当前周.

<br>
<br>
小白教程移步这里 [Termux查课](https://blog.csdn.net/qq_17802895/article/details/115335960)
