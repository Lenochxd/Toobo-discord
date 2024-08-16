# Toobo discord bot

![License](https://img.shields.io/github/license/Lenochxd/Toobo-discord)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/Lenochxd/Toobo-discord.svg?style=flat)](https://github.com/Lenochxd/Toobo-API/releases)
![Stars](https://img.shields.io/github/stars/Lenochxd/Toobo-discord?style=flat)
[![Discord](https://img.shields.io/discord/391919052563546112?style=flat&logo=Discord&logoColor=fff&label=Discord&color=5e6ae8&link=https%3A%2F%2Fdiscord.gg%2FtUPsYHAGfm)](https://discord.gg/tUPsYHAGfm)


Toobo is a character from the French children's weather forecast show "[La météo de Gulli](https://fr.wikipedia.org/wiki/La_M%C3%A9t%C3%A9o_de_Gulli)". This adorable mascot presents weather information in a fun and engaging way for young viewers. In the show, Toobo uses simple language and playful animations to explain weather concepts and forecasts, making meteorology accessible and entertaining for children.

This Discord bot uses the [Toobo-API](https://github.com/Lenochxd/Toobo-API) to cast daily messages with meteorological information. It brings a cheerful approach to weather updates on Discord servers, providing weather information and forecasts with a friendly personality, making it both informative, enjoyable and funny.


## Commands

- **/meteo:** Get weather information for a specific date
- **/setup:** Set up daily weather updates for a channel at a specified time
- **/prefix:** Change the bot's command prefix
- **/enable-toobo:** Enable automatic messages
- **/disable-toobo:** Disable automatic messages

<!-- To see all available commands, use the `/help` command. -->


## Add Toobo to Your Server

To add the Toobo bot, click the link below:

https://discord.com/oauth2/authorize?client_id=1264602192564981863

<br>

---

## Dev Setup

### Setup for Linux

#### Setup Python

1. **Install Python:**
   - Install [Python](https://www.activestate.com/products/python/) using your package manager. For example, on Debian-based systems:
     ```sh
     sudo apt update
     sudo apt install python3 python3-venv python3-pip
     ```

2. **Setup Virtual Environment:**
   - Create a virtual environment:
     ```sh
     python3 -m venv .venv
     ```
   - Activate the virtual environment:
     ```sh
     source .venv/bin/activate
     ```

3. **Install Requirements:**
   - Install the necessary Python packages:
     ```sh
     pip install -r requirements.txt
     ```

#### Setup MySQL

1. **Install MySQL:**
   - Install MySQL using your package manager. For example, on Debian-based systems:
     ```sh
     sudo apt update
     sudo apt install mysql-server
     ```

2. **Secure MySQL Installation:**
   - Run the security script to set up MySQL:
     ```sh
     sudo mysql_secure_installation
     ```

3. **Create Database:**
   - Log into MySQL and create the database:
     ```sh
     sudo mysql -u root -p
     CREATE DATABASE your_database_name;
     CREATE USER 'your_username'@'localhost' IDENTIFIED BY 'your_password';
     GRANT ALL PRIVILEGES ON your_database_name.* TO 'your_username'@'localhost';
     FLUSH PRIVILEGES;
     EXIT;
     ```

#### Configure Application

1. **Edit Configuration:**
   - Open `config/config.json`.
   - Update the configuration based on the default template provided.

---

### Setup for Windows

#### Setup Python

1. **Install Python:**
   - Download and install Python from [python.org](https://www.python.org/downloads/).

2. **Setup Virtual Environment:**
   - Create a virtual environment:
     ```sh
     python -m venv .venv
     ```
   - Activate the virtual environment:
     ```sh
     .venv\Scripts\activate.bat
     ```

3. **Install Requirements:**
   - Install the necessary Python packages:
     ```sh
     pip install -r requirements.txt
     ```

#### Setup MySQL

1. **Install MySQL:**
   - Download and install MySQL from [MySQL Installer - Community](https://dev.mysql.com/get/Downloads/MySQLInstaller/mysql-installer-community-8.0.37.0.msi).

2. **Create Database:**
   - Use `MySQL Installer - Community` to create a database and set up a password.

#### Configure Application

1. **Edit Configuration:**
   - Open `config/config.json`.
   - Update the configuration based on the default template provided.
