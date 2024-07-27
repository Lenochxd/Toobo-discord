INSERT INTO guilds (
    id,
    prefix,
    auto_channelid,
    auto_message_hour,
    auto_message_enabled,
    request_count
) VALUES (
    %s,      -- id
    %s,      -- prefix
    NULL,    -- auto_channelid
    %s,      -- auto_message_hour
    FALSE,   -- auto_message_enabled
    0        -- request_count
)