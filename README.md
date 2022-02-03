# be
Serverless backend


## Requirements:
### Node v14
If you don't have node currently installed on your system, use the following steps to install:
- To use the installer, [click here](https://nodejs.org/en/download/)
- Alternatively, on macOS you can install node using the terminal:
Install [Homebrew](https://brew.sh/), and then write the following command in your terminal:
```
$ brew install node
```
To verify node installation, you can use the following command on your terminal/cmd: 
```
$ node -v
```

If you already have an older version of node installed on your system, you can update it using the online installer (linked above) or by entering the following commands on your terminal/cmd:
#### macOS
```
$ brew update && brew upgrade node
```
#### Windows
Run as admin:
```
$ npm install -g n
$ n latest
```

### Python 3.9
If you don't have python currently installed on your system, use the following steps to install:
- To use the installer, [click here](https://www.python.org/downloads/)
- Alternatively, on macOS you can install python using the terminal:
Install [Homebrew](https://brew.sh/), and then write the following command in your terminal:
```
$ brew install python
```
To verify python installation, you can use the following command on your terminal/cmd: 
```
$ python --version
```

If you already have an older version of python installed on your system, you can update it using the online installer (linked above) or by entering the following commands on your terminal/cmd:
#### macOS
```
$ brew update && brew upgrade python
```
#### Windows or macOS
Install conda and then run the following commands:
```
$ conda update python
```
OR
```
$ conda install python=<version-number>
```

### Poetry
Run the following command on your terminal/cmd:
```
$ pip install poetry
```

### AWS CLI
You can install the AWS CLI using the [online installer](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html), or by using the terminal/cmd:
#### macOS
```
$ curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
$ sudo installer -pkg AWSCLIV2.pkg -target /
```
#### Windows
```
msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi
```

To verify installation and check version, use:
```
$ aws --version
```

### AWS Credentials
You can use the following [guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) to refer to docs related to generating AWS credentials and configuring the CLI for use on your system


## Install
Run the following commands to install the necessary node and python dependencies in your environment and run the serverless app offline:
```
$ npm run setup
$ npm run offline
```

