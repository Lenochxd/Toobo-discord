INSERT INTO guilds (
    id,
    prefix,
    auto_channelid,
    auto_message_hour,
    request_count
) VALUES (
    %s,      -- id
    %s,      -- prefix
    NULL,    -- auto_channelid
    '19:50', -- auto_message_hour
    0       -- request_count
)