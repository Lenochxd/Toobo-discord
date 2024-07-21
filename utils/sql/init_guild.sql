INSERT INTO guilds (
    id,
    prefix,
    bot_language,
    ratio_emoji,
    sniper,
    antisniper_backup,
    sniper_enabled,
    GIFs_enabled,
    GIFs_sus_enabled,
    GIFs_supernut_enabled,
    talkingben_enabled,
    wordplay_enabled,
    confess_cooldown,
    confess_channels,
    confess_banned,
    bot_logs_enabled
) VALUES (
    %s,    -- id
    '!',   -- prefix
    %s,    -- bot_language
    NULL,  -- ratio_emoji
    '{}',  -- sniper
    '{}',  -- antisniper_backup
    TRUE,  -- sniper_enabled
    TRUE,  -- GIFs_enabled
    TRUE,  -- GIFs_sus_enabled
    TRUE,  -- GIFs_supernut_enabled
    TRUE,  -- talkingben_enabled
    FALSE, -- wordplay_enabled
    3,     -- confess_cooldown
    '{}',  -- confess_channels
    '{}',  -- confess_banned
    FALSE  -- bot_logs_enabled
)