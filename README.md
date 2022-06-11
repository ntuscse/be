# be
Serverless backend


## Requirements:
### Node v14
If you don't have node currently installed on your system, use the following steps to install:
- To use the installer, [click here](https://nodejs.org/en/download/)
- Alternatively, you can install node using the terminal:

#### macOS
```bash
$ brew install node
```
#### Debian/Ubuntu
```bash
$ sudo apt-get install -y nodejs
```

#### Other Linux distros
See the instructions to install via your distro's package manager [here](https://nodejs.org/en/download/package-manager/).

#### Windows via chocolatey
Run as admin:
```powershell
$ choco install nodejs.install
```

To verify node installation, you can use the following command in your terminal/cmd: 
```bash
$ node -v
```
### Python 3.9
If you don't have python currently installed on your system, use the following steps to install:
- To use the installer, [click here](https://www.python.org/downloads/)
- Alternatively, on macOS you can install python using the terminal:
Install [Homebrew](https://brew.sh/), and then write the following command in your terminal:
  ```bash
  $ brew install python
  ```
To verify python installation, you can use the following command on your terminal/cmd: 
```bash
$ python --version
```

If you already have an older version of python installed on your system, you can update it using the online installer (linked above) or by entering the following commands on your terminal/cmd:
#### macOS
```bash
$ brew update && brew upgrade python
```
#### Windows or macOS
Install conda via https://conda.io/miniconda.html, and then run the following commands:
```powershell
$ conda update python
```
OR
```powershell
$ conda install python=<version-number>
```

### Poetry
Run the following command on your terminal/cmd:
#### macOS & Linux
```bash
$ curl -sSL https://install.python-poetry.org | python3 -
```
#### Windows
```powershell
$ (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

### AWS CLI
You can install the AWS CLI using the [online installer](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html), or by using the terminal/cmd:
#### macOS
```bash
$ curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
$ sudo installer -pkg AWSCLIV2.pkg -target /
```
#### Linux x64
```bash
$ curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
$ unzip awscliv2.zip
$ sudo ./aws/install
```

#### Windows
```powershell
$ msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi
```

To verify installation and check version, use:
```powershell
$ aws --version
```

### AWS Credentials
You can use the following [guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) to refer to docs related to generating AWS credentials and configuring the CLI for use on your system


## Install
Run the following commands to install the necessary node and python dependencies in your environment and run the serverless app offline:
```bash
$ npm run setup
$ npm run offline
```

## Test
Create a dotenv file and follow the format as shown in stub.env

Run the following command to run tests:
```bash
$ npm run test
```

To run tests in watch mode:
```bash
$ npm run test:watch
```

