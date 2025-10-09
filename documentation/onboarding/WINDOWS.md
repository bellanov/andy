# Windows

Windows onboarding instructions.

## Chocolatey

[Chocolatey](https://chocolatey.org/) is a very popular package manager for both *Windows*. It simplifies the process of installing packages, enabling developer environments to stay in sync.

### NodeJS

*Node.js* is a free, open-source, cross-platform JavaScript runtime environment that lets developers create servers, web apps, command line tools and scripts.

```sh
choco install nodejs-lts
```

## Visual Studio Code

[Visual Studio Code](https://code.visualstudio.com/) is a very powerful code editor. It enables you to work in any programming language (i.e., NodeJS, Python).

## GitHub Desktop

[GitHub Desktop](https://desktop.github.com/download/) simplifies your development workflow by managing interactions with *Git*.

## Docker Desktop

[Docker Desktop](https://docs.docker.com/desktop/) is a one-click-install application for your *Mac*, *Linux*, or *Windows* environment that lets you build, share, and run containerized applications and microservices.

## Minikube

[minikube](https://minikube.sigs.k8s.io/docs/start/#windows) is local Kubernetes, focusing on making it easy to learn and develop for *Kubernetes*.

## Google Cloud CLI (gcloud)

[gcloud](https://cloud.google.com/sdk/docs/install) is a CLI tool that enables interactions with *Google Cloud Platform (GCP)*.

## Postman

[Postman](https://www.postman.com/) is a popular tool used to make *web requests*. It is very useful in testing REST APIs before consuming them within your application. You can also save and share requests as **collections**.

## Terraform

[Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli) is an *infrastructure as code* tool that lets you build, change, and version infrastructure safely and efficiently.


## PowerShell

Had to execute the following command to enable local PowerShell _script execution_.

```sh
set-executionpolicy remotesigned
```

## WSL

[Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/about) s a feature of Windows that allows you to run a Linux environment on your Windows machine, without the need for a separate virtual machine or dual booting.

For file Access, Use `/mnt/c/...` for Windows files; keep projects in *Linux home* for speed.

Follow the steps below to install WSL and the **Ubuntu** distro.

```sh
# To enable WSL, execute the following command in PowerShell (Admin) → reboot.
wsl --install

# Install Linux Distro: Get Ubuntu/Debian from Microsoft Store → set username/password.
# https://apps.microsoft.com/detail/9pdxgncfsczv?hl=en-US&gl=US

# Update Packages
sudo apt update && sudo apt upgrade -y.

# Set WSL2 Default
wsl --set-default-version 2.

# Install Dev Tools
udo apt install build-essential git curl -y.

# VS Code Integration: Install VS Code + Remote - WSL extension for coding.
# https://code.visualstudio.com/docs/remote/wsl

# To launch a folder in VS Code, execute the following in the WSL terminal
code ./folder

```
