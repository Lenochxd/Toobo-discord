CREATE TABLE IF NOT EXISTS users (
    id BIGINT PRIMARY KEY,
    request_count BIGINT
);

CREATE TABLE IF NOT EXISTS guilds (
    id BIGINT PRIMARY KEY,
    prefix TINYTEXT,
    auto_channelid BIGINT,
    auto_message_hour TEXT(5),
    request_count BIGINT
);

CREATE TABLE IF NOT EXISTS guild_count (
    `time` TIMESTAMP PRIMARY KEY,
    count INT
);