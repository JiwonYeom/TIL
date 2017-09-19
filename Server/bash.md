# Bash shell

#### Variables
1. Shell Variables : internal type of variable within a shell
2. Environment Variables : shared variable throughout the shell

```BASH
# temporal change - example of $PATH
PATH = $PATH:/Users/test/bin    # will be reset after reboot

# .bash_profile
PATH = $PATH:/Users/test/bin

# if linux
if [ -f ~/.bashrc ] ; then
    source ~/.bashrc
fi
```
.bash_profile ==> MAC & Windows
.bashrc ==> Linux

Using this, you can add hello message for when bash opens too :)

```BASH
# .bash_profile
echo "hi!"
```

* Scope of variables: they do not have to be declared. Which means, if undeclared variable is called, it wouldn't cause any error - it will call an empty string.


#### shell script grammars
[reference](http://egaoneko.github.io/os/2015/05/24/linux-starter-guide-8.html)

* shell variable does not have any type (string)
* Case-sensitive
* Use variables by calling with '$' prefix

* Collect user input

```BASH
read x y z
#input how are you
echo x  #how
```

* 사전 정의 환경변수
`$USER`, `$TERM`, `$PATH`, `$HOME`, `$SHELL`, `$MAIL`, `$HOSTNAME`

* [Special Bash variables](http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_03_02.html)
(Will be completed later)

| Character     | Def           |
| ------------- |:-------------:|
| $*      |  |
| $@      |       |
| $# |       |
| $? |       |
| $$ |       |
| $! |       |
| $# |       |
| $_ |       ||


* [Arithmetics](https://bash.cyberciti.biz/guide/Perform_arithmetic_operations)
```BASH
# contain within $(())
echo $(( 5 + 5))
x = 3
y = 4
result = $(( x + y ))
echo "$x + $y = $result"
```

* Comparison


* declaration
