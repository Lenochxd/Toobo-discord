CREATE TABLE IF NOT EXISTS bot (
    vips JSON,
    donators JSON,
    donations JSON,
    support_tickets JSON,
    support_tickets_ban JSON,
    GIFs_enabled BOOL,
    GIFs_sus_enabled BOOL,
    GIFs_supernut_enabled BOOL
);

CREATE TABLE IF NOT EXISTS users (
    id BIGINT PRIMARY KEY,
    bot_language TINYTEXT,
    bot_reply BOOL,
    is_oomf BOOL,
    is_vip BOOL,
    vip_end DATE,
    first_dm_received BOOL,
    dms_accepted BOOL,
    dms_anon_accepted BOOL,
    dms_pub_accepted BOOL,
    wordplay_enabled BOOL,
    howgay_enabled BOOL,
    howgay_min INT,
    howgay_max INT,
    birthday DATE
);

CREATE TABLE IF NOT EXISTS guilds (
    id BIGINT PRIMARY KEY,
    prefix TINYTEXT,
    bot_language TINYTEXT,
    ratio_emoji BIGINT,
    sniper JSON,
    antisniper_backup JSON,
    sniper_enabled BOOL,
    GIFs_enabled BOOL,
    GIFs_sus_enabled BOOL,
    GIFs_supernut_enabled BOOL,
    talkingben_enabled BOOL,
    wordplay_enabled BOOL,
    confess_cooldown BIGINT,
    confess_channels JSON,
    confess_banned JSON,
    bot_logs_enabled BOOL
);

CREATE TABLE IF NOT EXISTS guild_count (
    `time` TIMESTAMP PRIMARY KEY,
    count INT
);

CREATE TABLE IF NOT EXISTS message_logs (
    `time` TIMESTAMP PRIMARY KEY,
    guild_id BIGINT,
    user_id BIGINT,
    guild_name TINYTEXT,
    user_name TINYTEXT,
    raw_message TEXT(10000)
);

CREATE TABLE IF NOT EXISTS confess (
    id INT PRIMARY KEY,
    guild_id BIGINT,
    channel_id BIGINT,
    user_id BIGINT,
    guild_name TINYTEXT,
    channel_name TINYTEXT,
    user_name TINYTEXT,
    raw_message TEXT(10000),
    `time` TIMESTAMP
);
