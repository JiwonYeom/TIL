## Process of Installing a Package

1. Update existing software packages
```
sudo yum update -y
```

2. Add program repo
```
sudo wget -O /etc/yum.repos.d/[program].repo [repo address]
```

3. Import key file from the repository
```
sudo rpm --import [key address]
```

4. Install
```
sudo yum install [program]
```
