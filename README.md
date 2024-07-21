# Bishokus
Discord Bot Rewrite

Bishokus is a French Discord bot designed to enhance and entertain your server. Originally developed by [Lenoch](https://github.com/Lenochxd), the bot is being rewritten to improve functionality and maintainability.

While only three commands are currently available in this version, more features will be added soon. \
The bot is built using [Nextcord](https://github.com/nextcord/nextcord) and uses MySQL for data. \
Works with every os. 

<!-- ## Features

- **Word Games:** Enjoy fun word games to liven up your server (e.g., "quoi? FEUR XDDDD").
- **Sniper Function:** View deleted messages with the `/snipe` command.
- **Ratio Battles:** Start a ratio battle by replying to a message with `/ratio` or a Tenor GIF.
- **TalkingBen:** The bot can mimic TalkingBen, the famous talking dog.
- **Music:** Play music from various sources including YouTube, SoundCloud, Twitch, Bandcamp, Vimeo, and more.

To see all available commands, use the `/help` command.

Feel free to send your suggestions using `/suggestions` or [GitHub Issues](https://github.com/Bishoko/Bishokus/issues/new/choose). All feedback is appreciated and will be considered. -->

## Add Bishokus to Your Server

To add the old version of Bishokus, which includes all existing commands, click the link below:

[Add Bishokus to Your Server](https://discord.com/api/oauth2/authorize?client_id=854081099638112256&permissions=277582703681&scope=bot%20applications.commands)

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
