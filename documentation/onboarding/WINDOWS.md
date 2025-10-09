# Windows

Windows onboarding instructions.

## Visual Studio Code

[Visual Studio Code](https://code.visualstudio.com/) is a very powerful code editor. It enables you to work in any programming language (i.e., NodeJS, Python).

## GitHub Desktop

[GitHub Desktop](https://desktop.github.com/download/) simplifies your development workflow by managing interactions with *Git*.

## Docker Desktop

[Docker Desktop](https://docs.docker.com/desktop/) is a one-click-install application for your *Mac*, *Linux*, or *Windows* environment that lets you build, share, and run containerized applications and microservices.

## Minikube

[minikube](https://minikube.sigs.k8s.io/docs/start/#windows) is local Kubernetes, focusing on making it easy to learn and develop for *Kubernetes*.

## Postman

[Postman](https://www.postman.com/) is a popular tool used to make *web requests*. It is very useful in testing REST APIs before consuming them within your application. You can also save and share requests as **collections**.

## PowerShell

Had to execute the following command to enable local PowerShell _script execution_.

```sh
set-executionpolicy remotesigned
```

## Windows Subsystem for Linux (WSL)

[Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/about) is a feature of Windows that allows you to run a Linux environment on your Windows machine, without the need for a separate virtual machine or dual booting.

For file Access, Use `/mnt/c/...` for Windows files; keep projects in *Linux home* for speed.

Follow the steps below to install WSL and the **Ubuntu** distro.

```sh
# To enable WSL, execute the following command in PowerShell (Admin) → reboot.
wsl --install

# Install Linux Distro: Get Ubuntu/Debian from Microsoft Store → set username/password.
# https://apps.microsoft.com/detail/9pdxgncfsczv?hl=en-US&gl=US

# Update Packages
sudo apt update && sudo apt upgrade -y

# Set WSL2 Default
wsl --set-default-version 2

# Install Dev Tools
sudo apt install build-essential git curl -y

# VS Code Integration: Install VS Code + Remote - WSL extension for coding.
# https://code.visualstudio.com/docs/remote/wsl

# To launch a folder in VS Code, execute the following in the WSL terminal
code ./folder
```
