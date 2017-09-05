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

shell script grammars (working)
