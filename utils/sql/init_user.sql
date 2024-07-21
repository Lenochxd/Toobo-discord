INSERT INTO users (
    id,
    bot_language,
    bot_reply,
    is_oomf,
    is_vip,
    vip_end,
    first_dm_received,
    dms_accepted,
    dms_anon_accepted,
    dms_pub_accepted,
    wordplay_enabled,
    howgay_enabled,
    howgay_min,
    howgay_max,
    birthday
) VALUES (
    %s,    -- id
    %s,    -- bot_language
    TRUE,  -- bot_reply
    FALSE, -- is_oomf
    FALSE, -- is_vip
    NULL,  -- vip_end
    FALSE, -- first_dm_received
    TRUE,  -- dms_accepted
    TRUE,  -- dms_anon_accepted
    TRUE,  -- dms_pub_accepted
    FALSE, -- wordplay_enabled
    TRUE,  -- howgay_enabled
    0,     -- howgay_min
    100,   -- howgay_max
    NULL   -- birthday
)
